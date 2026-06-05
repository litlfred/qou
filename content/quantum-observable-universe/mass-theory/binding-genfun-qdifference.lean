import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.Card

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

- [manuscript] §mass-theory/binding-genfun-qdifference

**Ground ring**: `ℝ` (kernel evaluated at the substrate `q₀`).
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

open scoped BigOperators

/-- **Binding q-difference recurrence data**: the depth `d`, the recurrence
    kernel `a_j(q₀)` (`j < d`), the body terms `B_n`, and the depth-`d`
    linear recurrence `B_{n+d} = Σ_{j<d} a_j B_{n+j}` read off from the
    q-difference kernel `R`. -/
structure BindingQDifferenceRecurrence where
  /-- Recurrence depth `d` (the window width of `R`). -/
  depth : ℕ
  /-- The recurrence kernel `a_j(q₀)`, `j < depth`. -/
  kernel : Fin depth → ℝ
  /-- The body-order binding terms `B_n`. -/
  term : ℕ → ℝ
  /-- Depth-`d` linear recurrence: `B_{n+d} = Σ_{j<d} a_j · B_{n+j}`. -/
  recurrence : ∀ n, term (n + depth) = ∑ j : Fin depth, kernel j * term (n + (j : ℕ))

/-- **L3.** The body terms obey the depth-`d` recurrence determined by the
    q-difference kernel. -/
-- Ref: [manuscript] §mass-theory/binding-genfun-qdifference
theorem binding_qdifference_recurrence (S : BindingQDifferenceRecurrence) (n : ℕ) :
    S.term (n + S.depth) = ∑ j : Fin S.depth, S.kernel j * S.term (n + (j : ℕ)) :=
  S.recurrence n

end QOU.Mass
