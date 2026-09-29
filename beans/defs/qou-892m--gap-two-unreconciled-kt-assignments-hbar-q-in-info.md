---
# qou-892m
title: 'GAP: two unreconciled kT assignments -- hbar_q in information-theory vs E_0 in the binding law'
status: todo
type: task
priority: normal
created_at: 2026-08-19T17:31:15Z
updated_at: 2026-08-19T17:32:16Z
---

Found doing the literature check on the S-vs-H question (qou-y0mc, already closed).

Two blocks assign kT differently and nothing reconciles them:

  information-theory/boltzmann-constant.md
      k_B * T_phys = hbar_q = (q-1)/q   ~ 0.09908171604   (dimensionless)

  mass-endomorphism/markov-trace-gibbs-free-energy.md
      Delta F = kT ln(Z1/Z2)  with  kT = E_0 = 4.185981363 MeV

NOT a unit conversion. Measured: E_0/m_e = 8.191761172 against 1/hbar_q =
10.09267946; m_e*hbar_q = 0.0506 MeV; m_e/hbar_q^2 = 52.05 MeV. No simple
relation lands on E_0.

Grepped: the information-theory chapter is 177 blocks and NEVER mentions E_0.
So the two thermodynamic frames do not refer to each other anywhere.

This is orthogonal to which entropy functional is right (that is settled -- S,
by extensivity). It asks whether the framework has ONE temperature or two
unrelated ones wearing the same name.
