---
# qou-302y
title: 'V0/alpha: three independent routes converge on the NN interface energy scale alpha being ~2.70x too large'
status: todo
pr: 8215
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T18:45:57Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

NOT YET STARTED — scoping only, opened 2026-08-29 (PR #6059 session).

Three independent routes land on the interface energy scale alpha =
m_e/(q0(q0-1)) = E_0 = 4.1860 MeV being wrong for the NN interface, by ~2.70x:

1. qou-brg3 (CLOSED 2026-08-16, route 4 "the last one"). mu+ + mu- = 1 proved
   => AM-GM => mu+*mu- <= 1/4 => B(T=1)+B(T=0) >= alpha*log4 = 5.8030 MeV
   against nature 2.1510 MeV. The FLOOR over-binds 2.70x whatever the projector
   scalars are; substrate value 7.0377 over-binds 3.27x. Escapes closed both
   ways: smaller normalisation binds HARDER (needs s >= 1.5469 > 1); more
   channels worse (alpha*k*log k rises). Framing f cancels identically. Its own
   closing line: "the surviving direction is alpha, not the interface ...
   needs alpha <= 1.5516 MeV against E_0 = 4.1860." Lean
   TwoChannelTotalBindingFloor.lean, 7 decls sorry-free (verified this session).
2. docs/audits/2026-08-08-...-attack-vectors...md section 10b, independently:
   "either the derivation of z is wrong, or alpha = m_e/(q0(q0-1)) — an
   electron-scale quantity — is not the right scale for the NUCLEON-NUCLEON
   interface." The framework applies one alpha to leptons, nucleon masses and
   nuclear binding alike; only the first two are calibrated.
3. docs/audits/2026-08-21-binding-hbarq-rung-forward-test.md: measured two-scale
   separation ~1/hbar_q^2 — mass multiplier O(1/hbar_q^2), binding multiplier
   O(1). Lean BindingMassRung.lean sorry-free (mass = order-2 pole, binding
   regular at q=1). CAUTION: its one candidate MECHANISM (volume-defect) is
   REFUTED — overpredicts 102-250x.

HAZARD: 2.70 is O(1) and there is no cheap decisive test. Do not chase a
closed-form for 2.698 (e = 2.71828 is a numerology trap, explicitly not chased).
The honest unit is: is there a DERIVED reason the NN interface carries a scale
other than E_0 — and does route 3's proved O(hbar_q^2) dichotomy supply it once
the refuted volume-defect mechanism is replaced?


## CONSTRAINED 2026-08-30 by the b3 threshold result (PR #6059, commit dfcfa9c6)

alpha is an overall energy scale, and b3's SIGN is scale-free, so alpha cannot
bear on the wrong-signed 3-body cumulant at all. Recorded because the natural
hope -- "the scale is 2.70x off, maybe that is also what breaks b3" -- is now
excluded: QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos shows b3 > 0 requires
fpn > 2/3 whatever the scale.

So alpha stays a MAGNITUDE-only question. It cannot fix the sign, and any story
that closes the magnitude via alpha must still leave the sign to a change of
assembly.


## FURTHER CONSTRAINED 2026-08-30 — the 2.70x figure is ASSEMBLY-CONDITIONAL

Following the trilemma landing (qou-edt7, PR #6088): the strongest evidence that
alpha is ~2.70x too large is qou-brg3's floor

    B(T=1) + B(T=0) >= alpha*log 4 = 5.8030 MeV   vs nature 2.1510 MeV

and that floor is derived from mu+ + mu- = 1 via AM-GM -- i.e. from the PROJECTOR
CONVEX DECOMPOSITION, which is an assembly assumption. If the assembly is the
defect (which is now machine-checked for both corpus assemblies at the 3-body
sign), then the floor indicting alpha may be indicting the assembly instead.

So the three "independent routes" are less independent than the bean's own
scoping claims:
  - qou-brg3's floor and 08-08 s10b are ONE observation stated twice (already
    noted in the roast);
  - and that one observation is conditional on the very assembly now under
    suspicion.
The hbar_q-rung two-scale separation is the only route that does not route
through the assembly, and its one mechanism (volume-defect) is refuted at
102-250x.

RECOMMENDATION (judgement): keep PARKED. Do not work alpha until the assembly
question (qou-edt7) resolves, because a scale extracted against a wrong assembly
is a fit against a wrong assembly. Working it now is the most fit-prone move on
the board -- an O(1) number, no mechanism, no decisive test, and e = 2.71828 is
0.7% from E_0/1.5516 = 2.698.


## Progress Update (PR #8215)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`FreeNucleonPrecisionStraddleDefect.lean`, `TowerPartitionGrowthAndWeightSubstitution.lean`, `InterfaceScaleFloorAndBandDisjointness.lean`, `SWaveAntisymmetryIsospinGrading.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact integer-partition DP probe (`computations/probes/free_nucleon_straddle_h3a_band_isospin_probe.py`) and stamped witness (`computations/probes/free-nucleon-straddle-h3a-band-isospin-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8215 (`ready: 5d009c2bc892c5362b5b72a46c0f7f2e162d8d40`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8215, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
