---
# qou-6b9y
title: '1D-D: XXZ n-string band by momentum-resolved ED (measure, do not quote the formula)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-14T16:44:07Z
updated_at: 2026-09-14T17:30:52Z
parent: qou-ifto
---

MEASURED 2026-09-14 (probe computations/onedim/xxz_string_band_probe.py, 6/6).

ESTABLISHED: momentum-block symmetrisation verified (blocks == full sector, 1e-18). An isolated level above the two-magnon continuum exists in EVERY momentum sector at N=8,10,12, at the substrate AND at a q=2 control -- the bound state IS present at q0. Substrate binding is 1.5-2 orders of magnitude below the control (the quantitative form of 'only marginally inside the massive phase').

NOT ESTABLISHED: the band energy. NOT converged at accessible N -- binding falls monotonically with N at both anisotropies and the ratio drifts 54.5 -> 70.2 over N=8..14. CHECK 4 asserts the drift so it cannot be silently forgotten. Quote no number from this probe as a thermodynamic-limit binding.

REFUTED: candidate band formula -2 sinh(eta) sinh(2eta)/(cosh 2eta - cos k) -- gives -2.5 at q=2,k=0 against a measured +0.288. Do not re-try it.

TRAP: with +Delta sz sz and Delta>0 the all-up state is the TOP of the band, so the bound state lies ABOVE the continuum. A first pass looked below and found nothing INCLUDING at the strong-anisotropy control. The control is what exposed it.

STAYS OPEN. Next: finite-size scaling to larger N, or a direct two-string Bethe solve.
