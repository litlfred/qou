import Mathlib.Data.Real.Basic
import Mathlib.Tactic

/-!
# QOU.BraidKnot.S5bbGeometricIndex

Lean formalisation of the geometric index for the `s5bb` keystone.

This file carries the conditional index hypothesis for the 5-manifold
(the contact-geometry marker class `IsColourReeb` was removed 2026-11-15),
specifically the existence of a nowhere-zero U(1) ⊂ SU(3) colour Reeb vector field
outside the SO(3) isotropy, and defines its equivariant index against the
Ocneanu weights.

Honesty note: the target value `4143/90` that `S5bbClosure` posits this index
hits is **fit-tier** (no derivation trail; cited Reeb route refuted — see the
class docstring). Everything here is an *assumed* hypothesis; nothing in this
file derives `c₄`.
-/

namespace QOU.BraidKnot.S5bbGeometricIndex

/-- Abstract types for the 5-manifold and vector fields to serve as conditional hooks. -/
opaque Manifold5 : Type
opaque VectorField (M : Manifold5) : Type
opaque WenzlWeights : Type

/-! **Removed 2026-11-15: `IsColourReeb`.** Both fields were `True`. The
Reeb condition (θ(ξ) = 1, ι_ξ dθ = 0) and SO(3)-isotropy avoidance cannot be
stated over the opaque `Manifold5`; Mathlib has no contact geometry, and no
file used the class. Recorded in bean `qou-n2un`. -/

/-- The equivariant index evaluated against the Ocneanu weights via Atiyah-Bott localization. -/
opaque EquivariantIndex {M : Manifold5} (ξ : VectorField M) (W : WenzlWeights) : ℝ

/--
**Conditional class — an open hypothesis, not a derivation.** Carries the
assumption that the equivariant index of the colour Reeb field against the
Wenzl weights equals `4143/90`, the value the term-6 Habiro residue `c₄` would
take for the 4-loop `u⁴` closure.

`4143/90` is **fit-tier**: it has no derivation trail (it occurs on a single
producer line and nothing in the corpus computes it), the cited U(1)
colour-Reeb-index route is **refuted**, and it is a *worse* fit than the bare
integer `46`. See
`docs/audits/2026-07-04-c4-mu-p-tension-pin-dependence.md` §"mislabeled
numerology" and `docs/audits/2026-06-16-s5so3-reeb-resonance-probe-negative.md`.
The geometric derivation that would *discharge* this hypothesis (the contact
equivariant index on the s5bb 5-manifold) is obstructed (Wu-manifold) and
owner-gated. Per AGENTS.md §"Axiomatization is NOT a Proof": an instance of
this class *assumes* `c₄`, it does not derive it.
-/
class S5bbClosure (M : Manifold5) (ξ : VectorField M) (W : WenzlWeights) : Prop where
  /-- Assumed (open hypothesis, not proved): the equivariant index is posited
  to equal `4143/90` — a fit-tier value; see the class docstring. -/
  index_evaluates_to_c4 : EquivariantIndex ξ W = 4143 / 90

/-- **Parameterized colour-Reeb pairing carrier** (`qou-d838`): replaces the removed
    `: True` marker fields with caller-supplied 1-form pairing `contactPairing`,
    exterior-derivative contraction `dContract`, and isotropy norm `isotropyNorm` on
    `VectorField M`, constraining `ξ` to satisfy `contactPairing ξ = 1`, `dContract ξ = 0`,
    and `0 < isotropyNorm ξ`. -/
class ColourReebPairing
    (M : Manifold5)
    (contactPairing dContract isotropyNorm : VectorField M → ℝ)
    (ξ : VectorField M) : Prop where
  /-- Normalization on the contact 1-form: `θ(ξ) = 1`. -/
  contact_one : contactPairing ξ = 1
  /-- Vanishing contraction against the contact 2-form: `ι_ξ dθ = 0`. -/
  d_contract_zero : dContract ξ = 0
  /-- Strict avoidance of the isotropy locus: `0 < isotropyNorm ξ`. -/
  isotropy_pos : 0 < isotropyNorm ξ

/-- Under `[ColourReebPairing M contactPairing dContract isotropyNorm ξ]`, the difference
    `contactPairing ξ - dContract ξ` equals `1`. -/
theorem colourReeb_contact_sub_dContract
    {M : Manifold5} {contactPairing dContract isotropyNorm : VectorField M → ℝ}
    {ξ : VectorField M}
    [h : ColourReebPairing M contactPairing dContract isotropyNorm ξ] :
    contactPairing ξ - dContract ξ = 1 := by
  rw [h.contact_one, h.d_contract_zero, sub_zero]

/-- Under `[S5bbClosure M ξ W]`, the posited fit-tier value `4143 / 90` (`= 46.0333…`)
    exceeds the bare integer `46` by `1 / 30` (`EquivariantIndex ξ W - 46 = 1 / 30`
    and `90 * (EquivariantIndex ξ W - 46) = 3`). -/
theorem s5bb_index_ninety_mul_gap
    {M : Manifold5} {ξ : VectorField M} {W : WenzlWeights}
    [h : S5bbClosure M ξ W] :
    90 * (EquivariantIndex ξ W - 46) = 3 := by
  rw [h.index_evaluates_to_c4]
  ring

end QOU.BraidKnot.S5bbGeometricIndex
