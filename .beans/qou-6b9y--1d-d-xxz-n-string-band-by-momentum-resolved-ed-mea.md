---
# qou-6b9y
title: '1D-D: XXZ n-string band by momentum-resolved ED (measure, do not quote the formula)'
status: completed
type: task
priority: normal
created_at: 2026-09-14T16:44:07Z
updated_at: 2026-09-14T18:34:18Z
parent: qou-ifto
---

MEASURED 2026-09-14 (probe computations/onedim/xxz_string_band_probe.py, 6/6).

ESTABLISHED: momentum-block symmetrisation verified (blocks == full sector, 1e-18). An isolated level above the two-magnon continuum exists in EVERY momentum sector at N=8,10,12, at the substrate AND at a q=2 control -- the bound state IS present at q0. Substrate binding is 1.5-2 orders of magnitude below the control (the quantitative form of 'only marginally inside the massive phase').

NOT ESTABLISHED: the band energy. NOT converged at accessible N -- binding falls monotonically with N at both anisotropies and the ratio drifts 54.5 -> 70.2 over N=8..14. CHECK 4 asserts the drift so it cannot be silently forgotten. Quote no number from this probe as a thermodynamic-limit binding.

REFUTED: candidate band formula -2 sinh(eta) sinh(2eta)/(cosh 2eta - cos k) -- gives -2.5 at q=2,k=0 against a measured +0.288. Do not re-try it.

TRAP: with +Delta sz sz and Delta>0 the all-up state is the TOP of the band, so the bound state lies ABOVE the continuum. A first pass looked below and found nothing INCLUDING at the strong-anisotropy control. The control is what exposed it.

STAYS OPEN. Next: finite-size scaling to larger N, or a direct two-string Bethe solve.

CLOSED 2026-09-14 (355b11107, 9534fba59). The band IS extractable; xxz_string_band_probe's 'cannot' was an ALGORITHM limit, not a physics one.

    E_n(k) = -2 (q^n + q^-n - 2 cos k) / [n]_q
    B(k)   = 4 (Delta - |cos(k/2)|)^2 / Delta
    B(0)   = 2 q^2 hbar_q^4 / [2]_q = 1.180983e-4   (framework variables, no free parameters)

Exact at n=1 for every finite N and k (1.8e-39); n=2 at the substrate to 1.0e-13 at N=4096; n=3 to 2.7e-6 at a q=3 control. Finite-size residual obeys |E_N - E_inf| ~ z^N, z = cos(k/2)/Delta — a scaling law, not a threshold.

METHOD: the m=2 momentum block is EXACTLY real-symmetric tridiagonal in the relative coordinate (dim ~N/2, not ~N^2/2); Sturm bisection is O(N), so N=4096 costs 2.6 s. The earlier probe did dense ED at N<=14 against a bound state xi = 1/log(Delta) = 184 sites across.

VERIFIED INDEPENDENTLY before relaying: band(n=1,k) reproduces the hand-derived -4(Delta - cos k) to EXACTLY 0.0; B(0), xi and the 1693.5 ratio all reproduce.

FOUR CORRECTIONS to the earlier probe, all mine:
 1. 'not converged' was RIGHT; the suspected cause was not. At k=0 the finite-N continuum edge IS the thermodynamic edge exactly.
 2. 'a level above the continuum in EVERY momentum sector' is an ARTIFACT at m=1 and m=N-1 (edge depressed 21-53x the true binding; the level sits BELOW the true edge). Even sectors are genuine and carry the conclusion.
 3. '1.5-2 orders below the control' was a FLOOR: the thermodynamic ratio is 1693.5 (3.23 orders), not 70.2.
 4. TRAP — the formula I recorded as REFUTED is NOT refuted. It is half the n=2 string energy in the string-centre RAPIDITY lambda, and lambda(k=0) = pi, not 0, so I read the band at the opposite end of its own zone. With lambda(k) and the factor 2 it reproduces E_2(k) to 3.7e-40. A scope-(a) negative asserted as scope-(b), with no invariant. Re-scoped at both live sites.

CAVEAT, load-bearing: the numerator IS the TL loop parameter at level n and the denominator IS the quantum dimension — suggestive, and NOT a measured bridge to the Hecke tower. tl_is_the_xxz_chain identifies TL with the OPEN chain plus a boundary field; the band was measured on the PERIODIC chain. The difference is boundary operators, which should not move a bulk band in the thermodynamic limit — an ARGUMENT, not a measurement.
