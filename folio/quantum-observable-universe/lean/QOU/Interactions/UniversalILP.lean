import Mathlib.Tactic

/-!
# QOU.Interactions.UniversalILP

Canonical declaration for content block referenced by
`qou:QOU.Interactions.UniversalILP`.

The claim is *named* as a `Prop` over a primitive-data carrier
(pattern C of the vacuity-fix playbook) rather than asserted via a
self-assuming projection; an instance of the proposition is the open
structural claim. -/

namespace QOU.Interactions


/-- Carrier for the `UniversalILP` data — only the primitive,
    non-conclusory fields (pattern C): the construction-level count
    and the per-level ILP Gram-matrix dimension.  The conclusion
    (`n_levels = 4`, dimension constant across levels) is **not** a
    field here — it is the named proposition `UniversalILP` below, so
    the claim is stated, not self-assumed. -/
class UniversalILPContext where
  /-- Proton number `Z`. -/
  Z : ℕ
  /-- Neutron number `N`. -/
  N : ℕ
  /-- Number of construction levels (quarks, nucleons, atoms,
      molecules). -/
  n_levels : ℕ
  /-- ILP Gram matrix dimension per level. -/
  gram_dim : ℕ → ℕ

/-- **Universal ILP Algorithm** (pattern C — named, not asserted).

**Content statement** (from manuscript): *a single integer linear
program selects the operator at every level of the QOU construction;
the same Gram matrix $G$, the same Frobenius check $Gx \geq 0$, and
the same ILP are applied to quarks, nucleons, atoms, and molecules.*

The structural reading is that there are exactly four construction
levels and the ILP Gram dimension is constant across them.  We
**name** this as a `Prop` over the context's primitive data, rather
than projecting it from self-assuming `h_*` fields — an instance of
this proposition is the open structural claim. -/
-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/universal-ilp-algorithm.ts
def UniversalILP [ctx : UniversalILPContext] : Prop :=
    ctx.n_levels = 4 ∧
    ∀ ℓ : ℕ, ℓ < ctx.n_levels → ctx.gram_dim ℓ = ctx.gram_dim 0

end QOU.Interactions
