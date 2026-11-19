---
# qou-51yf
title: Closed-Form Convention-D Q_beta / m_n Habiro-Kashiwara Rungs c_3, c_4 on Mirror-Projected alpha_D^proj + Two-Term QED
status: todo
type: task
priority: high
created_at: 2026-11-19T06:43:32Z
updated_at: 2026-11-19T06:43:32Z
parent: qou-wxhi
---

## Problem & 80-dps Truncation Level vs Experimental Accuracy Evidence

Related to `qou-cds1`. In `computations/probes/truncation_level_vs_accuracy_sweep_probe.py` (`truncation-level-vs-accuracy-sweep.witness.json`), the $Q_\beta$ & neutron mass $m_n$ Habiro–Kashiwara + two-term QED truncation sweep (`T3`) measures the exact progression across levels $N = 0, 1, 2, 2+\text{2tQED}$ and the truncation envelope $u^N = (b_{\mathrm{Kash}} \hbar_q^2)^N$ for $N = 3, 4, 5, 6$:

```
Level N (Q_beta & m_n Tower)          | Q_beta err (ppQ) | Q_beta (sigma) |  m_n err (ppQ) | m_n (sigma_exp)
--------------------------------------+------------------+----------------+----------------+----------------
N0_FormA_tree                         |      +1.678e+12  |       +2152.0  |    +1.397e+09  |        +2734.0
N1_FormA_Kashiwara_cos_alphaD         |      +6.750e+11  |        +865.7  |    +5.619e+08  |        +1100.0
N2_FormA_c2_neg1_strong_only          |      +6.024e+11  |        +772.6  |    +5.015e+08  |         +981.6
N2_FormA_plus_2tQED_plain             |      +1.785e+11  |        +228.9  |    +1.484e+08  |         +290.5
N2_FormA_plus_2tQED_cartan_q          |      +1.318e+11  |        +169.1  |    +1.096e+08  |         +214.5
N2_KD6_unproj_alphaD_plus_2tQED       |      -9.418e+12  |      -12080.0  |    -7.842e+09  |       -15350.0
N2_KD6_mirrorProj_alphaD_plus_2tQED   |      -9.962e+12  |      -12780.0  |    -8.295e+09  |       -16240.0
```

And the exact Habiro expansion parameter $u = b_{\mathrm{Kash}} \hbar_q^2 = \sqrt{\frac{h_0^2+3}{h_0^2+4}} \left(\frac{q_0-1}{q_0}\right)^2 = 8.51748 \times 10^{-3}$ has higher-rung envelopes:

```
Rung N |       u^N | Q_A * u^N (eV) | Envelope / sigma_exp(Q_beta) | Envelope / sigma_exp(m_n)
-------+-----------+----------------+------------------------------+--------------------------
N = 3  | 6.179e-07 |     0.4842 eV  |                 0.7938 sigma |              1.0090 sigma
N = 4  | 5.263e-09 |   0.004124 eV  |               0.006761 sigma |            0.008592 sigma
N = 5  | 4.482e-11 |  3.512e-05 eV  |               5.758e-05 sigma|            7.318e-05 sigma
N = 6  | 3.818e-13 |  2.992e-07 eV  |               4.904e-07 sigma|            6.233e-07 sigma
```

Thus the $O(1)$-coefficient Habiro ladder converges inside $1\sigma_{\mathrm{exp}}(Q_\beta) = 0.61\text{ eV}$ at **$N = 3$** and inside $0.0086\,\sigma_{\mathrm{exp}}(m_n)$ at **$N = 4$**, while the current $+139.2\text{ eV}$ ($178.5\text{ ppm}$) residual at `N2_FormA_plus_2tQED_plain` comes from the $O(\hbar_q^2)$ cross-term between the strong Form-A / KD6 base and the two-term Borromean QED connected cumulant $\Delta m_{\mathrm{QED}}^{\mathrm{conn}}$.

## Exact Algebraic Starting Point

1. **Mirror-Projected Convention-D Eigenphase (`WedderburnPhaseAndTwoTermPinBridge.lean`):**
   $$\alpha_D^{\mathrm{proj}}(q) = \frac{z_D(q) - 1}{2} h - \frac{h^2}{4} = -\frac{q^4 + 2q^3 - 2q^2 + 2q + 1}{4 q^2 (q^2 + 1)}, \qquad h = q - q^{-1},\quad z_D = \frac{q^3}{q^2 + 1},$$
   obtained by subtracting the chiral $(3)$-sector mean shift $h/2$ from the $H_3(q)$ Markov trace defect before taking the $\sigma_1 \mapsto -q^{-1}$ `(2,1)` character projection.
2. **Coupled Strong + Two-Term QED Habiro Rungs ($N = 3, 4$):**
   $$Q_\beta^{(N)}(q_0) = Q_A(q_0) \cos\!\left(\alpha_D(q_0) - \frac{u}{2}\right) \left(1 - u^2 + c_3 u^3 + c_4 u^4\right) + \Delta m_{\mathrm{QED}}^{\mathrm{conn}}(q_0)\left(1 + d_1 \hbar_q + d_2 \hbar_q^2\right),$$
   where $\Delta m_{\mathrm{QED}}^{\mathrm{conn}}(q_0) = -\frac{\alpha_{\mathrm{EM}}}{\pi} E_0 (1 - \tau_{\mathrm{Bor}}^3)$ currently truncates the QED-strong dressing at $d_1 = d_2 = 0$ (noting that $Q_A \hbar_q^2 \approx 57.8\text{ eV}$ and $|\Delta m_{\mathrm{QED}}^{\mathrm{conn}}| \approx 331.7\text{ eV}$, so an $O(1)$ one-loop strong-QED cross-dressing or the Cartan-$q$ + $E_0^{(\infty)} = E_0/(1-\hbar_q^2)$ dressing shifts $Q_\beta$ at the $\sim 100\text{ eV}$ scale).
3. **Deliverables:**
   - Derive the Convention-D $c_3, c_4$ Habiro–Kashiwara coefficients and the $O(\hbar_q)$ strong-QED cross-dressing coefficient $d_1$ on $\Delta m_{\mathrm{QED}}^{\mathrm{conn}}$ from the $H_3(q_0)$ two-row Hoefsmit representation without empirical fitting.
   - Formalize the resulting closed-form $N=3,4$ identity in Lean (`folio/quantum-observable-universe/lean/QOU/QBeta/`).
