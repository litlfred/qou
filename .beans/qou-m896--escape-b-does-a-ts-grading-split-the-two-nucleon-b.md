---
# qou-m896
title: 'Escape (b): does a (T,S) grading split the two-nucleon binding sign?'
status: completed
type: task
priority: normal
created_at: 2026-09-01T08:08:29Z
updated_at: 2026-09-01T08:12:23Z
---


RESOLVED 2026-09-01 -- computations/probes/isospin_grading_restores_the_sign_probe.py,
6/6. YES for the sign; NO for the magnitude. Necessary, not sufficient.

THE IDENTIFICATION IS FORCED BY PAULI, NOT FITTED. Two nucleons need a totally
antisymmetric wavefunction: 1S0 (spin-singlet, spatially symmetric) needs
SYMMETRIC isospin => T=1; 3S1 needs ANTISYMMETRIC => T=0. The two-strand Hecke
algebra has exactly two Wedderburn blocks, both 1-dimensional:
    (2)    <-> T=1 (1S0)   pp, nn, np-singlet
    (1,1)  <-> T=0 (3S1)   np only
Eigenvalues +q and -1/q, verified against build_seminormal_matrices to 1e-16.

THE RESULT. At beta = 0 -- a pure sigma crossing carrying NO FLAVOUR INFORMATION
AT ALL:
    T=1 block:  |mu| = q   = 1.10998 > 1  ->  UNBOUND   (pp, nn, np-singlet) OK
    T=0 block:  |mu| = 1/q = 0.90092 < 1  ->  BOUND     (deuteron)           OK
Exactly the physical pattern. qou-v3u2 proved a flavour-assigned offset CANNOT
produce this at all (mu(d) = z+d is affine, superlevel set is a half-line). The
structure was already sitting in the two Wedderburn blocks; nothing in the
construction uses it.

THE WINDOW, CLOSED FORM:
    T=1 unbound <=> beta < (q-1)/h   = q/(q+1) = 0.526061540067
    T=0 bound   <=> beta < (1-1/q)/h = 1/(q+1) = 0.473938459933
    both        <=> beta in [0, 1/(q+1))
Thresholds are complementary: q/(q+1) + 1/(q+1) = 1 exactly. Two consequences:
1/(q+1) < 1/2 for EVERY q > 1, so the unoriented average beta=1/2 is outside the
window at any substrate; and production's beta_pn = 0.499656 misses by 0.025718.

THE LIMIT -- FORCED MIRROR SYMMETRY. The achievable asymmetry between the bound
and unbound channels, |L(T=0)|/|L(T=1)|:
    beta      L(T=0)       -L(T=1)      ratio
    0         0.10434072   0.10434072   1.000000   <- maximum
    0.10      0.08140062   0.08532647   0.953990
    0.25      0.04794799   0.05610951   0.854543
    0.40      0.01557831   0.02601317   0.598863
    ->beta*   -> 0         0.01181758   -> 0
CAPPED AT EXACTLY 1, attained ONLY at beta=0, where both channels equal log q to
5.7e-42. The single point that gets both signs right is the point of exact
mirror symmetry.

Nature: deuteron 2.224566 MeV bound vs np 1S0 virtual state ~0.066 MeV unbound
=> ratio 33.7055, on a quantity the model cannot push above 1. Robust to the
virtual-state energy (67.4 at half, 16.9 at double). Magnitudes: alpha*log q =
0.43676831 MeV for BOTH channels -- 5.0932x low vs the deuteron and 6.6177x high
vs the 1S0 state, being the same number for both, which is the degeneracy
restated.

VERDICT: escape (b) removes the impossibility and replaces it with a forced
degeneracy. The failure changes CHARACTER rather than going away. That is real
progress and should not be oversold.

CAVEATS:
 - "BOUND" is read as |mu| < 1. The antisymmetric eigenvalue is NEGATIVE, so
   -log(mu) is undefined there and the magnitude is used. Defensible (the sign is
   fixed by which Hecke eigenvalue the block carries, not by an energy) but it IS
   a convention doing real work. Under a convention treating a negative ratio as
   unphysical, the T=0 channel has no binding reading and this escape does not run.
 - n=2 INTERFACE ONLY: one strand per nucleon, where the atom words give three.
   Lifting the (T,S) grading into the 3-strands-per-nucleon construction is NOT
   done here and is the next test.
 - escape (a) (>1 crossing per bond) remains untried and is not exclusive with this.
