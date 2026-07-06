# Google AlphaProof-Nexus QA rubrics & tooling — adoption design + discussions

**Date:** 2026-06-07
**PR:** (this branch `claude/google-paper-qa-rubrics-2026-06-07`)
**Predecessors:** [`2026-06-06-alphaproof-nexus-comparative-assessment.md`](2026-06-06-alphaproof-nexus-comparative-assessment.md) (merged in #1913), the Δ_λ refutation lemma (#1923).

This doc covers four asks: (1) wire the AlphaProof-Nexus **rater rubric** in as scored QA sidecar criteria + a watch→backlog *rate-and-improve* loop; (2) map the paper's **other QA points** to criteria; (3) discuss an **external prover as an MCP tool**; (4) discuss **`formal-conjectures` schemas**, alternatives, pros/cons.

---

## Part 1 — Rater rubric as scored QA criteria (+ rate→improve loop)

**Status: not yet a sidecar.** Corpus-grep (regex, `.` = wildcard) `strategy.clar|plausibilit|novelty|rater|plackett|p-?ucb|sketch.qualit` hits only the gap-criticality *skill* (`proof-gap-audit`) and `ontologist` — no scored criterion exists.

**What the paper does.** In tier (C), **rater subagents (Gemini Flash)** rank proof *sketches* by **strategy clarity / plausibility of remaining goals / novelty** → Plackett–Luce → Gibbs → Elo → P-UCB sampling drives the search. It is a **quality score**, not pass/fail.

**Design — three agent-scored criteria** (domain `proof-rater`, `automated: false`, applies to provable kinds + their `-proof` blocks):

| Criterion | Question (0–1 score) |
|---|---|
| `proof-rater-strategy-clarity` | Is the proof *strategy* explicit and legible — would a competent reader know the plan before reading the steps? |
| `proof-rater-goal-plausibility` | For any remaining `sorry`/gap, how plausible is closing it (cross-refs the gap-criticality tag `routine`, `core`, `restates-target`)? `restates-target` ⇒ score 0. |
| `proof-rater-novelty` | Does the proof/approach add something non-redundant vs. the corpus (not a near-duplicate of a sibling proof)? |

**Schema change (minimal).** `QaCriterionEntry` gains an optional
`score?: { value: number; max: number; rubric?: Record<string, number> }`.
Rater criteria populate `score` and map to a single `result` per band (the
exact `QaCriterionEntry.result` enum): `value ≥ 0.66 → "pass"`;
`0.33 ≤ value < 0.66 → "warn"`; `value < 0.33 → "fail"` (severity `"minor"`).
Informational — **not** merge-blocking by default; the existing pass/fail
criteria remain the gates.

**Rate→improve loop (the AlphaProof-Nexus pattern, applied to QOU):**
- **`/integration-watch proof`** dispatches a rater agent per fresh proof block → writes a `score` entry (reviewer `kind: "agent"`). This is the *rate* half.
- **`/integration-backlog proof`** orders blocks by **ascending score** (lowest first), dispatches the mapped improver skill (`proof-simplifier` for clarity, `proof-triage`/`lean-build-fix` for plausibility, `proposition-consolidation-audit` for novelty), then **re-rates** to confirm the score rose. This is the *improve* half — the Elo-search analogue, but the "population" is the corpus and the objective is corpus quality, not solves/\$.

This is the **symbiotic inversion** of their loop (assessment §3): they rate to *drive a search for one proof*; we rate to *raise the standing quality of the whole corpus*.

---

## Part 2 — Other Google-paper QA points → criteria

| Paper QA point | QOU mapping | Status |
|---|---|---|
| **SafeVerify / `verify_integrity`** (no statement-weakening, no `sorryAx`) | `proof-statement-integrity` (signature-diff vs prior commit + axiom sweep) | skill landed (#1913 Review Type 4); **promote to a criterion** here |
| **Disproof path** (numeric counterexample → formalized `≠`) | `canonical-refutation-formalized` (a refuted ansatz cited in prose must have a Lean `≠`) | discipline landed (compute-author §3.4, #1923 lemma); **add criterion** |
| **`EVOLVE-VALUE` markers** (tunable knobs) | `compute-evolve-value-fenced` (tunable literals sit inside a fence; canonical values do not) | discipline landed (#1913); **add criterion** |
| **"lessons-learned" episode comments** | `authorNotes` (AGENTS.md §4d) — already the home for working-draft notes | no new criterion (existing) |
| **Rater rubric** | Part 1 | this PR |

The three new criteria (`proof-statement-integrity`, `canonical-refutation-formalized`, `compute-evolve-value-fenced`) are mostly **`automated: true`** (git-diff + grep/AST), unlike the rater rubric.

---

## Part 3 — Discussion: external prover as an MCP tool

**What it is.** The paper calls **AlphaProof** as a *tool*: subagent hands it a subgoal, gets back **proof / disproof / failure**; proofs are substituted, disproofs+failures fed back. QOU already has half of this via the **lean-lsp MCP** (`lean_multi_attempt`, `lean_state_search`, `lean_hammer_premise`) — those are *premise/tactic* assist, not a closing prover.

**Where it would fit.** As a `prover_*` MCP tool consumed by `proof-triage` / `lean-build-fix`: given a goal, return a candidate proof term. Natural place in the **gap taxonomy** (#1913): a prover-MCP discharges **`routine`** gaps automatically; **`core`** gaps stay human (the prover can't supply the missing idea, and shouldn't be trusted to).

| | Pros | Cons / guardrails |
|---|---|---|
| **Discharge routine sorries** | clears proof debt fast; the disproof path realises *formalize-the-refutation* automatically | output **must** pass the statement-integrity gate (Part 2) — a prover that "succeeds" by `sorry`/axiom injection is a regression; `lean_verify` every returned term |
| **Trust** | deterministic re-check (it returns a Lean term we compile ourselves) | provenance: tag the reviewer `kind:"agent" id:"prover-mcp/<engine>"`; never accept an unverified term |
| **Canonical discipline** | fine for *pure-math* lemmas (Hecke/GS/Wenzl identities) | **does not** apply to mass/binding derivations — a found proof may violate the 3-calibration / substrate discipline; restrict the tool to `braids-and-knots`-style algebraic lemmas, not `mass-theory` observable claims |
| **Candidates** | LeanCopilot/Duper, Canonical, an AlphaProof-style RL prover, or an LLM-prover MCP | cost + rate limits; pin engine version in the sidecar for staleness |

**Recommendation:** add a thin `prover-mcp` shim wired into `proof-triage` step 3 (try-prover-before-escalate), **gated** to algebraic lemmas and **always** re-verified locally with `lean_verify`. Low-risk, high-leverage for the `routine`-gap backlog; explicitly out-of-scope for observable/mass claims.

---

## Part 4 — Discussion: `formal-conjectures` schemas — alternatives, pros/cons

**Their schema** (`google-deepmind/formal-conjectures`): each conjecture is a **Lean declaration** (`theorem foo … := by sorry`) with a docstring (natural-language statement, source/reference), AMS-classification + `@[category …]`-style attributes, and an `answer(…)`/status convention. Flat, Lean-centric, community/benchmark-oriented.

**QOU's schema:** a **content-object triple** (`conj:*` = `.ts` manifest + `.md` narrative + `.lean`) inside a **dependency graph** (`uses[]`), with **witnesses** (`*.witness.json`) and **QA sidecars** (`*.qa.json`). Richer (narrative + provenance + DAG + empirical support) but QOU-specific.

**Three ways to contribute QOU conjectures:**

| Option | What | Pros | Cons |
|---|---|---|---|
| **A. Author directly in their repo** | Write QOU conjectures in their Lean+attribute schema, PR to formal-conjectures | max visibility; benchmark inclusion | second source of truth; drifts from QOU; loses narrative/DAG/witness context |
| **B. Mirror via an exporter (recommended)** | Keep QOU `conj:*` as source of truth; build `conj-block → formal-conjectures` exporter (Lean decl + map docstring/refs/AMS from manifest) | single source of truth; auditable; regenerable; preserves QOU provenance internally | build + maintain the exporter; map `uses[]`→their refs |
| **C. Dual-tag in place** | Add their `@[category …]`/AMS attributes inside QOU `.lean` conjecture files so they're dual-compatible | minimal divergence | their attributes/macros may not resolve in QOU's Lean toolchain; couples QOU build to their conventions |

**Recommendation:** **Option B.** It matches QOU's "content object is the authoritative source, everything else is a render target" architecture (AGENTS.md) — `formal-conjectures` becomes another *render target* of the `conj:*` blocks, like LaTeX or the blueprint. Candidate conjectures to seed: the genuinely-open QOU `conj:*` (e.g. `conj:rho-prefactor-structural` / GAP-A-4, `conj:kashaev-density-equals-sdp-multiplicity`). This remains an **owner decision** (outward-facing contribution).

---

## Implementation status (this PR)
- [x] Design + discussions (this doc).
- [x] Schema: `score?` on `QaCriterionEntry` (`block-qa.ts`).
- [x] Registry: `proof-rater-{strategy-clarity,goal-plausibility,novelty}` + `proof-statement-integrity` in `qa-criteria-registry.ts`. (Part-2 `canonical-refutation-formalized` / `compute-evolve-value-fenced` deferred to a follow-up so the first rollout + baseline stays focused on proof blocks — "no QA issues at scale".)
- [x] Wire rate→improve into `proof-integration-watcher.md` (dispatch table) + `integration-backlog.md` (ascending-score drain + re-rate).
- [ ] Parts 3 & 4 are **discussion only** — no code here; Part 3 (prover-MCP) and Part 4 Option B (exporter) are follow-up tranches pending owner go-ahead.
