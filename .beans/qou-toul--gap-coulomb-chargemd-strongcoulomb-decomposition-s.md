---
# qou-toul
title: 'GAP: coulomb-charge.md strong/Coulomb decomposition swaps (p+m)/(p-m) multiplicities — Lean-refuted, 5 blocks propagate'
status: in-progress
type: task
priority: normal
created_at: 2026-08-08T13:04:42Z
updated_at: 2026-08-29T02:31:23Z
---

## VERIFIED AND FIXED — 2026-08-29

The bean title was correct and I confirmed it independently before acting
(it carried no body, so it was a claim rather than evidence).

### The defect, derived rather than asserted

`def:crossing-energy` weights a positive crossing `q` and a NEGATIVE crossing
`-q^-1`, citing the Skein relation. So `E = n+ q - n- q^-1`. Solving
`E = A(q+q^-1) + B(q-q^-1)` gives

    A (symmetric / strong)      = (n+ - n-)/2     the WRITHE
    B (antisymmetric / Coulomb) = (n+ + n-)/2     the crossing COUNT

`coulomb-charge.md` had these exchanged. Its decomposition expands to
`n+ q + n- q^-1`, exceeding the crossing energy by `2 n- q^-1`, and agreeing
only on positive braids — which is why it survived: the canonical atomic
braids the corpus evaluates are positive.

### The corpus was already right three files away

`prop:crossing-energy-decomposition` states `E_sym = (p-m) cosh`,
`E_asym = (p+m) sinh`, and scopes the tanh ratio to `m = 0` explicitly. So
this was never a corpus-wide error — `coulomb-charge.md` and
`crossing-energy.lean` were the two outliers. `QOU.Braiding.crossing_energy_channels`
in the Lake tree is also correct.

### How it survived — the part worth keeping

`crossing-energy.lean` did not inherit the error passively. Its docstring
said: *"with `-q^-1` the baseline + Coulomb decomposition would not hold, so
the energy is the additive `n+ q + n- q^-1`"* — the DEFINITION was adjusted so
the theorem would be provable, then `decomposition` was closed by `ring`,
sorry-free. A fit located in a definition rather than a parameter; no numeric
audit could catch it.

### What landed

- `coulomb-charge.md`: correct decomposition; the trichotomy replaced by the
  two real consequences (the Coulomb coefficient is non-negative, so no
  attractive channel and no negative charge; `n+ = n-` annihilates the
  SYMMETRIC term, so the ratio diverges there rather than vanishing); the
  tanh ratio scoped to `n- = 0`; the electromagnetic identification marked
  NOT established by this decomposition, with the name retained so the 12
  citing blocks do not cascade.
- `crossing-energy.lean`: Skein sign restored, correct multiplicities, the
  laundering docstring replaced by a record of it, and two new theorems so
  the defect cannot recur silently — `swapped_decomposition_off_by` (the
  discrepancy is exactly `2 n- q^-1`) and `swapped_agrees_iff_positive_braid`.
- `coulomb-charge.lean`: `coulombCorrection` (the swapped channel) replaced by
  `coulombContribution` / `strongContribution`, plus
  `antisymCoefficient_nonneg` and `antisymCoefficient_eq_zero_iff` making the
  falsifiable consequences theorems.

All sorry-free; lean-direct exit 0 on both files; `#print axioms` clean on all
seven.

### Still open — deliberately NOT done here

The bean says "5 blocks propagate". I did not verify that number and did not
rewire downstream: 12 `.ts` files carry a `def:coulomb-charge` edge, and
separating genuine dependence from citation, then deciding whether `Q` should
be renamed, is a physics/naming call for the author. The blast radius of the
Lean fix itself is zero — both corrected definitions were used only in their
own files.
