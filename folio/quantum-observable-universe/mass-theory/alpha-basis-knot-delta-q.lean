import Mathlib.Algebra.Ring.Units
import Mathlib.Tactic.Ring


/-!
# QOU.AlphaBasisKnot.deltaQ_eq_h_qbracket

The q-dimension decoration of the α_{basis-knot} couplings:
`δ_q(T_{2,k}) = q^k − q^{-k} = h·[k]_q`, `h = q − q⁻¹`, `[k]_q = (q^k−q^{-k})/h`.

A trivial but pre-archimedean identity — it lives entirely in the substrate
ring (no `ℝ`, no `π`); only the invertibility of `h = q − q⁻¹` is needed for
the division.
Underlies `prop:alpha-em-categorical-trace-ratio`
(`α_EM = h²/(q·δ_q(T_{2,9})·δ_q(T_{3,5}))`). Symbolic cross-check:
`computations/delta_q_h_bracket_identity.py`.

LaTeX label: `prop:alpha-basis-knot-delta-q`.

**Ground ring (§7c)**: a generic `[CommRing R]`, i.e. the substrate ring
`ℤ[q, q⁻¹]` itself — *not* a field.  The two inverses the statement needs are
carried as **units** rather than field divisions:

* `q : Rˣ`, so `q⁻¹` is the ring element `↑q⁻¹` of `ℤ[q, q⁻¹]`;
* `h : Rˣ` together with the coherence hypothesis `↑h = q − q⁻¹`, which is
  the honest form of the old side condition `q − q⁻¹ ≠ 0` — over a field
  "nonzero" and "unit" coincide, so no generality is lost and the field
  instance is recovered by `Units.mk0`.

`[k]_q` is therefore `(q^k − q^{-k})·h⁻¹`, a genuine element of the substrate
ring, and the identity below is a Laurent identity rather than field algebra.
-/

namespace QOU.AlphaBasisKnot

variable {R : Type*} [CommRing R]

/-- q-dimension decoration `δ_q(T_{2,k}) = q^k − q^{-k}`, over the substrate
    ring with `q` a unit. -/
def deltaQ (q : Rˣ) (k : ℕ) : R := (q : R) ^ k - (↑q⁻¹ : R) ^ k

/-- Quantum integer `[k]_q = (q^k − q^{-k})·h⁻¹`, with the Hecke amplitude
    `h = q − q⁻¹` carried as a unit `h : Rˣ` (see the module note). -/
def qbracket (q h : Rˣ) (k : ℕ) : R :=
  ((q : R) ^ k - (↑q⁻¹ : R) ^ k) * (↑h⁻¹ : R)

/-- **`δ_q(T_{2,k}) = h·[k]_q`** with `h = q − q⁻¹` — the pre-archimedean
    q-dimension identity (no `π`, no field). Sorry-free. -/
-- Ref: [leitner2026] mass-theory/alpha-basis-knot-delta-q
theorem deltaQ_eq_h_qbracket (q h : Rˣ) (k : ℕ)
    (hh : (h : R) = (q : R) - (↑q⁻¹ : R)) :
    deltaQ q k = ((q : R) - (↑q⁻¹ : R)) * qbracket q h k := by
  unfold deltaQ qbracket
  rw [← hh, mul_comm ((q : R) ^ k - (↑q⁻¹ : R) ^ k) (↑h⁻¹ : R), ← mul_assoc,
    Units.mul_inv, one_mul]

end QOU.AlphaBasisKnot
