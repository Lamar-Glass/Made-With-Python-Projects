# 🗺️ The AI Engineer Roadmap

> **The plan:** ~40 projects, 6 phases, roughly 12–15 months from "fun beginner scripts" to "I trained and shipped my own models." Every project has a finish line so you always know when you're done.
>
> **The rule:** *One project at a time. Build it, break it, ship it, write about it.*

Assumes **10–15 focused hours per week**. If you have less, don't skip projects — stretch the calendar (see [Adjusting the pace](#-adjusting-the-pace)).

---

## 📊 Phase Overview

| Phase | Theme | Duration | Projects | You'll be able to… |
|:-----:|-------|:--------:|:--------:|--------------------|
| 0 | Setup | 1 weekend | — | Run, commit, and push code comfortably |
| 1 | Fun beginner | Weeks 1–6 | 9 | Write a CLI from scratch without a tutorial |
| 2 | Confident builder | Months 2–3 | 6 | Design and ship a tested API with a database |
| 3 | Data & classic ML | Months 4–5 | 6 | Train a model and *prove* it works |
| 4 | Deep learning & NLP | Months 6–9 | 7 | Train, fine-tune, and serve neural networks |
| 5 | LLM engineering | Months 9–12 | 6 | Ship an LLM product guarded by evals |
| 6 | Mastery | Year 2+ | 8 | Build what other engineers only use |

---

## Phase 0 — Setup *(1 weekend)*

Not a project, but the launchpad.

- [ ] Install Python 3.12+ and [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- [ ] Configure git identity + SSH key; confirm you can push to this repo
- [ ] Pick an editor (VS Code / Cursor) and learn: run file, debug breakpoint, integrated terminal
- [ ] Create a test project: `uv init hello && cd hello && uv run main.py`
- [ ] Learn just enough Markdown to write READMEs (headings, code blocks, tables, links)

**Checkpoint:** you can create a folder, write a script, run it, commit it, and push it — all from the terminal, no googling.

---

## Phase 1 — Fun Beginner: *Make the computer do things* *(weeks 1–6)*

**Mindset:** small, playful, finishable. 1–3 days per project. The goal is fluency, not impressiveness — typing code without fighting the syntax.

**Concepts earned:** control flow, functions, data structures, files & JSON, `argparse`, `random`/`secrets`, `requests`, error handling, environment variables.

| # | Project | You build | Core lesson | ⭐ Stretch |
|:-:|---------|-----------|-------------|-----------|
| 01 | **Number Guessing Game** | Computer picks a number, player guesses with hints | Loops, conditionals, input validation that never crashes | Difficulty levels, high-score file |
| 02 | **Text Adventure / Mad Libs** | A branching story in the terminal | Strings, f-strings, dicts, program state | Inventory system, save/load game |
| 03 | **Dice Roller & Coin Flip** | `dice 3d6+2` on the command line | Functions, `argparse`, clean CLI design | Parse full dice notation (`2d20kh1`) |
| 04 | **Todo CLI** | `add / list / done / remove`, data survives restart | Lists, dicts, JSON read/write | Due dates, priorities, color output |
| 05 | **Password Generator + Strength Meter** | Secure passwords + entropy scoring | `secrets` (not `random`!), string manipulation | Check against HaveIBeenPwned's k-anonymity API |
| 06 | **Unit & Currency Converter** | `convert 100 usd eur` | First API calls, env-var API keys, caching responses to disk | Offline fallback with saved rates |
| 07 | **Quiz Flashcards** | Deck of cards from CSV, quiz mode, score tracking | First OOP: `Card` & `Deck` classes | Track accuracy over time, simple spaced repetition |
| 08 | **Weather CLI** | Current weather for any city, pretty output | API error handling (bad city, no network), `rich` | 3-day forecast, `--json` flag |
| 09 | **Quotes Scraper** | Scrape quotes.com (or similar) → CSV | `requests` + `BeautifulSoup`, pagination | Respect `robots.txt`, rate limiting, resume support |

**✅ Phase checkpoint:** sit down with no internet and write a ~100-line CLI (data + user input + a file that persists). If you can, you're ready.

---

## Phase 2 — Confident Builder: *Real programs, real users* *(months 2–3)*

**Mindset:** now things get *used* — by you, forever. 1–2 weeks per project. Quality bar goes up: tests, structure, READMEs that a stranger could follow.

**Concepts earned:** OOP + dataclasses, SQLite & ORMs, FastAPI + Pydantic, `asyncio`/`httpx`, pytest, GitHub Actions CI, logging, deployment.

| # | Project | You build | Core lesson | ⭐ Stretch |
|:-:|---------|-----------|-------------|-----------|
| 10 | **Expense Tracker** | CLI or TUI app, SQLite storage, monthly reports + matplotlib charts | Schema design, SQL, separation of logic/UI | Excel export, budget alerts |
| 11 | **Flashcards 2.0 — a real package** | Rebuild project 07 as an installable package with tests | `pyproject.toml`, pytest + fixtures, GitHub Actions CI | Publish to TestPyPI, `pipx install` it |
| 12 | **URL Shortener API** | FastAPI service: shorten, redirect, click stats | REST design, Pydantic validation, auto docs | Rate limiting; deploy on Fly.io/Render |
| 13 | **Async News Aggregator** | Fetch 5 sources *concurrently*, dedupe, print a digest | `asyncio`, `httpx.AsyncClient`, gather | < 3 seconds total; email the digest |
| 14 | **Daily Digest Bot** | Scheduled scrape → email/Telegram message (cron or GH Actions) | Running unattended, logging, failure alerts | SQLite state to dedupe across days |
| 15 | **Terminal Dashboard** | Pomodoro timer + stats with Textual | TUI frameworks, event loops | Persistent stats, ASCII charts |

**✅ Phase checkpoint:** design an app's data model and API *on paper first*, build it, and the paper survives contact with reality.

---

## Phase 3 — Data & Classic ML: *Learn from data* *(months 4–5)*

**Mindset:** the ML begins. Every project now splits: **explore → train → evaluate honestly → ship**. The word of the phase is *honesty* — no leaking test data, no cherry-picked metrics.

**Concepts earned:** numpy, pandas, matplotlib/seaborn, Jupyter, scikit-learn, train/test splits, cross-validation, overfitting, precision/recall, feature engineering, pipelines, model persistence.

| # | Project | You build | Core lesson | ⭐ Stretch |
|:-:|---------|-----------|-------------|-----------|
| 16 | **EDA Notebook** | Pick a dataset you *actually care about*; 10 charts + written findings | pandas groupby, joins, storytelling with data | Publish as a blog post |
| 17 | **Data Cleaning Pipeline** | Messy CSV → clean parquet, as tested functions | Nulls, duplicates, types; reproducible pipelines | Run it on 1M rows; measure time |
| 18 | **Spam Detector** | TF-IDF + Naive Bayes / logistic regression; CLI to predict one message | Text featurization, confusion matrix, precision/recall trade-offs | Ship as an API |
| 19 | **Price/Salary Predictor** | Regression with feature engineering & cross-validation | MSE/MAE/R², why R² lies, leakage in features | Uncertainty estimates (quantile regression) |
| 20 | **Movie Recommender** | "Because you watched X…" from embeddings | Cosine similarity, vector math (the foundation of all LLM work!) | Hybrid: content + collaborative |
| 21 | **Customer Segmentation** | KMeans clusters + PCA visualization | Unsupervised learning, choosing k, interpreting clusters | Profile each cluster in plain English |

**✅ Phase checkpoint:** explain overfitting to a friend in one minute, and show a project where you prevented it (split strategy) and *proved* your number.

---

## Phase 4 — Deep Learning & NLP *(months 6–9)*

**Mindset:** from *using* models to *training* them. Learn PyTorch properly — it's the industry standard. 2–4 weeks per project. Debugging a training loop is the skill.

**Concepts earned:** tensors, autograd, training loops, loss & optimizers, CNNs, transfer learning, Hugging Face ecosystem, tokenization, embeddings, transformers, RAG.

| # | Project | You build | Core lesson | ⭐ Stretch |
|:-:|---------|-----------|-------------|-----------|
| 22 | **MNIST From Scratch** | Your first neural net, written by hand | Tensors, autograd, the training loop: forward → loss → backward → step | 98%+ accuracy; plot the loss curve |
| 23 | **CIFAR-10 CNN** | Convolutional net + data augmentation | Convolutions, pooling, augmentation, regularization | Beat your own baseline with a ResNet |
| 24 | **Custom Image Classifier** | Fine-tune a pretrained model on *your own* photos (plants, fashion, anything) | Transfer learning, dataset collection & labeling | Ship it as an app your friends can use |
| 25 | **Text Classifier, Fine-tuned** | Fine-tune a small transformer (e.g. DistilBERT) on a dataset | Hugging Face `Trainer`, tokenization, datasets library | Push model to the HF Hub |
| 26 | **Chat With Your Docs (RAG v1)** | Embeddings + ChromaDB + LLM API → Q&A over your PDFs | Chunking, embeddings, retrieval, prompt assembly | Compare retrieval strategies; cite sources |
| 27 | **Transcription App** | Whisper → transcript → structured summary/notes | Speech-to-text, working with audio, longer pipelines | Batch mode; meeting-notes generator |
| 28 | **Semantic Search Engine** | Search your own notes by *meaning*, not keywords | Vector search — the core skill of modern AI engineering | Local embeddings; hybrid keyword+vector |

**✅ Phase checkpoint:** train a model, diagnose whether it's overfitting or underfitting from the curves, fix it, and save it for reuse — without a tutorial open.

---

## Phase 5 — LLM Engineering: *Production AI* *(months 9–12)*

**Mindset:** AI engineering ≠ prompt tricks. It's **product engineering around unreliable components**: evals, guardrails, cost, latency, UX. This phase builds a hirable portfolio.

**Concepts earned:** structured outputs, function/tool calling, agents, streaming, memory, RAG at production quality, evaluation (RAGAS, LLM-as-judge), observability/tracing, cost engineering, Docker, deployment.

| # | Project | You build | Core lesson | ⭐ Stretch |
|:-:|---------|-----------|-------------|-----------|
| 29 | **Production RAG API** | Project 26 rebuilt properly: FastAPI + vector DB + citations + **evals** | Chunking strategies, retrieval metrics, regression gates | Deploy publicly; run evals in CI |
| 30 | **Tool-Using Agent** | Agent that can search the web, read pages, and answer with sources | Function calling, agent loops, stopping conditions | Sandbox tools safely |
| 31 | **Multi-Agent System** | Researcher + Writer + Critic pipeline that produces a report | Decomposition, orchestration, when agents help vs hurt | Human-in-the-loop checkpoint |
| 32 | **Chat App with Memory** | Streaming chat, conversation history, SQLite persistence, multiple sessions | Streaming (SSE), memory strategies, token budgeting | Summarize old turns to save context |
| 33 | **Eval Pipeline** | Golden dataset + LLM-as-judge; blocks changes that regress quality | The skill that separates hobbyists from professionals | Wire evals into GitHub Actions |
| 34 | **Ship One AI Product** | Pick your best project. Dockerize, add auth + tracing, deploy, get 10 real users | End-to-end ownership: cost, latency, errors, feedback | Landing page + analytics; charge $1 for it |

**✅ Phase checkpoint:** an LLM app is live, a stranger used it, and your evals caught a regression before your users did.

---

## Phase 6 — Mastery *(year 2+)*

**Mindset:** depth. Build the things you've only *used*. This is what turns "AI user" into "AI engineer people seek out."

| # | Project | You build | Why it matters |
|:-:|---------|-----------|----------------|
| 35 | **GPT From Scratch** | nanoGPT-style: train a small transformer on your own corpus | You'll never be intimidated by "LLM" again |
| 36 | **Serve an Open-Weight Model** | vLLM or llama.cpp behind an API; quantization, KV cache, throughput tuning | Inference engineering — a rare, paid skill |
| 37 | **Vector DB From Scratch** | Implement an ANN index (even a simple HNSW/IVF) | You'll understand retrieval at a depth most don't |
| 38 | **Rust × Python** | Rewrite a hot Python path in Rust (PyO3) — see the Rust repo | Performance engineering for AI systems |
| 39 | **MLOps Pipeline** | Experiment tracking (MLflow/W&B), model registry, drift monitoring, retraining triggers | ML that survives contact with production |
| 40 | **Research Replication** | Reimplement a paper (attention, LoRA, or diffusion) from scratch | Reads papers → builds things. The compounding skill. |
| 41 | **OSS Contributions** | PRs to Hugging Face, LangChain, or a library you use | Proof of skill at industry scale |
| 42 | **AI Safety Project** | Red-teaming harness or guardrail system for LLM apps | The most future-proof skill in the field |

**✅ Mastery checkpoint:** you can go from *paper or idea* to *deployed system* without waiting for a tutorial to exist.

---

## 🗓️ Weekly Rhythm (suggested)

| Day | Focus |
|-----|-------|
| Mon–Wed | Build (new feature or next project step) |
| Thu | Debug + test what you built |
| Fri | **Ship**: commit, update README, write the retro |
| Sat | Study: read docs/chapters *related to next week's problem* |
| Sun | Rest or refactor an old project (optional) |

**The Friday ritual is the whole system.** An unfinished project teaches half of what a shipped one does.

---

## 🐢 Adjusting the Pace

- **5 h/week?** Same order, half the speed → ~2 years to Phase 5. Totally fine.
- **25 h/week?** You can compress phases 1–2 (they're fluency-building), but don't skip the projects.
- **Already know some Python?** Do projects 01–09 as a timed gauntlet: if each takes < 1 hour, jump to Phase 2.
- **Stuck two weeks on one project?** Cut scope, ship the smaller version, move on. A shipped 60% project beats an abandoned 100% idea.

---

## 📚 Curated Free Resources (only what the schedule needs)

| When | Resource |
|------|----------|
| Phase 1 | [Python docs tutorial](https://docs.python.org/3/tutorial/), [Real Python](https://realpython.com/) |
| Phase 2 | [FastAPI docs](https://fastapi.tiangolo.com/), [pytest docs](https://docs.pytest.org/), [Automate the Boring Stuff](https://automatetheboringstuff.com/) |
| Phase 3 | [Kaggle Learn](https://www.kaggle.com/learn), [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) |
| Phase 4 | [PyTorch tutorials](https://pytorch.org/tutorials/), [Hugging Face Course](https://huggingface.co/learn) (free, excellent) |
| Phase 5 | [HF Agents Course](https://huggingface.co/learn), [RAGAS docs](https://docs.ragas.io/), [promptingguide.ai](https://www.promptingguide.ai/) |
| Phase 6 | [nanoGPT](https://github.com/karpathy/nanoGpt), [Karpathy's Zero to Hero](https://karpathy.ai/zero-to-hero.html), papers w/ code |

---

## 🏁 Progress Tracker

- [ ] Phase 0 — setup complete
- [ ] Phase 1 — 9/9 shipped · *checkpoint passed*
- [ ] Phase 2 — 6/6 shipped · *checkpoint passed*
- [ ] Phase 3 — 6/6 shipped · *checkpoint passed*
- [ ] Phase 4 — 7/7 shipped · *checkpoint passed*
- [ ] Phase 5 — 6/6 shipped · *checkpoint passed*
- [ ] Phase 6 — mastery capstones (ongoing)

*Update this file as you go. Future-you is the audience.*
