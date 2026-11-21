import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# QOU.Mass.binding_qdifference_recurrence — depth-d recurrence from a
  q-difference equation on the binding generating function

Workplan Lemma **L3** (step-9b). If the binding generating function
`G(x;q)=Σ B_n x^n` satisfies a fibre-level q-difference equation
`G(qx)=R(q,x)G(x)` with `R` of bounded depth `d`, then the body terms
satisfy a depth-`d` linear recurrence `B_{n+d} = Σ_{j<d} a_j B_{n+j}`
(the `q`-holonomic ⇒ `P`-recursive passage). The recurrence determines
every term — hence the scale rule `ρ·A` — from `R`, with no fit.

The existence of the kernel `R` for the binding `G` is the conjectural
input; it is packaged here as the structure hypothesis, so the
term-recurrence identity is available sorry-free.

LaTeX label: `prop:binding-genfun-qdifference`.

## References

- [leitner2026] §mass-theory/binding-genfun-qdifference

**Ground ring**: `ℝ` (kernel evaluated at the substrate `q₀`).
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

open scoped BigOperators

/-- **Binding q-difference data**: the depth `d`, the coefficients `c_j(q₀)`
    of the depth-`d` q-difference annihilating operator obtained from the
    kernel `R` (the coefficient form of `G(qx) = R(q,x) G(x)` after clearing
    denominators), the body terms `B_n`, the annihilation identity
    `∑_{j≤d} c_j B_{n+j} = 0`, and the order condition `c_d ≠ 0`.

    Neither the annihilation identity nor the order condition is the
    depth-`d` recurrence conclusion: the recurrence is **solved for** from
    them below, realising the q-holonomic ⟹ P-recursive passage rather
    than carrying it as a field. -/
structure BindingQDifferenceRecurrence where
  /-- Recurrence depth `d` (the window width of the kernel `R`). -/
  depth : ℕ
  /-- The body-order binding terms `B_n`. -/
  term : ℕ → ℝ
  /-- Coefficients `c_{n,j}(q₀)` of the depth-`d` q-difference annihilating
      operator at position `n`, obtained from `R` by clearing denominators.
      They depend on `n` through `q^n`. -/
  opCoeff : ℕ → ℕ → ℝ
  /-- The fibre q-difference equation in coefficient form:
      `∑_{j≤d} c_{n,j} B_{n+j} = 0` for all `n`. -/
  annihilates :
    ∀ n, ∑ j ∈ Finset.range (depth + 1), opCoeff n j * term (n + j) = 0
  /-- The operator has order exactly `d` at every position: its leading
      coefficient is nonzero. -/
  leading_ne_zero : ∀ n, opCoeff n depth ≠ 0

/-- **L3.** The body terms obey the depth-`d` linear recurrence read off from
    the q-difference kernel:

      `B_{n+d} = ∑_{j<d} (-c_{n,j} / c_{n,d}) · B_{n+j}`.

    **Derived**, not projected: peel the top (`j = d`) term of the
    annihilation identity `∑_{j≤d} c_j B_{n+j} = 0` and solve for `B_{n+d}`
    (`c_{n,d} ≠ 0`). The coefficients `a_{n,j} = -c_{n,j} / c_{n,d}` are an
    output of `R` and depend on `n` — the q-holonomic ⟹ q-recursive passage. -/
-- Ref: [leitner2026] §mass-theory/binding-genfun-qdifference
theorem binding_qdifference_recurrence (S : BindingQDifferenceRecurrence) (n : ℕ) :
    S.term (n + S.depth)
      = ∑ j ∈ Finset.range S.depth,
          (- S.opCoeff n j / S.opCoeff n S.depth) * S.term (n + j) := by
  have hd := S.leading_ne_zero n
  have h := S.annihilates n
  rw [Finset.sum_range_succ] at h
  have hcong : ∀ j ∈ Finset.range S.depth,
      (- S.opCoeff n j / S.opCoeff n S.depth) * S.term (n + j)
        = (- (S.opCoeff n S.depth)⁻¹) * (S.opCoeff n j * S.term (n + j)) := by
    intro j _
    ring
  rw [Finset.sum_congr rfl hcong, ← Finset.mul_sum]
  have hsum : (∑ j ∈ Finset.range S.depth, S.opCoeff n j * S.term (n + j))
      = - (S.opCoeff n S.depth * S.term (n + S.depth)) := by linarith [h]
  rw [hsum, neg_mul_neg, ← mul_assoc, inv_mul_cancel₀ hd, one_mul]

end QOU.Mass
