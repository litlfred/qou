---
# qou-4x8r
title: Sec.10b's 2H over-binding is +27.4% in convention D, not the recorded +74.9% (that figure is convention C)
status: in-progress
pr: 8205
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T10:05:43Z
updated_at: 2026-10-04T15:24:22Z
parent: qou-v2om
---

## Measured 2026-08-30

`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
Sec.10b gives the zero-freedom 2H prediction `B(2H) = -alpha ln mu_pn` with
`alpha = m_e/(q0(q0-1))`, and Sec.10a's table records the log form at **+74.9%**
over AME.

That audit is dated **2026-08-08** and writes `z = 1/(sqrt(q0) + 1/sqrt(q0))` —
**convention C**. The owner ruling making convention D canonical is 2026-08-15,
a week later.

Recomputed at the proton pin (`computations/probes/ursell_alternation_sign_identity_probe.py`,
`boltzmann_chain`), same alpha, same formula, only z changed:

    convention   mu_pn            B(2H)        / AME 2.224566
    C (Sec.10a)  0.3948620864     3.8897 MeV       1.7485    (= the recorded +74.9%)
    D (canonical) 0.5082297894    2.8332 MeV       1.2736    (= +27.4%)

The C row reproducing +74.9% is the cross-check that this is the same
computation and not a different object.

**So Sec.10b's headline number is +27.4% under the canonical convention, not
+74.9%.** The migration more than halves the over-binding of the corpus's only
zero-free-parameter 2H prediction. The DERIVATION is convention-independent (it
needs only trace multiplicativity plus extensivity); only the numbers move.

## Scope and next

Not fixed in place: Sec.10a/b is a dated audit document and qou-3nva's standing
decision is to leave those as historical records of their analysis. What is
needed is a currency note at the section, or a successor audit, saying the
figures are C-frame and giving the D values. Check the rest of Sec.10's tables
(the linear-form ceiling table, the B_can^0 column) the same way before quoting
any of them: they are all C-frame.

Related: qou-cds1 (the Q_beta c_k ladder is C-frame and un-re-derived), which is
the same class of debt.


## Progress Update (PR #8205)
- [x] Pure Lean 4 formalization wired into `QOU.lean` (`AtomNFQDegreeBondSetDichotomy.lean`, `TwoNucleonChannelSignObstruction.lean`, `PairLayerLinearRampParity.lean`, `ChainMirrorSplittingChargeSymmetry.lean`; 0 `sorry`, 0 vacuity advisories across all 6 static audits)
- [x] 50-dps `mpmath` + exact `TL_3` Laurent polynomial probe (`computations/probes/atom_nf_qdegree_pair_ramp_mirror_probe.py`) and stamped witness (`computations/probes/atom-nf-qdegree-pair-ramp-mirror-probe.witness.json`, 0 raw `float64` fields)
- [ ] Awaiting adversarial review and Merge Manager merge of PR #8205 (`ready: ed5c0c87c86301f2666c843555cc576831d17a74`)
