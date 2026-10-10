---
# qou-7xpx
title: 'M6: re-run interface-knot full/constit tr_M table at convention D'
status: todo
type: task
priority: normal
created_at: 2026-10-10T08:52:03Z
updated_at: 2026-10-10T14:06:36Z
parent: qou-d8c7
---

interface-knot-markov-z-proof.md table (D, T, He3, He4) was measured with pyhecke_native under convention C. The factorisation predicts 0.6127/0.2473/0.3754/0.1515 at z_D (proton pin). Re-run the full/constit trace at H6/H9/H12 under D and replace the table, or report the identity failing. conj:constit-factor-2q-minus-1 (0.033%) was also C-measured; per-Z step z_D(2q-1)=0.7475 unverified. Labelled historical on PR #7562 (owner pick 2a, 2026-10-10). Sibling of qou-2cof.


## 2026-10-10 re-run at convention D (branch claude/interface-knot-d-rerun-2026-10-10, commit 22f7ca495)

Probe: computations/probes/interface_knot_markov_z_convention_d_probe.py (+ witness). Route: tr_M = sum y_lambda^D chi_lambda, chi via pyhecke_native.chi_lambdas_braid_mpfr at the proton pin, 70 dps; averaged letters expanded by linearity; route checked against the Rust Markov-ascent tr_m_atomic_mpfr (agree 5e-52). (tr_m_atomic_mpfr alone fails on these words: 'Case C not implemented'.) Old producer delta_lambda_fr_identity_phase5c.py marshalled every averaged letter as bare sigma, so it traced a different element; not ported.

FACTORISATION HOLDS at D, rel err <= 5e-50, all four atoms, H6/H9/H12, three p-n letters:
- census word (p-n = sigma): D 0.61268804, T 0.24729789, 3He 0.37538663, 4He 0.15151646 (= predicted).
- live canonical (colour-weighted p-n): 0.50822979 / 0.20513564 / 0.31138631 / 0.12568415 (= prod(z+d_i)).
- colour-blind: 0.50815789 / 0.20510662 / 0.31134226 / 0.12566637.
Constit traces: D 0.29901502, T 0.14207206, 3He 0.18817864, 4He 0.08940998; constit = tr_p^Z tr_n^N to 1.5e-50.

CONSTIT STEP FAILS (scope-a negative): step = tr_M(proton) = 0.62932840 (alternating word) / 1.14575969 (grouped word) vs 2q-1 = 1.21995717 -> 48.4% / 6.1% miss. Full per-Z step canonical 0.38558198, not z_D(2q-1) = 0.74745316. conj:constit-factor-2q-minus-1 does not hold at D on either intra ordering; no claim about other closed forms. Note: that conj label has no content block (dangling code-quoted ref).

Proof .md updated: table replaced with D values + dated note; constit paragraph records the negative. Closeable as far as this bean's task goes (table re-run done); the open research is whether a D-frame closed form for tr_M(proton) exists - not tracked here.
