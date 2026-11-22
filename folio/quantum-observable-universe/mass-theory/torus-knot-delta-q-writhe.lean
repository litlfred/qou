import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Tactic.Ring


/-!
# QOU.TorusKnotDeltaQ.torus_deltaQ_eq_h_qbracket

The **writhe exponent** of the torus-knot q-dimension decoration:
`δ_q(T_{m,p}) = q^w − q^{-w} = h·[w]_q` at `w = (m-1)p`, the writhe of the
standard positive braid `(σ₁⋯σ_{m-1})^p`.

`δ_q` is the bar-odd (`sinh`, `e_-`) part of the trivial/top-channel twist
`q^{(m-1)p}` (in the trivial block of `H_m(q)` every `σ_i ↦ q`, so the Coxeter
word `↦ q^{m-1}` and its `p`-th power `↦ q^{(m-1)p}`).  The `m = 2` case recovers
the basis-knot decoration `δ_q(T_{2,k}) = h[k]_q` (`prop:alpha-basis-knot-delta-q`,
`w = k`); the three-strand carriers give `δ_q(T_{3,4}) = h[8]_q`,
`δ_q(T_{3,5}) = h[10]_q`.

A trivial but pre-archimedean identity — entirely in the substrate ring (no `ℝ`,
no `π`).  Symbolic cross-check:
`computations/rosso_jones_three_strand_delta_q.py`.

LaTeX label: `prop:torus-knot-delta-q-writhe`.

**Ground ring** (AGENTS.md §7c): `ℤ[q, q⁻¹]`, i.e. a generic
`{R : Type*} [CommRing R]` with the substrate modulus carried as a **unit**
`q : Rˣ`, so `↑q⁻¹` is a `Units` coercion and no ring inverse appears. Two
consequences:

* `qbracket` is now the **division-free** symmetric q-integer
  `[w]_q = ∑_{i<w} qⁱ · q^{-(w-1-i)}` rather than the quotient
  `(q^w − q^{-w})/(q − q⁻¹)`. `qbracket_eq_div` records that over a field with
  `h = q − q⁻¹ ≠ 0` the two agree, so nothing is lost — and the sum form is
  additionally total.
* Consequently `torus_deltaQ_eq_h_qbracket` needs **no** hypothesis: the old
  `h ≠ 0` was only there to cancel the denominator. What was
  `div_mul_cancel₀` is now the telescoping identity `geom_sum₂_mul`, which
  actually identifies the quotient as a Laurent polynomial.

A field appears only in the `RatioForm` section, where `[w]_q` is written as an
actual quotient. That presentation needs division; the mathematics does not.
-/

namespace QOU.TorusKnotDeltaQ

variable {R : Type*} [CommRing R]

/-- q-dimension decoration `δ_q = q^w − q^{-w}` at writhe `w`. -/
def deltaQ (q : Rˣ) (w : ℕ) : R := (q : R) ^ w - (↑q⁻¹ : R) ^ w

/-- Quantum integer `[w]_q`, written division-free as the Laurent polynomial

  `[w]_q = ∑_{i<w} qⁱ · q^{-(w-1-i)} = q^{w-1} + q^{w-3} + ⋯ + q^{-(w-1)}`.

It satisfies `[w]_q · (q − q⁻¹) = q^w − q^{-w}`
(`deltaQ_eq_h_mul_qbracket`), which was the previous *definition* — a
quotient, hence meaningful only where `q − q⁻¹ ≠ 0`. -/
def qbracket (q : Rˣ) (w : ℕ) : R :=
  ∑ i ∈ Finset.range w, (q : R) ^ i * (↑q⁻¹ : R) ^ (w - 1 - i)

/-- Writhe of the standard positive torus braid `(σ₁⋯σ_{m-1})^p`
    (number of positive crossings). -/
def torusWrithe (m p : ℕ) : ℕ := (m - 1) * p

/-- **`δ_q = h·[w]_q` at any exponent `w`**, with `h = q − q⁻¹`.  This is the
    telescoping identity `(∑_{i<w} xⁱ y^{w−1−i})(x − y) = x^w − y^w`
    (`geom_sum₂_mul`), pure commutative-ring algebra: no hypothesis, no
    division. -/
theorem deltaQ_eq_h_mul_qbracket (q : Rˣ) (w : ℕ) :
    deltaQ q w = ((q : R) - (↑q⁻¹ : R)) * qbracket q w := by
  have h := geom_sum₂_mul (q : R) (↑q⁻¹ : R) w
  unfold deltaQ qbracket
  rw [← h]
  exact mul_comm _ _

/-- **`δ_q(T_{m,p}) = h·[(m-1)p]_q`** with `h = q − q⁻¹` — the torus-knot
    q-dimension decoration at the writhe exponent `w = (m-1)p` factors as `h`
    times the quantum integer `[(m-1)p]_q`.  Pre-archimedean (no `ℝ`, no `π`);
    sorry-free.  `m = 2` recovers `δ_q(T_{2,k}) = h[k]_q` (`w = k`). -/
-- Ref: [leitner2026] mass-theory/torus-knot-delta-q-writhe
theorem torus_deltaQ_eq_h_qbracket (q : Rˣ) (m p : ℕ) :
    deltaQ q (torusWrithe m p)
      = ((q : R) - (↑q⁻¹ : R)) * qbracket q (torusWrithe m p) :=
  deltaQ_eq_h_mul_qbracket q (torusWrithe m p)

/-! ## Quotient presentation (a field is needed only to divide)

The narrative writes `[w]_q` as a quotient. A quotient needs division, so this
section — and only this section — is over a field. -/

section RatioForm

variable {K : Type*} [Field K]

/-- Over a field with `h = q − q⁻¹ ≠ 0`, the division-free `[w]_q` above is
    literally the classical quotient `(q^w − q^{-w})/(q − q⁻¹)`.  Nothing is
    lost by carrying the Laurent-polynomial form. -/
theorem qbracket_eq_div (q : Kˣ) (w : ℕ)
    (hh : (q : K) - (↑q⁻¹ : K) ≠ 0) :
    qbracket q w = deltaQ q w / ((q : K) - (↑q⁻¹ : K)) := by
  rw [eq_div_iff hh, mul_comm, ← deltaQ_eq_h_mul_qbracket]

end RatioForm

end QOU.TorusKnotDeltaQ
