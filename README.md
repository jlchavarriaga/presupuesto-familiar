# presupuesto-familiar
Sistema de gestión de presupuestos familiares con Flask

# Sistema de Presupuesto Familiar

Aplicación web para gestión de presupuestos familiares desarrollada con:
- Python + Flask (Backend)
- MySQL (Base de datos)
- Bootstrap (Frontend)

## Instalación

1. Clonar repositorio:
   ```bash
   git clone https://github.com/tu-usuario/presupuesto-familiar.git
   cd presupuesto-familiar
   ```


2. Crear entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3. Instalar dependencias:
    ```bash
       pip install -r requirements.txt

```bash
/presupuesto-familiar
│
├── /venv/                  # Entorno virtual (ignorado por git)
│
├── /app/                   # Módulo principal
│   ├── __init__.py         # Factory de la aplicación
│   ├── config.py           # Configuración (con .env)
│   │
│   ├── /models/            # Modelos de la base de datos
│   │   ├── __init__.py     # Exportación de modelos
│   │   ├── usuario.py      # Modelo Usuario
│   │   ├── presupuesto.py  # Modelo Presupuesto
│   │   └── ...             # Otros modelos
│   │
│   ├── /routes/            # Controladores/Vistas
│   │   ├── __init__.py     # Inicialización de blueprints
│   │   ├── auth.py         # Autenticación
│   │   ├── presupuesto.py  # Lógica de presupuestos
│   │   └── api/            # Endpoints API REST (opcional)
│   │
│   ├── /services/          # Lógica de negocio
│   │   ├── proyecciones.py # Cálculo de proyecciones
│   │   └── reportes.py     # Generación de reportes
│   │
│   ├── /static/            # Assets estáticos
│   │   ├── /css/
│   │   ├── /js/
│   │   └── /images/
│   │
│   ├── /templates/         # Plantillas Jinja2
│       ├── base.html       # Layout principal
│       ├── auth/           # Plantillas de autenticación
│       └── presupuesto/    # Vistas de presupuesto
│
├── /migrations/            # Migraciones de la BD (generado por Flask-Migrate)
│
├── /tests/                 # Pruebas unitarias/integración
│   ├── conftest.py         # Configuración de pytest
│   ├── test_models.py
│   └── test_routes.py
│
├── .env                    # Variables de entorno (NO se sube a git)
├── .gitignore              # Archivos ignorados
├── requirements.txt        # Dependencias
└── run.py                  # Punto de entrada
```

4. Configurar la base de datos:
   - Crear una base de datos MySQL llamada `presupuesto_familiar`.
   - Configurar las credenciales en `app/config.py`.

5. ejecuta las migraciones:
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

6. EJECUTAR LA APLICACIÓN
   flask run