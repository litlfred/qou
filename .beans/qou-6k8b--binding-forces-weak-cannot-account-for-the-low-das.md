---
# qou-6k8b
title: 'binding forces: weak cannot account for the low-dashboard error; charge-symmetry breaking is 2.97x too large'
status: todo
type: task
created_at: 2026-08-08T21:46:35Z
updated_at: 2026-08-08T21:46:35Z
---

Asked whether the weak force is a missing binding term. Analysed all four contributions against the measured low-dashboard misses.

THE MISSES (B_AME - B_sym, MeV):
    2H -0.01 | 3H +1.07 | 3He +2.58 | 4He +17.98 | 6Li +13.59 | 7Li +15.66

SCALE CHECK — what can produce a 1-18 MeV miss:
  * STRONG, via coordination (1 -> ~2.15 bonds/nucleon): O(1-20 MeV). Right scale. This is the dominant term. See qou-h7mh.
  * EM (Coulomb): O(0-2.4 MeV) here, and already computed as E_C (not subtracted, deliberately).
  * WEAK: the parity-violating NN interaction is ~1 eV = 1e-6 MeV. SIX TO SEVEN ORDERS too small.
  * Gravity: not worth the line.

SO: NO, the weak force cannot account for any of it. That is not a limitation of this framework -- the weak interaction does not BIND. It converts n<->p (beta decay) and therefore selects WHICH nuclei are stable, not how tightly they hold together. Its role in this framework is already correct and already present: CAL-2 IS the weak sector (D_beta, the neutron beta-decay width), and it enters by PINNING q0, not as a term in the braid word. Adding a weak crossing to the word would be double-counting the calibration.

WHAT IS ACTUALLY WRONG WITH THE FORCE CONTENT — CHARGE SYMMETRY. The mirror pair is the clean probe: 3H(Z=1,N=2) and 3He(Z=2,N=1) share a strong core by isospin symmetry, so their binding difference should be near-pure Coulomb.

    B_AME    3H 8.482   3He 7.718   difference +0.764 MeV   <- nature
    B_sym    3H 7.412   3He 5.141   difference +2.271 MeV   <- framework
    overshoot 2.97x

That splitting is ENTIRELY alpha*(L_nn - L_pp) = +2.271 MeV. The strong force is charge-symmetric to ~1%, so L_nn should ~= L_pp; here they differ by 0.5425 (1.2370 vs 0.6945). The framework carries a charge-symmetry-breaking term about 3x larger than the whole physical mirror splitting, and it is in the STRONG bond constants, not in EM.

Note the ordering is independently suspect: L_nn (1.2370) > L_pp (0.6945) > L_pn (0.5336) makes the p-n bond the WEAKEST, yet the deuteron (pn) binds and the dineutron (nn) does not.

ALSO: the pn constant is not measured the same way as the other two -- see qou-xzda. Any conclusion about L_pn vs L_nn/L_pp must account for that first, since the three are not derived alike.

WHAT THE BRAID ACTUALLY CONTAINS (surveyed, for the record):
  strong: B3 confinement (sigma0 sigma1^-1)^3 per nucleon; quark crossings (uu->sigma, ud->mixed, dd->sigma^-1); gluon self-coupling (2 sigma0); inter-nucleon pp/pn/nn
  EM:     electron pe crossings on gen 1; E_C computed separately and NOT subtracted
  weak:   absent from the word, present as CAL-2 pinning q0
  torus operators: nothing outside _deprecated/

Acceptance: the mirror splitting 3H-3He comes out near 0.764 MeV, from Coulomb rather than from L_nn - L_pp.
