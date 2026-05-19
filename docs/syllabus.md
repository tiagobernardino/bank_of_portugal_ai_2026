# AI Tools for Economics Research — Syllabus

Banco de Portugal, 2026.\
Four daily sessions, 3 hours each (1.5 + 1.5).\
Instructor: João B. Sousa (NOVA SBE), joao.sousa@novasbe.pt.

No software-engineering background assumed.
Environment:

- Claude Code (subscription) + git
- Optional: VS Code with Copilot

---

## Session 1 — Foundations (3h)

What an AI coding agent is, and what it is not.

1. The landscape (45m). Claude Code, Codex, Gemini CLI, Copilot, Cursor. Model vs. agent vs. interface. Where each one runs, what it can touch, what we can configure in the agent layer.
2. Chat interface vs. CLI agent (60m). Web chat, IDE chat, terminal agent. What changes when the model can read files, run commands, edit code. Cost, control, reproducibility.
3. The surrounding infrastructure (60m). Filesystem, shell, git, editor. Why agents are only useful on top of these. Permissions and sandboxing.
4. Setup check (15m). Claude Code + git, and optionally Copilot in VS Code.

## Session 2 — Worked examples (3h)

Tasks economists actually do. Live demo.

1. Literature triage from a folder of PDFs (40m).
2. Data cleaning and summary tables from raw data (40m).
3. Code review and debugging (40m).
4. Replication: reproducing a figure from an existing repo (30m).
5. Q&A and discussion (30m).

Each example: prompt, agent output, what the user still has to verify.

## Session 3 — Failure modes and best practices (3h)

What goes wrong, and how to catch it.

1. Failure modes (60m). Hallucinated citations, fabricated data, silent code edits, context drift, overconfident wrong answers.
2. Verification habits (45m). Reading diffs, running tests, spot-checking numbers, review by an independent agent.
3. Prompting and scoping (45m). One task at a time. Constraints up front. When to start a fresh session.
4. Cost and tokens (30m). What burns budget. Caching. When a smaller model is enough.

## Session 4 — Advanced use (3h)

Customising the agent for recurring research workflows.

1. Skills (45m). Reusable instructions for recurring tasks (cleaning a dataset, formatting a table, drafting a memo).
2. Hooks (45m). Automating actions around the agent: pre-commit checks, formatting, logging.
3. Subagents (45m). Delegating focused subtasks; parallelising independent work.
4. MCP and external tools (30m). Connecting the agent to data sources, reference managers (Zotero), TeX editors (Overleaf), papers.
5. Building a small team workflow (15m). What a BdP research team can put in shared config.

---

## Materials

Slides, demo code, sample data.
