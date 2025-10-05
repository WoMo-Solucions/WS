# 🧩 WS — WoMo Soluciónˢ  
## Plataforma Tecnológica Central  

![Estado](https://img.shields.io/badge/🚀_En_Producción-green) ![Licencia](https://img.shields.io/badge/Licencia-🔒_Privada-red) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-Auth_%26_DB-3ECF8E?logo=supabase&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) ![n8n](https://img.shields.io/badge/n8n-Automation-orange?logo=n8n&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white) ![Render](https://img.shields.io/badge/Render-Cloud_Deploy-0099FF?logo=render&logoColor=white)

## 📋 Descripción del Sistema  
**WS — WoMo Soluciónˢ** es la **plataforma tecnológica central** del ecosistema WoMo.  
Opera como el **núcleo corporativo** que unifica autenticación, orquestación de servicios, monitoreo y configuración global de los demás proyectos (ProTrack, GateKeeper, MiStock, etc.).  

Incluye:  
- Autenticación y gestión de roles centralizada (RBAC + JWT)  
- Panel de monitoreo para servicios activos en la nube  
- Módulo de configuración de integraciones (n8n, Supabase, Render)  
- Control de estado y despliegue continuo de cada subsistema  
- API base para consultas corporativas y auditoría técnica  

## 🛠 Stack Tecnológico
**Backend:**
- Flask (Python 3.12)  
- Control de roles y autenticación JWT  
- Conexión directa con Supabase (REST API / RLS)  

**Base de Datos:**
- PostgreSQL gestionado por **Supabase**  
- Schema dedicado: `womo_site`  
- Políticas **RLS** activas en todas las tablas críticas  

**Frontend:**
- HTML5, CSS3 (Bootstrap 5), JavaScript (ES6+)  
- Configuración dinámica mediante `config.js`  
- Comunicación directa con el backend (`/health`, `/auth/me`)  

**Automatizaciones:**
- **n8n**: flujos automatizados de monitoreo, correo, alertas y jobs programados  
- Integración con Gmail API, Supabase Webhooks y Render Deploy Hooks  

---

## 🖥️ Infraestructura
**Render (Producción):**  
- Servicios separados: `ws-frontend`, `ws-backend`, `ws-n8n` (todos Dockerizados)  
- HTTPS forzado, variables de entorno seguras y CI/CD automático  

**Supabase:**  
- Autenticación (Auth) + PostgreSQL con RLS  
- Backups automáticos y métricas integradas  
- Conexión segura con claves gestionadas (anon / service role)  

**n8n:**  
- Imagen `n8nio/n8n:latest`  
- Encriptación avanzada con `N8N_ENCRYPTION_KEY`  
- Volumen persistente `/home/node/.n8n`  

**Monitoreo:**  
- Logs estructurados y visualización de estado por API `/health`  
- Integración de alertas en tiempo real vía n8n  

---

## 🚀 Próximas Implementaciones  
- Dashboard centralizado para métricas globales de proyectos WoMo  
- Gestión multi-tenant por schema (12 proyectos integrados)  
- Conexión SSO entre PortiFy y ProTrack  
- Panel visual para supervisar cron jobs de n8n  

---

## 🖥️ Estructura del Proyecto  
📁 00 - WS  
├── 📂 backend/ # API central Flask  
│ ├── 📂 app/  
│ │ ├── 📂 core/ # Módulos principales  
│ │ │ ├── auth.py # Autenticación JWT  
│ │ │ └── dashboard.py # Monitoreo /health  
│ │ └── __init__.py  
│ ├── 📄 run.py # Punto de entrada  
│ ├── 📄 Dockerfile  
│ └── 📄 .env.example  
├── 📂 frontend/ # Interfaz base  
│ ├── 📄 index.html  
│ ├── 📄 config.js  
│ ├── 📂 assets/  
│ │ ├── css/styles.css  
│ │ └── js/main.js  
│ └── 📄 Dockerfile  
├── 📂 n8n/ # Automatizaciones  
│ ├── .env  
│ └── README.md  
└── 📄 docker-compose.yml  

---

## 🔍 Características Clave  
- Autenticación y roles centralizados para todo el ecosistema  
- Integración directa con Supabase y Render vía API  
- Healthcheck global para monitoreo de servicios  
- Scripts automatizados con n8n (deploy, backups, alertas)  
- Totalmente modular y escalable para nuevos proyectos  

---

## 🛡️ Seguridad Avanzada  
- Políticas RLS activas en todas las tablas Supabase  
- Cifrado de tokens JWT y credenciales n8n  
- Acceso restringido por dominio (CORS)  
- Claves privadas fuera del frontend (`SERVICE_ROLE` solo backend)  
- Autenticación federada en desarrollo (OAuth planeado)  

---

## 📊 Métricas de Rendimiento  
- Tiempo de respuesta medio: <200ms  
- Disponibilidad objetivo: 99.95%  
- Supervisión de 12 proyectos activos  
- Escalabilidad automática en Render (Docker Containers)  

---

## 📝 Gestión de Versiones  
- Despliegue modular por microservicio (frontend / backend / n8n)  
- Versionado semántico (SemVer)  
- Repositorio GitHub: `00-WS`  
- Integración con Render CI/CD  

---

## 📬 Contacto Corporativo  
**Julián Alberto Ramírez**  
💻 Socio Fundador & Visionario Tecnológico  
⚙️ Automatización | 🧩 Soluciones software | 💡 Innovador Tecnológico | 🔍 Apasionado por IA  
<img width="222" height="29" alt="Logo WSˢ" src="https://github.com/user-attachments/assets/24519130-f605-4762-a4f2-374c450f2b64" />  
🏢 **Soluciones Tecnológicas Avanzadas – WoMo Soluciónˢ**  
<img width="150" height="150" alt="Logo" src="https://github.com/user-attachments/assets/09c23a95-e483-452e-880f-e7c90c222014" />  

💡 **Notas Técnicas:**  
Este sistema está diseñado para:  
✅ Unificar la administración y autenticación de todo el ecosistema WoMo  
✅ Integrar automatizaciones corporativas con n8n  
✅ Garantizar seguridad, trazabilidad y control centralizado  

“**La excelencia técnica al servicio de la gestión eficiente.**”  

📅 **Control de Versiones**  
![Versión](https://img.shields.io/badge/Versión-3.2.0-blue) ![Última Actualización](https://img.shields.io/badge/Actualizado-Oct_2025-green)
