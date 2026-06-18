# Lean vacuity scanner — recall-gap fix + drain queue

**Date:** 2026-06-18
**Branch:** `claude/stoic-pasteur-jwqdlh` ([PR #2462](https://github.com/litlfred/qou/pull/2462))
**Predecessor:** [`2026-06-17-lean-vacuity-axiom-audit.md`](2026-06-17-lean-vacuity-axiom-audit.md) (#2428)
**Scanner:** [`content/pipeline/lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
**Witness:** [`2026-06-17-lean-vacuity-axiom-audit.json`](2026-06-17-lean-vacuity-axiom-audit.json) (refreshed)

This closes the recall gap #2428 flagged at `knot_factor_spectral_derivation:70`
and **queues** the other two follow-ups. The recall fix turned out to be a 9×
undercount, not a one-line miss, so the remaining drains are scoped here rather
than force-completed (they are research-grade and/or Lean-env-blocked this
session).

## 1. Recall-gap fix (done)

### Root cause

`splitDecls` sliced each declaration's text up to the **next** declaration
start (`codeLines.slice(i, end)`). The trailing top-level structural lines that
sit between a declaration and the next one — a `namespace`/`section` `end`
closer, `open`, `variable`, … — therefore got swept into the body of the
**last declaration in each namespace**. A projection body then read as

```
ctx.claim_field

end QOU.Foo
```

which fails the `PROJECTION_BODY` (`/^([a-z][\w']*)\.([A-Za-z_][\w']*)\s*$/`)
`\s*$` anchor. So the self-assuming detector silently missed **every
last-decl-before-a-closer**. `plancherelWeight_sum_eq_one:61` was caught only
because the *next* declaration's comment-stripped docstring left blank lines
after its body; its structural sibling `knot_factor_spectral_derivation:70`
(literally `:= ctx.claim_knot_factor_spectral`) sat last before
`end QOU.BraidKnot` and was missed.

### Fix

Drop trailing blank / structural lines (`end`, `namespace`, `section`, `open`,
`variable`, `universe`, `attribute`, `set_option`) that belong to no
declaration before splitting `sig`/`body`. This is a strict parser-accuracy
improvement: it only removes non-declaration content, so it cannot merge
unrelated text or create false positives.

### Effect (1755 `.lean` scanned)

| category | #2428 | now | Δ |
|---|---|---|---|
| `proof-no-self-assuming-projection` | 22 | **199**² | +177 |
| `proof-no-trivial-true` | 130 | 123 | −7 |
| &nbsp;&nbsp;↳ `placeholder-true` | 48 | **111** | +63 |
| &nbsp;&nbsp;↳ `conclusion-True` | 73 | 3 | −70¹ |
| &nbsp;&nbsp;↳ `reflexive-tautology` | 9 | 9 | 0 |
| `proof-no-decide-masking` | 31 | 31 | 0 |
| `proof-no-false-premise` | 13 | 13 | 0 |
| exempt (shadow-stubs + iff-from-directions) | 39 | 48² | +9 |
| **total candidates** | 196 | **366**² | +170 |

¹ `conclusion-True` decls whose body was previously polluted (`… end Foo`) now
parse cleanly and reclassify into `placeholder-true` / `self-assuming` per their
real body — net recall up across the board.

² Post **precision-fix** (§1a): the recall-fix alone produced 201 self-assuming
/ 368 total; the precision-fix then exempted 2 false-positives (201→199,
exempt 46→48, total 368→366).

### 1a. Precision-fix (2 false-positive exemptions)

The recall-fixed scanner flagged 2 *legitimate* `§3b-cond` proofs as
self-assuming: `q_bkm_criterion` and `ns_obstruction_tower`. Both are
`theorem : A ↔ B := ⟨ctx.fwd, ctx.bwd⟩` that **derive** the iff from two
direction fields (`A → B`, `B → A`) — the class carries the two *implications*,
not the conclusion. The anonymous `Iff.intro` constructor `⟨_, _⟩` is not in the
`DERIVES` regex, hence the false-positive.

Fix: exempt a two-field tuple-projection whose conclusion's **top-level**
connective is `↔` (`reason: "legitimate iff-from-directions conditional-class"`).
A new `conclusionTypeAscription` helper reads the conclusion at the *first*
top-level `:` (robust to a conclusion containing a binder colon such as
`∃ n : ℕ` — `ns_obstruction_tower`'s case, which the existing last-colon
`conclusionOf` mis-sliced). Narrow by construction: a tuple-projection of a
top-level `↔` can only be `Iff.intro` of the two directions. Verified: exactly
these 2 move to exempt; `proof-no-trivial-true` (123), `-decide-masking` (31),
`-false-premise` (13) unchanged.

`self-assuming` splits 114 field-projection / 85 tuple-projection (+2 exempt
iff-from-directions). Sampled 12 of the new hits — all the genuine `§3b-cond`
conditional-class pattern
(`theorem foo [ctx : FooContext] : <claim> := ctx.claim_foo`), not false
positives. The original 22 were simply the subset that didn't sit last before a
closer.

## 2. Drain queue (the three #2428 follow-ups — not drained this session)

> **Why not drained here.** (a) Each item below changes Lean statements and
> requires `lake build` / `lean`-direct verification, and the Lean toolchain is
> unavailable in this sandbox (elan cannot fetch from `release.lean-lang.org`).
> (b) Items 2–3 demote/restate `theorem` claims, which per the #2428 skill's
> recipe-4 and CLAUDE.md is a **claim-change requiring owner sign-off**, not an
> auto-commit. The right vehicle is `/integration-backlog proof` over many
> small per-chapter PRs.

### Q1 — `self-assuming-projection` triage (199 ✓ catalogued in #2468)

**Read-only triage drained in [PR #2468](https://github.com/litlfred/qou/pull/2468)**
([`2026-06-18-self-assuming-projection-triage.md`](2026-06-18-self-assuming-projection-triage.md)):
all 201 classified — **199 degenerate / 2 legitimate**. The 114 field-projections
are degenerate by a typing argument (a bare conclusion-named single-field
projection necessarily carries the conclusion); 85 tuple-projections are
degenerate-split; the 2 legitimate (iff-from-directions) are now scanner-exempt
per §1a. Per-block verdicts in the #2468 sidecar JSON.

What remains is the *remediation* (not the triage): per degenerate block, restate
the class to carry the *hypotheses* and derive the conclusion per `§3b-cond`
item 5, or demote to `conjecture`/`remark`. This is a claim-change (owner
sign-off + Lean verification) — the `/integration-backlog proof` campaign below.

Suggested batches (by chapter, ≤ 49 files each — the Gemini review limit):

| batch | chapter / tree | self-assuming count |
|---|---|---|
| 1 | `lean/QOU/BraidKnot` | 28 |
| 2 | `lean/QOU/Archimedean` | 20 |
| 3 | `lean/QOU/ParticleInteractions` | 19 |
| 4 | `lean/QOU/FluidDynamics` (11) + `Torsion` (7) + `Braiding` (7) | 25 |
| 5 | `lean/QOU/BraidsAndKnots` (7) + `AlgebraicSubstrate` (7) + `QuantumObservableUniverse` (6) + `Observations` (6) + `Molecular` (6) | 32 |
| … | remaining trees | balance to 201 |

### Q2 — `placeholder-true` gaps (111, ↑ from 48)

Genuine `: True := trivial/sorry` stubs with no resolvable real declaration.
Honest fix: state the real proposition (`sorry` + `-- Ref:`), or **demote
`theorem → conjecture`** — a claim-change requiring owner sign-off. Shadow stubs
(real formalisation elsewhere) are already exempted by the scanner (46 exempt).

### Q3 — genuine `r_matrix` YBE / `SubstrateEW` proofs (research-grade)

The drain assessment in #2428 found these are atomic cited/conjectural claims
whose honest fix is a real Yang–Baxter / electroweak-substrate derivation — out
of scope for a mechanical drain, and gated by the same Lean-env + claim-change
constraints. Track as a research item, not a backlog batch.

## 3. Verification

- `bun run content/pipeline/lean-vacuity-axiom-audit.ts` → exit 0; the witness
  reflects the counts above; `knot_factor_spectral_derivation:70` now flagged.
- No `.lean` files changed by this PR → no `lake build` required.
