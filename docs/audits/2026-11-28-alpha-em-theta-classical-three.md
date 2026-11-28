# α_EM two-loop: the θ-graph's classical `3` is the unsigned history count minus the singlet (2026-11-28)

Bean `qou-l4t2`. Mathematics only. Lean:
[`QOU/MassTheory/EmThetaClassicalThree.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/EmThetaClassicalThree.lean)
(lean-direct exit 0 with `-DautoImplicit=false`; axioms `propext`, `Quot.sound`,
`Classical.choice` only; no `sorry`). Follows
[the placement-count note](2026-11-28-alpha-em-two-loop-placement-count.md), which
showed `[3]_q = 3 + h² = 3 − V` and that no skein chain gives the `3`.

## Result

At one convention-D generator `σ` (`σ² = hσ + 1`):

1. `σ + σ⁻¹ = 2σ − h` (`sum_eq_two_sigma_sub`).
2. The **unsigned** sum over the four chiral histories, `(σ + σ⁻¹)²`, is the scalar
   `4 + h² = [2]_q²` (`unsignedPair_eq_two_sq`, `unsignedPair_eq_qInt2_sq`).
3. `[3]_q = (unsigned pair) − 1` (`qInt3_eq_unsignedPair_sub_one`). This is the
   Clebsch–Gordan split `[2]² = [3] + [1]`.

**Consequence.** The two readings use the same four histories with different
weights:

| | weights on `(ε₁, ε₂)` | value at one position | at `q = 1` |
|---|---|---|---|
| Form B | signed, `−ε₁ε₂` (bar-Hermitian) | `−h²` | `0` |
| θ-graph | unsigned, then remove the singlet | `[3]_q = 3 + h²` | `3` |

The `3` is the four chiral histories counted with weight 1, less the spin-0
(singlet) channel. The signed weights cancel that count. Both readings have the same
`h²` piece up to sign convention.

One structural difference: the signed pair is the scalar `−h²` at **any** two
positions (`vertexPair_eq_neg_hsq`). The unsigned pair is a scalar at one position
only; at two different generators `(2σ − h)(2τ − h)` is not central in general.

## Open (a choice, not derived here)

Which weights the two-vertex photon insertion carries: signed (Form B) or unsigned
with the singlet removed (θ-graph). `qou-aemx` keeps the canonical form open, and
this note does not choose.
