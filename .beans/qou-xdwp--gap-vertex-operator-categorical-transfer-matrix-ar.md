---
# qou-xdwp
title: 'GAP: vertex-operator + categorical-transfer-matrix — architectural blockers behind the parse errors'
status: todo
type: task
priority: normal
created_at: 2026-09-03T23:11:58Z
updated_at: 2026-09-03T23:12:45Z
---

Two of the four parse-failures from the sibling sweep (`qou-e7xv`). Both are
now much closer, and both stop at something structural rather than syntactic.

    categorical-transfer-matrix.lean   13 errors -> 3
    vertex-operator.lean                7 errors -> 1

## Fixed (mechanical, verified)

1. A `/-- … -/` docstring immediately followed by `noncomputable section`.
   A docstring must attach to a DECLARATION; `section` is not one. Moved the
   `section` above the docstring. (Both files, identical.)
2. `LaurentPolynomial` unknown — neither imported
   `Mathlib.Algebra.Polynomial.Laurent`, though both declare
   `abbrev R_q := LaurentPolynomial ℤ`.
3. An unclosed `noncomputable section`: both open `namespace QOU` then a
   section, and close only with `end QOU`. Pre-existing, and MASKED by defect
   1 — the parse error meant the section never opened, so the imbalance could
   not surface. Added the bare `end`.
4. `vertex-operator` wrote `-(q⁻¹)` with `q : R_q`. Same shape as the
   `Inv GroundRing.R_q` cluster, but here the file is genuinely categorical,
   so `⁻¹` is simply the wrong spelling — the file declares `q_inv_param`
   itself, three lines up. Now `-q_inv_param`.

## Still open — architectural, one each

**`vertex-operator.lean`, 1 error: `ReebBundle` is not in scope.**
It is declared in `mass-theory/reeb-bundle.lean` — ANOTHER CONTENT-BLOCK
SIBLING, which this file structurally cannot import: siblings live outside
the Lake globs (`globs = ["QOU", "QOU.+"]`, `srcDir = "."`), so there is no
module path to them. Options: promote `ReebBundle` into the Lake library
(same shape as the queued `VolumeConjecture` promotion), or re-declare it
locally. Note also a wall issue if promoted as-is: `structure ReebBundle
(q : ℝ)` is archimedean while `vertex-operator` is categorical (`q : R_q`).

**`categorical-transfer-matrix.lean`, 3 errors: an undetermined implicit.**
`CategoricalTransferMatrix q` has a field `base : ExceptionalDivisor` where
`ExceptionalDivisor` is not a parameter of the structure and cannot be
inferred at the use site, so `T₁.base = T₂.base` fails to elaborate. The
structure needs to be parameterised over it (or `ExceptionalDivisor` needs to
be a concrete type).

Worth flagging: the declaration this blocks is
`axiom transfer_matrix_level_independence`, and
`prop:transfer-matrix-level-independence` is one of the FOUR provable-kind
blocks whose Lean is a bare `axiom` (found earlier this session by
`scripts/provable-block-axiom-audit.ts`). So this file wants the axiom
question settled at the same time, not two passes.

No `sorry` was added anywhere (§Zero-sorry default).
