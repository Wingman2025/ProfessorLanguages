# Spanish Teaching App

A web application for Spanish teachers and students, built with **FastAPI**, **Jinja2**, **Bootstrap**, and **Vanilla JavaScript**. It includes interactive challenges:

- **One-Minute Challenge**: Generate simple everyday topics.
- **Word Hot Potato**: Produce single Spanish vocabulary words.
- **Scenario Generator**: Create short role-play scenarios with assigned roles.

Agents powered by **openai-agents==0.0.13** to orchestrate prompt execution; no chat completion endpoints are used.

## Prerequisites

- Python 3.11+
- Git
- PostgreSQL (local or cloud)

## Setup Locally

1. Clone repository:
   ```bash
   git clone <your-repo-url>
   cd ProfessorLanguages
   ```
2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Create `.env` file in `backend/` with:
   ```ini
   OPENAI_API_KEY=<your-openai-key>
   DATABASE_URL=postgresql://user:pass@host:port/dbname
   ```
5. Run database migrations:
   ```bash
   cd backend
   alembic upgrade head
   ```
6. Start development server:
   ```bash
   uvicorn app:app --reload
   ```
7. Open browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Migration Configuration (TOML)

A `pyproject.toml` configures Alembic:

```toml
[tool.alembic]
script_location = "backend/alembic"
sqlalchemy_url = "${DATABASE_URL}"
```

## Deployment on Railway

1. Push code to GitHub.
2. Create a Railway project and link the GitHub repo.
3. Set environment variables in Railway dashboard:
   - `OPENAI_API_KEY`
   - `DATABASE_URL`
4. Railway will detect the `Procfile`:
   ```Procfile
   web: uvicorn backend.app:app --host 0.0.0.0 --port $PORT
   ```
5. Deploy and enjoy!

## Project Structure
```
.
├── .gitignore
├── Procfile
├── pyproject.toml
├── README.md
└── backend
    ├── app.py
    ├── database.py
    ├── services
    │   └── agentjorge.py
    ├── alembic.ini
    ├── alembic
    ├── requirements.txt
    ├── static/
    └── templates/
```
