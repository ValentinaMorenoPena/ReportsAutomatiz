📊 Reportes Integraciones
Sistema modular en Python para procesamiento y generación automática de reportes de:

✅ Contabilidad INT05
✅ Tesorería INT05
✅ Valorización INT06
✅ Instrumentos
Cada ejecución genera archivos Excel estructurados con hojas estandarizadas y nombre versionado por fecha y hora.

🏗 Arquitectura del Proyecto

Reportes integraciones/
│
├── .env
├── main.py
├── requirements.txt
│
├── config/
│   └── settings.py
│
├── data/
│   ├── contabilidad/
│   │   ├── input/
│   │   └── output/
│   ├── tesoreria/
│   │   ├── input/
│   │   └── output/
│   └── valorizacion/
│       ├── input/
│       └── output/
│
├── models/
│   └── schemas.py
│
├── request/
│   └── contabilidad_request.py
│
├── services/
│   ├── contable.py
│   ├── tesoreria.py
│   ├── valorizacion.py
│   ├── excel_writer.py
│   ├── json_loader.py
│   └── parsers/
│       ├── base_parser.py
│       └── contabilidad_parser.py
│
├── utils/
│   └── helpers.py
│
└── venv/
🧠 Diseño Arquitectónico
El sistema sigue una arquitectura basada en:

✅ Service Layer Pattern
✅ Separación por dominios
✅ Centralización de configuración
✅ Estandarización de respuesta
✅ Generación automática de versionado de archivos

🔄 Flujo de Ejecución
main.py inicia el proceso.
Se construyen rutas desde config/settings.py.
Cada dominio:
Carga JSON desde data/{dominio}/input
Procesa la información
Construye estructura estándar
Genera archivo Excel con timestamp
Se guarda en data/{dominio}/output.
📄 Estructura del Excel Generado
Cada archivo Excel contiene 3 hojas:

1️⃣ Records
Contiene los registros procesados.

2️⃣ Pagination
Información estructural del resultado:

Campo	Descripción
totalRecords	Total de registros
pageSize	Tamaño de página
totalPages	Total de páginas
currentPage	Página actual
generatedAt	Timestamp UTC
3️⃣ Status
Información del estado del proceso:

Campo	Descripción
code	200 / 500
success	true / false
message	Mensaje del proceso
timestamp	Fecha ejecución
🕒 Nueva Funcionalidad: Versionado Automático de Archivos
Cada archivo generado incluye fecha y hora de ejecución en el nombre.

✅ Formato:


{dominio} DD-MM-YYYY HH-MM.xlsx
✅ Ejemplo real:

contabilidad 17-02-2026 14-40.xlsx
tesoreria 17-02-2026 14-40.xlsx
valorizacion 17-02-2026 14-40.xlsx
⚠ Nota: Se usa HH-MM en lugar de HH:MM para compatibilidad con Windows.

📂 Estructura de Datos
Cada dominio debe tener:



data/{dominio}/input/input.json
El archivo puede contener:

json

[]
O una lista de objetos JSON válidos.

⚙️ Instalación
1️⃣ Activar entorno virtual
PowerShell:

powershell

.\venv\Scripts\Activate.ps1
CMD:

cmd

venv\Scripts\activate
2️⃣ Instalar dependencias
bash

pip install -r requirements.txt
🚀 Ejecución
Desde la raíz del proyecto:

bash

python main.py
Salida esperada en consola:



===================================
 Iniciando procesamiento reportes 
===================================
===================================
 Procesamiento finalizado ✅
===================================
📦 Tecnologías Utilizadas
Python 3.13
Pandas
OpenPyXL
python-dotenv
🧩 Componentes Clave
main.py
Orquesta la ejecución de todos los dominios.

config/settings.py
Centraliza rutas y variables de entorno.

services/
Contiene la lógica de negocio por dominio.

excel_writer.py
Servicio estándar para escribir:

Records
Pagination
Status
helpers.py
Contiene:

Construcción de respuestas estándar
Manejo de errores
Generación de nombre de archivo con timestamp
✅ Buenas Prácticas Implementadas
✔ DRY (Don't Repeat Yourself)
✔ Single Responsibility Principle
✔ Estandarización de respuestas
✔ Manejo uniforme de errores
✔ Versionado automático de archivos
✔ Arquitectura modular
⚠️ Consideraciones Importantes
Ejecutar siempre desde la raíz del proyecto.
No modificar venv/.
Verificar que existan archivos JSON en cada input/.
No usar : en nombres de archivo (Windows restriction).
