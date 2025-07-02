# ADK: AI Developer Kit - Agent Examples

This repository contains a collection of agent-based AI examples using the [Google ADK](https://github.com/google/adk) framework. Each folder demonstrates a different agent architecture or capability, from basic greeting agents to complex multi-agent pipelines with persistent memory, callbacks, and tool integrations.

## Table of Contents
- [Project Structure](#project-structure)
- [Agent Examples](#agent-examples)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Project Structure

```
ADK/
  1-basic-agent/           # Simple greeting agent
  2-tool-agent/            # Agent with tool usage (e.g., Google Search)
  3-litellm-agent/         # Agent using LiteLLM for model abstraction
  4-structured-outputs/    # Agent with structured (JSON) outputs
  5-sessions-and-state/    # Agent with session and state management
  6-persistent-storage/    # Agent with persistent memory (SQLite)
  7-multi-agent/           # Multi-agent manager with sub-agents
  8-stateful-multi-agent/  # Multi-agent with stateful interactions
  9-callbacks/             # Agents demonstrating before/after callbacks
  10-sequential-agent/     # Sequential pipeline agent
  11-parallel-agent/       # Parallel agent for system monitoring
  12-loop-agent/           # Loop agent for iterative refinement
  business_research_agent/ # Business research pipeline
  project/                 # Research pipeline example
  test/                    # Test agents (e.g., profile searcher)
  requirements.txt         # Python dependencies
```

---

## Agent Examples

### 1. Basic Agent
- **Greeting Agent**: A simple agent that asks for the user's name and greets them.

### 2. Tool Agent
- **Tool Agent**: Integrates tools like Google Search to answer queries.

### 3. LiteLLM Agent
- **Dad Joke Agent**: Uses LiteLLM to tell dad jokes via a tool function.

### 4. Structured Outputs
- **Email Agent**: Generates professional emails with structured (JSON) output.

### 5. Sessions and State
- **Question Answering Agent**: Maintains user preferences and session state.

### 6. Persistent Storage
- **Memory Agent**: Remembers reminders and user info across sessions using SQLite.

### 7. Multi-Agent
- **Manager Agent**: Delegates tasks to sub-agents (stock analyst, funny nerd, news analyst).

### 8. Stateful Multi-Agent
- **Customer Service Agent**: Routes queries to specialized agents (policy, sales, support, order) and maintains user state.

### 9. Callbacks
- **Before/After Agent**: Demonstrates before and after agent callbacks for logging and timing.

### 10. Sequential Agent
- **Lead Qualification Pipeline**: Validates, scores, and recommends actions for sales leads in sequence.

### 11. Parallel Agent
- **System Monitor Agent**: Gathers CPU, memory, and disk info in parallel, then synthesizes a report.

### 12. Loop Agent
- **LinkedIn Post Agent**: Generates and iteratively refines LinkedIn posts until quality is met.

### Business Research Agent
- **Business Research Pipeline**: Enriches professional profiles using Google and LinkedIn data.

### Project/Research Agent
- **Research Pipeline**: Gathers and reports on a person using Google and LinkedIn.

### Test Agents
- **Profile Searcher**: Searches for LinkedIn profiles and summaries from CSV data.

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd ADK
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   - Some agents require API keys (e.g., `GOOGLE_API_KEY`, `OPENROUTER_API_KEY`).
   - Create a `.env` file in the root directory and add your keys:
     ```env
     GOOGLE_API_KEY=your_google_api_key
     OPENROUTER_API_KEY=your_openrouter_api_key
     ```

---

## Usage

- Each agent example is self-contained. Navigate to the relevant directory and run the main script (if provided), or use the agent in your own pipeline.
- For persistent memory and stateful agents, see the `6-persistent-storage/main.py` and `8-stateful-multi-agent/main.py` for interactive CLI examples.
- For business research and profile enrichment, see the `business_research_agent/` and `project/` folders.

---

## Contributing

Contributions are welcome! Please open issues or pull requests for improvements, bug fixes, or new agent examples.

---

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) for details. 
