---
# qou-dq2q
title: 'T2: closed-form the sibling''s cyclotomic-coefficient-asymmetry odd datum — run it over the trace field (cubic disc −23) / its ℚ(√−23) resolvent, NOT the ℚ(√−7) ladders [corrected 2026-08-11, qou-ynff]'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-19T00:05:02Z
updated_at: 2026-11-15T23:50:00Z
parent: qou-avtq
---


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: OPEN.** Open. The field premise was fixed by qou-ynff, and the closed-form computation has not been run.

Evidence: Premise corrected by qou-ynff (completed): trace field disc −23 (`FiveTwoSumRuleIntegrand.lean:249 disc_eq_neg_23`). Commits a0417e9822/853560fde5 only retitled it, and no result exists.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.


## 2026-11-15 — executed under owner ruling `Q-AVTQ-2 = 1` (PR #8063, absorbing `qou-ynff`, `qou-5gh6`, `qou-7lim`, `qou-ized`)

- **Probe & Witness:** `computations/qbeta/five_two_disc_neg23_cyclotomic_asymmetry_probe.py` & `computations/qbeta/five-two-disc-neg23-cyclotomic-asymmetry.witness.json`.
- **Exact Discriminant $-23$ Resolvent & Bézout Inverse:** Proved the explicit ring isomorphism $K_{5_2} = \mathbb{Q}(\xi)/(\xi^3 - 2\xi^2 + 3\xi - 1) \cong \mathbb{Q}(z)/(z^3 - z^2 + 1)$ via $\xi = 1 - z^2$, $z = -\xi^2 + \xi - 1$, with $\Delta = -23$ and quadratic resolvent $\mathbb{Q}(\sqrt{-23})$ ($h(-23)=3$, disjoint from $\mathbb{Q}(\sqrt{-7})$). Using the exact Bézout inverse $1/P'(\xi_0) = (10\xi_0^2 - 17\xi_0 + 18)/23$ and Vieta saddle identity $(\xi_1 - \xi_2)^2 P'(\xi_0)^2 = -23$, every $\alpha = a + b\xi + c\xi^2 \in K_{5_2}$ has exact bar-odd projection:
  $$\sigma_1(\alpha) - \sigma_2(\alpha) = \frac{(18b + 26c) - (17b + 22c)\xi_0 + (10b + 17c)\xi_0^2}{23}\sqrt{-23}.$$
  For the 1-loop invariant $P_1 = (-139 + 178\xi - 65\xi^2)/(4\cdot 23)$, a factor of $23$ cancels in the numerator, yielding $\Delta_{\mathrm{odd}}(P_1) = \frac{11(-10 + 7\xi_0 - 8\xi_0^2)}{4\cdot 23^2}\sqrt{-23} \approx -0.2111457559i$.
- **Masbaum Cyclotomic Coefficient Asymmetry:** For $C_{5_2,1}(q) = -(q^2+q^4)$, the normalized bar-odd/bar-even ratio is $\rho_1(q) = O_1(q)/E_1(q) = \frac{q^3-q^{-3}}{q^3+q^{-3}} = \tanh(3\ln q) \approx 0.30318397$ at $q_0$, identically equal to the $H_3$ bare content asymmetry $x(c=3)$. Neither matches `S_muon`, `S_proton`, `Im_Vb`, or `X_req` without fitting.
- **Lean 4 Formalization:** Added 8 sorry-free theorems to `folio/quantum-observable-universe/lean/QOU/QBeta/FiveTwoSumRuleIntegrand.lean` (`fiveTwo_cubic_x_of_z_factorization`, `fiveTwo_deriv_bezout_identity`, `fiveTwo_resolvent_sq_poly_identity`, `fiveTwo_saddle_diff_sq`, `fiveTwo_saddle_diff_mul_deriv_sq_eq_neg_23`, `fiveTwo_barOdd_resolvent_basis`, `fiveTwo_oneLoop_barOdd_factorization`, `masbaum_c52_one_barOdd_ratio`, `disc_neg23_neg7_not_int_sq`). Held at `status: in-progress` pending PR #8063 merge and owner closure review.
