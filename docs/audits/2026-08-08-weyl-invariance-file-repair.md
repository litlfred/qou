# `WeylInvarianceQDeformation.lean` — red on `main`, and its headline theorem was a tautology

**Date:** 2026-08-08
**Branch / PR:** `claude/std-model-1ppq-l2-vectors-mf0rrb` / #4727
**Lean:** [`QOU/Eightfold/WeylInvarianceQDeformation.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/WeylInvarianceQDeformation.lean)
— now `lean`-direct **exit 0**, sorry-free, axioms `{propext, Quot.sound, Classical.choice}` only.

## How this surfaced

Not from an audit sweep. While recording refuted-class row **C20** (the
eightfold layer carries no L2 leverage) I cited
`cartanMatrix_A2_q_independent` as the load-bearing invariant for the
scope-(b) exclusion of the classification sub-layer, then opened the file to
check an adjacent `native_decide` hygiene item. The declaration did not say
what three `.md` blocks claim it says.

This is the failure mode AGENTS.md §"QA is agent-owned" names explicitly: a
**standalone library `.lean` file with no `<block>.qa.json` sidecar** is not
covered by `lean-content-siblings.yml` and escapes every per-block checker.
With CI auto-triggers disabled repo-wide, nothing but an agent reads it. It had
been red since it landed.

## Four defects

| # | defect | rule violated |
|---|---|---|
| 1 | **File did not compile.** Two `error: No goals to be solved` — a dead `ring` after a closing `simp` in `qSerre_eq_cartan_at_classical` (line 78), and a dead `native_decide` after a closing `simp` in `root_angle_ratio_A2` (line 87). | — (plain breakage) |
| 2 | **Headline theorem was a tautology.** `cartanMatrix_A2_q_independent (R) (q₁ q₂ : R) : cartanMatrix_A2 = cartanMatrix_A2 := rfl`. The `R, q₁, q₂` binders are unused — the linter said so — so the statement quantifies over `q` while asserting nothing about it. | §"Strict Lean Discipline" item 5: `X = X := rfl` is always a review failure |
| 3 | **`qSerre_neq_cartan_diag` assumed its conclusion.** Hypothesis `q² + 1 ≠ 2q`; conclusion `gaussianBinomial2Framed R q ≠ 2 * q`. But `gaussianBinomial2Framed R q` is *definitionally* `q² + 1`, so the proof `intro h; exact hq (h ▸ rfl)` is a restatement modulo unfolding. | §3b-cond item 5 (self-assuming projection); §"Strict Lean Discipline" item 5 |
| 4 | **Three `native_decide` on concrete finite lookups.** `cartan_A2_offdiag`, `serre_exponent_A2`, `root_angle_ratio_A2`. | §"Strict Lean Discipline" item 6 — **already flagged** in bean `qou-8fl1` item 4 |

Defect 4 was known. Defects 1–3 were not.

## What the file now proves

The honest content of "the two 2s are different objects" is a **conjunction**,
and only one half of it has force:

- `cartanMatrixAt_const` — the Cartan datum is constant in `q`. Kept, but
  renamed and re-documented as **true by construction**: `cartanMatrixAt`
  ignores its argument, so this is `rfl` and carries no information alone. Its
  docstring now says so, and says explicitly not to cite it as evidence for
  q-independence of the classification.
- `qSerre_not_constant` — **new, and the half with content**: `∃ q : ℤ,
  gaussianBinomial2Framed ℤ q ≠ 2 * q`, witnessed at `q = 2` (`5 ≠ 4`).
  Without it, `cartanMatrixAt_const` is equally compatible with *both* sides
  being constant — precisely the confusion the file exists to dispel.
- `cartan_fixed_while_qSerre_moves` — **new**: the conjunction. This is the
  file's actual claim.
- `qSerre_neq_cartan_diag` — restated with the genuinely upstream hypothesis
  `(q - 1)² ≠ 0`; the proof now supplies the identity
  `(q² + 1) - 2q = (q - 1)²` via `linear_combination`.
- `native_decide` → `decide` (×2); the third was dead code and is deleted.

## What this does NOT change

**The mathematics is unaffected.** The A₂ Cartan datum *is* q-independent under
Drinfeld–Jimbo quantisation — that is a theorem of Lusztig/Kashiwara, which the
chapter cites and this file never formalised. What was wrong was the *evidence
line*, not the claim.

Accordingly:

- **C20 sub-layer (i) survives**, re-scoped: its invariant is **standard**
  (Drinfeld–Jimbo), not proved-in-corpus. The ledger row and the two `.md`
  blocks are corrected to say so.
- **C20 sub-layers (ii) and (iii) are unaffected** — this survey independently
  `lean`-direct verified [`GellMannOkuboIdentity.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/GellMannOkuboIdentity.lean)
  and [`RowCapObstruction.lean`](../../content/quantum-observable-universe/lean/QOU/Eightfold/RowCapObstruction.lean)
  at **exit 0, zero errors**, with real statements and real proofs
  (`Nat.choose_eq_zero_iff`, `ring`). Those citations stand as written.
- **No L2 movement.** Nothing here touches a precision target.

## Verification

Restored `lake-cache/qou-v4-24-0` (6990 mathlib oleans), then `lean`-direct via
[`scripts/lean-verify.sh`](../../scripts/lean-verify.sh) — **never** `lake
build`, per the skill's standing warning:

| file | before | after |
|---|---|---|
| `WeylInvarianceQDeformation` | exit 1, 2 errors | **exit 0**, 0 errors, 0 unused-binder warnings |
| `RowCapObstruction` | exit 0 | exit 0 |
| `GellMannOkuboIdentity` | exit 0 | exit 0 |
| `Sym2Gate`, `Sym2GateParity` | exit 0 | exit 0 |

`#print axioms` on all eight declarations of the repaired file: `propext`,
`Quot.sound`, `Classical.choice` only — **no `sorryAx`**.

## Follow-ups not taken here

- **`Sym2Gate.lean` is vacuous** (bean `qou-8fl1` item 3): declarations reduce
  to `6 = 6 ∧ 0 = 0`. It compiles, and the chapter prose already handles it
  honestly ("not excluded by the Sym² gate", "should not be cited as" a
  machine-checked pass), so it is a live but correctly-labelled item. Left to
  `qou-8fl1`.
- **A sweep for the same shape elsewhere.** This file was found by accident, not
  by a checker. `X = X := rfl` with unused binders in an un-sidecar'd library
  file is mechanically detectable, and the fact that a red file sat on `main`
  undetected suggests the class is worth a pass. Beaned separately.
