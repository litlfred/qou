---
# qou-bsec
title: jones_wenzl_weight is wrong and LIVE at mass_at_3A_proper.py:592
status: todo
type: task
priority: normal
created_at: 2026-08-23T18:17:08Z
updated_at: 2026-08-23T18:18:41Z
---

## Evidence

`computations/mass_at_3A_proper.py::jones_wenzl_weight` (line 89) implements

    omega_lam = z^{n-1} * prod_{x in lam} (1 - z q^{2c(x)}) / (1 - q^{2h(x)})

with a docstring claiming `Sum_lam omega_lam = 1`.

**It is live**, not dead code: `ocneanu_weights_3A` (line 123) wraps it and is called at
**line 592** (`weight_table = ocneanu_weights_3A((Z + N))`). It is also mirrored into
`qou-mass/src/qou_mass/_internal/mass_at_3A_proper.py` by the vendor sync.

**It is wrong.** Measured in exact sympy over Q(q,z)
(`computations/schurweyl/ocneanu_weight_validation.py`): across 160 convention
combinations -- exponent convention, four q-substitutions, ten z-substitutions, both
plausible targets -- it never reproduces the Lean-proved n=3 weights
`QOU.SchurWeyl.HeckeMarkov3.markovWeight0/1/2`, and never sums to 1.

Three separate defects:

1. **Wrong formula.** The correct closed form is derived in
   `computations/schurweyl/ocneanu_weight_general_n.py` and Lean-proved against the n=3
   case in `QOU/SchurWeyl/OcneanuWeightMarkov3.lean` (PR #5575):

       W_lam(q,z) = prod_{(i,j) in lam} [ q^{2i}(q^2-1-qz) + q^{2j+1} z ]
                    / prod_{(i,j) in lam} [ q^{2h(i,j)} - 1 ]

2. **Wrong normalisation in the docstring.** The Markov trace normalisation is
   `Sum_lam d_lam * W_lam = 1`, not `Sum_lam W_lam = 1` -- `d_lam` is the character of
   the identity in block lam. `computations/ocneanu_weights.py` states it correctly
   (its `omega_lam` is `d_lam * W_lam`); this file does not.

3. **float64.** `q: float = Q0`, `z: float = Z_MARKOV`, `product` accumulated in float.
   AGENTS.md NO-FLOAT64 applies to every `computations/` script.

## Why it survived

Nothing in the repo checked any weight above n = 3, and n <= 3 is where a wrong formula
is hardest to catch: every partition of n <= 3 has DISTINCT cell contents, so a formula
can be off by a whole monomial and still look plausible. The first content repeat is the
two content-0 cells of (2,2), at n = 4.

## Next step

Replace the body with the derived closed form, carried in `mpmath.mpf`; fix the
docstring's normalisation; re-run whatever consumes line 592 and diff the result. Note
that `computations/ocneanu_weights.py::omega_lambda_via_inversion` already computes the
correct weights by a p(n) x p(n) linear solve -- the closed form can replace that solve
outright (cross-checked at n = 2..5 in
`computations/schurweyl/ocneanu_weight_convention_d_support.py`), so the two paths should
converge on one implementation rather than three.
