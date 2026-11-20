---
# qou-qcov
title: 'GAP: braid-covariant non-pairwise QED insertion with derived M-coefficient b and scale c_em'
status: todo
type: task
priority: high
created_at: 2026-11-20T08:45:45Z
updated_at: 2026-11-20T08:45:45Z
parent: qou-9pl8
---

**Open (scope a).** Follows PR #8552 (QOU.BraidsAndKnots.NucleonQEDCovariance, 70 theorems, sorry-free).

Proved (scope b): on W_p=(2,1), W_n=(1,2) the commutant of the crossing action is {a·1 + b·M}
(commutant_A_iff/_B_iff); the #8518 adjacent insertion Q12+Q23 is not covariant (T2) and on W_p
tr((Q12+Q23)X) = −tr(Q13 X) for every X (T3); the all-pairs Coulomb insertion projects to b = 0
(E_QPair_Mcoeff_zero), giving n−p = (q⁻¹ − q − c_em/3)·tr(w). Any covariant insertion yields
a·tr(w) + b·q^|w|·tr N on positive words (T4); a·tr(V³) + b·tr N on V³.
Projected onto its covariant part the #8518 proton term shrinks by factor −0.00718 (0.2201 →
0.0016 keV); the connected n−p by −0.00238.

Scales measured (proton q0, connected trace 4.307e-4): m_e 0.2201 keV, E0_tower 1.821, alpha_bind
1.613, alpha_em·E0_tower 0.0133 vs the mu–p gap 0.2288 keV. Single-functional consistency asks for
c_em = alpha_em·E0_tower; only m_e lands near the gap ⇒ the scored two-term is a selection.

What would close it: a braid-covariant-by-construction non-pairwise operator (candidate: strand-
labelled crossing insertion; Milnor μ̄(123)·Q1Q2Q3 for the Borromean, all pairwise lk = 0) with b
and c_em derived, not tuned. Front: branch claude/qed-crossing-covariant-mubar-2026-11-20.
NOTE: owner ruled 2026-11-20 that two-term is PRIMARY in the scorecard (PR #8549) and in the q0
pin (PR #8554) regardless; this bean tracks the derivation, which those rulings do not supply.
