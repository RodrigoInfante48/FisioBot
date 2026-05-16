# FisioBot — Contexto de proyecto para Claude Code

## Qué es FisioBot

FisioBot es un sistema de automatización de historia clínica / evaluación inicial para fisioterapeutas, vendido como producto digital de pago único. El flujo automatiza el registro del paciente antes de que llegue a la camilla usando cuatro herramientas encadenadas orquestadas por Make.com:

1. **Tally** — El paciente recibe un formulario por WhatsApp y lo llena en 3 minutos desde su celular, sin apps ni login.
2. **Make.com** — Orquesta todo el flujo: recibe la respuesta de Tally, llama a Gemini AI, y distribuye el output a Notion mediante un Router con dos ramas paralelas.
3. **Gemini AI** — Procesa las respuestas una sola vez, extrae lesiones previas, medicamentos y factores de riesgo, y genera el contenido para ambas fichas clínicas.
4. **Notion** — Recibe las dos fichas simultáneas vía el Router de Make y las almacena en el workspace del fisioterapeuta.

### El flujo técnico completo

```
Tally → Make.com → Gemini AI → Router (Make)
                                    ├── Ruta 1: Notion Create → Append → Update  (Ficha PRE, para el fisioterapeuta)
                                    └── Ruta 2: Notion Create → Append → Update  (Ficha POST, para el paciente)
```

### Las dos fichas que genera FisioBot

**Ficha PRE-sesión (para el fisioterapeuta)**
Se crea antes de que el paciente llegue a la camilla. Contiene historia clínica estructurada, escala EVA de dolor, lesiones previas, factores de riesgo y alertas clínicas. El fisioterapeuta la revisa antes de atender.

**Ficha POST-sesión (para el paciente)**
Se crea al mismo tiempo en Notion. Contiene un resumen de la sesión, ejercicios en casa, objetivos de rehabilitación y registro de progreso. El fisioterapeuta la comparte con el paciente al terminar la cita.

### Flujo narrativo completo

Paciente llena Tally → Make procesa → Gemini genera ambas fichas → Router las distribuye a Notion → fisioterapeuta llega y revisa la ficha pre → tiene la sesión → termina y comparte la ficha post con el paciente.

**Propuesta de valor central:** Recuperar 10-15 minutos por sesión eliminando las evaluaciones iniciales repetitivas, los planes de tratamiento sin registro y el abandono de tratamiento — generando automáticamente dos fichas clínicas (una para el fisioterapeuta, una para el paciente) sin intervención manual.

---

## Fundador, visión y metas de negocio

**Fundador:** Rodrigo Infante — DailyDuty / Instituto para el Desarrollo Diario

### La misión
FisioBot nació con una misión clara: **ayudar a la mayor cantidad posible de fisioterapeutas en Colombia y en el mundo** a recuperar su tiempo, elevar su estándar clínico y darle a cada paciente una experiencia que los haga continuar su tratamiento. No es solo un producto digital — es una declaración de intenciones sobre cómo debería funcionar la fisioterapia moderna.

### Metas de negocio (norte del proyecto)
- **Volumen:** Vender muchísimas licencias — el modelo de pago único y precio accesible está diseñado para escalar masivamente sin fricción
- **Impacto geográfico:** Arrancar en Bogotá (Usaquén, Chapinero, Cedritos, Chía), expandir a toda Colombia, y después a México, Perú y el resto de Latinoamérica
- **Impacto real:** Que cada fisioterapeuta que use FisioBot recupere 10-15 minutos por sesión y le dé a su paciente una experiencia que ningún centro de rehabilitación sin IA puede igualar

### Por qué esto importa al desarrollar
Cada decisión de diseño, copy y funcionalidad debe estar orientada a **remover fricción de compra** y a **maximizar el valor percibido**. El producto es barato pero debe sentirse premium. El onboarding debe ser tan simple que el fisioterapeuta más ocupado del mundo lo active en minutos.

---

## Mercado objetivo

- Fisioterapeutas en Bogotá, Colombia (Usaquén, Chapinero, Cedritos, Chía) — mercado inicial
- Expansión planeada: Colombia completa → México → Perú → resto de Latinoamérica
- Perfil: profesional independiente con consultorio propio, no grandes centros de rehabilitación
- Dolor principal: tiempo perdido en evaluaciones repetitivas, planes de tratamiento sin seguimiento y pacientes que abandonan la terapia

---

## Productos y precios

| Producto | Precio | Canal | Estado |
|---|---|---|---|
| Setup Completo | $9.99 USD (pago único) | Hotmart | Por configurar |
| FisioBot Copilot | Order bump en checkout Hotmart | Hotmart | Por configurar |

### Setup Completo — $9.99 ⭐ (más vendido)
- Configuración completa por el equipo FisioBot
- Logo y colores del consultorio en el form
- Sesión de onboarding de 30 minutos
- Soporte prioritario por 30 días
- **🎁 Bono gratuito: FisioBot Copilot** (ver abajo)
- **Link de pago:** *(por definir — links Hotmart propios para FisioBot pendientes)*

### FisioBot Copilot (bono + order bump)
Asistente de IA clínica alojado en Google NotebookLM, entrenado exclusivamente con una biblioteca curada de documentos clínicos rigurosos sobre fisioterapia y rehabilitación. **No busca en internet. No improvisa.** Solo responde con base en esa bibliografía — respuestas precisas, trazables y alineadas con los estándares de la profesión.

**Estrategia comercial:**
- Incluido gratis como bono en el Setup Completo ($9.99)
- Disponible como order bump en el checkout — precio por definir
- Nombre oficial del cuaderno: *"Banco de conocimiento: protocolos clínicos y gestión de pacientes — FisioBot Copilot"*

**Áreas de conocimiento (por definir):**

La biblioteca de documentos del FisioBot Copilot está pendiente de curaduría. Las áreas temáticas previstas son:

- ⚖️ **Marco legal y normativo** — Historia clínica como documento médico-legal para fisioterapeutas; estándares de documentación clínica; consentimiento informado; protección ante auditorías
- 🩺 **Evaluación y escala de dolor** — Uso clínico de la escala EVA; evaluación funcional del paciente; clasificación de riesgo y banderas rojas
- 🔬 **Historia clínica y evaluación inicial** — Modelos de historia clínica en fisioterapia; evaluación postural; anamnesis músculo-esquelética; patologías frecuentes
- 🏥 **Protocolos de rehabilitación** — Protocolos por tipo de lesión; ejercicio terapéutico; manejo del dolor crónico; adherencia al tratamiento
- ⚙️ **Gestión y eficiencia del consultorio** — Automatización de procesos en centros de rehabilitación; seguimiento de progreso; reducción de abandono de tratamiento

**Biblioteca de documentos:** *Por definir — pendiente de curaduría con especialistas en fisioterapia*

**Casos de uso principales:**
1. **Consultas en tiempo real** — Antes de atender un paciente complejo: contraindicaciones, banderas rojas, protocolos de emergencia
2. **Auditoría legal de notas clínicas** — Evaluar si las evoluciones cumplen estándares de protección y documentación
3. **Capacitación de personal auxiliar** — Resúmenes simplificados de protocolos para entrenar asistentes
4. **Diseño de planes de ejercicios** — Recomendaciones respaldadas por literatura para ejercicios en casa
5. **Optimización del flujo del consultorio** — Recomendaciones de automatización y eficiencia respaldadas por literatura académica

**Acceso y entrega:**
- Acceso individual vía enlace único encriptado, vinculado al ID de compra en Hotmart
- No requiere instalación — abre en cualquier dispositivo con cuenta de Google
- Política de acceso vinculante: compartir el enlace resulta en revocación automática, inmediata y permanente del acceso y futuras actualizaciones
- Documento de onboarding: `FisioBot Copilot — Guía de Acceso.pdf` (se envía al comprador)

---

## Proceso de onboarding post-venta

Lo que recibe cada comprador inmediatamente después de pagar en Hotmart.

### Setup Completo ($9.99)
El comprador recibe `FisioBot_Premium_Bienvenida.pdf` con instrucciones para agendar. El proceso es:
1. **WhatsApp al fundador** — mensaje prefabricado, solo presionar enviar
2. **Respuesta en menos de 2 horas** — Rodrigo confirma la compra y coordina horario
3. **Sesión de set-up en vivo (20-40 min)** — configuración adaptada a la especialidad, tipo de pacientes y flujo de trabajo del fisioterapeuta; formulario personalizado con las preguntas relevantes para su práctica; fichas con el nombre e identidad del consultorio
4. **Prueba con paciente real o ficticio** — se valida que todo funciona antes de terminar
5. **Soporte prioritario activo** — cualquier ajuste posterior tiene respuesta prioritaria

### FisioBot Copilot (bono del $9.99 / order bump)
El comprador recibe `FisioBot Copilot — Guía de Acceso.pdf` con:
- Enlace único encriptado al cuaderno en Google NotebookLM
- Vinculado al ID de compra en Hotmart (política anti-sharing)
- Acceso inmediato desde cualquier dispositivo con cuenta Google

---

## Voz y tono de marca

FisioBot habla como un socio, no como un proveedor de software. El tono es cálido, directo y respetuoso del tiempo del fisioterapeuta. Nunca técnico por el gusto de serlo.

### Frases clave de la marca (usar como referencia de copy)
- *"FisioBot no es solo una herramienta, es una declaración de intenciones. Estás diciéndole a tus pacientes: 'me importas lo suficiente como para prepararme antes de atenderte.'"*
- *"Un paciente que se siente escuchado y un fisioterapeuta que llega preparado."*
- *"Cuando elegiste FisioBot Premium, no compraste un producto, compraste un socio para tu consultorio."*
- *"Tu éxito con FisioBot es mi éxito. Así de simple."*
- *"Menos tiempo buscando historiales. Más tiempo rehabilitando a tu paciente."*
- *"No todos los profesionales se atreven a modernizar su flujo de trabajo."* (validación al comprador)

### Principios de comunicación
- **Hablarle al fisioterapeuta como Profesional** — respeto profesional, no condescendencia
- **Enfocarse en el resultado emocional**, no en la tecnología — el fisioterapeuta no compra automatización, compra tiempo y tranquilidad
- **Simplicidad radical en el onboarding** — "no necesitas configurar nada, no necesitas ver tutoriales"
- **Personalización como argumento de venta** — FisioBot se adapta al consultorio, no al revés
- **El paciente como beneficiario final** — cada feature se explica desde el impacto en la experiencia del paciente

---

## Stack técnico

### Automatización del producto
- **Make.com** — Orquestador central del flujo. Conecta Tally, Gemini AI y Notion. Contiene el Router que divide el output en dos ramas paralelas hacia Notion.
- **Tally** — Formulario de historia clínica / evaluación inicial que el paciente llena por WhatsApp
- **Google Gemini AI** — Modelo de IA que procesa las respuestas del formulario (una sola llamada, genera contenido para ambas fichas)
- **Notion** — Base de datos donde se almacenan la Ficha PRE (fisioterapeuta) y la Ficha POST (paciente)

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

1. **Header fijo** — Logo FisioBot + botón WhatsApp
2. **Hero** — Headline de dolor + subheadline de solución + demo de video + prueba social (barrios de Bogotá)
3. **Sección dolor** — 3 problemas específicos del fisioterapeuta (evaluación repetitiva, planes sin registro, paciente que abandonó la terapia)
4. **Sección solución** — 3 pasos del flujo (Tally → Make.com → Gemini → Notion) con mockup de Notion y las dos fichas generadas
5. **Sección oferta/precios** — Barra de escasez (40/48 cupos) + dos cards de precio + ancla de precio vs software tradicional
6. **CTA final** — Demo personalizada por WhatsApp
7. **Barra sticky mobile** — "Empezar ahora" fija en la parte inferior
8. **Footer** — FisioBot by DailyDuty / Instituto para el Desarrollo Diario

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
- **OG image:** `og-image.png` (900×1200px) *(pendiente de actualizar para FisioBot)*

### Documentos de entrega al comprador
| Archivo | Plan | Contenido |
|---------|------|-----------|
| `FisioBot_Premium_Bienvenida.pdf` | Setup Completo ($9.99) | Bienvenida + instrucciones para agendar set-up personalizado |
| `FisioBot Copilot — Guía de Acceso.pdf` | Copilot (bono incluido) | Acceso al cuaderno NotebookLM + política de uso |

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

## Estado del arte (al 22 de abril de 2026)

### Hecho
- [x] Sección 1 — Renombrado global de marca DentBot → FisioBot en `index.html`
- [x] CLAUDE.md reescrito completamente para FisioBot

### Pendiente
- [ ] Link de pago Hotmart propio para FisioBot (Setup Completo)
- [ ] OG image actualizada con identidad visual de FisioBot
- [ ] Video demo propio de FisioBot (actualmente usa video de DentBot)
- [ ] Sección 2 — Hero adaptado al dolor del fisioterapeuta
- [ ] Sección 3 — Dolor adaptado (evaluación repetitiva, planes sin registro, abandono de tratamiento)
- [ ] Sección 4 — Solución adaptada con fichas PRE/POST de fisioterapia
- [ ] Sección 5 — Oferta/precios con links Hotmart de FisioBot
- [ ] Sección 6 — CTA final y Footer con marca FisioBot
- [ ] Contenido de la biblioteca FisioBot Copilot (curaduría con especialistas pendiente)
- [ ] Configurar FisioBot Copilot como order bump en Hotmart
- [ ] Definir precio del order bump del Copilot
- [ ] Testimoniales reales de fisioterapeutas
