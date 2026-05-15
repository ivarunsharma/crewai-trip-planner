# Contributing to crewai-trip-planner

Thank you for considering contributing! This guide will get you from zero to a merged pull request.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Commit Message Format](#commit-message-format)
- [Pull Request Checklist](#pull-request-checklist)
- [Good First Issues](#good-first-issues)

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to uphold it. Please report unacceptable behavior to **contact4varun@gmail.com**.

---

## Ways to Contribute

- **Bug reports** — Open an issue describing what went wrong and how to reproduce it.
- **Feature requests** — Open an issue with the `enhancement` label and describe the use case.
- **Code** — Fix a bug, add a feature, or improve performance.
- **Documentation** — Improve the README, add docstrings, or write a usage guide.
- **Tests** — Add missing unit or integration tests.

---

## Getting Started

### Prerequisites

- Python 3.10+
- A [Serper API key](https://serper.dev) (free tier available)
- An Azure OpenAI resource with a GPT-4o deployment

### 1. Fork and clone

```bash
git clone https://github.com/<your-username>/crewai-trip-planner.git
cd crewai-trip-planner
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install pytest ruff black  # dev tools
```

### 4. Configure environment variables

Copy the example and fill in your keys:

```bash
cp .env.example .env
```

```env
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_API_VERSION=2024-02-01
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4o
SERPER_API_KEY=your_serper_key
```

### 5. Run the app

```bash
streamlit run main.py
```

---

## Development Workflow

1. Create a branch from `main`:
   ```bash
   git checkout -b feat/your-feature-name
   ```
2. Make your changes and write/update tests where applicable.
3. Lint and format before committing:
   ```bash
   ruff check .
   black .
   ```
4. Run tests:
   ```bash
   pytest
   ```
5. Push and open a Pull Request against `main`.

---

## Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <short description>

[optional body]
```

Common types:

| Type | When to use |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `test` | Adding or updating tests |
| `chore` | Maintenance, dependency updates |
| `refactor` | Code restructuring without behavior change |

Examples:
```
feat: add budget comparison chart to itinerary tab
fix: handle missing organic results in search tool
docs: add troubleshooting section to README
```

---

## Pull Request Checklist

Before submitting, make sure:

- [ ] Code passes `ruff check .` with no errors
- [ ] Code is formatted with `black .`
- [ ] New functionality has tests (if applicable)
- [ ] No API keys or secrets are committed
- [ ] PR title follows Conventional Commits format
- [ ] PR description explains *what* changed and *why*

---

## Good First Issues

New to the project? Look for issues tagged [`good first issue`](https://github.com/ivarunsharma/crewai-trip-planner/labels/good%20first%20issue) — they are small, well-scoped tasks that are a great starting point.

Some ideas if the list is empty:

- Add docstrings to `agents.py` and `tasks.py`
- Add a `.env.example` file
- Write a unit test for `CalculatorTools.calculate`
- Add input validation for empty city fields in `main.py`

---

Thank you for contributing! Every improvement, no matter how small, makes this project better for everyone.
