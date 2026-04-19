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

## Fundador, visión y metas de negocio

**Fundador:** Rodrigo Infante — DailyDuty / Instituto para el Desarrollo Diario

### La misión
DentBot nació con una misión clara: **ayudar a la mayor cantidad posible de odontólogos en Colombia y en el mundo** a recuperar su tiempo, elevar su estándar clínico y darle a cada paciente una experiencia que los haga volver. No es solo un producto digital — es una declaración de intenciones sobre cómo debería funcionar la odontología moderna.

### Metas de negocio (norte del proyecto)
- **Volumen:** Vender muchísimas licencias — el modelo de pago único y precio accesible está diseñado para escalar masivamente sin fricción
- **Impacto geográfico:** Arrancar en Bogotá (Usaquén, Chapinero, Cedritos, Chía), expandir a toda Colombia, y después a México, Perú y el resto de Latinoamérica (el Copilot ya incluye marcos legales de México y Perú como señal de esa intención)
- **Impacto real:** Que cada odontólogo que use DentBot recupere 10-15 minutos por consulta y le dé a su paciente una experiencia que ningún consultorio sin IA puede igualar

### Por qué esto importa al desarrollar
Cada decisión de diseño, copy y funcionalidad debe estar orientada a **remover fricción de compra** y a **maximizar el valor percibido**. El producto es barato pero debe sentirse premium. El onboarding debe ser tan simple que el odontólogo más ocupado del mundo lo active en minutos.

---

## Mercado objetivo

- Odontólogos en Bogotá, Colombia (Usaquén, Chapinero, Cedritos, Chía) — mercado inicial
- Expansión planeada: Colombia completa → México → Perú → resto de Latinoamérica
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
Asistente de IA clínica alojado en Google NotebookLM, entrenado exclusivamente con una biblioteca curada de 27 documentos clínicos rigurosos — papers de PubMed, PMC y SciELO, guías universitarias, manuales de la OPS y protocolos especializados seleccionados por especialistas. **No busca en internet. No improvisa.** Solo responde con base en esa bibliografía — respuestas precisas, trazables y alineadas con los estándares de la profesión.

**Estrategia comercial:**
- Incluido gratis como bono en el Setup Completo ($33)
- Disponible como order bump en el checkout del Self-Setup ($9.99) — precio por definir
- Nombre oficial del cuaderno: *"Banco de conocimiento: protocolos clínicos y gestión de pacientes consultados con IA"*

**Áreas de conocimiento cubiertas:**

- ⚖️ **Marco legal y normativo** — Historia clínica como documento médico-legal (México UAEH, Perú Colegio Odontológico, Cuba SciELO, España Granada); estándares internacionales de documentación clínica; consentimiento informado; protección ante auditorías y procesos legales
- 🩺 **Paciente médicamente complejo** — Gestión de pacientes de alto riesgo (Pacific Univ. Dental); clasificación de riesgo ASA (Redalyc); alergias a antibióticos en odontología (guía diagnóstico + UNMSM Sanmarquina); protocolo clínico de bifosfonatos; reacciones adversas a medicamentos en cavidad oral; medicamentos de alto riesgo 2023 (España); Oral Medicine (Univ. de Florida)
- 🔬 **Historia clínica y anamnesis** — Formularios y modelos de historia dental (Salt Lake CC, SDPT, FuturaLabs); anamnesis en odontología (DtDental Colombia); componentes clínicos del registro dental (DentalCare CE); historia clínica estomatológica (SciELO Cuba); manual de procedimientos clínicos (BVS/OPS); odontología preventiva (Granada)
- 🏥 **Documentación y registros digitales** — Dental records overview (PMC NIH); clinical documentation era EHR (PMC); essentials of medical history-taking (PubMed); clinical components of the dental record (DentalCare CE)
- ⚙️ **Gestión y eficiencia del consultorio** — Ten fundamental components of dental practice management (PubMed); efficiency improvement of dentistry clinics (PMC); boost dental office efficiency 2024 (Adit); workflow automation for dental practices (Dentistry Dashboard); dental practice workflow automations (Keragon); AI for dental practice management (Overjet)

**Los 27 documentos de la biblioteca:**

*Protocolos clínicos numerados (base core del Copilot):*
1. Formulario Historia Dental — Salt Lake Community College
2. Gestión de Pacientes Médicamente Complejos — Pacific Univ. Dental
3. Guía Diagnóstico Alergia a Antibióticos en Odontología
4. Guías Clínicas Oral Medicine — Univ. de Florida
5. Historia Clínica Odontológica — Colegio Odontológico del Perú
6. Historia Clínica como Documento Médico Legal — UAEH México
7. Historia Clínica en Odontología Preventiva — Univ. de Granada
8. Manual de Procedimientos Clínicos Odontológicos — BVS/OPS
9. Protocolo Clínico — Bifosfonatos
10. Reacciones Adversas a Medicamentos en Cavidad Oral
11. Recomendaciones Uso Seguro de Medicamentos Alto Riesgo 2023 — España

*Documentación, registros e historia clínica (fuentes académicas internacionales):*
12. Dental Records - An Overview — PMC NIH
13. Clinical Documentation of Dental Care (era EHR) — PMC
14. Essentials of Medical History-taking in Dental Patients — PubMed
15. Clinical Components of the Dental Record — DentalCare CE
16. La Historia Clínica Estomatológica — SciELO Cuba
17. Alergias en la Atención Dental — UNMSM Odontología Sanmarquina
18. Riesgo Médico Pacientes según Clasificación ASA — Redalyc
19. Qué es la Anamnesis en Odontología — DtDental Colombia
20. Historia Clínica Odontológica — FuturaLabs
21. Modelo de Historia Clínica Dental — SDPT

*Gestión, eficiencia y tecnología en la práctica dental:*
22. Ten Fundamental Components of Dental Practice Management — PubMed
23. Efficiency Improvement of Dentistry Clinics — PMC
24. Boost Dental Office Efficiency 2024 — Adit
25. Workflow Automation for Dental Practices — Dentistry Dashboard
26. Dental Practice Workflow Automations — Keragon
27. AI for Dental Practice Management — Overjet

**Casos de uso principales:**
1. **Consultas en tiempo real** — Antes de atender un paciente complejo: interacciones medicamentosas, contraindicaciones, clasificación ASA, paso a paso de un protocolo de emergencia
2. **Auditoría legal de notas clínicas** — Evaluar si las evoluciones cumplen estándares de protección y confidencialidad (normativas México, Perú, estándares internacionales)
3. **Capacitación de personal auxiliar** — Resúmenes simplificados de protocolos para entrenar asistentes dentales
4. **Preparación de consentimientos informados** — Lenguaje exacto para procedimientos específicos (resección, extracción quirúrgica, blanqueamiento)
5. **Optimización del flujo del consultorio** — Recomendaciones de automatización y eficiencia respaldadas por literatura académica

**Acceso y entrega:**
- Acceso individual vía enlace único encriptado, vinculado al ID de compra en Hotmart
- No requiere instalación — abre en cualquier dispositivo con cuenta de Google
- Política de acceso vinculante: compartir el enlace resulta en revocación automática, inmediata y permanente del acceso y futuras actualizaciones
- Documento de onboarding: `DentBot Copilot — Guía de Acceso.pdf` (se envía al comprador)

**Conocimiento clínico clave extraído de los 27 documentos:**

*Umbrales críticos para toma de decisiones clínicas:*
- **Sangrado/coagulación:** NO operar si INR >3.5, tiempo de sangrado >10 min, o plaquetas <60,000
- **Hipertensión:** Posponer cirugía si PA >160/100 mmHg
- **Post-infarto:** Diferir 3 meses para cirugía, 6 meses para anestesia general
- **DOACs** (Pradaxa, Xarelto, Eliquis): no suspender para procedimientos menores; suspender 24-36h para cirugía extensa
- **Bifosfonatos IV:** contraindicados para cirugía oral y periodoncia quirúrgica; vía oral son relativamente seguros
- **Bifosfonatos (cirugía):** suspender 1-3 meses antes y 3 meses después en procedimientos extensos
- **Índice O'Leary:** referencia <20%; si supera, implementar terapia de higiene antes de tratamiento
- **Clasificación ASA:** 63.3% de pacientes tienen comorbilidades; hipertensión (56.6%) y diabetes (36.6%) son las más frecuentes; 43.3% son ASA II

*Protocolos farmacológicos clave:*
- **Bifosfonatos + cirugía:** clorhexidina desde antes hasta 2 meses post-op; amoxicilina + metronidazol (o clindamicina) 2 días antes a 14 días después
- **Alergias a betalactámicos:** 85-90% son tipo A (predecibles), solo 10-15% son tipo B (inmunológicas reales); la mayoría toleran anestésicos amida — las "alergias reportadas" a anestésicos locales casi nunca son reales
- **Anafilaxia:** epinefrina es el fármaco de elección; antihistamínicos y corticoides como complemento
- **Medicamentos de alto riesgo:** anticoagulantes orales, heparinas, opioides, insulinas, bloqueantes neuromusculares, potasio IV, metotrexato oral
- **Interacciones a vigilar:** eritromicina y ketoconazol potencian warfarina; AINEs y aspirina prolongan sangrado

*Documentación médico-legal:*
- La historia clínica previene el 90% de situaciones de riesgo (UAEH México)
- Elementos obligatorios: anamnesis, examen clínico, diagnóstico, plan de tratamiento, consentimiento informado, historia médica (alergias, medicamentos, enfermedades sistémicas)
- Actualizar historia médica en CADA cita, no solo en la primera
- Documentar rechazos de tratamiento y citas canceladas
- Retención: registros vitales = indefinido; registros importantes = 5-7 años
- Normativas cubiertas: México (UAEH), Perú (Colegio Odontológico), Cuba (SciELO), España (Granada), estándares internacionales

*Eficiencia y automatización del consultorio:*
- Inasistencias (no-show) representan 11-15% de citas; automatizar recordatorios reduce este índice significativamente
- Automatizar tareas administrativas reduce carga operativa en ~40%
- Intervenciones de eficiencia pueden multiplicar ingresos 5x y pacientes atendidos 4x (estudio PMC Irán)
- IA para análisis radiográfico automatiza detección de caries y medición ósea en tiempo real

---

## Proceso de onboarding post-venta

Lo que recibe cada comprador inmediatamente después de pagar en Hotmart.

### Self-Setup ($9.99)
El comprador recibe `DentBot_Plantilla_Bienvenida.pdf` con:
1. **Acceder al link de DentBot** — formulario Tally preconfigurado
2. **Registrar un paciente de prueba** — ficticio o real; la IA genera ambas fichas en segundos
3. **Revisar las fichas en Notion** — Ficha PRE (para el odontólogo) y Ficha POST (para el paciente)

**Tips clave que se le comunican al comprador:**
- Ser detallado en el formulario = fichas más precisas
- Compartir la ficha POST por WhatsApp o imprimirla = diferenciador frente a otros consultorios
- Revisar la ficha PRE 10 minutos antes de cada cita = llegar preparado
- Funciona perfecto desde el celular, sin computador

### Setup Completo ($33)
El comprador recibe `DentBot_Premium_Bienvenida.pdf` con instrucciones para agendar. El proceso es:
1. **WhatsApp al fundador** — mensaje prefabricado, solo presionar enviar
2. **Respuesta en menos de 2 horas** — Rodrigo confirma la compra y coordina horario
3. **Sesión de set-up en vivo (20-40 min)** — configuración adaptada a la especialidad, tipo de pacientes y flujo de trabajo del odontólogo; formulario personalizado con las preguntas relevantes para su práctica; fichas con el nombre e identidad del consultorio
4. **Prueba con paciente real o ficticio** — se valida que todo funciona antes de terminar
5. **Soporte prioritario activo** — cualquier ajuste posterior tiene respuesta prioritaria

### DentBot Copilot (bono del $33 / order bump del $9.99)
El comprador recibe `DentBot Copilot — Guía de Acceso.pdf` con:
- Enlace único encriptado al cuaderno en Google NotebookLM
- Vinculado al ID de compra en Hotmart (política anti-sharing)
- Acceso inmediato desde cualquier dispositivo con cuenta Google

---

## Voz y tono de marca

DentBot habla como un socio, no como un proveedor de software. El tono es cálido, directo y respetuoso del tiempo del odontólogo. Nunca técnico por el gusto de serlo.

### Frases clave de la marca (usar como referencia de copy)
- *"DentBot no es solo una herramienta, es una declaración de intenciones. Estás diciéndole a tus pacientes: 'me importas lo suficiente como para prepararme antes de atenderte.'"*
- *"Un paciente que se siente escuchado y un odontólogo que llega preparado."*
- *"Cuando elegiste DentBot Premium, no compraste un producto, compraste un socio para tu consultorio."*
- *"Tu éxito con DentBot es mi éxito. Así de simple."*
- *"Menos tiempo buscando historiales. Más tiempo conectando con tu paciente."*
- *"No todos los profesionales se atreven a modernizar su flujo de trabajo."* (validación al comprador)

### Principios de comunicación
- **Hablarle al odontólogo como Doctor(a)** — respeto profesional, no condescendencia
- **Enfocarse en el resultado emocional**, no en la tecnología — el odontólogo no compra automatización, compra tiempo y tranquilidad
- **Simplicidad radical en el onboarding** — "no necesitas configurar nada, no necesitas ver tutoriales"
- **Personalización como argumento de venta** — DentBot se adapta al consultorio, no al revés
- **El paciente como beneficiario final** — cada feature se explica desde el impacto en la experiencia del paciente

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

- **Fundador:** Rodrigo Infante
- **WhatsApp:** +57 320 997 4750
- **Email:** roesinf2@gmail.com
- **Marca paraguas:** DailyDuty / Instituto para el Desarrollo Diario
- **Linktree:** linktr.ee/dailyduty
- **OG image:** `og-image.png` (900×1200px)

### Documentos de entrega al comprador
| Archivo | Plan | Contenido |
|---------|------|-----------|
| `DentBot_Plantilla_Bienvenida.pdf` | Self-Setup ($9.99) | Bienvenida + instrucciones de activación en 3 pasos |
| `DentBot_Premium_Bienvenida.pdf` | Setup Completo ($33) | Bienvenida premium + instrucciones para agendar set-up personalizado |
| `DentBot Copilot — Guía de Acceso.pdf` | Copilot (ambos planes) | Acceso al cuaderno NotebookLM + política de uso |

### Recursos de contenido (YouTube)
Videos de referencia usados para construir el conocimiento del proyecto:
- https://www.youtube.com/watch?v=Dtb1cCCKH80
- https://www.youtube.com/watch?v=IM7FJF6AF_w
- https://www.youtube.com/watch?v=Q5Gg7zgWCIo
- https://www.youtube.com/watch?v=G_n8p9DjNYo
- https://www.youtube.com/watch?v=efT-jUY6rhg
- https://www.youtube.com/watch?v=dcLghieKNtA

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

## Estado del arte (al 19 de abril de 2026)

### Hecho
- [x] Landing page completa y publicada en GitHub Pages
- [x] Dos planes de precio activos en Hotmart ($9.99 y $33)
- [x] Card $33 posicionada primero como "Más vendido"
- [x] Barra de escasez animada (40/48 cupos)
- [x] Meta Pixel y Google Analytics integrados
- [x] OG image para redes sociales
- [x] DentBot Copilot agregado como bono en el plan $33
- [x] Cuaderno NotebookLM creado con papers y protocolos clínicos
- [x] Estrategia completa del Copilot documentada (áreas de conocimiento, casos de uso, política de acceso)
- [x] Documento de onboarding del Copilot creado (`DentBot Copilot — Guía de Acceso.pdf`)
- [x] CLAUDE.md expandido con visión del fundador, metas de negocio, tono de marca, proceso de onboarding post-venta y recursos de contenido

### Pendiente
- [ ] Configurar DentBot Copilot como order bump en Hotmart para el plan $9.99
- [ ] Definir precio del order bump del Copilot
- [ ] Video demo embebido en la sección hero (actualmente es thumbnail estático)
- [ ] Testimoniales reales de odontólogos (sección eliminada en refactor anterior)
