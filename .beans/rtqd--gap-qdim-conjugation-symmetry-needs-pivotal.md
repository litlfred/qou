---
# rtqd
title: 'GAP: qDimObj(Xᘁ)=qDimObj X general-object conjugation symmetry needs a pivotal structure Mathlib lacks'
status: open
type: task
priority: normal
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-08-02T00:00:00Z
---

Residual gap from bean `rtrb` (RT-1 ribbon extension), branch
`claude/rtrb-ribbon-dual-2026-08-02`, file
`content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneRibbonCategory.lean`.

## What is closed (this branch, sorry-free)

- `RibbonCategory C` class = `BalancedCategory C` + `[RightRigidCategory C]` + the
  dual-compatibility ribbon axiom `twist_dual : (θ_X)ᘁ = θ_{Xᘁ}` (`rightAdjointMate`).
- `RibbonCategory.ofSymmetric` — every symmetric right-rigid category is ribbon with θ=𝟙
  (ribbon axiom = `rightAdjointMate_id`). Non-vacuity.
- `RibbonCategory.twist_dualDual` — twist commutes with double-dualization,
  `θ_{Xᘁᘁ} = (θ_X)ᘁᘁ` (ribbon axiom twice). Conjugation symmetry at the *twist* level.
- `qDim_of_unitPairing` + `qDim_unit` — the categorical quantum dimension of the monoidal
  unit (vacuum) is 1: `qDimObj (𝟙_C) = 𝟙 (𝟙_C)`. Grounds `RibbonMTCInput.vac_dim_one`
  categorically; trivial case of conjugation symmetry.

## What is OPEN (this gap)

The general-object conjugation symmetry — the corpus fact `qDim_conj` —

    qDimObj (Xᘁ) = qDimObj X   for every object X

is NOT proved (and is NOT `sorry`'d / axiomatised — that would be anti-laundering, since the
statement is not one computation away from the current data).

## Why it does not close in `[BraidedCategory C] [RightRigidCategory C]`

`qDimObj (Xᘁ)` internally traverses the **double dual** `Xᘁᘁ`. A plain braided right-rigid
category does not identify `Xᘁᘁ` with `X`; that identification is a **pivotal structure** —
a natural monoidal isomorphism `X ≅ Xᘁᘁ` compatible with duality. Mathlib provides no such
class (`CategoryTheory.Monoidal.Rigid.*` has no `PivotalCategory`). Without it the equality is
not merely unproved but not expressible as a rewrite on the existing `η_`, `ε_`, `β_`,
`rightAdjointMate` data — confirmed: `simp`/`aesop_cat`/`monoidal` all stall at the `Xᘁᘁ` wall
(they close the unit case but make no progress on the general case).

## Next honest step for whoever picks this up

1. Add a content-bearing `PivotalStructure C` class (natural iso `pivotal X : X ≅ Xᘁᘁ` +
   the monoidal-naturality square) — a genuine hypothesis class, NOT one that carries the
   conclusion `qDimObj (Xᘁ) = qDimObj X` as a field (that would be a self-assuming projection,
   §3b-cond item 5).
2. Under `[PivotalStructure C]`, derive `qDimObj (Xᘁ) = qDimObj X` from the pivotal iso +
   the mate lemmas (`comp_rightAdjointMate`, `rightAdjointMate_comp`) + braiding naturality.
   This is the real coherence content; it is a conditional (`§3b-cond`) theorem, not a closure
   of `bwse`.
3. Either build the pivotal class here or check whether a later Mathlib bump adds
   `PivotalCategory` upstream (probe `rightPivotal` / `Monoidal.Rigid` on bump).

Does NOT close `bwse`; nothing wired; L2 unchanged (2/7).

---
2026-08-11 PROGRESS (branch claude/rtqd-pivotal-infra-2026-08-11) — infra BUILT per the standing
rule "build needed Mathlib infra instead of beaning it". File: KeystonePivotalSpherical.lean,
lean-direct exit 0, sorry-free. Gap NOT closed; substantially advanced.

BUILT (the infra Mathlib lacks — re-confirmed absent: rightAdjointMate / comp_rightAdjointMate /
ExactPairing exist, no PivotalCategory):
 - leftQDim: the LEFT quantum dimension, the mirror trace via the INVERSE braiding
   (beta_ Xdual X).inv in place of (beta_ X Xdual).hom. Genuinely different morphism from qDimObj.
 - PivotalStructure: pivotor X : X ~= Xdualdual + the naturality square against double mates.
   Content-bearing; does NOT carry the conclusion as a field (avoids the Sec3b-cond item-5
   self-assuming projection the earlier note warned about).
 - SphericalStructure: the standard "left trace = right trace" class.

PROVED:
 - braiding_inv_eq_hom_of_symmetric: in a symmetric category (beta_ X Xd).hom = (beta_ Xd X).inv.
 - leftQDim_eq_qDimObj_of_symmetric: EVERY symmetric right-rigid category is SPHERICAL. Real
   theorem + the non-vacuity witness for SphericalStructure (inhabited, not conditional-on-False).
 - spherical_of_symmetric: that as an instance.
 - qDim_conj_of_pivotalTransport_of_spherical (Sec3b-cond): the gap FACTORED into exactly two
   named classical inputs, neither of which is the conclusion — (1) pivotal transport
   qDimObj(Xdual) = leftQDim X, (2) sphericality leftQDim X = qDimObj X.
 - qDim_conj_of_pivotalTransport / _symmetric: with sphericality discharged (class, or proved in
   the symmetric case), the gap reduces to input (1) ALONE.

RESIDUAL (still open, this bean stays open): the pivotal transport lemma
qDimObj(Xdual) = leftQDim X — the classical statement that the right dimension of the dual is the
left dimension of the object. Its proof is a string-diagram coherence argument (ribbon => spherical;
Deligne/Yetter, Bakalov-Kirillov ch.2). NOT proved, NOT axiomatised, NOT sorry'd — carried as an
explicit hypothesis of the conditional theorems. So the state moved from "not expressible on the
available data" to "expressible, and one named classical lemma from closing".
Does NOT close bwse; nothing wired; L2 unchanged.
