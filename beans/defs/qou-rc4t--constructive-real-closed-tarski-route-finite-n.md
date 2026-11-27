---
# qou-rc4t
title: 'Constructive: real-closed (Tarski) route for finite-N comparisons'
status: in-progress
type: task
priority: normal
tags:
    - constructive
    - volume-conjecture
created_at: 2026-11-27T17:25:00Z
updated_at: 2026-11-27T20:03:45Z
parent: qou-dk7p
---

Owner standing pick (recommended option) 2026-11-27, alternative raised
alongside the Lawvere cut.

Goal: state every finite-N comparison (per-N certificate values, which are
algebraic over Q(zeta_N)+) inside the real algebraic numbers, a real-closed
field where order is decidable, so finite-N positivity claims need no axiom.
Mechanism: Sturm-sequence / sign-determination checks on the minimal
polynomial; Mathlib real-closed support is thin, so expect finite checks.

Scope: finite N only. The N -> infinity limit stays on [Coev E]
(QOU/Core/LawvereCut.lean, PR #9487). Pairs with qou-pc7n (certificates).

Not adopted, recorded as options: topos-internal Dedekind reals (moves the
axiom, large); order-only MacNeille cut (special case of the Lawvere cut).

## 2026-11-27 progress (PR #9527, head 7092958ad66)
- QOU/Core/TarskiSign.lean: Bernstein / Taylor-shift positivity certificates over any ordered field; root exclusion (bisection without IVT); Gonshor windows `follow`/`signPrefix` (first sign + iff 0 < alpha); `pos_of_window` (decision depth = birthday of deciding window); `gonshorCut` located in Archimedean K with no Coev.
- QOU/Core/TarskiSignKashaev.lean: <4_1>_N over any comm ring (Dickson identity proved); <4_1>_5 = 48+4c mod Psi_5, <4_1>_7 = 103+25c+11c^2 mod Psi_7; embedding = sign "+"; prefixes + - + - and + + - -; 50 < <4_1>_5 <= 51, 139 < <4_1>_7, <4_1>_5 < <4_1>_7; c_5 located without Coev.
- Birthday caveat recorded: irrational algebraics are born on day omega; birthdays grade the windows, not the numbers.
Still open: Bernstein completeness (degree elevation); locatedness without the bounds hypothesis (integer phase); certificate generator for general N; appendix-surreals exposition block.

## 2026-11-27 follow-up (PR #9561, head 50b67ccd84e)
#9527 merged as 356f1fcc71. Follow-up adds computations/knots/tarski_sign_certificates.py (exact generator), QOU/Core/TarskiSignKashaevGen.lean (floors of <4_1>_N, N = 3..16: 13, 27, 50, 89, 151, 250, 407, 651, 1030, 1610, 2495, 3835, 5855, 8883; increasing chain), and appendix-surreals prop:tarski-sign-decision-depth. Embedding depths 0-4, decision depths up to 18.
Still open: Bernstein completeness proof; locatedness without the bounds hypothesis; N > 16 (elaboration time grows, ~1m45 at N <= 16).


## 2026-11-27 follow-ups (PR #9603)
- gonshorCut_located' : the Gonshor cut of every α is located in any Archimedean ordered field; the integer phase (exists_follow_bounded) discharges the bounds hypothesis. Sorry-free.
- exists_bernstein_certificate : f ≥ δ > 0 on [0,1] gives some degree-N Bernstein certificate, so the generator's search always terminates. Uniform δ is needed (over Q a polynomial positive at rationals can vanish at an irrational). Sorry-free.
- Floors of <4_1>_N for N = 17..24 (TarskiSignKashaevGen2, stepwise value proofs): 13404, 20128, 30092, 44814, 66501, 98361, 145056, 213336.
- Still open: the N → ∞ limit (stays on [Coev E]); N > 24 (compile time is about 3 min per 8 levels, so this is mechanical).
