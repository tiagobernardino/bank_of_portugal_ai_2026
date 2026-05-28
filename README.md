# Bank of Portugal — AI Tools for Economics Research (2026)

12-hour course on AI tools for economics research and policy, delivered at Banco de Portugal.

**Sessions**: Mon 25 May, Fri 29 May, Mon 22 June, Tue 23 June (2026). Each day 10:30–12:00 and 14:30–16:00.

**Instructor**: João B. Sousa, Nova SBE — <joao.sousa@novasbe.pt>.

## What's in this repo

```
bank_of_portugal_ai_2026/
├── slides/
│   ├── decks/        # Marp slide source (.md) and rendered .pdf
│   └── assets/       # Figures and diagrams
├── code/             # Demo scripts written during class
├── data/
│   ├── raw/          # Original data (e.g. cpi.csv from FRED)
│   └── processed/    # Derived files written by demo code
├── papers/           # PDFs used in the Session 2 literature-triage demo
└── docs/             # Syllabus (.md and .pdf)
```

Session-by-session plan: [`docs/syllabus.pdf`](docs/syllabus.pdf).

## Prerequisites

Claude Code (with an active subscription) and git. VS Code + Copilot is optional.

## Getting the repo

```
git clone https://github.com/jbrogueira/bank_of_portugal_ai_2026.git
cd bank_of_portugal_ai_2026
```

## Following along

- Slides are PDFs in `slides/decks/`.
- The Session 1 demo reads `data/raw/cpi.csv` (US CPI from FRED) and produces `data/processed/inflation.csv` via a Python script the agent writes during class.
- To work in the repo yourself: `claude` (or your CLI of choice).

## Running the Python yourself

The demo scripts need Python ≥ 3.11 and a couple of packages:

```
pip install -r requirements.txt
```

Run them from the repo root — paths such as `data/raw/cpi.csv` are relative. Or just let Claude Code set up the environment and run the script for you.
