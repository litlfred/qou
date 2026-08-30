---
# qou-302y
title: 'V0/alpha: three independent routes converge on the NN interface energy scale alpha being ~2.70x too large'
status: todo
type: task
priority: normal
created_at: 2026-08-29T18:45:57Z
updated_at: 2026-08-30T02:46:56Z
parent: qou-mhj9
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
