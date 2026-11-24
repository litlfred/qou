import Mathlib.Tactic

/-!
# The Jones–Markov weights are Webster–Williamson Molien series (n = 3, exact)

`qou-sf1t` / `qou-3quc`. The 2026-08-21 Molien lead
(`docs/audits/2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md`)
observed that Webster–Williamson (*The geometry of Markov traces*,
`arxiv-0911.4494v2`, bib key `webster-williamson-2014-markov`) realise the
Jones–Ocneanu trace weights as **Molien series** `M_ν(u,t)` of the reflection
representation, and named four verification items. The 2026-08-22 note refuted
the *guessed* closed form `y_λ = f^λ q^{−κ_λ}/[n]_q!` — the wrong normaliser.

This file supplies the **correct** identification for `n = 3`, exact-symbolic:
under the forced specialisation

  `u = q²,   t = q z / (q² − q z − 1)`

the `S₃` Molien series `M_ν(u,t)` equal the Jones–Markov Hecke weights `y_λ(z)`
up to a **single common normaliser** `Z = (q² − q z − 1)²` — a perfect square,
the *Poincaré/Molien* shape the lead predicted, NOT `[n]_q!`:

  `y_(3) = M_triv · Z,   y_(2,1) = M_std · Z,   y_(1³) = M_sign · Z.`

The specialisation is not fitted: eliminating `t` gives a Molien conic in the
weight ratios, and requiring the three `y_λ`-ratios to lie on it is an
**overdetermined** system (three `z`-coefficients, one unknown `u`) whose only
solution is the monomial `u = q²` (and its bar `u = q⁻²`). This resolves the
lead's items 4 (weight family = Jones–Markov `y_λ`), 2 (specialisation), and the
weight-level half of item 1 (the geometric-trace weights are `tr_M`'s) — **for
`n = 3`**. General `n` (`qou-3quc`) stays open; this is one (strong) data point.

## What is proved here

Each theorem is the **denominator-cleared** form of `y_λ = M_ν(q², tSpec) · Z`,
a pure polynomial identity over any commutative ring (`ring`). Writing
`N_ν := molNum_ν(q², tSpec) · (q²−qz−1)²` (the Molien numerator with the weight
variable specialised and the normaliser cleared — a polynomial), the identity
`y_λ = M_ν · Z` is exactly

  `y_λ^num · molDen_ν(q²) = y_λ^den · N_ν`.

The `N_ν` are the polynomials named `nThree/nSign/nStd` below; that each equals
`molNum_ν(q², q z/(q²−qz−1))·(q²−qz−1)²` is a one-line rational computation (done
in the companion probe, exact `ℚ(q,z)`), and the polynomial identities are what
the corpus's checker can re-verify. The `S₃` Molien series and the `H₃(q)`
Jones–Markov weights are computed by unrelated routes, so the match is an
identity, not a tautology.

Base ring (§7c): a generic `CommRing K` — a polynomial identity, no ordering,
no archimedean structure, no division.

-- Ref: [webster-williamson-2014-markov] arXiv:0911.4494, The geometry of Markov traces
-- Ref: [leitner2026] docs/audits/2026-08-21-webster-williamson-molien-lead-for-equivariant-index.md
-/

namespace QOU.QBeta.MolienJonesMarkovN3

variable {K : Type*} [CommRing K]

/-! ### The Jones–Markov weight numerators / denominators (`H₃(q)`, parameter `z`) -/

/-- `y_(3)` numerator. -/
def yThreeNum (q z : K) : K := q ^ 4 * z ^ 2 + q ^ 3 * z + q ^ 2 * z ^ 2 + 2 * q * z + 1
/-- `y_(1³)` numerator. -/
def ySignNum (q z : K) : K := q ^ 2 * (q ^ 4 - 2 * q ^ 3 * z + q ^ 2 * z ^ 2 - q * z + z ^ 2)
/-- `y_(2,1)` numerator. -/
def yStdNum (q z : K) : K := q * (q ^ 2 * z - q * z ^ 2 + q - z)
/-- Shared `y` denominator for the one-dimensional reps. -/
def yOneDimDen (q : K) : K := q ^ 6 + 2 * q ^ 4 + 2 * q ^ 2 + 1
/-- `y_(2,1)` denominator. -/
def yStdDen (q : K) : K := q ^ 4 + q ^ 2 + 1

/-! ### The Molien denominators at `u = q²` (Webster–Williamson, `S₃`) -/

/-- `molOneDimDen(q²) = (q²)⁵ − (q²)³ − (q²)² + 1`. -/
def molOneDimDenAtQsq (q : K) : K := q ^ 10 - q ^ 6 - q ^ 4 + 1
/-- `molStdDen(q²) = (q²)⁴ − (q²)³ − q² + 1`. -/
def molStdDenAtQsq (q : K) : K := q ^ 8 - q ^ 6 - q ^ 2 + 1

/-! ### The cleared Molien numerators `N_ν = molNum_ν(q², tSpec)·(q²−qz−1)²` -/

/-- `N_(3)` — the trivial-rep Molien numerator, specialised and denom-cleared. -/
def nThree (q z : K) : K :=
  q ^ 8 * z ^ 2 + q ^ 7 * z - q ^ 6 * z ^ 2 - q ^ 4 * z ^ 2 + q ^ 4 - 3 * q ^ 3 * z
    + q ^ 2 * z ^ 2 - 2 * q ^ 2 + 2 * q * z + 1
/-- `N_(1³)` — the sign-rep Molien numerator, specialised and denom-cleared. -/
def nSign (q z : K) : K :=
  q ^ 10 - 2 * q ^ 9 * z + q ^ 8 * z ^ 2 - 2 * q ^ 8 + 3 * q ^ 7 * z - q ^ 6 * z ^ 2 + q ^ 6
    - q ^ 4 * z ^ 2 - q ^ 3 * z + q ^ 2 * z ^ 2
/-- `N_(2,1)` — the standard-rep Molien numerator, specialised and denom-cleared. -/
def nStd (q z : K) : K :=
  q ^ 7 * z - q ^ 6 * z ^ 2 + q ^ 6 - 3 * q ^ 5 * z + 2 * q ^ 4 * z ^ 2 - 2 * q ^ 4
    + 3 * q ^ 3 * z - q ^ 2 * z ^ 2 + q ^ 2 - q * z

/-! ### The Webster–Williamson `S₃` Molien numerators (generic `u, t`) -/

/-- Molien numerator of the trivial rep `V_(3)`: `t²u³ + tu² + tu + 1`. -/
def molTrivNum (u t : K) : K := t ^ 2 * u ^ 3 + t * u ^ 2 + t * u + 1
/-- Molien numerator of the sign rep `V_(1³)`: `t² + tu² + tu + u³`. -/
def molSignNum (u t : K) : K := t ^ 2 + t * u ^ 2 + t * u + u ^ 3
/-- Molien numerator of the standard rep `V_(2,1)`: `t²u + tu² + t + u`. -/
def molStdNum (u t : K) : K := t ^ 2 * u + t * u ^ 2 + t + u

/-! ### Grounding: each `N_ν` IS the Molien numerator at `u=q²`, `t=qz/(q²−qz−1)`,
denominator-cleared by `(q²−qz−1)²`. Setting `W := q²−qz−1` and `t = qz/W`,
`molNum_ν(q², t)·W²` is a polynomial (the `W` in `t = qz/W` cancels), and it is
exactly `N_ν`. Pure `ring`; this is the step that makes the Molien identification
Lean-certified rather than probe-asserted. -/

/-- `N_(3) = molTrivNum(q², qz/W)·W²` with `W = q²−qz−1` (cleared). -/
theorem nThree_is_molien (q z : K) :
    nThree q z
      = (q * z) ^ 2 * (q ^ 2) ^ 3
        + (q * z) * (q ^ 2 - q * z - 1) * ((q ^ 2) ^ 2 + q ^ 2)
        + (q ^ 2 - q * z - 1) ^ 2 := by
  unfold nThree; ring

/-- `N_(1³) = molSignNum(q², qz/W)·W²` (cleared). -/
theorem nSign_is_molien (q z : K) :
    nSign q z
      = (q * z) ^ 2
        + (q * z) * (q ^ 2 - q * z - 1) * ((q ^ 2) ^ 2 + q ^ 2)
        + (q ^ 2) ^ 3 * (q ^ 2 - q * z - 1) ^ 2 := by
  unfold nSign; ring

/-- `N_(2,1) = molStdNum(q², qz/W)·W²` (cleared). -/
theorem nStd_is_molien (q z : K) :
    nStd q z
      = (q * z) ^ 2 * (q ^ 2)
        + (q * z) * (q ^ 2 - q * z - 1) * ((q ^ 2) ^ 2 + 1)
        + (q ^ 2) * (q ^ 2 - q * z - 1) ^ 2 := by
  unfold nStd; ring

/-! ### The identification `y_λ = M_ν · Z` (denominator-cleared) -/

/-- **`y_(3) = M_triv · Z`**, cleared:
`yThreeNum · molOneDimDen(q²) = yOneDimDen · N_(3)`. -/
theorem yThree_eq_molien (q z : K) :
    yThreeNum q z * molOneDimDenAtQsq q = yOneDimDen q * nThree q z := by
  unfold yThreeNum molOneDimDenAtQsq yOneDimDen nThree; ring

/-- **`y_(1³) = M_sign · Z`**, cleared:
`ySignNum · molOneDimDen(q²) = yOneDimDen · N_(1³)`. -/
theorem ySign_eq_molien (q z : K) :
    ySignNum q z * molOneDimDenAtQsq q = yOneDimDen q * nSign q z := by
  unfold ySignNum molOneDimDenAtQsq yOneDimDen nSign; ring

/-- **`y_(2,1) = M_std · Z`**, cleared:
`yStdNum · molStdDen(q²) = yStdDen · N_(2,1)`. -/
theorem yStd_eq_molien (q z : K) :
    yStdNum q z * molStdDenAtQsq q = yStdDen q * nStd q z := by
  unfold yStdNum molStdDenAtQsq yStdDen nStd; ring

/-- **(CAPSTONE) The whole `S₃` Jones–Markov weight system is Webster–Williamson
Molien series** at the single forced specialisation `u = q²`, `t = qz/(q²−qz−1)`,
with one common perfect-square normaliser `(q²−qz−1)²`. Resolves the Molien
lead's items 4 / 2 and the weight-level half of item 1 for `n = 3`. -/
theorem jonesMarkov_weights_are_molien (q z : K) :
    yThreeNum q z * molOneDimDenAtQsq q = yOneDimDen q * nThree q z
    ∧ ySignNum q z * molOneDimDenAtQsq q = yOneDimDen q * nSign q z
    ∧ yStdNum q z * molStdDenAtQsq q = yStdDen q * nStd q z :=
  ⟨yThree_eq_molien q z, ySign_eq_molien q z, yStd_eq_molien q z⟩

end QOU.QBeta.MolienJonesMarkovN3
