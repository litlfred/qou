---
# qou-jogb
title: 'Gap 1: charge radius as a falloff coefficient -- five routes, and the proton-radius-puzzle block may be stale'
status: in-progress
pr: 8203
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-09-13T05:32:01Z
updated_at: 2026-10-10T07:15:57Z
parent: qou-8lxd
---

## RE-SCOPED 2026-09-13 before any work — this was nearly a duplicate

Created on the belief that a spatial/density layer was a BLANK in the corpus.
**That belief was wrong** and the corpus-grep caught it before anything was built.
What is actually present:

- **`qou-usft`** (todo) — *"Light-nucleus regime: derive the Coulomb radius AND
  density shape from binding + q-CLT, not r0*A^(1/3)"*. Already carries a DERIVED
  length: the binding length `1/kappa = hbar c / sqrt(2 mu S_sep)`, giving
  3He `1/kappa = 2.3795 fm` against measured `2.5382` — **-6.26 %**, against
  `r0*A^(1/3)`'s **-31.81 %**. A 5x improvement from a quantity the framework
  predicts rather than an imported constant. Its RESULT 3 is *the owner's q-CLT
  question quantified* — shape-only factor `f` with the radius divided out:
  uniform ball 0.464758 (-10.87 %), Gaussian 0.488602 (-6.29 %), exponential
  0.454663 (-12.80 %). It also flags `sqrt(5/3)` as the UNIFORM-BALL moment
  relation, i.e. a classical import, not a neutral conversion.
- **`qou-bn8e`** (in-progress) — framework lengths exist and have been tested:
  the reduced pion Compton wavelength as the nuclear Coulomb length; a solved
  `r ~ 0.480 fm`; and the measured **"charge radius is off by 1.75x. Neither
  framework length reproduces"** it.
- **`qou-7e67`** — **OWNER RULING, item 5: "MEASURED CHARGE RADIUS AS A DECLARED
  INPUT -- NO. Rejected. Do not add a CAL-4. The parameter-free claim is not to
  be traded for light-nucleus EM numbers."** Item 4: **"BINDING-DERIVED SIZE --
  YES"**, approved, but *"Currently circular: QOU binding is ~30 % off so it
  gives +37.8 %. Unblocks the moment the NN sector lands."*
- `qou-4waf`, `qou-o16k` — the same `E_C = 0.680772 MeV / -10.9 %` row.

## What the greps actually showed, correctly read

`impact parameter` 0, `transverse plane` 0, `momentum space` 0 are all TRUE.
The inference "therefore the framework cannot reach a size" was false: it reaches
size through a **binding length**, not through a transverse plane. Different
route, same observable.

## The residue that is genuinely absent

Of the three equivalent physical definitions of the charge radius, the corpus
works two:

1. **density moment** `<r^2> = int r^2 rho / int rho` — `qou-usft` RESULT 3 is
   exactly this, as a shape comparison. LIVE.
2. **form-factor slope** `<r^2> = -6 dG_E/dQ^2` at `Q^2 = 0` — **ABSENT**, and it
   is the only one needing momentum transfer.
3. **energy shift** (finite-size correction to a bound-state energy) — this is
   the `E_C` Coulomb-energy route. LIVE.

So definition 2 is the ALICE-adjacent one and the charge radius is **not** gated
on it. Do not open a fresh radius arc.

## Disposition
This bean is now a POINTER, not a work item. The live work is `qou-usft`
(blocked behind the NN sector per the owner ruling) and `qou-bn8e`. The one
thing here not covered elsewhere is the staleness question on
`observations/proton-radius-puzzle.md` — see below.

## Progress (2026-11-16, PR #8203)
- [x] Formalized `formFactorLinearDrop`, `uniformBallRmsResidual`, and `he3_binding_length_fivefold_improvement` in `folio/quantum-observable-universe/lean/QOU/Eightfold/RootOfUnityCutoffIsotopeHyperfineBetaCoulombAndSymplecticRoots.lean` + 50-dps mpmath witness (`qou_jogb_he3_binding_length_fivefold_improvement`) in PR #8203 (`74a091a53fd300f6f906db42c72c6a5e3e84e7b3`).
