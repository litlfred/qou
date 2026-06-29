import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring


/-!
# QOU.Information.operationalEntropy — Operational entropy of the Reeb dynamics

The operational entropy η_q := (2q - 1) / q³ measures the information
generated per f_q-iteration in natural units (nats).

LaTeX label: `def:operational-entropy`

## References
- [manuscript] §9/operational-entropy
-/

namespace QOU.Information

/-- **Operational entropy** of the Reeb dynamics at substrate parameter q.

    η_q := (2q - 1) / q³

    Measures the information generated per f_q-iteration in nats. -/
-- Ref: [manuscript] §9/operational-entropy
noncomputable def operationalEntropy {k : Type*} [Field k] (q : k) : k :=
  (2 * q - 1) / (q * q * q)

/-- The q-deformed Hausdorff dimension d_{H,q} = η_q / χ_q = (2q-1)² / q³. -/
-- Ref: [manuscript] §9/operational-entropy
noncomputable def qHausdorffDimension {k : Type*} [Field k] (q : k) : k :=
  (2 * q - 1) ^ 2 / (q * q * q)

/-- Operational entropy relates to Hausdorff dimension via
    d_{H,q} = η_q · (2q - 1). -/
-- Ref: [manuscript] §9/operational-entropy
theorem hausdorff_eq_entropy_mul_lyapunov {k : Type*} [Field k] (q : k)
    (hq : q ≠ 0) :
    qHausdorffDimension q = operationalEntropy q * (2 * q - 1) := by
  -- Ref: [manuscript] §9/operational-entropy
  -- d_{H,q} = (2q-1)²/q³ = ((2q-1)/q³) · (2q-1) = η_q · (2q-1)
  unfold qHausdorffDimension operationalEntropy
  field_simp [hq]

end QOU.Information
