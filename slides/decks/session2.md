---
marp: true
theme: bdp
paginate: true
---

<!-- _class: title -->
<!-- _paginate: false -->

# AI Tools for Economics Research

<div class="meta">

Session 2 — Worked examples
Friday 29 May 2026
10:30–12:00 · 14:30–16:00
Banco de Portugal
João B. Sousa · Nova SBE

</div>

---

<!-- _class: center -->

<h4>Today</h4>

## Real tasks, live.

<p class="wide">Four examples in identical structure: the task, the prompt, what comes back, what remains to verify.</p>

---

<!-- _class: takeaways -->

<h4>The four examples</h4>

## What we'll cover today.

<ul>
<li><strong>Literature triage</strong> &nbsp; a folder of PDFs → comparison table.</li>
<li><strong>Data cleaning</strong> &nbsp; two raw series → aligned panel, summary, plot.</li>
<li><strong>Code review</strong> &nbsp; a script with a planted bug.</li>
<li><strong>Replication</strong> &nbsp; clone a repo, reproduce a figure.</li>
</ul>

<p class="source">Live demonstration.</p>

---

<h4>Getting in and out</h4>

## A session lives in one folder.

<pre><code>$ cd ~/my-project        # a folder under version control
$ claude                 # start a session here

&gt; /help                  # list everything you can type
&gt; Esc                    # interrupt the agent mid-task
&gt; /clear                 # forget the conversation, keep the session

&gt; /exit                  # leave   (or Ctrl-D)

$ claude --continue      # reopen the last session, context intact</code></pre>

<p class="source">Start it where your project is — never in your home directory or a folder holding credentials or supervisory data.</p>

---

<!-- _class: split -->

<div>
<h4>Standing instructions</h4>
<h2>CLAUDE.md — read at the top of every session.</h2>

<p class="wide">Recall Monday's context bundle: <code>CLAUDE.md</code> sits in the preamble, prepended before your first prompt. Write a convention once; the agent follows it every turn, every session — no need to repeat it in prompts.</p>

<p class="source">Two levels, both loaded automatically. Add a line mid-session by typing it with a leading <code>#</code>.</p>
</div>

<div>
<pre><code>~/.claude/CLAUDE.md   &larr; user
  every project, this machine
  "Prefer Stata for empirics,
   JAX/NumPy in Python."
./CLAUDE.md   &larr; project
  shared via git with the repo
  "data/raw/ is read-only;
   write to processed/."</code></pre>
</div>

---

<!-- _class: divider -->
<!-- _paginate: false -->

<div class="num">01</div>

## Literature triage.

---

<h4>The task</h4>

## Thirty PDFs, one afternoon.

<p class="wide">Skim each paper, summarise its data and method, cluster by approach, isolate the subset matching your question, build a comparison table.</p>

<p class="source">Routine work at the start of a project. The agent handles the first pass; verification remains yours.</p>

---

<h4>The folder</h4>

## Six papers on inflation expectations.

<pre><code>papers/inflation_expectations/
├── cagan_1956_hyperinflation.pdf
├── muth_1961_rational_expectations.pdf
├── friedman_1968_role_of_monetary_policy.pdf
├── coibion_gorodnichenko_2015_info_rigidity.pdf
├── armantier_etal_2017_sce_overview.pdf
└── candia_coibion_gorodnichenko_2021_firms.pdf</code></pre>

<p class="wide">Six today — enough to watch the workflow live. The same prompt scales to thirty without change.</p>

<p class="source">Three foundational papers, three recent empirical studies.</p>

---

<h4>The prompt</h4>

## What we type.

<pre><code>Read every PDF in papers/inflation_expectations/.

For each one, write:
  - title, year, authors
  - data source and sample
  - identification or empirical strategy
  - headline result, one sentence

Then a markdown comparison table with the same columns.
For the headline column, quote the sentence in the paper
that supports it, with a page number. Do not paraphrase.</code></pre>

<p class="source">Two design choices: a specified output format, and a quote-with-page rule to constrain fabrication.</p>

---

<!-- _class: split -->

<div>
<h4>What comes back</h4>
<h2>A table you can audit.</h2>

<p class="wide">A markdown table: one row per paper, the requested columns, the headline column populated with quoted sentences and page numbers.</p>

<p class="source">The quote-with-page rule anchors verification. Without it, the headline column reflects the model's prior rather than the paper's content.</p>
</div>

<div>
<pre><code>| Paper            | Data        | ID            | Headline (p.) |
|------------------|-------------|---------------|---------------|
| Cagan            | hyperinf.   | adaptive exp. | "…" (p. 37)   |
| Muth             | theory      | rational exp. | "…" (p. 316)  |
| Friedman         | review      | exp.-aug. PC  | "…" (p. 8)    |
| Coibion & G.     | SPF + cons. | IV on FE      | "…" (p. 2655) |
| Armantier et al. | SCE         | survey design | "…" (p. 60)   |
| Candia et al.    | firm survey | new data      | "…" (p. 14)   |</code></pre>
</div>

---

<h4>Before any of it reaches a draft</h4>

## The output is fluent. Verify it.

<ul>
<li><strong>Fabricated quotes</strong> &nbsp; a headline sentence that is not in the paper.</li>
<li><strong>Wrong page numbers</strong> &nbsp; right quote, wrong location — worse on scanned PDFs.</li>
<li><strong>Conflated papers</strong> &nbsp; a result attributed to the wrong row.</li>
</ul>

<p class="source">Open the cited page before you trust any cell. Failure mechanisms in Session 3.</p>

---

<!-- _class: divider -->
<!-- _paginate: false -->

<div class="num">02</div>

## Data cleaning and summary tables.

---

<h4>The task</h4>

## Two series — one on disk, one to fetch.

<p class="wide">US CPI from Monday is already in <code>data/raw/</code>. The Portuguese HICP is not — the agent retrieves it from Eurostat, then aligns the two and compares.</p>

<p class="source">Obtaining the data is the first step. The agent does it the way you would: find the series, download it, save it to the repo.</p>

---

<h4>The raw material</h4>

## We start with one file.

<pre><code>data/raw/
└── cpi.csv     FRED, US CPI-U, monthly, 1947–2026</code></pre>

<p class="wide">The Portuguese HICP is not on disk. The agent downloads it from Eurostat, then reconciles two different date formats, column names, and missing-value codes.</p>

---

<h4>The prompt</h4>

## What we type.

<pre><code>US CPI is on disk: data/raw/cpi.csv (FRED).
1. Download monthly HICP for Portugal (all-items) from
   Eurostat — just that one series, plain CSV. Save to
   data/raw/hicp_pt.csv.
2. Align both to monthly frequency on the common sample.
   Compute year-over-year inflation.
3. Write:
   - data/processed/inflation_us_pt.csv   long format
   - a markdown table: mean, sd, min, max by decade
   - slides/assets/inflation_us_pt.png    two lines
Stop and ask if anything is ambiguous before writing.</code></pre>

<p class="source">Step 1 has the agent fetch the data, not just clean it.</p>

---

<!-- _class: split -->

<div>
<h4>What comes back</h4>
<h2>Three outputs.</h2>

<ul>
<li>A CSV in long format that <code>read_csv</code> can parse.</li>
<li>A summary table ready to paste into a memo.</li>
<li>A PNG ready to drop into a slide.</li>
</ul>

<p class="source">Diffs are stored in git; commands in shell history. The session is reproducible.</p>
</div>

<div>
<pre><code>| Decade  | US mean | PT mean |
|---------|---------|---------|
| 1990s   |   2.0   |   2.1   |
| 2000s   |   2.6   |   2.6   |
| 2010s   |   1.8   |   1.2   |
| 2020s   |   4.0   |   3.2   |
</code></pre>
</div>

---

<h4>A short verification pass</h4>

## Four checks before the table goes into a memo.

<ul>
<li><strong>Column choice</strong> &nbsp; headline "CPI" vs core "CPILFESL" — whichever you intended.</li>
<li><strong>Types and missingness</strong> &nbsp; spot-check the date column and each series' missing-value count.</li>
<li><strong>Date conventions</strong> &nbsp; FRED stamps first-of-month, Eurostat last-of-period — check they align.</li>
<li><strong>Sample period</strong> &nbsp; was "common sample" read as intersection or forward-fill?</li>
</ul>

---

<!-- _class: takeaways -->

<h4>End of morning</h4>

## What the two examples share.

<ol>
<li>The agent works on your filesystem with one prompt — no copy-paste, no upload limits.</li>
<li>Structured prompts (specified format, quote-with-page rule, stop-and-ask) yield outputs ready for audit.</li>
<li>Every step is reproducible: edits land in git, commands in shell history.</li>
</ol>

<p class="source">After lunch: code review, and a replication exercise.</p>

---

<!-- _class: center -->
<!-- _paginate: false -->

<h4>Break</h4>

<div class="big">14:30</div>

<p class="lede">Back after lunch.</p>

---

<!-- _class: divider -->
<!-- _paginate: false -->

<div class="num">03 · AFTERNOON</div>

## Code review and debugging.

---

<h4>The setup</h4>

## A script you have not read line by line.

<p class="wide">It runs without error and writes a CSV. The plot looks plausible at a glance. You want to reuse it.</p>

<p class="source">Code that runs and produces plausible output is easy to leave unchecked.</p>

---

<h4>The code</h4>

## <code>code/scripts/compute_inflation.py</code>

<pre><code>import pandas as pd

cpi = pd.read_csv("data/raw/cpi.csv", comment="#",
                  parse_dates=["observation_date"])
cpi = cpi.sort_values("observation_date")

# year-over-year inflation
p = cpi["CPIAUCSL"]
cpi["yoy"] = 100 * (p / p.shift(11) - 1)

cpi[["observation_date", "yoy"]].to_csv(
    "data/processed/inflation.csv", index=False)</code></pre>

<p class="source">Twelve lines, one bug. Identify it before the next slide.</p>

---

<h4>The prompt</h4>

## What we type.

<pre><code>Walk me through code/scripts/compute_inflation.py line by
line. What does each step do? Flag anything you would
double-check against a published source before trusting
the output. Do not edit the file.</code></pre>

<p class="source">"Do not edit" is the constraint that matters. It keeps the walkthrough and any subsequent fix in separate diffs.</p>

---

<h4>What comes back</h4>

## A line-by-line walkthrough — and a flag.

<p class="wide">The agent describes each step, then notes one line worth double-checking: <code>shift(11)</code> compares each month to <strong>eleven</strong> months earlier, but year-over-year on monthly data requires <code>shift(12)</code>.</p>

<p class="wide">The fix is one character. Without the walkthrough, nothing else in the script would have flagged it.</p>

<p class="source">Asking for an explanation surfaces issues alongside the description; asking only for a fix often returns style edits.</p>

---

<h4>What you do next</h4>

## Three steps before the fix lands.

<ul>
<li><strong>Read the explanation against the code</strong> &nbsp; the walkthrough is the audit trail.</li>
<li><strong>Confirm the symptom</strong> &nbsp; compare a few output values against a trusted source (FRED, BdP).</li>
<li><strong>Ask for the diff before applying</strong> &nbsp; one-character fixes still go through the same review loop.</li>
</ul>

<p class="source">Each step happens before the fix is written to the file.</p>

---

<!-- _class: center -->

<h4>The habit</h4>

## Diagnose first, fix second.

<p class="wide">Two turns produce two diffs and two opportunities to review before any change is written.</p>

---

<!-- _class: divider -->
<!-- _paginate: false -->

<div class="num">04</div>

## Replication.

---

<h4>The task</h4>

## Clone a repo. Reproduce one figure.

<p class="wide">The exercise required when you need to reproduce a published figure — for a referee report, a robustness check, or a presentation.</p>

<p class="source">Replication packages are typically written once and not revisited. Environmental drift accumulates by the time anyone clones them.</p>

---

<h4>What usually breaks</h4>

## Three things that commonly break.

<ul>
<li><strong>Package versions</strong> &nbsp; a dependency pinned to an old version; the current one renamed a function, and the script raises.</li>
<li><strong>Hard-coded paths</strong> &nbsp; absolute paths to the author's machine, written into the scripts.</li>
<li><strong>Missing data</strong> &nbsp; listed as "available on request," with no working way to obtain it.</li>
</ul>

<p class="source">Model-based — no data to download, so the third never arises.</p>

---

<h4>The prompt</h4>

## What we type.

<pre><code>Clone https://github.com/shade-econ/sequence-jacobian
into ./replication/.

Read the README. Set up the environment. Run
notebooks/hank.ipynb and reproduce the impulse responses
to a monetary policy shock. Save the figure to ./figures/.
If a script (not the notebook) makes the figure, save it
to ./code/ for inspection. Stop after the figure is saved.

For every change you make to the code or environment, log
it as a bullet so I can read the list before you continue.</code></pre>

<p class="source">The figure and its code land on disk — to inspect and re-run.</p>

---

<h4>What to ask for</h4>

## Ask for outputs you can audit and re-run.

<ul>
<li><strong>The result</strong> &nbsp; the figure or table, to compare with the published one.</li>
<li><strong>A change-log</strong> &nbsp; every code and environment edit, to see what changed.</li>
<li><strong>The environment</strong> &nbsp; the deps and commands, to rebuild from a clean clone.</li>
</ul>

<p class="source">Name the deliverables — you get what you ask for.</p>

---

<h4>What you still verify</h4>

## Match the reproduction to the paper.

<ul>
<li><strong>Same axes, same scale, same legend.</strong></li>
<li><strong>A reference number</strong> &nbsp; market-clearing residuals, a steady-state value — confirm it matches the notebook.</li>
<li><strong>The change-log</strong> &nbsp; environment only; the model code is never touched.</li>
</ul>

<p class="source">If a change touches the model — calibration, equations, the solution method — stop. Environment fixes should not alter the results.</p>

---

<!-- _class: divider -->
<!-- _paginate: false -->

<div class="num">05</div>

## Q&amp;A.

---

<!-- _class: takeaways -->

<h4>End of session</h4>

## Three habits to take forward.

<ol>
<li><strong>The agent compresses the mechanical parts of research</strong> — triage, cleaning, replication setup, reading unfamiliar code.</li>
<li><strong>Structured prompts are the lever</strong> — specify the format, require citations, ask the agent to stop and explain.</li>
<li><strong>Diagnose first, fix second</strong> — review the diff before any change is committed.</li>
</ol>

<p class="source">Session 3, 22 June: failure mechanisms and habits for early detection.</p>

---

<!-- _class: center -->

<h4>Suggested videos</h4>

## Claude Code for Applied Economists.

<p class="wide">Paul Goldsmith-Pinkham's video series at Markus' Academy — full empirical workflows in Claude Code, from data analysis to web scraping. youtube.com/@markus_academy</p>

---

<!-- _class: title center -->
<!-- _paginate: false -->

# See you on 22 June.

<div class="meta">

joao.sousa&#64;novasbe.pt

</div>
