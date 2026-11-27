import Mathlib.Data.Real.Basic

/-!
# QOU.AppendixSurreals.ClassicalLimitStpart

Conjectural axiomatisation of the **classical-limit functor as
standard-part of evaluation at q = 1 + ε**: the categorical
classical-limit functor `cl : C_q → C_classical` factors through
evaluation of the substrate parameter `q` at the surreal point
`1 + ε` (an infinitesimal), with the classical realm recovered
as the standard-part of the resulting surreal value.

The conjecture is encoded as a `class` (AGENTS.md §3b-cond);
`sorry` in any concrete instance is understood as **conjecture**, not
missing proof.  Downstream conditional results take
`[ClassicalLimitStpart]` as a hypothesis and remain
`theorem`/`proposition`.

LaTeX label: `conj:classical-limit-stpart`

## References

- [robinson1966] Non-standard Analysis
- [berarducci-mantova2018] https://arxiv.org/abs/1503.00315
-/

namespace QOU.AppendixSurreals

/-- Surrogate for the surreal-number standard part: a function
    extracting the real component of a hyperreal/surreal value. -/
abbrev StandardPart := ℝ → ℝ

/-- **Conjecture class.**  An instance asserts the existence of:
    * a classical-limit functor `cl_value : ℝ → ℝ` taking a
      "q-deformed quantity" (parameterised by q ≥ 1) to its
      classical limit;
    * the standard-part identification `cl_via_stpart` showing
      that `cl_value(q)` equals the standard part of the surreal
      evaluation at `q = 1 + ε` (here represented as a real
      function for the formal Lean shell).

    A concrete instance discharges `cl_via_stpart_holds` with
    `sorry` (the conjecture); downstream theorems condition on it. -/
class ClassicalLimitStpart where
  /-- Classical-limit value of a q-deformed real-valued quantity. -/
  cl_value : ℝ → ℝ
  /-- Standard-part operator (surrogate for the surreal-st map). -/
  st_part : StandardPart
  /-- The q-deformed quantity itself, evaluated at q = 1 + ε
      (here represented as a function ε ↦ value(1 + ε)). -/
  q_quantity_at : ℝ → ℝ
  /-- **Conjectural identification.**  The classical limit equals
      the standard part of the q-evaluation at q = 1 + ε.  A
      concrete instance discharges this by `sorry` (the conjecture);
      downstream theorems condition on it. -/
  cl_via_stpart_holds :
    ∀ q : ℝ, q ≥ 1 →
      cl_value q = st_part (q_quantity_at (q - 1))

/-- **Downstream conditional theorem (AGENTS.md §3b-cond).**
    Conditional on `[ClassicalLimitStpart]`, the classical-limit
    value at any q ≥ 1 is the standard-part of the q-evaluation
    at q = 1 + ε.  Fully verified by Lean once an instance is
    fixed. -/
theorem classical_limit_eq_stpart [inst : ClassicalLimitStpart]
    (q : ℝ) (hq : q ≥ 1) :
    inst.cl_value q = inst.st_part (inst.q_quantity_at (q - 1)) :=
  inst.cl_via_stpart_holds q hq

/-- **Trivial-zero skeleton.**  All three functions are constant zero,
    so `cl_via_stpart_holds` reduces to `0 = 0` and closes by `rfl`.
    It encodes none of the classical-limit / standard-part content.

    **A `def`, not an `instance`, since 2026-08-24.**  It takes no
    parameters, so as an `instance` it was *the* global
    `ClassicalLimitStpart`: `classical_limit_eq_stpart`, labelled a
    "Downstream conditional theorem (AGENTS.md §3b-cond)", had nothing
    left to be conditional on and asserted `0 = 0` for every `q ≥ 1`.

    Note also what the class docstring above says a concrete instance
    should look like: it *"discharges `cl_via_stpart_holds` with
    `sorry` (the conjecture)"*.  This one discharges it with `rfl`.
    Those are different states — a `sorry` is an admitted conjecture
    that `#print axioms` reports and the vacuity audit can find; a
    `rfl` over constant-zero data reports clean while proving nothing.
    The class docstring describes a declaration this file does not
    contain.

    Callers name it: `letI := canonical`. -/
-- Ref: [leitner2026] conj:classical-limit-stpart §"Skeleton"
def canonical : ClassicalLimitStpart where
  cl_value := fun _ => 0
  st_part := fun _ => 0
  q_quantity_at := fun _ => 0
  cl_via_stpart_holds := fun _ _ => rfl

end QOU.AppendixSurreals
