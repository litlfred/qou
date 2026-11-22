import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Units.Defs
import Mathlib.Tactic.Ring


/-!
# QOU.Information.operationalEntropy — Operational entropy of the Reeb dynamics

The operational entropy η_q := (2q - 1) / q³ measures the information
generated per f_q-iteration in natural units (nats).

LaTeX label: `def:operational-entropy`

## References
- [leitner2026] §9/operational-entropy
-/

namespace QOU.Information

/-! §7c: `q` enters only through `q` and `q⁻¹`, so it is carried as a **unit**
`q : kˣ` of a bare `CommRing k` and `q⁻³` is the coercion `(↑q⁻¹)³` — no field
inverse of a possibly-zero element, hence no `[Field k]` and no `q ≠ 0`
side-condition. Nothing here is archimedean; the numerical evaluation at the
substrate `q_0` happens downstream by instantiating `k := ℝ`. -/

/-- **Operational entropy** of the Reeb dynamics at substrate parameter q.

    η_q := (2q - 1) · q⁻³

    Measures the information generated per f_q-iteration in nats. -/
-- Ref: [leitner2026] §9/operational-entropy
def operationalEntropy {k : Type*} [CommRing k] (q : kˣ) : k :=
  (2 * (q : k) - 1) * ((↑q⁻¹ : k) * (↑q⁻¹ : k) * (↑q⁻¹ : k))

/-- The q-deformed Hausdorff dimension d_{H,q} = η_q / χ_q = (2q-1)² · q⁻³. -/
-- Ref: [leitner2026] §9/operational-entropy
def qHausdorffDimension {k : Type*} [CommRing k] (q : kˣ) : k :=
  (2 * (q : k) - 1) ^ 2 * ((↑q⁻¹ : k) * (↑q⁻¹ : k) * (↑q⁻¹ : k))

/-- Operational entropy relates to Hausdorff dimension via
    d_{H,q} = η_q · (2q - 1). -/
-- Ref: [leitner2026] §9/operational-entropy
theorem hausdorff_eq_entropy_mul_lyapunov {k : Type*} [CommRing k] (q : kˣ) :
    qHausdorffDimension q = operationalEntropy q * (2 * (q : k) - 1) := by
  -- Ref: [leitner2026] §9/operational-entropy
  -- d_{H,q} = (2q-1)²·q⁻³ = ((2q-1)·q⁻³) · (2q-1) = η_q · (2q-1)
  unfold qHausdorffDimension operationalEntropy
  ring

end QOU.Information
