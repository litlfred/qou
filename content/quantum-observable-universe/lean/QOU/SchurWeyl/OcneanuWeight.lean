import Mathlib.Algebra.BigOperators.Field
import Mathlib.Combinatorics.Young.YoungDiagram

/-!
# QOU.SchurWeyl.OcneanuWeight — the Ocneanu/Markov weight at general `n`

`HeckeWedderburnData` realises the Markov trace on `H_n(q)` as a weighted character sum
`tr_M = Σ_λ w_λ χ_λ`.  `HeckeMarkov3` proves the three weights at `n = 3`
(`markovWeight0/1/2`, derive-then-check against the normalisation and the two Markov relations);
`HeckeWedderburnDataGeneral` supplies the block decomposition at every `n` but leaves the weight
family an explicit **parameter**, because what makes a family *the* Ocneanu one is the Markov
condition, and that is proved only at `n = 3`.

This file supplies the missing ingredient's *definition*: a single closed form
`ocneanuWeight q z μ`, one formula for every Young diagram.  That it **reproduces
`markovWeight0/1/2` exactly** at `n = 3` is proved in `OcneanuWeightMarkov3`, which is a separate
file because those comparisons are `ℝ`-valued (§7c below) while everything here is generic.

## The formula

For a Young diagram `μ`,

```
ocneanuWeight q z μ  =  ∏_{(i,j) ∈ μ} ( q^{2i}·(q² − 1 − q·z) + q^{2j+1}·z )
                      / ∏_{(i,j) ∈ μ} ( q^{2·h(i,j)} − 1 )
```

with `h` the hook length.  Numerator: one factor per cell, affine in the Markov parameter `z`, with
a framing monomial in the row index.  Denominator: the `q²`-hook product.  Pulling the row index
out of the numerator gives the equivalent form `q^{2n(λ)}·∏_x ((q²−1) + zq(q^{2c(x)}−1)) /
∏_x (q^{2h(x)}−1)`, with `c` the cell content and `n(λ) = Σ_i i·λ_i`.

## Provenance — derived, not recalled

The corpus already carried a candidate general-`n` weight
(`computations/mass_at_3A_proper.py::jones_wenzl_weight`).  It is **wrong**: it fails to reproduce
the proved `n = 3` weights under any of 160 convention combinations, and never sums to `1`
(`computations/schurweyl/ocneanu_weight_validation.py`).  The formula above was therefore derived
rather than recalled, in exact `ℚ(q,z)`
(`computations/schurweyl/ocneanu_weight_general_n.py`): solve `n = 2` from `tr(1) = 1` and
`tr(σ₁) = z`; read `n ≤ 3` as a per-cell content product over the hook denominator; then solve
`n = 4, 5` from scratch to pin the framing monomial, which `n ≤ 3` **cannot** see — every partition
of `n ≤ 3` has distinct cell contents, and the first repeat is the two content-`0` cells of `(2,2)`.

Numerically validated in exact arithmetic: `Σ_λ d_λ w_λ = 1` and `Σ_λ w_λ χ^λ(σ₁) = z` through
`n = 6`, and the branching identity `w_μ^{(n)} = Σ_{λ = μ + □} w_λ^{(n+1)}` through `n = 5 → 6`.

## What is NOT claimed here

`OcneanuWeightMarkov3`'s `n = 3` specialisations are the only Lean-proved content about this
formula.  **The Markov property at general `n` is open.**  Nothing in either file instantiates
`HeckeWedderburnData` with `ocneanuWeight` — doing so would let a downstream consumer read the
resulting functional as a Markov trace on the strength of a numerical check, which is exactly the
laundering `HeckeWedderburnDataGeneral`'s docstring warns against.  The general-`n` Markov property
has to be *proved* before that instantiation is honest.

## Base ring (§7c)

`ocneanuWeight` is stated over a generic `[Field R]`: it is a rational function of `q` and `z` with
no ordering, no `Real.sqrt`, no archimedean content — this file mentions `ℝ` nowhere.  The
specialisation to `ℝ` is confined to `OcneanuWeightMarkov3`, and is forced only because
`markovWeight0/1/2` are `ℝ`-valued.

References: Jones (1987) `[jones1987]`, Wenzl (1988) `[wenzl1988]`, Ram (1997) `[ram1997]`.

LaTeX label: `def:ocneanu-weight`
-/

namespace QOU.SchurWeyl

open YoungDiagram

/-- Hook length of the cell `c` in the Young diagram `μ`: arm (cells weakly to the right of `c` in
its row, `c` included) plus leg (cells strictly below `c` in its column). -/
def hookLength (mu : YoungDiagram) (c : ℕ × ℕ) : ℕ :=
  (mu.cells.filter (fun d => d.1 = c.1 ∧ c.2 ≤ d.2)).card
    + (mu.cells.filter (fun d => d.2 = c.2 ∧ c.1 < d.1)).card

/-- **The Ocneanu/Markov weight of a Young diagram**, one closed form for every `n`.

`w_μ(q,z) = ∏_{(i,j) ∈ μ} (q^{2i}(q² − 1 − qz) + q^{2j+1} z) / ∏_{(i,j) ∈ μ} (q^{2h(i,j)} − 1)`.

See the module docstring for how this was derived and for what is *not* proved about it. -/
noncomputable def ocneanuWeight {R : Type*} [Field R] (q z : R) (mu : YoungDiagram) : R :=
  (∏ c ∈ mu.cells, (q ^ (2 * c.1) * (q ^ 2 - 1 - q * z) + q ^ (2 * c.2 + 1) * z))
    / (∏ c ∈ mu.cells, (q ^ (2 * hookLength mu c) - 1))

end QOU.SchurWeyl
