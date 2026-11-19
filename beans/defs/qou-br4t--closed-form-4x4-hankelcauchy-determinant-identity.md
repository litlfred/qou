---
# qou-br4t
title: Closed-Form 4x4 Hankel/Cauchy Determinant Identity for 4-Row SU(4) q-Plancherel Normalization Z_{3A}^{(4)}(q)
status: todo
type: task
priority: high
created_at: 2026-11-19T06:42:10Z
updated_at: 2026-11-19T06:42:10Z
parent: qou-v2om
---

## Problem & 80-dps Truncation Level vs Experimental Accuracy Evidence

In `computations/probes/su4_occupancy_binding_mass_probe.py`, the unnormalized balanced $q$-Plancherel weight $W_\lambda(q_0) = [3A]_{q_0}! / \prod_{\square\in\lambda} [h(\square)]_{q_0}^2$ exceeds $1$ for $A \ge 20$ ($-\ln W_\lambda < 0$), causing $-E_0 \ln W_\lambda - E_C$ to flip sign to massive unbinding (`40Ca`: $W_{\mathrm{un}} = 2.46 \times 10^{74}$; `56Fe`: $W_{\mathrm{un}} = 8.14 \times 10^{192}$; `208Pb`: $W_{\mathrm{un}} = 7.58 \times 10^{3885}$; `238U`: $W_{\mathrm{un}} = 2.79 \times 10^{5164}$).

In `computations/probes/truncation_level_vs_accuracy_sweep_probe.py` (`truncation-level-vs-accuracy-sweep.witness.json`), we proved and verified to 76+ decimal digits ($|\text{rel\_err}| < 1.6 \times 10^{-77}$ at $n=168$) that the 4-row $SU(4)$ $q$-Plancherel partition sum $Z_n^{(4)}(q_0) = \sum_{\lambda\vdash n, \ell(\lambda)\le 4} W_\lambda(q_0)$ satisfies an exact $4 \times 4$ Hankel determinant identity, making $\widetilde{W}_\lambda^{(4)}(q_0) = W_\lambda(q_0) / Z_{3A}^{(4)}(q_0) \in (0, 1)$ strictly bounded for all $A = 1 \dots 238$:

```
Nuclide |   n |   W_unnorm(q0) |     Z_n^(4)(q0) | W_norm4 = W/Z^(4) | B_norm4 - E_C (MeV) | B_AME (MeV)
--------+-----+----------------+-----------------+-------------------+---------------------+------------
2H      |   6 |      1.113e-01 |       9.574e-01 |         1.163e-01 |            9.091726 |    2.224566
3H      |   9 |      2.249e-02 |       8.106e-01 |         2.774e-02 |           15.156330 |    8.481796
3He     |   9 |      2.249e-02 |       8.106e-01 |         2.774e-02 |           14.308910 |    7.718041
4He     |  12 |      7.737e-04 |       5.759e-01 |         1.343e-03 |           27.184470 |   28.295660
12C     |  36 |      4.105e-06 |       2.529e-01 |         1.623e-05 |           38.616990 |   92.161740
16O     |  48 |      6.414e-04 |       9.139e+01 |         7.018e-06 |           36.587370 |  127.619300
40Ca    | 120 |      2.456e+74 |       9.224e+79 |         2.662e-06 |          -13.636310 |  342.052200
56Fe    | 168 |     8.143e+192 |      2.299e+196 |         3.542e-04 |          -70.231760 |  492.260000
208Pb   | 624 |    7.581e+3885 |     2.821e+3905 |         2.687e-20 |         -494.545700 | 1636.430000
238U    | 714 |    2.785e+5164 |     1.573e+5194 |         1.770e-30 |         -535.955800 | 1801.690000
```

## Exact Algebraic Starting Point

1. **Frobenius shifted-part representation ($\ell_i = \lambda_i + 4 - i$, $\ell_1 > \ell_2 > \ell_3 > \ell_4 \ge 0$, $\sum_{i=1}^4 \ell_i = n + 6$):**
   $$\prod_{\square\in\lambda} [h(\square)]_q = \frac{\prod_{i=1}^4 [\ell_i]_q!}{\prod_{1\le i<j\le 4} [\ell_i - \ell_j]_q}, \qquad W_\lambda(q) = [n]_q! \frac{\prod_{1\le i<j\le 4} [\ell_i - \ell_j]_q^2}{\prod_{i=1}^4 ([\ell_i]_q!)^2}.$$
2. **Exact $4 \times 4$ Andréief / Cauchy–Binet Hankel determinant identity:**
   Using $\prod_{1\le i<j\le 4} [\ell_i - \ell_j]_q = (q - q^{-1})^{-6} q^{-3(\ell_1+\ell_2+\ell_3+\ell_4)} \det_{0\le j\le 3}(q^{2j\ell_i})$ and symmetry in $(\ell_1,\ell_2,\ell_3,\ell_4)$:
   $$Z_n^{(4)}(q) = \frac{[n]_q!}{(q - q^{-1})^{12}} \, [z^{n+6}] \det_{0 \le j, k \le 3} \left( \tilde{F}_{j+k}(z; q) \right), \qquad \tilde{F}_m(z; q) = \sum_{\ell \ge 0} \frac{q^{(2m - 6)\ell}}{([\ell]_q!)^2} z^\ell \quad (m = 0, \dots, 6).$$
3. **Deliverables:**
   - Formalize the Frobenius shifted-part hook identity for $\ell(\lambda)\le 4$ and the $4 \times 4$ Hankel determinant formula for $Z_n^{(4)}(q)$ in Lean (`folio/quantum-observable-universe/lean/QOU/`), proving $0 < \widetilde{W}_\lambda^{(4)}(q) < 1$ for all $q > 1$.
   - Replace the unnormalized $W_\lambda(q_0)$ in `su4_occupancy_binding_mass_probe.py` with $\widetilde{W}_\lambda^{(4)}(q_0) = W_\lambda(q_0) / Z_{3A}^{(4)}(q_0)$ and combine with the 3D $\alpha$-simplex coordination operator so $-E_0 \ln \widetilde{W}_\lambda^{(4)}$ scales extensively across $A = 4 \dots 238$.
