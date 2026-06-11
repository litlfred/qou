# Discussion-corpus meta-analysis — mining the session archive for skills

**Date:** 2026-06-11 · **Owner direction:** the #2115 session archive
(`human-agent-discussions/`) should be mined — proof strategies,
mathematical intuition, literature-search-by-analogy moves,
generalization patterns — primarily to **augment the skill library**;
long-term (post-open-sourcing, explicitly deferred) as LLM training
data. This plan defines the pipeline. Execution is gated on the
archive ingestion step that only the owner can perform (claude.ai
data exports → `_incoming/` → archiver run, per #2115's workflow).

## P0 — Redaction protocol (HARD PREREQUISITE for any public artifact)

The transcripts contain three content classes with different fates:

| class | examples | disposition |
|---|---|---|
| **mathematical / engineering** | proof attempts, refutations, probe designs, compute discipline | include — this is the minable corpus |
| **strategic / reception** | publication strategy, reviewer outreach plans, media handling | **exclude or redact** before anything public; minable privately for skills |
| **personal / employer** | accessibility context, employer considerations | **exclude** from public artifacts entirely |

Per-session classification happens at ingestion review (the archiver's
numbered `--list` dry-run); a `privacy` field in each session's
`metadata.json` records the class and is honoured by every downstream
consumer. **No session publishes without an explicit owner `public: true`.**

## P1 — Corpus preparation

- Ingest all three accounts' exports + the CLI `.jsonl` logs (archiver
  already handles both); regenerate `INDEX.md`; verify the
  session ↔ PR/commit tag graph (the commit-trailer linkage gives
  ground truth for "which discussion produced which artifact").
- Completeness ledger: sessions per account per month vs the 57
  session-trailer commits already detected in repo history — gaps are
  recorded, not papered over.

## P2 — Extraction (the "super-thorough meta-analysis")

One background extraction agent per session, emitting a typed sidecar
(`<session>/mining.json`) with records in a fixed taxonomy:

| record type | what it captures | downstream use |
|---|---|---|
| `proof-strategy` | tactic sequences, decomposition moves, bridging-lemma patterns | formalizer / proof-* skills |
| `refutation-arc` | hypothesis → counterexample/probe → retraction (incl. flip-flops) | MDL search-history ledger; production-vs-exploratory discipline |
| `formalize-first-save` | structural argument that killed a numerical search | compute-author §3.3 precedent table |
| `analogy-search` | "X is like Y in field Z" moves that found literature or structure | new skill candidate: literature-by-analogy |
| `corpus-grep-save` | "already resolved" catches | proof-gap-audit §K precedents |
| `generalization-move` | special case → parametrized statement lifts | lean-generation / category-theory skills |
| `prompt-pattern` | phrasings/decompositions that reliably worked | skill authoring guidance |
| `prompt-lexicon` | categorized author phrasings per register (steer / gap / seed) with usage counts and outcomes | the "related language" lists carried by `symbiotic-interaction` and sibling skills |
| `socratic-steering` | known/nearly-known-answer questions used as course corrections, vs flagged genuine-gap questions; per-arc α̂ (coactive correction quality) and turns-to-convergence T per the formal adoption in the outreach note | methodology paper (the root-finding claim); outreach-note §Socratic steering |
| `intuition-seed` | tenuous cross-domain identifications volunteered by the author (e.g. the Reeb-flow ↔ Julia-set linkage), with literature-absence check, validation latency, and verdict (validated→rigorized / refuted / undecidable-cheaply) | novelty attribution (auditable author-origin credit); methodology paper; `symbiotic-interaction` lexicon |
| `failure-mode` | agent errors, misreadings, wasted passes | watcher checklists |

Aggregation pass: cross-session frequency tables, exemplar selection
(2–3 best instances per type), and a provenance link (session id +
turn) on every exemplar.

## P3 — Skill augmentation (the primary payoff)

- Map each mined pattern to the skill it strengthens; each skill edit
  cites its source sessions (provenance trailer in the skill file).
- New-skill candidates expected from the taxonomy: literature-by-
  analogy; negative-result handling (refutation-arc hygiene);
  reception-strategy (private skill, never synced).
- Cadence: one `skills(mining):` PR per batch of ≤ 5 skill edits,
  normal review pipeline.

## P4 — Outward artifacts (each owner-gated)

1. **Methodology-paper dataset**: refutation-arc and
   formalize-first-save tables pair with the A/B metrics witness as
   the empirical core of the symbiotic-authoring paper.
2. **Receptivity decision input**: the public/curated subset of the
   archive (see P0) ships as a standalone "genesis corpus" dataset —
   separate artifact layer from the physics paper (the paper cites
   results and witnesses; the corpus is the methodology dataset).
3. **LLM training-set export**: deferred per owner (post-open-source);
   requires licence choice + formatting; indirect payoff; revisit
   after P3 lands.

## Effort + gating

| phase | effort | gate |
|---|---|---|
| P0 protocol | done (this doc) — per-session classification at ingest | owner ingestion |
| P1 | ~1 session after exports land | owner ingestion |
| P2 | ~1 agent-session per ~10 transcripts, parallelizable | P1 |
| P3 | rolling, per batch | P2 |
| P4.1 | ~1 session | P2 |
