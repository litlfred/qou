---
# qou-fi1p
title: DeuteronKernel.bondL's writhe sign is opposite to InterfaceScalar's — latent, 3.57x on the mirror split
status: todo
pr: 8219
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-13T10:54:22Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-v2om
---

## The finding

Two Lean carriers of the same writhe normalisation disagree on its **sign**.
Measured, not inferred; every figure below is mpmath at `dps >= 40` on the
proton-pinned `q0` from `qou_substrate.constants.Q_50_DIGIT_STR`, with
`alpha = m_e/(q(q-1)) = 4.18598136` (matching `InterfaceScalar`'s own quoted
`4.1859814`).

`QOU.MassTheory.DeuteronKernel.bondL` (`DeuteronTwoBodyKernel.lean:170`):

    bondL q t = -log (interfaceFactor q t) - (t - 1/2) * log (1 - h)

so `L_nn - L_pp = bondL(1) - bondL(0) = log(z/(z-h)) - log(1-h)`.

`QOU.QBeta.InterfaceScalar` (docstring, lines 99-101) reports the same named
quantity `alpha*(L_nn - L_pp)` as **0.76532 MeV** "under D with the derived
writhe term wired". Solving for the formula that produces it:

    alpha * (4 log q + log(1-h))  =  0.765320193   <- matches 0.76532
    alpha * (4 log q - log(1-h))  =  2.72882629    <- what bondL gives

**Opposite sign of `log(1-h)`, a factor 3.57 on the quantity that is the
model's entire 3H/3He mirror split.**

Cross-checks that pin both ends rather than leaving it as my arithmetic:

- `InterfaceScalar`'s other quoted number resolves exactly too:
  `alpha*log(z_C/(z_C-h)) = 2.27077202` against its quoted **2.27077**
  (convention C, no writhe). So the two numbers it quotes use *different*
  formulas, which its own text says ("under D **with** the derived writhe term
  wired") -- that part is consistent and is not the defect.
- Bean `qou-0pzi`'s table (`B_pp = +2.5416`, `B_nn = +3.3069`) independently
  carries the SAME sign as `InterfaceScalar`: `alpha*L_pp = 2.0507` and
  `alpha*L_nn = 3.7978` from the bare factors, and their B's sit at
  `+0.4909` and `-0.4909` off those -- exactly `alpha*(1/2)*|log(1-h)| =
  0.49075`, i.e. `mu_pp = z*(1-h)^(+1/2)`, `mu_nn = (z-h)*(1-h)^(-1/2)`.

So **two independent carriers agree and `bondL` is the odd one out.**

## 🛑 It is LATENT, not live — scope this correctly

`bondL` is used only near `t = 1/2`. `tDerived_bounds`
(`DeuteronTwoBodyKernel.lean:402`) proves `0.4996 <= tDerived q <= 1/2`, so the
writhe term contributes `|t - 1/2| * |log(1-h)| <= 9.4e-5` in the regime the
file actually evaluates. The sign is immaterial there. `bondL_half` even proves
the term vanishes exactly at `t = 1/2`.

It becomes live the moment anyone evaluates `bondL` at `t = 0` or `t = 1` to
get the pp / nn bonds, where the term is `+-(1/2)log(1-h) = -+0.11724`.

**And I am the one who opened that door.** The only consumer of
`DeuteronKernel` outside its own file is `QOU/Hecke/BondLetterIdentification`
(this session, PR #7285), whose `tr_bond_interp` spans the whole interpolation
family *including* the endpoints. Recording it now rather than after someone
takes the obvious next step.

## Also established on the way (and it corrects an inference of mine)

The **live production trace** `tr_m_atom_via_transfer.tr_m_atom_zn` at `A = 2`
returns, at `dps = 50`:

    pp: tr_atom/tr_free = 0.612688037146  ==  z_D          exactly
    nn: tr_atom/tr_free = 0.403627738351  ==  z_D - h      exactly
    pn: tr_atom/tr_free = 0.508229789377

So the production path carries the **bare** bond factors with **no** writhe
normalisation, and the `tr_bondWord` product theorem is confirmed against it at
`A = 2`. Consequently `L_nn - L_pp = 4 log q = 0.417362881` there and
`alpha*(L_nn - L_pp) = 1.74707324 MeV` -- a third value, distinct from both
quoted numbers, because it is the un-normalised one.

🛑 **Retracting my own intermediate inference:** I first concluded from
`qou-0pzi`'s B table that the production trace carries `(1-h)^(1/2)`. It does
not -- the live trace above has no such factor. Those B values carry it
*downstream* of `tr_m_atom_zn`. The table was right; my attribution of it to
the trace path was wrong.

## NOT doing the fix

Deciding which sign is right, and changing `bondL` if it is the wrong one, is
another arc's call: it is not a precision fix and not corpus-derived in the
ASK-BEFORE-CHANGING sense (two carriers say one thing, one says another --
that is a disagreement to adjudicate, not an artifact to point at), and it
would move `BSymDeuteron` and `bondL_strictMono`. Reported, not touched.


## Progress Update (PR #8219)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`ThermodynamicTemperatureAndRepinBound.lean`, `SiteVsBondVolumeFactorTwo.lean`, `TwoDimensionalInterfaceCollapseAndOrdering.lean`, `WritheSignOppositionEndpointSplit.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` probe (`computations/probes/kt_repin_octahedron_interface_writhe_probe.py`) and stamped witness (`computations/probes/kt-repin-octahedron-interface-writhe-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8219 (`ready: 0004396c02a14ba756cc43c66855073b0a08f82d`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8219, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — binding-hygiene drain (session https://claude.ai/code/session_01Qmmkt97hXiyVzatJQADqZY)

Premise check against `docs/coordination/owner-rulings.md` on main `2ae54ab40` (owner instruction 2026-11-21: no bean is worked on a superseded basis). **Superseded premise found:** both carriers compare `interfaceFactor` values for the old pp/nn/pn interface letters (γγ rescope), and `InterfaceScalar` also quotes a convention-C number. The writhe-sign disagreement is still a real Lean inconsistency to settle when the γγ word defines its bond letters. Not changed here.
