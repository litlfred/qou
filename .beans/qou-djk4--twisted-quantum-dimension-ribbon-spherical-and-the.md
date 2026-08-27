---
# qou-djk4
title: 'Twisted quantum dimension: ribbon => spherical, and the qDimObj borrowed name'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T22:34:41Z
updated_at: 2026-08-26T22:41:06Z
---

Parent context: `bwrt` introduced `KeystoneRibbonMTCInput.qDimObj X = η ≫ β ≫ ε` and documents it
as "the ribbon trace tr(𝟙_X)". That is a BORROWED NAME: the variable block there is
`[BraidedCategory C] [RightRigidCategory C]` with no `BalancedCategory`, so no θ is in scope and
none appears in the body. `qDimObj` is the TWISTLESS braided closure. Same for
`KeystonePivotalSpherical.leftQDim`, and hence `SphericalStructure.leftQDim_eq` is a hypothesis
ASSERTED about the twistless pair, not derived — which is why Barrett–Westbury's
braided-pivotal ⇒ spherical argument never reached it.

DONE (PR #5866, branch claude/twisted-quantum-dimension-2026-08-26,
QOU/MathlibExt/TwistedQuantumDimension.lean, lean-direct exit 0, all sorry-free, `#print axioms`
= propext / Classical.choice / Quot.sound only):

- `qDimTwistedWith A B = η_ A B ≫ (θ_A ▷ B) ≫ β_{A,B} ≫ ε_ A B` — stated over an explicit
  `[ExactPairing A B]` rather than over `Xᘁ`, which is what makes dual-independence statable.
- `qDimTwistedWith_twist_right` — the twist may sit either side of the braiding.
- `qDimTwistedWith_congr_dual` — independent of the chosen dual. MEASURED CHEAPER THAN PREDICTED:
  needs `[BalancedCategory C]` only, NO ribbon axiom. Transports along `rightDualIso` by the two
  mate identities at f = 𝟙, then `whisker_exchange` + `braiding_naturality_right`.
- `qDimTwistedWith_rightDual` — dim(Xᘁ) = dim(X). Ribbon axiom used EXACTLY ONCE.
- `qDimTwistedLeftWith A B = η ≫ (θ_A⁻¹ ▷ B) ≫ (β_ B A).inv ≫ ε`.
- `qDimTwistedLeftWith_eq_of_cap` — SPHERICALITY REDUCED TO ONE CAP IDENTITY. Holds on a merely
  BALANCED category as soon as `(θ_B ▷ A) ≫ ε = (B ◁ θ_A) ≫ ε`. The Joyal–Street balancing
  axiom does all the geometry (absorbs into the coevaluation via θ_𝟙 = 𝟙 + naturality; the double
  braiding converts left closure to right; the θ_A cancel the inverse twist; braiding naturality
  sweeps the residual θ_B onto the cap).
- `qDimTwistedLeftWith_eq` — RIBBON ⇒ SPHERICAL. The ribbon axiom discharges exactly that residue:
  `twist_dual` turns θ_{Xᘁ} into (θ_X)ᘁ, and `rightAdjointMate_comp_evaluation` at f = θ_X IS the
  cap identity.

Why the twistless pair cannot have this, stated as a scope-(b) structural exclusion: at θ = 𝟙 the
cap identity is trivially true, but the two closures then differ by the MONODROMY
(`(β_ B A).inv` vs `(β_ A B).hom`), and no axiom of a braided rigid category forces that to
vanish. So the twistless `SphericalStructure` is not derivable from ribbon at ANY twist including
the trivial one — the twist is what carries the statement.

NON-VACUITY CHECKED, NOT ASSUMED: `qDimTwistedLeftWith A B = qDimTwistedWith A B := rfl` is
rejected by the elaborator ("not definitionally equal"), so the theorem relates two genuinely
distinct morphisms rather than restating one.

STILL OPEN (follow-on, this bean):
1. Rename the twistless `qDimObj` / `leftQDim` honestly — they are the braided closure, not the
   ribbon trace. RENAME, do not delete: the vacuum-row results in `bwrt` are correct about the
   object they actually name, and since θ_𝟙 = 𝟙, `qDim_unit` is untouched either way.
2. Decide the disposition of `KeystonePivotalSpherical.SphericalStructure`: it is an asserted
   hypothesis about the twistless pair. Either keep it under an honest name as a hypothesis, or
   migrate consumers to `qDimTwistedLeftWith_eq` where a `BalancedCategory` is genuinely in scope.
3. Migrate consumers.


CORRECTION (same session, before the PR was reviewed). My end-of-turn summary table claimed the
TWISTLESS trace lacks dual-independence and conjugation symmetry. BOTH ROWS WERE WRONG, and I
found it by grepping consumers for the rename step rather than by re-reading what I had already
written — the module docstring in TwistedQuantumDimension.lean states the correct version, so the
error was in the summary, not in the Lean.

Measured on main:
- `QOU.MathlibExt.qDimWith_congr_dual` — twistless dual-independence, ALREADY EXISTS.
- `QOU.MathlibExt.qDimWith_rightDual` — twistless `qDim(Xᘁ) = qDim(X)`, ALREADY EXISTS and needs
  only `[BraidedCategory C] [RightRigidCategory C]`: no balanced structure, NO RIBBON AXIOM. Its
  docstring says so outright ("with no pivotal, spherical or transport hypothesis"), and
  `QOU.BraidKnot.Ribbon.qDim_conj_object` is its consumer.

So the honest ledger for adding the twist is a TRADE, not a strict gain:

| property | twistless `qDimWith` | twisted `qDimTwistedWith` |
|---|---|---|
| dual-independence | already, braided only | ported, balanced only |
| dim(Xᘁ) = dim(X) | already, braided only — FREE | needs the RIBBON AXIOM — a COST |
| left = right (spherical) | structurally impossible | ribbon => spherical — the GAIN |

The mechanism behind the middle row, which is the part worth keeping: `qDimWith_swap`'s proof
turns on the swapped pairing's `β⁻¹` meeting the trace's own `β` and CANCELLING. Insert a twist
between them and that cancellation no longer happens on its own — which is precisely the gap
`RibbonCategory.twist_dual` fills. So the twist does not merely fail to help conjugation
symmetry, it is what breaks the free proof.

Net: the ONE genuinely new and genuinely unreachable-twistless result in PR #5866 is
`qDimTwistedLeftWith_eq` (ribbon => spherical). The other two twisted theorems are ports of
facts the corpus already had, and one of them is strictly more expensive than its twistless
original.
