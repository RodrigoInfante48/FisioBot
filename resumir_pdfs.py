import pdfplumber
import anthropic
import os
import re
import time
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

FOLDER = r"C:\Users\rodri\OneDrive\Desktop\DentBot\DentBot Copilot"
OUTPUT = os.path.join(FOLDER, "resumen-copilot.md")

SYSTEM_PROMPT = (
    "Eres un asistente clínico dental. "
    "Resume documentos en español con: título y fuente, tema principal (1 línea), "
    "y los 5 puntos clínicos más importantes y accionables."
)

def make_custom_id(filename: str, index: int) -> str:
    """Genera un custom_id válido: solo a-z, A-Z, 0-9, _, - y máx 64 chars."""
    clean = re.sub(r"[^a-zA-Z0-9_-]", "_", filename.replace(".pdf", ""))
    clean = re.sub(r"_+", "_", clean).strip("_")
    return f"doc{index:02d}_{clean}"[:64]

# ── 1. Extract text from PDFs ──────────────────────────────────────────────
pdf_data = []  # [(filename, custom_id, text)]
for i, filename in enumerate(sorted(os.listdir(FOLDER))):
    if not filename.endswith(".pdf"):
        continue
    path = os.path.join(FOLDER, filename)
    try:
        with pdfplumber.open(path) as pdf:
            text = "\n".join(
                page.extract_text() or "" for page in pdf.pages[:15]
            )
        custom_id = make_custom_id(filename, i)
        pdf_data.append((filename, custom_id, text))
        print(f"Extraído: {filename}")
    except Exception as e:
        print(f"⚠ Error leyendo {filename}: {e}")

if not pdf_data:
    print("No se encontraron PDFs.")
    raise SystemExit(1)

# ── 2. Submit as a single batch (50 % cheaper, all PDFs in parallel) ───────
requests = [
    Request(
        custom_id=custom_id,
        params=MessageCreateParamsNonStreaming(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=[
                {
                    "type": "text",
                    "text": SYSTEM_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[
                {
                    "role": "user",
                    "content": f"Documento: {filename}\n\nContenido:\n{text[:8000]}",
                }
            ],
        ),
    )
    for filename, custom_id, text in pdf_data
]

print(f"\nEnviando batch con {len(requests)} documentos…")
batch = client.messages.batches.create(requests=requests)
print(f"Batch ID: {batch.id}")

# ── 3. Poll until done ─────────────────────────────────────────────────────
while True:
    batch = client.messages.batches.retrieve(batch.id)
    if batch.processing_status == "ended":
        break
    pending = batch.request_counts.processing
    print(f"  Procesando… ({pending} pendientes)")
    time.sleep(30)

print(f"✓ Batch completo — exitosos: {batch.request_counts.succeeded}, "
      f"errores: {batch.request_counts.errored}")

# ── 4. Collect results ─────────────────────────────────────────────────────
summaries: dict[str, str] = {}
for result in client.messages.batches.results(batch.id):
    if result.result.type == "succeeded":
        text_block = next(
            (b.text for b in result.result.message.content if b.type == "text"), ""
        )
        summaries[result.custom_id] = text_block
    else:
        summaries[result.custom_id] = f"[Error: {result.result.type}]"

# ── 5. Write markdown output ───────────────────────────────────────────────
with open(OUTPUT, "w", encoding="utf-8") as out:
    out.write("# Resumen Consolidado — DentBot Copilot\n\n")
    for filename, custom_id, _ in pdf_data:
        summary = summaries.get(custom_id, "[Sin resultado]")
        out.write(f"## {filename}\n{summary}\n\n---\n\n")

print(f"\nListo → {OUTPUT}")
