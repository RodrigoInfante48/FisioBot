# DentBot — Contexto de proyecto para Claude Code

## Qué es DentBot

DentBot es un sistema de automatización de anamnesis para odontólogos, vendido como producto digital de pago único. El flujo automatiza la historia clínica del paciente antes de que llegue al consultorio usando cuatro herramientas encadenadas orquestadas por Make.com:

1. **Tally** — El paciente recibe un formulario por WhatsApp y lo llena en 3 minutos desde su celular, sin apps ni login.
2. **Make.com** — Orquesta todo el flujo: recibe la respuesta de Tally, llama a Gemini AI, y distribuye el output a Notion mediante un Router con dos ramas paralelas.
3. **Gemini AI** — Procesa las respuestas una sola vez, extrae alergias, medicamentos y factores de riesgo, y genera el contenido para ambas fichas clínicas.
4. **Notion** — Recibe las dos fichas simultáneas vía el Router de Make y las almacena en el workspace del odontólogo.

### El flujo técnico completo

```
Tally → Make.com → Gemini AI → Router (Make)
                                    ├── Ruta 1: Notion Create → Append → Update  (Ficha PRE, para el odontólogo)
                                    └── Ruta 2: Notion Create → Append → Update  (Ficha POST, para el paciente)
```

### Las dos fichas que genera DentBot

**Ficha PRE-consulta (para el odontólogo)**
Se crea antes de que el paciente llegue al consultorio. Contiene anamnesis estructurada, alergias, medicamentos, factores de riesgo y alertas clínicas. El odontólogo la revisa antes de atender.

**Ficha POST-consulta (para el paciente)**
Se crea al mismo tiempo en Notion. Contiene un resumen personalizado de la consulta, recomendaciones y plan de seguimiento. El odontólogo la comparte con el paciente al terminar la cita.

### Flujo narrativo completo

Paciente llena Tally → Make procesa → Gemini genera ambas fichas → Router las distribuye a Notion → odontólogo llega y revisa la ficha pre → tiene la consulta → termina y comparte la ficha post con el paciente.

**Propuesta de valor central:** Recuperar 10-15 minutos por consulta eliminando la anamnesis repetitiva, los papeles perdidos y el mal seguimiento del paciente — generando automáticamente dos fichas clínicas (una para el odontólogo, una para el paciente) sin intervención manual.

---

## Mercado objetivo

- Odontólogos en Bogotá, Colombia (Usaquén, Chapinero, Cedritos, Chía)
- Perfil: profesional independiente con consultorio propio, no grandes clínicas
- Dolor principal: tiempo perdido en preguntas repetitivas, notas incompletas y pacientes que no regresan

---

## Productos y precios

| Producto | Precio | Canal | Estado |
|---|---|---|---|
| Self-Setup | $9.99 USD (pago único) | Hotmart | Activo |
| Setup Completo | $33 USD (pago único) | Hotmart | Activo |
| DentBot Copilot | Order bump en checkout Hotmart | Hotmart | Por configurar |

### Self-Setup — $9.99
- Plantilla de formulario Tally
- Instrucciones paso a paso
- Acceso a comunidad WhatsApp
- Actualizaciones futuras
- **Link de pago:** https://pay.hotmart.com/U105362980Y

### Setup Completo — $33 ⭐ (más vendido)
- Todo lo del Self-Setup
- Configuración completa por el equipo DentBot
- Logo y colores del consultorio en el form
- Sesión de onboarding de 30 minutos
- Soporte prioritario por 30 días
- **🎁 Bono gratuito: DentBot Copilot** (ver abajo)
- **Link de pago:** https://pay.hotmart.com/X105362860D

### DentBot Copilot (bono + order bump)
Cuaderno NotebookLM alimentado con papers científicos, guías clínicas y protocolos de expertos en odontología. El odontólogo puede consultarlo con IA en segundos entre paciente y paciente.
- Incluido gratis en el Setup Completo ($33)
- Disponible como order bump en el checkout del Self-Setup ($9.99) — precio por definir
- Nombre oficial del cuaderno: *"Banco de conocimiento: protocolos clínicos y gestión de pacientes consultados con IA"*

---

## Stack técnico

### Automatización del producto
- **Make.com** — Orquestador central del flujo. Conecta Tally, Gemini AI y Notion. Contiene el Router que divide el output en dos ramas paralelas hacia Notion.
- **Tally** — Formulario de anamnesis que el paciente llena por WhatsApp
- **Google Gemini AI** — Modelo de IA que procesa las respuestas del formulario (una sola llamada, genera contenido para ambas fichas)
- **Notion** — Base de datos donde se almacenan la Ficha PRE (odontólogo) y la Ficha POST (paciente)

### Landing page
- **Frontend:** HTML5 + Tailwind CSS (CDN) + Vanilla JavaScript (todo en un solo archivo)
- **Fuentes:** Plus Jakarta Sans (Google Fonts)
- **Analytics:** Google Analytics (G-M08G3EFVMM) + Meta Pixel (1304108798298040)
- **Pagos:** Hotmart
- **Deploy:** GitHub Pages desde la rama `main`
- **Archivo principal:** `index.html` (único archivo de la landing)

### Paleta de colores del design system

```
Navy (fondo principal):  #1a1a2e
Navy dark:               #0f0f1a
Surface:                 #16213e
Surface light:           #1f2f52
Teal (acento principal): #00E6C7
Teal dark (hover):       #00C4B0
Gold (acento secundario):#FFB800
Gold dark (hover):       #E5A500
```

---

## Estructura de la VSL (landing page)

La landing page `index.html` ES la VSL (Video Sales Letter). Sigue esta estructura narrativa:

1. **Header fijo** — Logo DentBot + botón WhatsApp
2. **Hero** — Headline de dolor + subheadline de solución + demo de video + prueba social (barrios de Bogotá)
3. **Sección dolor** — 3 problemas específicos del odontólogo (anamnesis repetitiva, notas perdidas, paciente que no volvió)
4. **Sección solución** — 3 pasos del flujo (Tally → Make.com → Gemini → Notion) con mockup de Notion y las dos fichas generadas
5. **Sección oferta/precios** — Barra de escasez (40/48 cupos) + dos cards de precio + ancla de precio vs software tradicional
6. **CTA final** — Demo personalizada por WhatsApp
7. **Barra sticky mobile** — "Empezar ahora" fija en la parte inferior
8. **Footer** — DentBot by DailyDuty / Instituto para el Desarrollo Diario

### Escasez activa
- 40 de 48 cupos tomados (83.3%)
- Mensaje: "Solo quedan 8 cupos a este precio — cuando se acaben, sube"
- Barra animada con gradiente teal-gold

---

## Contacto y marca

- **WhatsApp:** +57 320 997 4750
- **Marca paraguas:** DailyDuty / Instituto para el Desarrollo Diario
- **Linktree:** linktr.ee/dailyduty
- **OG image:** `og-image.png` (900×1200px)

---

## Reglas de desarrollo — MUY IMPORTANTE

### Git y deploy
- La página live está publicada en **GitHub Pages desde la rama `main`**
- **Todos los cambios deben terminar en `main`** para que se reflejen en la página pública
- Se puede (y se debe) trabajar en branches separadas, pero **siempre hacer merge a `main` al finalizar**
- Nunca dejar cambios importantes solo en una branch sin mergear
- No crear Pull Requests a menos que el usuario lo pida explícitamente

### Flujo estándar de trabajo
```bash
# Trabajar en branch
git checkout -b claude/<descripcion-corta>
# ... editar index.html ...
git add index.html
git commit -m "descripción del cambio"
git push -u origin claude/<descripcion-corta>

# Cuando el cambio está listo, mergear a main
git checkout main
git pull origin main
git merge claude/<descripcion-corta> --no-ff
git push -u origin main
```

### Qué se puede editar
- `index.html` — El único archivo de la landing. Todo el HTML, CSS y JS está aquí.
- `og-image.png` — Solo si se necesita actualizar la imagen de redes sociales

### Qué NO hacer
- No crear archivos CSS o JS separados — todo va inline en `index.html`
- No cambiar los links de pago de Hotmart sin confirmación del usuario
- No modificar los IDs de Analytics o Meta Pixel
- No agregar dependencias externas más allá de las ya existentes (Tailwind CDN, Google Fonts)

---

## Estado del arte (al 17 de abril de 2026)

### Hecho
- [x] Landing page completa y publicada en GitHub Pages
- [x] Dos planes de precio activos en Hotmart ($9.99 y $33)
- [x] Card $33 posicionada primero como "Más vendido"
- [x] Barra de escasez animada (40/48 cupos)
- [x] Meta Pixel y Google Analytics integrados
- [x] OG image para redes sociales
- [x] DentBot Copilot agregado como bono en el plan $33
- [x] Cuaderno NotebookLM creado con papers y protocolos clínicos

### Pendiente
- [ ] Configurar DentBot Copilot como order bump en Hotmart para el plan $9.99
- [ ] Definir precio del order bump del Copilot
- [ ] Video demo embebido en la sección hero (actualmente es thumbnail estático)
- [ ] Testimoniales reales de odontólogos (sección eliminada en refactor anterior)
