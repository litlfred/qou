---
# rtqd
title: 'GAP: qDimObj(Xᘁ)=qDimObj X general-object conjugation symmetry needs a pivotal structure Mathlib lacks'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T00:00:00Z
updated_at: 2026-11-18T10:47:00Z
parent: qou-o9ge
---

Residual gap from bean `rtrb` (RT-1 ribbon extension), branch
`claude/rtrb-ribbon-dual-2026-08-02`, file
`folio/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneRibbonCategory.lean`.

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



## Progress 2026-08-26 (branch claude/8-fold-way-qou-k4e8ch)

The gap narrowed by one named step, and it is worth recording exactly which step.

**Closed: the isomorphism.** `QOU.MathlibExt.drinfeldIso` proves `X` is isomorphic to
its double dual, unconditionally, in ANY braided right-rigid category:

    noncomputable def drinfeldIso (X : C) : X = ((X : C)-dual : C)-dual :=
      rightDualIso (BraidedCategory.exactPairing_swap X X-dual) (HasRightDual.exact (X := X-dual))

Uniqueness of duals, twice: `exactPairing_swap` turns the pairing `X` / `X-dual` around,
so `X` is a right dual OF `X-dual`; `X-dual-dual` is the chosen one; `rightDualIso`
compares them. Sorry-free, `#print axioms` clean.

**Still open: its NATURALITY.** `f >> drinfeldIso Y = drinfeldIso X >> ((f-mate)-mate)`
is what a `PivotalCategory` instance needs and what the transport hypothesis consumes.
Attempted; not obtained. `simp [drinfeldIso, rightDualIso, rightAdjointMate]` unfolds it
to a ~20-term string-diagram identity of the same shape as Mathlib's own
`coevaluation_evaluation_braided'` (a transcribed Whitney move built on `yang_baxter`).
It is a real coherence proof, not a rewrite of the pieces. Mathlib has NO naturality
lemma for `rightDualIso` at all -- the only lemma about it is `rightDualIso_id`.

**Infrastructure now in place for whoever takes it.**
`QOU/MathlibExt/PivotalCategory.lean` carries `rightDualFunctor : Cop => C`,
`doubleDualFunctor : C => C`, and `PivotalCategory` in the shape Mathlib's own
"Future work" list asks for (a natural iso `id C = double-dual`), plus
`PivotalCategory.ofPointwise` so a pointwise string-diagram proof lands directly.
`PivotalStructure` (the old pointwise class in `KeystonePivotalSpherical.lean`) is
retired in its favour; it had zero consumers.

**Cheapest concrete route** if the coherence proof stalls: `FGModuleCat K` is Mathlib's
one `RightRigidCategory` instance, and there the pivotor is `Module.evalEquiv`, whose
naturality is already available. That gives a genuine `PivotalCategory` instance without
the general braided argument.



## Correction to the "cheapest route", measured 2026-08-26

I recommended `FGModuleCat K` as the cheap way to get a `PivotalCategory` instance
without the braided coherence proof. **Measured, that recommendation is wrong, or at
least not established** -- it is not obviously cheaper, and the reason is a second
missing piece of Mathlib infrastructure, not the pivotor.

**What is there.** `Module.evalEquiv K V : V = Dual K (Dual K V)` exists, and its
naturality is `Module.Dual.eval_naturality (f) : f.dualMap.dualMap <o eval = eval <o f`
-- proved by `rfl`. So the linear-algebra half is free.

**What is missing, and it is not small.** There is no bridge between the categorical
mate and the linear-algebra one. The lemma needed is

    (rightAdjointMate f).hom = LinearMap.dualMap f.hom     -- for f : V => W in FGModuleCat K

and `grep -rn "rightAdjointMate\|dualMap" Mathlib/Algebra/Category/FGModuleCat/*.lean`
returns **nothing**. Probed directly: the statement typechecks (the carriers unify --
`Vdual.obj` is defeq to `Module.Dual K V`), and `simp [rightAdjointMate]` reduces it to
the five-step composite

    lambda o (eps_W |> Vdual) o alpha^-1 o (Wdual <| f |> Vdual) o (Wdual <| eta_V) o rho^-1

applied to `phi`, and then **stops**. It stops because `FGModuleCat`'s monoidal structure
is *induced* on a full subcategory -- `instance : (ModuleCat.isFG R).IsMonoidal` -- so the
`ModuleCat.MonoidalCategory.whiskerLeft_apply` / `whiskerRight_apply` /
`associator_inv_apply` family does **not** fire on it, and
`Algebra/Category/FGModuleCat/Basic.lean` supplies no element-level replacements
(grep for `whiskerLeft` there: two hits, both `open MonoidalCategory`).

So the route needs element-level computation lemmas for the induced monoidal structure on
an `ObjectProperty` full subcategory FIRST, and only then the dual-basis expansion
`phi o f = sum_i phi(f e_i) . e*_i` over `Basis.ofVectorSpace`. Two missing layers, not
one.

**Net: both routes to the instance are Mathlib-contribution-sized.** Neither is a
tidy-up. Whoever takes this should pick on interest, not on expected cost -- and should
know the FGModuleCat one begins with subcategory plumbing rather than with duality.



## The pivotal structure now EXISTS (2026-08-26)

`QOU.MathlibExt.pivotalOfBraided`: every braided right-rigid category is pivotal,
unconditional and sorry-free, pivotor = drinfeldIso, naturality =
drinfeldIso_naturality. See qou-knsx for why my "Whitney move" estimate was wrong.

**This bean is NOT closed by that.** What it needs is the pivotal TRANSPORT identity
qDimObj (Xdual) = leftQDim X, which is a statement about the two TRACES. Having the
pivotor is a prerequisite for stating and proving it, not a proof of it. The
hypothesis in qDim_conj_of_pivotalTransport is still carried, not discharged.

What did change: the blocker recorded in KeystonePivotalSpherical.lean -- "a pivotal
structure is required, and Mathlib provides no such class" -- is gone. The next step
is the transport lemma itself, now expressible on data that exists.



## CLOSED 2026-08-26, and the impossibility claim in this bean was WRONG

qDimObj (Xdual) = qDimObj X is PROVED, unconditionally, in any braided right-rigid
category. QOU.BraidKnot.Ribbon.qDim_conj_object, one line from
QOU.MathlibExt.qDimWith_rightDual. Sorry-free, #print axioms clean.

No pivotal hypothesis. No spherical hypothesis. No transport hypothesis.

### What this bean got wrong

It recorded the general-object case as not merely unproved but "NOT EXPRESSIBLE as a
computation on the existing data" without a pivotal structure, because qDimObj (Xdual)
traverses the double dual and a braided right-rigid category does not identify Xdualdual
with X.

The PREMISE is correct. The CONCLUSION does not follow from it. The dimension never needs
the identification -- it needs only that a fixed object's dimension is the same whichever
dual computes it, and X is ITSELF a right dual of Xdual via
BraidedCategory.exactPairing_swap. Dual-INDEPENDENCE is strictly weaker than double-dual
IDENTIFICATION, and it is what the trace consumes.

### The proof, three steps

  qDimWith_congr_dual  the quantum dimension does not depend on the choice of dual.
                       rightDualIso is the comparison map; Mathlib's
                       coevaluation_comp_rightAdjointMate and
                       rightAdjointMate_comp_evaluation at f = id say it transports eta
                       and epsilon; braiding naturality slides it across the crossing
                       where the two occurrences cancel.
  qDimWith_swap        against the swapped pairing, the swapped coevaluation's beta-inverse
                       meets the trace's own beta and cancels, leaving qDim(X) exactly.
  qDimWith_rightDual   both duals of Xdual give the same dimension; against the swapped one
                       it is qDim(X).

### What is NOT closed

The pivotal TRANSPORT identity qDimObj (Xdual) = leftQDim X is still unproved and stays a
hypothesis of KeystonePivotalSpherical's conditional theorems (bean qou-we9a). Sphericality
is a separate condition, untouched. Those conditional theorems remain valid -- a conditional
result is not invalidated by an unconditional proof of its conclusion.

### What this bean got RIGHT and should be copied

Refusing to sorry it, and refusing to axiomatise it as a class field. Both correct. The
error was the impossibility claim, not the discipline around it.

## 2026-09-08 — reopened: `status` disagreed with this bean's OWN body (§13a sweep, `qou-7sin`)

This bean was `completed` while the text above says, in its author's own words,
that the bean itself is still open. Nothing about its mathematics was judged
here and no finding was revisited — only the `status` field was made to agree
with the body.

Found by the `qou-7sin` sweep of the tracker against AGENTS.md **§13a** (owner,
2026-09-06: *"Don't close beans with open conjectures!!!"*), which landed after
most of these were closed. 18 of 2627 completed beans carry this
self-contradiction. It is decidable without judgement — the discriminator is
the bean asserting *its own* openness, not merely mentioning something open.

Re-close it when the work its body names is actually done.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

- Round 80 (`lane-e667`): Formalized `bwrt`, `bwse`, `rtkb`, `rtqd`, `rtrb` in `QOU.Foundations.CategoricalQuantumDimensionVacuumRowModularPartitionSumSurgerySlideInvariancePivotalDualTraceRibbonBalancing` with 80-dps `mpmath` 2-commit witness stamp (`9665213be334ca01449913d997dcaa05341cba29` -> `bbf00cfbf597a3ca40051aee20f1eda6cf87da89`, `scriptHash=7b699b4f4747b371a7a9fb79fd09f0b495a31a2b2d536d50c421ec2b24457967`) in PR `litlfred/qou#8433` (`status: in-progress`).
