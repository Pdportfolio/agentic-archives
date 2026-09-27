# ASE Lead Qualification Pipeline

AI-powered lead qualification: Streamlit intake form → voice session → 4 AI agents → CRM dashboard.

## Quick Start (VS Code)

1. Open this folder in VS Code
2. Open Agent Chat panel (Ctrl+Alt+I)
3. Type: **start**
4. Paste your `.env` credentials when prompted
5. Done — pipeline starts automatically

## Architecture

```
Streamlit Form (8501) → FastAPI (8000) → Whisper STT → gpt-oss:20b-cloud
     → 4 AI Agents → leads.csv → Streamlit CRM Dashboard
```

## Manual Start

```bash
# 1. Create .env (copy .env.example → .env, fill values)
cp .env.example .env

# 2. Create venv + install
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Mac/Linux
pip install -r requirements.txt

# 3. Terminal A — FastAPI pipeline
python main.py

# 4. Terminal B — Streamlit dashboard
streamlit run dashboard.py

# 5. Optional: test without Streamlit
python scripts/test_webhook.py
```

## Environment Variables

| Variable | Description |
|---|---|
| `GMAIL_USER` | Gmail address used to send emails |
| `GMAIL_PASSWORD` | 16-char Gmail App Password (needs 2FA enabled) |
| `GMAIL_TO` | Sales rep email for hot lead alerts |
| `HF_TOKEN` | HuggingFace token (only if Whisper download fails) |
| `BASE_URL` | Always `http://localhost:8000` — never change |

## Models

| Task | Model |
|---|---|
| Speech-to-Text | Whisper `small` (local, ~244MB) |
| Real-time voice session | `gpt-oss:20b-cloud` via Ollama |
| All 4 analysis agents | `gpt-oss:20b-cloud` via Ollama |

## Project Structure

```
ase-lead-pipeline/
├── main.py                    ← Entry point
├── dashboard.py               ← Streamlit UI
├── requirements.txt
├── .env.example
├── routes/                    ← FastAPI routers
├── pipeline/                  ← Orchestrator + voice session
├── agents/                    ← 4 AI agents
├── utils/                     ← CSV, email, validation, logger
├── static/session.html        ← Browser voice UI
├── data/leads.csv             ← Auto-created CRM
├── docs/                      ← Architecture + sample data
└── scripts/test_webhook.py    ← Quick test
```

## Demo Flow

1. Open `http://localhost:8501` → fill intake form → Submit Lead
2. Watch `python main.py` terminal → "Lead received", "Email sent"
3. Check Gmail inbox → click session link → `http://localhost:8000/session/{id}`
4. Click Start Session → speak answers to 8 questions
5. Watch terminal → 4 agents analyse → lead scored
6. Open `http://localhost:8501` CRM tab → Refresh → see score + status

## Notes

- Tunnel not needed — browser and server both run on localhost
- Gmail needs 2FA + App Password (not your account password)
- `gpt-oss:20b-cloud` routes through Ollama to cloud — internet required for analysis
- Whisper small downloads once on first run (~244MB)
- Lead score > 70 triggers automatic sales rep email alert
