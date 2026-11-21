/-
# Binding q-Gaussian Habiro element — the `(q−1)`-order structure of its log-coefficients

The binding period `S(m) = Σ_{λ⊢m} dim_q(λ)` (q=1 → the involution numbers `I(m)`) has a
generating function that q-deforms the classical involution EGF `Σ_m I(m) x^m/m! = exp(x + x²/2)`.
In the symmetric q-factorial `[m]_q!`, the q-EGF `Ŝ(z) = Σ_m S(m) z^m/[m]_q!` factors as a
q-exponential

    Ŝ(z) = exp( L₁ z + L₂(q) z² + Σ_{m≥3} L_m(q) z^m ),

whose log-coefficients `L_m(q)` are computed exactly (no fit) in
`computations/substrate/lever1_binding_habiro_qexponential.py`
(witness `lever1-binding-habiro-qexponential.witness.json`; audit
`docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md`, Stage 5). There:

* `L₁ = 1` exactly, and `L₁, L₂ → 1, ½` at `q = 1` — the q-Gaussian skeleton, the q-analog of
  the classical `exp(x + x²/2)`.
* every higher log-coefficient `L_{m≥3}` **vanishes at `q = 1` with growing order**:
  `L₃, L₄ ∼ (q−1)²`, `L₅, L₆ ∼ (q−1)⁴`, `L₇, L₈ ∼ (q−1)⁶` — a suppressed Habiro tail.
* all `L_m` denominators are products of cyclotomic polynomials (the Habiro / cyclotomic-completion
  ring); `L₂`'s denominator is `Φ₄ = q²+1`, the `ζ₄` residue.

**What this file certifies.** The numerator of each `L_m` (the expanded polynomial emitted by the
exact symbolic compute) factors as `(q−1)^{e_m} · cofactor` with `e₃ = e₄ = 2`, `e₅ = 4` — i.e.
the suppressed-tail / q-Gaussian-skeleton-exactness claim, as machine-checked ring identities, plus
the `q = 1` classical limit `L₂ = ½`. The *provenance* (that these polynomials are the log-
coefficients of `Ŝ`) is the symbolic compute cited above, not re-proved here — formalizing the
partition-sum EGF and its formal-power-series logarithm is out of scope; this file proves exactly
the algebraic factorization it states.

**See also (sibling Rogers–Szegő formalization on main).** The binding period `S(m)` is the
q-involution number — a moment of the **Rogers–Szegő / q-Hermite** family that
`QOU.Mass.BindingQHermiteOscillator.FollowsRogersSzego` (the §3b recurrence class) and its concrete
instance `QOU.Mass.RogersSzegoInhabited.rsSeq` (`instFollowsRogersSzego`) formalize abstractly. That
work axiomatizes the q-oscillator three-term recurrence; **this** file is the complementary,
independent piece — the *log-coefficients* `L_m(q)` of the binding period's q-Gaussian EGF `Ŝ(z)`
and their cyclotomic `(q−1)`-order structure. Different objects (q-oscillator basis vs.
generating-function log-expansion); no overlap.

Generic base ring `[CommRing R]`: these are purely algebraic identities in the formal fibre
parameter `q`, with no archimedean structure (AGENTS.md §7c). Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md §"Stage 5"
-/
import Mathlib.Tactic

namespace QOU.Mass.BindingQGaussianHabiro

variable {R : Type*} [CommRing R]

/-! ## `L₂` — the q-Gaussian `z²` coefficient, and its classical limit -/

/-- Numerator of `L₂` (the q-Gaussian `z²`-coefficient): `−q² + 4q − 1`. -/
def L2num (q : R) : R := -q ^ 2 + 4 * q - 1

/-- Denominator of `L₂`: `2q² + 2 = 2·Φ₄` (the `ζ₄` residue). -/
def L2den (q : R) : R := 2 * q ^ 2 + 2

/-- **Classical limit.** At `q = 1`, `L₂ = L2num/L2den = 2/4 = ½` — the `z²` coefficient of the
classical involution EGF `exp(x + x²/2)`. Stated division-free as `num(1) = 2 ∧ den(1) = 4`. -/
theorem L2_classical_limit : L2num (1 : R) = 2 ∧ L2den (1 : R) = 4 := by
  refine ⟨?_, ?_⟩ <;> simp only [L2num, L2den] <;> norm_num

/-! ## The suppressed Habiro tail: `(q−1)`-divisibility of the higher log-coefficients -/

/-- Expanded numerator of `L₃` (degree 6). -/
def L3num (q : R) : R := q ^ 6 - 6 * q ^ 5 + 5 * q ^ 4 + 5 * q ^ 2 - 6 * q + 1

/-- Cofactor of `L₃` after removing `(q−1)²`. -/
def L3cof (q : R) : R := q ^ 4 - 4 * q ^ 3 - 4 * q ^ 2 - 4 * q + 1

/-- **`L₃` carries `(q−1)²`** (order `e₃ = 2`). -/
theorem L3_factor (q : R) : L3num q = (q - 1) ^ 2 * L3cof q := by
  simp only [L3num, L3cof]; ring

/-- Expanded numerator of `L₄` (degree 10, palindromic). -/
def L4num (q : R) : R :=
  -q ^ 10 + 9 * q ^ 9 - 23 * q ^ 8 + 22 * q ^ 7 - 8 * q ^ 6 + 2 * q ^ 5
    - 8 * q ^ 4 + 22 * q ^ 3 - 23 * q ^ 2 + 9 * q - 1

/-- Cofactor of `L₄` after removing `(q−1)²`. -/
def L4cof (q : R) : R :=
  -q ^ 8 + 7 * q ^ 7 - 8 * q ^ 6 - q ^ 5 - 2 * q ^ 4 - q ^ 3 - 8 * q ^ 2 + 7 * q - 1

/-- **`L₄` carries `(q−1)²`** (order `e₄ = 2`). -/
theorem L4_factor (q : R) : L4num q = (q - 1) ^ 2 * L4cof q := by
  simp only [L4num, L4cof]; ring

/-- Expanded numerator of `L₅` (degree 18, palindromic). -/
def L5num (q : R) : R :=
  q ^ 18 - 11 * q ^ 17 + 39 * q ^ 16 - 58 * q ^ 15 + 48 * q ^ 14 - 50 * q ^ 13
    + 82 * q ^ 12 - 112 * q ^ 11 + 110 * q ^ 10 - 98 * q ^ 9 + 110 * q ^ 8
    - 112 * q ^ 7 + 82 * q ^ 6 - 50 * q ^ 5 + 48 * q ^ 4 - 58 * q ^ 3
    + 39 * q ^ 2 - 11 * q + 1

/-- Cofactor of `L₅` after removing `(q−1)⁴`. -/
def L5cof (q : R) : R :=
  q ^ 14 - 7 * q ^ 13 + 5 * q ^ 12 + 8 * q ^ 11 + 21 * q ^ 10 + 13 * q ^ 9
    + 35 * q ^ 8 + 26 * q ^ 7 + 35 * q ^ 6 + 13 * q ^ 5 + 21 * q ^ 4
    + 8 * q ^ 3 + 5 * q ^ 2 - 7 * q + 1

/-- **`L₅` carries `(q−1)⁴`** (order `e₅ = 4`) — the tail suppression deepens from `(q−1)²`
(`m = 3, 4`) to `(q−1)⁴` (`m = 5`). -/
theorem L5_factor (q : R) : L5num q = (q - 1) ^ 4 * L5cof q := by
  simp only [L5num, L5cof]; ring

/-! ## Consequence: the higher log-coefficients vanish at `q = 1` (q-Gaussian skeleton) -/

/-- At `q = 1` the `L₃` numerator vanishes — the classical limit collapses the tail onto the
pure q-Gaussian. (Follows from `L3_factor`.) -/
theorem L3num_vanishes_at_one : L3num (1 : R) = 0 := by
  rw [L3_factor]; ring

theorem L4num_vanishes_at_one : L4num (1 : R) = 0 := by
  rw [L4_factor]; ring

theorem L5num_vanishes_at_one : L5num (1 : R) = 0 := by
  rw [L5_factor]; ring

end QOU.Mass.BindingQGaussianHabiro
