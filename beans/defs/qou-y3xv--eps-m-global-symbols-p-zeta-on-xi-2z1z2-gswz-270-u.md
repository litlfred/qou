---
# qou-y3xv
title: 'eps_m GLOBAL symbols: P_zeta on xi = 2[z1]+[z2] (GSWZ 270) — unramified mu_{624m} fields, d=ord_5(624m); z1=1-a^2, z2=z1^2-z1+2 verified 5-units both components; z3=z1; extend gswz_epsm_kummer_level machinery'
status: in-progress
pr: 8217
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T13:39:32Z
updated_at: 2026-10-04T15:12:29Z
parent: qou-r9ih
---


## Increment 1 done (2026-08-02): F-level machinery + collapse finding

Probe `gswz_epsm_global_symbols_probe.py` (5/5): fields to degree 96,
alpha Hensel-lift, root-difference law green. FINDING: chi_m kills
mu_624 in every constructed field (624m | 5^d-1) — F-level classes
collapse structurally; NOT eps data. NEXT: implement the CGZ descent
P(xi) = a*b^m with a in the base — Galois norm/transfer from F to
Q_25(zeta_m), then class of `a` in the BASE group. That is the true
eps_m(xi).

## Increment 2 spec (2026-08-10): norm route DEAD — equivariant splicing required

Feasibility table (derived, exact): d = ord_5(624m) gives
[F:Q_25] = d/2 = 2m for EVERY m | 24 (m=2..24 -> 4,6,8,12,16,24,48).
The norm map N_{F/Q_25} raises unit classes to the 2m-th power, which
is 0 mod m in every case — the norm route to CGZ's descended `a`
(P(xi) = a*b^m, a in the base) is MAXIMALLY obstructed, structurally
(not an accident of one m). The extraction must implement the
chi^{-1}-equivariant splicing from CGZ's own proof (their §2 Prop 2.5
/ §3 Lemmas 3.1+3.5): construct b via the Galois action of
Gal(F/Q_25) = <phi_25> on P (sigma(P)/P is an m-th power for every
sigma; Hilbert-90-style splice), then a = P/b^m, then class of a in
Q_25^x/(Q_25^x)^m (Teichmuller dlog mod gcd(m,624) — nontrivial
there). Requires a careful read of the CGZ §2-3 proofs (cgz.txt in
scratchpad, or re-extract library/arxiv-1712.04887v3/1712.04887v3.pdf).

## Also queued (xx9f item 2): Nahm-argument E-test

Extract the 5_2 Nahm z-data of the psi_{0,z,1}(w,x)^3 bracket
(GSWZ (281), §4.5-4.6; GZ §8.2-8.3 for the 4_1 template) and re-run
the shifted-tail hypothesis for the (287) lambda with THOSE arguments
(the roots-of-unity argument set is refuted; witness digits in
gswz_psi_section_division.witness.json).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-11 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update (2026-11-16T22:04:01Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/SteepestDescentEulerMaclaurinAndFrobeniusDiagonal.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/steepest-descent-euler-maclaurin-and-frobenius-diagonal.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8217 (`f4d145a08828886b4eba631166b3e61717adc12d`); keeping `status: in-progress` until PR merges.
