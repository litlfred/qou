---
# qou-6k8b
title: 'binding forces: weak cannot account for the low-dashboard error; charge-symmetry breaking is 2.97x too large'
status: todo
pr: 8205
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T21:46:35Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
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


## DERIVATION ATTEMPT (same session) — resolved down to one line

### 1. The linear law B = 5g is not merely ASSERTED, it is UNDERIVABLE as stated

`g = 1/sqrt(5 + (q0-1)^2/q0)` depends only on q0, which is a mass RATIO and
therefore dimensionless. So `5g = 2.23363534` is a PURE NUMBER declared to be
MeV. It does not scale with m_e:

    alpha = m_e/(q0(q0-1))  ->  4.185981 MeV = 4185.981 keV     scales correctly
    5g                      ->  2.2336 "MeV" != 2.2336 "keV"    off by 1000x

Every energy in this framework is alpha x dimensionless, and alpha carries the
CAL-1 unit m_e. A quantity with no m_e in it cannot be an energy here. The
+0.41% agreement with AME is a numerical coincidence IN MeV SPECIFICALLY.

Corollary: the three bond constants are not the same kind of object. L_pp and
L_nn are pure functions of q0 (`ln(tr_free/tr_atom)`); L_pn = 5g/alpha carries
m_e. Term-by-term, `alpha[(Z-1)L_pp + L_pn + (N-1)L_nn]` is dimensionally
incoherent -- the alpha cancels for the pn term and not for the others.

This cannot be repaired by tuning. It is the wrong kind of object.

### 2. A tempting deuteron coincidence, TESTED AND KILLED

The det form's 2-body shortfall is 1.292767 MeV; m_n - m_p = 1.293333 MeV,
agreeing to 0.044%. It does not survive contact with A>2:

    iso   shortfall/(m_n-m_p)
    2H    0.9996
    3H    1.7014
    3He   4.2023
    4He   1.3145

No pattern, not 1, not n_pn. Recorded as a disproved lead so nobody spends a
day rediscovering it.

### 3. WHAT IS ACTUALLY DERIVABLE: the mirror error is one line

Mirror splitting B(3H) - B(3He) from the determinant form, by sign pattern
(nature: +0.764 MeV, essentially pure Coulomb):

    pp=+1, nn=-1 (as landed)   3.99831 MeV   5.23x nature
    pp=+1, nn=+1               0.00000 MeV   exactly zero
    pp=-1, nn=-1               0.00000 MeV   exactly zero

ANY charge-symmetric pattern gives IDENTICALLY zero strong mirror splitting.
The whole 3.998 MeV comes from pp != nn -- and the same defect drives B_sym's
2.97x overshoot via L_nn - L_pp.

Root cause, `mass_at_3A_proper.py:337-338`:

    _X_PP = (mpf(1), mpf(0))      # sigma
    _X_NN = (mpf(1), -h_loc)      # sigma^-1

pp is assigned sigma and nn sigma^-1. The strong force is charge-symmetric to
~1%; this assignment breaks it at the braid level, and everything downstream
(L_pp != L_nn, the [1^4] sign pattern read off as pp=+1/nn=-1, both forms'
mirror failures) inherits it from these two lines.

PROPOSED, and parameter-free because charge symmetry is a symmetry and not a
fit: make the pp and nn inter-nucleon crossings identical, and let E_C supply
the physical mirror splitting. The framework already computes E_C = 1.00 MeV
for 3He against nature's 0.764 -- the right scale, ~30% high, consistent with
r0 = 1.2 fm being approximate.

CAUTION before acting: the pp/nn sign asymmetry is what produces mu_min = -sqrt5
and hence the DERIVED "5" in g_reeb. Imposing charge symmetry changes that
spectrum, so the 5 must be re-derived under the symmetric pattern rather than
carried over. The two findings are coupled and must move together.


## Progress Update (PR #8205)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`AtomNFQDegreeBondSetDichotomy.lean`, `TwoNucleonChannelSignObstruction.lean`, `PairLayerLinearRampParity.lean`, `ChainMirrorSplittingChargeSymmetry.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact `TL_3` Laurent polynomial probe (`computations/probes/atom_nf_qdegree_pair_ramp_mirror_probe.py`) and stamped witness (`computations/probes/atom-nf-qdegree-pair-ramp-mirror-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8205 (`ready: ed5c0c87c86301f2666c843555cc576831d17a74`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8205, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
