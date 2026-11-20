---
# qou-15sj
title: 'GAP: alpha_em [10]_q linchpin — delta_q(T_3,5)=q^10-q^-10 asserted not derived'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T20:56:46Z
updated_at: 2026-11-20T16:00:00Z
parent: qou-3l2l
---

Red-team 2026-08-22: docs/audits/2026-08-22-alpha-em-derivation-redteam.md

Bare alpha_em^-1 = q[9]_q[10]_q = 136.823 (0.155%) rests on (9,10) being Diophantine-forced by genus-4 saturation on Bring Sigma_4: (p-1)(q-1)=8, gcd=1 => exactly {T_2,9, T_3,5} (VERIFIED, real).

BUT [10]_q comes from an ASSERTED collapse delta_q(T_3,5)=q^10-q^-10 that the trace-ratio block never derives (no 3-term Rosso-Jones sum shown). Actual standard Jones of T(3,5) = t^4+t^6-t^10 (3-term, symbolic-exact), NOT a clean binomial. The '10' may be reverse-engineered from the crossing number to parallel the legit 2-strand T_2,9 case.

NEXT: produce the explicit 3-strand H_3 Rosso-Jones/Markov-trace sum over V_(3),V_(2,1),V_(1,1,1) at the framework's delta_q normalization; show whether it collapses to h*[10]_q. Collapses => derivation; not => [10]_q is selected and the (9,10) forcing is incomplete (it fixes the KNOTS, not that the observable is product-of-crossing-q-integers).

Also flagged (finding 2): meson EM factor (3q^2-1)/(2q^2) 'three generations = T(2,3),T(2,5),T(2,7)' uses genus-1/2/3 selection, INCONSISTENT with the force-carrier genus-4 rule it cites.

Corpus already honest on the -467.6 ppb structural gap (beans qou-gwio, qou-93ap; PR #5361). No new over-claim found live on main.

## Round 50 Formalization & 50-dps Witness (PR #8177)
- **Lean 4 Module (`0 sorry`, `0 axiom`, `0 vacuity`):** `folio/quantum-observable-universe/lean/QOU/AlphaEM/ChernSimonsTowerAndT35Linchpin.lean`
  - `t35_weighted_trace_eq_binomial_iff`: the 3-strand $H_3(q)$ weighted trace on $T(3,5) = (\sigma_1 \sigma_2)^5$ collapses to $q^{10} - q^{-10} = (q - q^{-1})[10]_q$ if and only if $(w_{(3)}, w_{(2,1)}, w_{(1,1,1)}) = (1, 0, -1)$ (pure exterior-power alternating character, $w_{(2,1)} = 0$).
  - `t35_conventionD_rowCap_excludes_binomial`: under Convention-D's $N=2$ row cap ($w_{(1,1,1)} = 0$), the $q^{-10}$ coefficient vanishes so the trace never equals $q^{10} - q^{-10}$.
  - `forceCarrier_vs_mesonGeneration_genus`: $2g(T(2,9)) = 2g(T(3,5)) = 8$ ($g = 4$, coinciding with the 8-dimensional $\mathfrak{su}(3)$ adjoint), whereas the 2-strand meson knots $T(2,3), T(2,5), T(2,7)$ have $2g \in \{2, 4, 6\}$ ($g \in \{1, 2, 3\}$).
- **50-dps Witness:** `computations/probes/round50-zeta4-bridge-and-alpha-em-cs-tower.witness.json` (`scriptHash: e7bf4a93b887`, `scriptCommitSha: cf283b8e199f4643fb9e0259ec0a2702096bdd9b`).
- **PR:** `litlfred/qou#8177` (`https://github.com/litlfred/qou/pull/8177`, head SHA `3fdbeeb87a6b1821ff8d57a95f95d4d20cf72628`).
- **Status:** Kept at `status: in-progress` per reviewer-separated closure discipline.

## 2026-11-20 (PR #8562, bean qou-q0pl)
Four alpha functionals measured side by side at the one-term proton / two-term
(#8554) / muon pins (docs/audits/2026-11-20-alpha-em-two-term-q0-pull.md):
form B -0.365/+75.970/+78.998 ppb; form A +0.994/+77.329/+80.357; CS tower
-467.636/-390.982/-387.942; ruled-out 45[3]_q +2.588/+5.885/+6.016. Form B and
the CS tower are different functions of q (additive term 8/(12 pi) constant vs
pi^2(98/45)[2]_q/2 hbar_q^2), coincident only at q0 — not truncations of one
another. The gram_kappa_numerical_value sorry was a false statement and is
replaced by a sorry-free refutation; kappa = 1.7216 is det G_cl/det G_q and
never used gramKappa (bean qou-wkgp). Status unchanged: the CS-tower conjecture
class still has no instance.
