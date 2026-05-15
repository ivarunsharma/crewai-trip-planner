# AI Trip Planner

A multi-agent AI travel planner built with **CrewAI** and **Azure OpenAI**. Three specialized agents collaborate to pick the best destination, build a 7-day itinerary, and compile a local city guide — all through a Streamlit web UI.

---

## How it works

```
User fills in the form (Streamlit)
        │
        ▼
  TripCrew.run()
        │
        ├── City Selection Expert  →  Picks the best city based on weather, events & budget
        │
        ├── Local Tour Guide       →  Compiles a detailed city guide & local insights
        │
        └── Expert Travel Agent   →  Builds the full 7-day itinerary with budget & packing tips
        │
        ▼
  Results shown in 3 tabs (Itinerary / City Selection / City Guide)
```

Each agent has access to real-time tools (internet search + calculator) and is powered by Azure OpenAI.

---

## Agents

| Agent | Role |
|-------|------|
| Expert Travel Agent | Creates the full 7-day itinerary with daily plans, hotels, restaurants, packing & budget |
| City Selection Expert | Picks the best destination by comparing weather, events, and travel costs |
| Local Tour Guide | Provides local attractions, hidden gems, cultural tips, and events |

## Tools

| Tool | What it does |
|------|--------------|
| `SearchTools.search_internet` | Searches the web via Serper API for real-time travel data |
| `CalculatorTools.calculate` | Evaluates math expressions for budget calculations |

---

## File structure

```
trip_planner/
├── main.py          # Streamlit UI — entry point
├── crew.py          # Assembles agents + tasks and runs the CrewAI crew
├── agents.py        # Defines the three travel agents
├── tasks.py         # Defines the three tasks assigned to agents
├── tools/
│   ├── search_tools.py      # Internet search via Serper API
│   └── calculator_tools.py  # Math expression evaluator
└── README.md
```

---

## Setup

### 1. Install dependencies

```bash
pip install crewai streamlit python-dotenv requests
```

### 2. Create a `.env` file

Place this at the root of the project (`lanchainProject/.env`):

```env
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_API_VERSION=2024-02-01
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4o

SERPER_API_KEY=your_serper_key_here
```

> Get a free Serper API key at [serper.dev](https://serper.dev)

### 3. Run

```bash
cd trip_planner
streamlit run main.py
```

---

## Example

Fill in the form:

| Field | Example |
|-------|---------|
| Traveling from | New York |
| Destination options | Paris, Rome, Barcelona |
| Travel dates | June 10–17, 2025 |
| Interests | art, food, hiking |

The crew will take ~1–2 minutes to research and generate:
- A recommended city with reasoning
- A full 7-day day-by-day itinerary
- A local guide with hidden gems and cultural tips
