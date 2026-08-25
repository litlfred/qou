# AlphaProof Nexus vs. QOU / Folio — comparative assessment

**Date:** 2026-06-06
**PR:** [litlfred/qou#1913](https://github.com/litlfred/qou/pull/1913)
**Subject paper:** Tsoukalas, Kovsharov, Shirobokov, … Kohli, Chaudhuri (Google
DeepMind), *Advancing Mathematics Research with AI-Driven Formal Proof Search*,
arXiv:2605.22763v1 [cs.AI], 21 May 2026.
**Local copy:** [`library/arxiv-2605.22763v1/2605.22763v1.pdf`](https://github.com/litlfred/qou/blob/main/library/arxiv-2605.22763v1/2605.22763v1.pdf)
(uploaded to `main` by the owner; arXiv blocks automated fetch).
**Their code:**
[`google-deepmind/alphaproof-nexus-results`](https://github.com/google-deepmind/alphaproof-nexus-results)
(Lean proofs only) ·
[`google-deepmind/formal-conjectures`](https://github.com/google-deepmind/formal-conjectures)
(the benchmark) ·
[`GasStationManager/SafeVerify`](https://github.com/GasStationManager/SafeVerify)
(their integrity checker).

---

## 0. One-paragraph verdict

The owner's read is correct: this paper is about **autonomous** proof-search
agents (headline metric = *problems solved per dollar*), with human–machine
*symbiosis* appearing only in the Discussion. QOU/Folio is the **symbiotic**
inverse — narrative + formal + manifest co-evolved as authoritative source,
under a heavy anti-numerology and provenance discipline that they have no need
for. **What is worth importing is their set of *disciplines* (gap taxonomy,
statement-integrity gate, evolve-markers, formalize-the-refutation loop), not
their *orchestration* (population DB, Elo, P-UCB) — that machinery exists to
run a workflow we deliberately do not run.** Net: ~4 high-value, low-effort
adoptions; several disciplines where *we are already ahead* and could say so.

---

## 1. Google's methodology (outline)

### 1.1 The framing
- LLMs are strong at math but **unreliable**; NL proofs need expensive expert
  review and errors cascade. Mitigation: generate proofs in **Lean**, where the
  compiler checks every step. Proving = "generate type-safe code with no
  `sorry`."
- First **large-scale** evaluation of this on **open research problems** (prior
  successes were competition math / human-aided formalization).

### 1.2 Input/output contract ("proof sketch")
- Input = a Lean file: target `theorem … := by sorry` + the definitions/imports
  it depends on, optionally + NL context + domain knowledge encoded in Lean.
- **`EVOLVE-BLOCK-START/END`** — the only regions the agent may add helper
  lemmas / definitions / proof steps.
- **`EVOLVE-VALUE-START/END`** — encloses *values/parameters* the agent may
  change (e.g. an algorithm's learning schedule, an `answer(…)` True/False).
- Output = a `sorry`-free proof, *with the original theorem statement
  unchanged*.

### 1.3 Agent ladder (A→D)
| Agent | What it adds |
|---|---|
| **(A) basic** | N independent "Ralph-loop" prover subagents, no shared state. Each: multi-turn LLM (Gemini 3.1 Pro) + `search_replace` tool; Lean compiles after every edit; compiler error → next turn. On episode end, **SafeVerify** checks integrity; if `sorry` remains, the agent **writes a "lessons-learned" comment** and the next episode resumes from that file. First to finish kills the rest. |
| **(B) + AlphaProof** | Subagent may call **AlphaProof** (RL olympiad prover [Hubert et al., *Nature* 2025]) as a tool to discharge a subgoal → returns **proof / disproof / failure**; proofs substituted, disproofs+failures fed back into the prompt. |
| **(C) + evolution** | AlphaEvolve-style **shared population DB** of sketches. Because proof success is binary, **rater subagents (Gemini 3.0 Flash)** rank sketches by *strategy clarity / plausibility of remaining goals / novelty* → **Plackett–Luce + Gibbs → Elo** → **P-UCB** sampling drives the search. |
| **(D) full** | (B) + (C) combined. The instrument for the open-problem sweep. |

### 1.4 Validation & anti-cheat (the load-bearing part for us)
- **Sandbox/`verify_integrity`**: a candidate may keep `sorry` placeholders but
  the **original target theorem statement must not be altered**.
- **SafeVerify**: final `sorry`-free proof is checked to compile **and to
  introduce no disallowed axioms** (incl. `sorryAx`, axiom injection).
- **Global goal cache**: deep-hash of the *exact Lean goal state* (`goal_id`);
  if any prior sketch in the population already proved/disproved that state, the
  tactic/value is retrieved instead of re-querying AlphaProof.
- **Rater rubric** (their Figure 7) — judging criteria in priority order:
  1. **Strategic robustness / generalizability** — *generalization over
     specialization*; penalize brute-force "overfitting"; reward diverse lines.
  2. **Quality of decomposition** — *grade the gaps*:
     - **Good gaps (routine/technical):** OK to `sorry` standard tasks.
     - **Bad gaps (miracles/strategic):** never `sorry` the *core insight*.
     - **The rule:** *a sketch with good gaps (even if the prover fails to close
       them) > a sketch with no gaps but a dead-end strategy.*
  3. **Logical correctness / coherence.** Red flags: asserting a falsehood,
     trivial/circular reasoning, strategic dead-ends.
- **Misformalization handling**: agents find proofs that expose ambiguity (e.g.
  "density" → "lower/upper density"); for OEIS they require **"test lemmas"**
  (verify the first few sequence terms against the formal def) *before*
  attempting the target.

### 1.5 Stack & results
- Python + `asyncio`; Lean **v4.27** in Docker sandboxes via **Pantograph**;
  Gemini 3.1 Pro (prover) + 3.0 Flash (rater); AlphaProof in low-compute
  tree-search mode (~400 sims, ~$60/problem).
- **9/353 Erdős, 44/492 OEIS**, a 15-yr Hilbert-function question, a tighter
  convex-optimization bound (found by searching a schedule in an
  `EVOLVE-VALUE`), Green's list #57, quantum-optics GHZ no-go's.
- **Ablation surprise:** the *basic* agent (A) solved all 9 Erdős too — just
  costlier on the hardest. "From specialized trained systems toward simple
  agentic loops." Their **two named failure modes**: (a) offloading the core
  difficulty into a single `sorry` in a helper lemma that *restates the target*;
  (b) `sorry`-ing lemmas the agent *claims are known literature* but are
  **hallucinations**.

---

## 2. What to ADOPT (ranked by value ÷ effort)

> All four top items are **disciplines / doc + small-CI changes**, not new
> infrastructure. They slot into skills we already run.

### A. "Good-gap / bad-gap" sorry taxonomy → `proof-gap-audit` + `proof-triage` **[HIGH / LOW]**
- **Their rule** (§1.4): grade every gap as *routine-technical* (deferrable) vs
  *core-insight / miracle* (not). A good-gap sketch beats a no-gap dead end.
- **Our state:** we mandate `-- Ref:` on every `sorry` (good), but
  `proof-gap-audit.md` has **no criticality classification** (confirmed: grep
  for routine/core/miracle/load-bearing → no matches). We treat all gaps alike.
- **Action:** add a gap-criticality axis to `proof-gap-audit` (and a triage
  ordering in `proof-triage`): every `sorry` tagged `routine` | `core` |
  `restates-target`. **`restates-target` is an automatic audit FAIL** — it *is*
  their failure mode (a). Reviewers then chase `core` gaps first.
- **Why it's the best buy:** pure doc change, sharpens two existing skills, and
  closes a real hole their own paper documents.

### B. Statement-integrity + axiom gate (SafeVerify-style) → `lean-proof-review` / `lean_ci` **[HIGH / MED]**
- **Theirs:** `verify_integrity` (the `theorem … :` signature is byte-identical
  before/after the agent's edits — only the proof body/EVOLVE regions changed)
  **+** `SafeVerify` (no `sorryAx` / axiom injection in a "proved" decl).
- **Our state:** we have `lean_verify` (MCP axiom audit) and
  `proof-narrative-lean-equivalence` (faithfulness), but **no mechanical gate
  that an agent didn't quietly weaken a `theorem` statement to make Lean pass.**
- **Action:** add a check (skill step now; CI gate later) — for any block whose
  `.lean` changed, diff the declaration *signatures* against the prior commit;
  flag any change to a `theorem/lemma/prop/cor` signature that wasn't an
  explicit owner-approved restatement. Pair with a `lean_verify` axiom sweep
  that fails on unexpected `sorryAx`. [`GasStationManager/SafeVerify`](https://github.com/GasStationManager/SafeVerify) is
  Apache-2.0 and directly reusable.

### C. `EVOLVE-VALUE` / `EVOLVE-BLOCK` markers → `formalizer` + `witnessed-values` + `production-vs-exploratory` **[MED-HIGH / LOW-MED]**
- **Theirs:** explicit "agent may only edit *here*" regions; `EVOLVE-VALUE`
  turns a *parameter* into a search target (they discovered a better optimizer
  schedule this way).
- **Our fit — but inverted:** their `EVOLVE-VALUE` *encourages* parameter
  search; for us unconstrained parameter search **is numerology** (the Δ_λ
  "don't propose a 7th fit" rule; CAL-4 / Rule 14). So adopt the *marker*, not
  the *freedom*: annotate `.lean`/compute files so that the **few legitimately
  tunable knobs** (truncation order `N`, exploratory `c_k`, the substrate `q₀`
  anchor) are explicitly fenced and *labelled production vs exploratory*, and
  everything else is FIXED. This makes "what may be tuned" auditable and gives
  `production-vs-exploratory-discipline` a concrete syntactic hook.
- **Net:** an `EVOLVE-VALUE`-style fence is the natural home for our existing
  witnessed-value + exploratory-fit policy.

### D. Numerics → counterexample → **formalize-the-refutation** → prove → `compute-author §3.3` (formalize-first) **[HIGH / MED]**
- **Theirs (Green #57):** floating-point heuristics produced a *candidate
  counterexample*; they **formalized "does this counterexample disprove the
  conjecture?"** and the agent proved that it does. AlphaProof returns
  *disproofs*, not just proofs.
- **Our live use-case:** the **Δ_λ gate** has **six** failed closure ansätze,
  all refuted numerically on the deuteron. Today that refutation lives in prose
  + witness JSON. **Formalize the refutations as Lean `disproof` lemmas**
  ("closed-form X ≠ required Δ_λ at the deuteron") so the "don't propose a 7th
  fit" rule becomes *machine-enforced*, and our `formalize-first` discipline
  (§3.3) gains a worked template for *killing a hypothesis class in Lean*.
- **Why:** we already have the numerics and the policy; this turns policy into a
  checkable artifact, and it's exactly the forward complement to our
  corpus-grep checklist.

### E. Lower-priority / situational
- **"Lessons-learned" carry-over comment** between stuck proof sessions →
  formalize via `authorNotes: {kind:"note"}` or a `.proof-log` sidecar so
  cross-session formalizer attempts inherit context. *(LOW-MED / LOW — partial
  overlap with `authorNotes` + todos.)*
- **Global goal-state cache** (deep-hash of Lean goal → reuse discharged
  subgoals). We hash *sources* for staleness; they hash *goals* for reuse.
  Worthwhile only if we start batch/auto proof attempts. *(MED / HIGH.)*
- **External prover as an MCP tool** — wire an open prover (Goedel-Prover-v2 /
  Seed-Prover; AlphaProof itself isn't released) as a "discharge this routine
  goal" tool in the formalizer loop. *(MED / depends on availability.)*
- **Contribute select QOU `conj:` blocks to `formal-conjectures`** (Δ_λ,
  kashaev-density, …) to get external proof-search on our open problems and to
  reuse their `@[category]` / `answer()` annotation schema. *(LOW-MED / MED,
  outward-facing → needs owner approval.)*
- **Diversity-injection prompts** ("decompose unsolved goals" / "combine prior
  attempts" / "try a completely new approach") as stock phrasings when
  `proof-triage` is stuck. *(LOW / LOW.)*

---

## 3. What WE already do that they DON'T (our differentiators)

The feature-by-feature **differentiators table** (and the `EVOLVE-VALUE`
inversion) now lives in the outward-facing companion note, so the shareable
artifact is self-contained:
[`docs/outreach/symbiotic-proof-authoring-note.md` §1 "Differentiators at a glance"](../outreach/symbiotic-proof-authoring-note.md).

**The symbiotic loop + the author's role.** These differentiators compose into a
five-step round-trip in which the **author owns intent and constraints**
(milestones, conjectures, proof strategies, the standing rule-set, and explicit
authorization of every merge / override / outward send) and the **agent owns
decomposition, execution, and QA**. The standing constraints are the
load-bearing inversion — *fences that forbid*, the opposite of `EVOLVE-VALUE`'s
*markers that reward search*. The "Continuous corpus QA" row is itself
multi-axis: proof rater + statement-integrity, **detangler** dependency-graph
heuristics, canonical-discipline, compute, voice, parameter-regime, and
bibliography — each recorded per block under one shared `.qa.json` reviewer-entry
schema (result / severity / score / reviewer / content-hash / evidence), with
failing verdicts draining automatically into review-sized fix-PRs. The
outward-facing companion note develops all of this — the loop, the author-role
table, the interaction-type taxonomy drawn from real PR activity, and the full
QA-axis list:
[`docs/outreach/symbiotic-proof-authoring-note.md`](../outreach/symbiotic-proof-authoring-note.md)
§3, §5.

---

## 4. Recommended next steps (prioritized)

1. ✅ **(A) gap taxonomy** → `proof-gap-audit.md` + `proof-triage.md`
   (`routine`/`core`/`restates-target`; last = auto-FAIL). *Done — `114a80fa`.*
2. ✅ **(D) formalize-the-refutation** → `compute-author.md §3.4` discipline +
   worked deuteron co-Casimir exemplar. *Done — `fd8bcc91`, `75e3cccc`.*
   Promoting the exemplar to a committed `lem:` content-object is tracked in
   [PR #1923](https://github.com/litlfred/qou/pull/1923).
3. ✅ **(B) statement-integrity gate** → `lean-proof-review.md` Review Type 4
   (signature-diff + axiom sweep; SafeVerify vendoring noted). *Done — `17cb39f7`.*
4. ✅ **(C) EVOLVE-VALUE fence** → `production-vs-exploratory-discipline.md` +
   `witnessed-values.md`. *Done — `573f7a9d`.*
5. *(owner decision, open)* contribute QOU open conjectures to `formal-conjectures`.

Items 1–4 landed on this branch as **skill-doc edits only** — no content block,
Lean, compute, or witness file was touched, so **no QA sidecars are
invalidated** by this PR. Item 5 is outward-facing and needs the owner.
