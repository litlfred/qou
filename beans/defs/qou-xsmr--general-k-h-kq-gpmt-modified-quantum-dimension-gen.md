---
# qou-xsmr
title: General-K H_K(q) GPMT Modified Quantum Dimension Generating Function & Mayer/Ursell Cluster Resummation
status: todo
type: task
priority: high
created_at: 2026-11-19T06:41:41Z
updated_at: 2026-11-19T06:41:41Z
parent: qou-rgj8
---

## Problem & 80-dps Truncation Level vs Experimental Accuracy Evidence

In `computations/probes/truncation_level_vs_accuracy_sweep_probe.py` (`truncation-level-vs-accuracy-sweep.witness.json`), the unscreened all-pairs Borromean sum in `borromean_binding_recompute.py` stops at $K=3,4$ and sums $\binom{A}{2}$ unscreened pairs with $f_{nn} = z_D - h_0$, blowing up quadratically on medium/heavy nuclides (`56Fe`: $B_{\text{old}} = 806.84\text{ MeV}$ vs AME $492.26\text{ MeV}$; `208Pb`: $B_{\text{old}} = 11704.22\text{ MeV}$ vs AME $1636.43\text{ MeV}$; `238U`: $B_{\text{old}} = 15403.35\text{ MeV}$ vs AME $1801.69\text{ MeV}$).

Evaluating the universal Ocneanu/Wenzl Wedderburn weight $w_\lambda(q, z)$ on $H_K(q)$ across $K = 3 \dots 8$ at 80-dps precision establishes:

```
K | #parts | #ord-1 (c=-2) | #ord>=2 | 2-row sum | s_GPMT(K) (signed) | Mayer cumulant mu_K
--+--------+---------------+---------+-----------+--------------------+--------------------
3 |      3 |             1 |       0 |         1 |       +0.16338323  |       +0.16338323
4 |      5 |             2 |       0 |         1 |       +0.56923018  |       -0.084302728
5 |      7 |             4 |       0 |         1 |       +0.66878594  |       -0.54353270
6 |     11 |             7 |       0 |         1 |       +0.066819055 |       +1.32489160
7 |     15 |            11 |       0 |         1 |       -0.61637972  |       -1.24425190
8 |     22 |            16 |       1 |         1 |       -0.49657641  |       -0.44996549
```

## Exact Algebraic Starting Point

1. **Universal Ocneanu/Wenzl content-hook product on $H_K(q)$:**
   $$w_\lambda(q, z) = q^{2 n(\lambda)} \prod_{\square=(i,j)\in\lambda} \frac{q^{2 c(\square)+1} z + (q^2 - 1) - q z}{(q^2 - 1) [h(\square)]_{q^2}}, \qquad c(\square) = j - i,\quad n(\square) = \sum_{i\ge 1}(i-1)\lambda_i.$$
2. **Order-of-vanishing filtration at $z_D = q^3/(q^2+1)$:**
   Since $G_c(q, z_D) = [c+2]_{q^2}/[2]_{q^2}$ vanishes iff $c = j - i = -2$ (cells $(3,1), (4,2), (5,3), \dots$), define $r(\lambda) = |\{(i,j)\in\lambda : i - j = 2\}|$.
   - $r(\lambda) = 0$ ($\ell(\lambda) \le 2$): $\sum_{\ell(\lambda)\le 2} f^\lambda w_\lambda(q, z_D) = 1$ identically for all $K \ge 1$.
   - $r(\lambda) = 1$ (contains $(3,1)$ but not $(4,2)$, covering all $\ell(\lambda)\ge 3$ for $3 \le K \le 7$):
     $$d_D^{(1)}(S^\lambda) = \left.\frac{\partial w_\lambda(q,z)}{\partial z}\right|_{z=z_D} = -\frac{q^{2 n(\lambda) - 3}}{[2]_{q^2}^{K-2}} \frac{\prod_{\square\in\lambda \setminus \{(3,1)\}} [c(\square)+2]_{q^2}}{\prod_{\square\in\lambda} [h(\square)]_{q^2}}.$$
   - $r(\lambda) \ge 2$ (onset at $K=8, \lambda=(2,2,2,2)$ containing $(3,1)$ and $(4,2)$): the $r$-th Geer–Patureau-Mirand–Turaev derivative $d_D^{(r)}(S^\lambda) = \frac{1}{r!}\frac{\partial^r w_\lambda}{\partial z^r}\big|_{z_D}$ provides the higher-order renormalized trace stratum.
3. **Closed-form Mayer/Ursell cluster generating function:**
   Derive and formalize in Lean (`folio/quantum-observable-universe/lean/QOU/`) the exponential cumulant generating function
   $$\mathcal{Z}_{\mathrm{GPMT}}(t; q) = 1 + \sum_{K\ge 3} s_{\mathrm{GPMT}}(K; q)\frac{t^K}{K!} = \exp\!\left(\sum_{K\ge 3} \mu_K(q)\frac{t^K}{K!}\right)$$
   and its Borel/Padé cluster resummation screening the $\binom{A}{2}$ pairwise divergence at large $A$.
