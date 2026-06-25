# Proof-QA re-audit — 2026-06-22 `qa-agent-drain` batch false positives

**Date:** 2026-06-25
**Branch:** `claude/great-goldberg-dvf9m0`
**Trigger:** owner request — "drain [proof sidecar] failures then warns … and
fix genuine fails."

## Summary

The proof-axis QA sidecars (`content/**/*.qa.json`, criteria `proof-*`) carried
**1,753 `fail`** verdicts. Nearly all originated from a single **agent** batch
(`reviewer.kind: "agent"`, `agent_skill: local/qa-agent-drain`,
`reviewed_at: 2026-06-22T02:56…Z`). Spot-auditing against the actual Lean
source showed that batch had a **high false-positive rate** on the
deterministically token-checkable criteria.

### Evidence (verified against resolved Lean source)

A block's Lean is resolved as: sibling `<block>.lean`, else the `lean.ref`
`qou:QOU.<Mod>.<Decl>` → `content/quantum-observable-universe/lean/QOU/<Mod>.lean`.

| criterion | fails | justified (token present) | false positive | FP rate |
|---|--:|--:|--:|--:|
| `proof-no-decide-masking` | 235 | 20 (real `decide`/`native_decide`) | 203 (no token) | ~86% |
| `proof-no-trivial-true` | 210 | 38 (real `: True`) | 160 (no token) | ~76% |
| `proof-no-bare-sorries` | 2 | 2 (real `sorry`) | 0 | 0% |

**Worked example — `prop:surreal-rate-calculus`**
(`lean/QOU/AlgebraicSubstrate/SurrealRateCalculus.lean`, 0 sorries):
- `proof-statement-integrity: fail` note *"contains sorryAx or unexpected
  axioms"* — the file has **0 sorries**. False note.
- `proof-no-decide-masking: fail` — the proof uses `norm_num`/`ring`, **no
  `decide`**. False positive.
- `proof-rater-strategy-clarity: fail (0.2)` note *"trivial skeleton stub with
  no stated plan"* — the `.md` carries a full four-claim narrative proof. False.
- `proof-no-unused-hypotheses: fail` — **correct**: the theorem takes 5
  conjecture instances `[QAubinLions] … [RegularityBreakdown]` and discharges
  via the trivial ε=1 instance without using them (a real §3b-cond rule-5
  degeneracy).

So the batch is a **signal/noise mix**, not pure noise: the deterministic
criteria are dominated by false positives, while the judgment criteria
(integrity / self-assuming / unused-hypotheses / false-premise) and the raters
contain genuine findings that must be re-read per block.

## Action taken (this pass — deterministic false-positive correction)

Tool: [`scripts/reaudit-proof-deterministic.py`](../../scripts/reaudit-proof-deterministic.py).
For `proof-no-decide-masking` and `proof-no-trivial-true`, it recomputes the
verdict from the comment-stripped resolved Lean source and **appends** a
corrected agent entry (latest-wins) only where the cached `fail` is contradicted
by the source. Conservative: blocks whose source *does* contain the token are
left as `fail` for the content-fix pass.

| criterion | flipped → `pass` | set → `n/a` (no Lean) | genuine `fail` left |
|---|--:|--:|--:|
| `proof-no-decide-masking` | 205 | 12 | 18 |
| `proof-no-trivial-true` | 155 | 12 | 43 |

**232 sidecars touched**, purely additive entries. Round-trip serialization is
byte-identical to the source, so diffs are confined to the appended entries.

## Remaining work (tracked on this branch)

1. **Fix genuine deterministic fails** — 18 real `decide`/`native_decide`
   maskings + 43 real `: True` conclusions (per §1a: prove / queue with
   `sorry` + `-- Ref:` / demote to `conjecture` — never `: True := trivial`).
2. **Fleet re-audit the judgment criteria** — `proof-statement-integrity` (232),
   `proof-no-self-assuming-projection` (165), `proof-no-unused-hypotheses` (232),
   `proof-no-false-premise` (233): each needs per-block reading of the resolved
   Lean vs the `.md` claim. Some are genuine (e.g. surreal unused-hyps), many
   are false positives.
3. **Re-rate the rater criteria** — `proof-rater-goal-plausibility`,
   `proof-rater-strategy-clarity`, `proof-rater-novelty`.
4. **Warns** — after the failures, per the owner directive.

## Tooling note

The canonical `qa-sweep` / `qa-agent-drain` pipeline lives in the separate
`litlfred/folio-assistant` repo, which is **out of this session's GitHub scope**
(clone → HTTP 403). The re-audit was therefore done directly against the
sidecars (which live in `qou`); `field_hash = sha256(file)[:12]` was verified
reproducible. A canonical re-sweep should be run when folio-assistant is back in
scope to confirm these corrections under the registry's checkers.
