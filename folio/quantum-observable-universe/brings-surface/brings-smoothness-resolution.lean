import Mathlib.Data.Complex.Basic


/-!
# QOU.BringsSurface.brings_smoothness_resolution — Bring surface is smooth

The three power-sum constraints defining the Bring surface are transverse
in ℙ⁴, so the intersection is smooth.  Projection singularities are
resolved intrinsically by the color coordinates.
-/
namespace QOU.BringsSurface

-- Ref: [leitner2026] Ch. 6, §1
-- Ref: [bring1786] Bring, "Meletemata quaedam mathematica circa transformationem aequationum algebraicarum," Lund 1786
-- The Bring surface S is defined by three power-sum constraints in P^4.
-- We encode the three transversality conditions as a structure.

/-! ## 2026-09-12: the previous proof term was `⟨⟨True, True, True⟩, …⟩`

This file previously declared the three conditions as fields typed bare `: Prop` — the
*universe* of propositions, not propositions — and then discharged the block's claim with

```
theorem brings_smoothness_resolution :
    ∃ S : BringSurfaceSmoothness, S.transverse ∧ S.intrinsic_resolution ∧ S.regular_foliation :=
  ⟨⟨True, True, True⟩, trivial, trivial, trivial⟩
```

i.e. **the smoothness of the Bring surface was "proved" by `True ∧ True ∧ True`.** The
triviality is proved for the shape in `QOU.ProofHygiene.SelfAssumingContexts`
(`propUniverse_inhabited`), and was demonstrated for *this* carrier by name in
`docs/audits/2026-08-23-free-prop-field-triviality-probe.lean`.

That matters more here than in the other `prop-universe-field` carriers, because this
block is a **`proposition`** (`prop:brings-smoothness-resolution`), not a `conjecture`, and
its `.ts` cites this declaration as the proof of an `.md` that states flatly *"The three
power-sum constraints are transverse in `ℙ⁴`, so `𝒮` is smooth."* So §3b's
conjecture carve-out does not apply, and this was a `proof-statement-integrity` failure:
the Lean did not derive the `.md`'s claim.

**What is fixed here, and what is not.** The three conditions are now **parameters** and
the fields carry actual proofs, so `⟨True, True, True⟩` no longer type-checks and the
triviality can no longer hide inside the carrier. **The block's claim is still not proved**
— it cannot be stated in this file at all, which imports only `Mathlib.Data.Complex.Basic`
and has no Bring surface, no `ℙ⁴` and no Jacobian to be transverse. Whether the block
should therefore be demoted from `proposition` to `conjecture` is an **author decision**
and is deliberately not taken here.
-/

/-- **Carrier for the three smoothness conditions**, with the conditions as parameters.

They are parameters rather than constructions because nothing in this file's import cone
can state them: there is no Bring surface object here. Parameterising is what lets the
carrier hold the three honestly without either fabricating them or pretending they are
proved. -/
structure BringSurfaceSmoothness
    (Transverse IntrinsicResolution RegularFoliation : Prop) : Prop where
  /-- The three power-sum constraints are transverse (Jacobian has full rank). -/
  transverse : Transverse
  /-- At each branch point z_c, the local color coordinate δ = x_i - x_j
      satisfies z - z_c ~ δ², so the blow-up is intrinsic. -/
  intrinsic_resolution : IntrinsicResolution
  /-- The radial parameter r = |w_1|² is regular and C_5 orbits foliate
      the surface without fixed points for 0 < r < ∞. -/
  regular_foliation : RegularFoliation

/-- **Conditional form of `prop:brings-smoothness-resolution`.**

Given the three conditions, their conjunction holds. **This is not a proof of the block's
claim** and must not be cited as one: it is an accessor, and by
`QOU.ProofHygiene.SelfAssumingContexts.tuple_contentless` the carrier is inhabited exactly
when the conjunction is, so the declaration carries no content of its own.

It is kept under this name because `brings-smoothness-resolution.ts` resolves its
`lean.ref` here; what has changed is that the content is now visibly in the hypothesis
rather than invisibly in a `True`. -/
theorem brings_smoothness_resolution {T I R : Prop} (S : BringSurfaceSmoothness T I R) :
    T ∧ I ∧ R :=
  ⟨S.transverse, S.intrinsic_resolution, S.regular_foliation⟩

end QOU.BringsSurface
