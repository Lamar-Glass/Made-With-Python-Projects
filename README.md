<div align="center">

# 🐍 Made With Python

**A living portfolio — every project I build on the path from Python beginner to AI engineer.**

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Roadmap](https://img.shields.io/badge/Roadmap-AI_Engineer-8A2BE2?style=flat-square)](ROADMAP.md)
[![License: GPL v3](https://img.shields.io/badge/License-GPL_v3-blue?style=flat-square)](LICENSE)

*Every project teaches something new. Every project ships.*

</div>

---

## 📖 About

This repo is my project-based learning lab. Instead of collecting certificates, I **build one real thing at a time**, in public, following the schedule in [ROADMAP.md](ROADMAP.md) — from fun beginner scripts all the way to training and serving my own models.

The roadmap is the plan. This README is the scoreboard.

## 🗺️ The Path (summary)

| Phase | Theme | Rough timeline | Flagship outcome |
|:-----:|-------|:---------------:|-------------------|
| **1** | Fun beginner — *make the computer do things* | Weeks 1–6 | Comfortable writing CLIs from scratch |
| **2** | Confident builder — *real programs, real users* | Months 2–3 | Tested APIs + apps with databases |
| **3** | Data & classic ML — *learn from data* | Months 4–5 | Models with honest evaluation |
| **4** | Deep learning & NLP | Months 6–9 | Training & fine-tuning neural nets |
| **5** | LLM engineering — *production AI apps* | Months 9–12 | Shipped, evaluated LLM products |
| **6** | Mastery | Year 2+ | Models trained & served from scratch, OSS contributions |

👉 **Full schedule, acceptance criteria, and stretch goals: [ROADMAP.md](ROADMAP.md)**

## ✅ Project Catalog

Each project lives in its own numbered folder. Status legend: ⬜ planned · 🚧 building · ✅ shipped

| # | Project | Phase | Core concepts | Status |
|:-:|---------|:-----:|---------------|:------:|
| 01 | [Number Guessing Game](01-guessing-game/) | 1 | loops, input validation, `random` | ⬜ |
| 02 | [Text Adventure / Mad Libs](02-text-adventure/) | 1 | strings, dicts, branching | ⬜ |
| 03 | [Dice Roller & Coin Flip](03-dice-roller/) | 1 | functions, `argparse` | ⬜ |
| 04 | [Todo CLI](04-todo-cli/) | 1 | JSON persistence, file I/O | ⬜ |
| 05 | [Password Generator + Strength Meter](05-password-forge/) | 1 | `secrets`, entropy, first API | ⬜ |
| 06 | [Unit & Currency Converter](06-converter/) | 1 | `requests`, env vars, caching | ⬜ |
| 07 | [Quiz Flashcards](07-flashcards/) | 1 | OOP first taste, CSV | ⬜ |
| 08 | [Weather CLI](08-weather-cli/) | 1 | APIs, error handling, `rich` | ⬜ |
| 09 | [Quotes Scraper](09-quotes-scraper/) | 1 | BeautifulSoup, CSV export | ⬜ |

*Later projects get added here as I reach each phase — the full list lives in the [ROADMAP](ROADMAP.md).*

## 📁 How Every Project Is Structured

```
NN-project-name/
├── README.md         # started BEFORE coding, finished after shipping
├── pyproject.toml    # dependencies & metadata
├── src/              # the code
└── tests/            # from Phase 2 onward
```

New project? `cp docs/project-template.md <NN-name>/README.md` and fill it in.

## ▶️ Running a Project

All projects use [uv](https://docs.astral.sh/uv/) for dependency management:

```bash
cd NN-project-name
uv sync          # create venv + install deps
uv run main.py   # run it
```

## 🧠 My Learning Rules

1. **Build, don't just watch.** No tutorial counts until the code is mine.
2. **One project at a time.** Finish, ship, then start the next.
3. **Ship publicly.** Every project ends with a commit, a README, and a share.
4. **README first.** Define "done" before writing code; write the retro after.
5. **Stuck > 45 min?** Write the problem down, rubber-duck it, then search, then ask.
6. **Refactor one old project per phase.** Revisiting old code is how growth becomes visible.

## 📄 License

Everything here is released under the [GPL-3.0 License](LICENSE) — learn from it, fork it, build on it.
