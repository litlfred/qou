import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
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
no `π`); only `q − q⁻¹ ≠ 0` is needed for the division.  Same proof shape as the
sorry-free 2-strand `deltaQ_eq_h_qbracket`, here at the writhe exponent.
Symbolic cross-check: `computations/rosso_jones_three_strand_delta_q.py`.

LaTeX label: `prop:torus-knot-delta-q-writhe`. **Ground ring**: a field `R`.
-/

namespace QOU.TorusKnotDeltaQ

variable {R : Type*} [Field R]

/-- q-dimension decoration `δ_q = q^w − q^{-w}` at writhe `w`. -/
def deltaQ (q : R) (w : ℕ) : R := q ^ w - q⁻¹ ^ w

/-- Quantum integer `[w]_q = (q^w − q^{-w})/(q − q⁻¹)`. -/
noncomputable def qbracket (q : R) (w : ℕ) : R := (q ^ w - q⁻¹ ^ w) / (q - q⁻¹)

/-- Writhe of the standard positive torus braid `(σ₁⋯σ_{m-1})^p`
    (number of positive crossings). -/
def torusWrithe (m p : ℕ) : ℕ := (m - 1) * p

/-- **`δ_q(T_{m,p}) = h·[(m-1)p]_q`** with `h = q − q⁻¹` — the torus-knot
    q-dimension decoration at the writhe exponent `w = (m-1)p` factors as `h`
    times the quantum integer `[(m-1)p]_q`.  Pre-archimedean (no `ℝ`, no `π`);
    sorry-free.  `m = 2` recovers `δ_q(T_{2,k}) = h[k]_q` (`w = k`). -/
-- Ref: [manuscript] mass-theory/torus-knot-delta-q-writhe
theorem torus_deltaQ_eq_h_qbracket (q : R) (m p : ℕ) (hh : q - q⁻¹ ≠ 0) :
    deltaQ q (torusWrithe m p) = (q - q⁻¹) * qbracket q (torusWrithe m p) := by
  unfold deltaQ qbracket
  rw [mul_comm, div_mul_cancel₀ _ hh]

end QOU.TorusKnotDeltaQ
