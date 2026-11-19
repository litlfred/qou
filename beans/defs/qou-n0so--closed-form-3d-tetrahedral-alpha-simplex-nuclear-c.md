---
# qou-n0so
title: Closed-Form 3D Tetrahedral alpha-Simplex Nuclear Coordination & Isospin-Asymmetry Operator (56Fe, 208Pb, 238U Saturation)
status: todo
type: task
priority: high
created_at: 2026-11-19T06:42:39Z
updated_at: 2026-11-19T06:42:39Z
parent: qou-v2om
---

## Problem & 80-dps Truncation Level vs Experimental Accuracy Evidence

In `computations/probes/truncation_level_vs_accuracy_sweep_probe.py` (`truncation-level-vs-accuracy-sweep.witness.json`), the heavy-nuclide error decomposition across `56Fe`, `208Pb`, and `238U` diagnoses two opposite truncation failures in existing binding formulas:

1. **Unscreened All-Pairs Borromean (`OLD m_can` in `borromean_binding_recompute.py`):**
   Sums all $\binom{A}{2}$ nucleon pairs without 3D nearest-neighbor saturation AND uses an asymmetric neutron-neutron factor $f_{nn} = z_D - h_0 < z_D = f_{pp} = f_{pn}$ (`borromean_binding_recompute.py:130`), which makes each $nn$ pair $1.56\times$ more attractive than $pn$ ($0.71183\text{ MeV}$ vs $0.45628\text{ MeV}$ per pair) instead of Pauli-repulsive:
   - `56Fe` ($Z=26, N=30$): $B_{\mathrm{old}} = 806.84\text{ MeV}$ vs $B_{\mathrm{AME}} = 492.26\text{ MeV}$ ($B_{nn} = 309.65\text{ MeV}$ alone);
   - `208Pb` ($Z=82, N=126$): $B_{\mathrm{old}} = 11704.22\text{ MeV}$ vs $B_{\mathrm{AME}} = 1636.43\text{ MeV}$ ($B_{nn} = 5605.66\text{ MeV}$ alone);
   - `238U` ($Z=92, N=146$): $B_{\mathrm{old}} = 15403.35\text{ MeV}$ vs $B_{\mathrm{AME}} = 1801.69\text{ MeV}$ ($B_{nn} = 7534.73\text{ MeV}$ alone).
2. **1D Open-Chain Bond Truncation (`NEW-1 B_sym - E_C` in `mass_binding_dashboard.py`):**
   Uses only $A - 1$ bonds (`(Z-1)` $pp$ + `1` $pn$ + `(N-1)` $nn$, ~2.92 MeV/bond), missing the $3\times$ higher coordination number of 3D close-packed $\alpha$-tetrahedra (6 bonds/tetrahedron vs 3 bonds in a 1D chain of 4 nucleons), so $B_{\mathrm{sym}} - E_C$ under-binds heavy nuclei once $E_C \propto Z(Z-1)/A^{1/3}$ grows (`56Fe`: $60.06\text{ MeV}$; `208Pb`: $-56.82\text{ MeV}$; `238U`: $-104.86\text{ MeV}$).

```
Nuclide |  Z |   N |   A | B_AME (MeV) | E_C (MeV) | B_old (MeV) | B_old nn-share | B_new1_1D (MeV) | M_new1_err (ppQ)
--------+----+-----+-----+-------------+-----------+-------------+----------------+-----------------+-----------------
2H      |  1 |   1 |   2 |    2.224566 |    0.0000 |    2.063077 |         0.0000 |        2.860910 |      -3.394e+11
4He     |  2 |   2 |   4 |   28.295660 |    0.7699 |    6.475460 |         0.7118 |        7.997450 |      +5.445e+12
12C     |  6 |   6 |  12 |   92.161740 |    8.0076 |   37.558670 |        10.6775 |       24.385700 |      +6.063e+12
16O     |  8 |   8 |  16 |  127.619300 |   13.5810 |   65.095700 |        19.9313 |       30.625500 |      +6.511e+12
40Ca    | 20 |  20 |  40 |  342.052200 |   67.9010 |  402.608200 |       135.2480 |       47.183400 |      +7.916e+12
56Fe    | 26 |  30 |  56 |  492.260000 |  103.8200 |  806.841200 |       309.6460 |       60.058500 |      +8.292e+12
208Pb   | 82 | 126 | 208 | 1636.430000 |  685.0500 |11704.220000 |      5605.6600 |      -56.816200 |      +8.742e+12
238U    | 92 | 146 | 238 | 1801.690000 |  825.5600 |15403.350000 |      7534.7300 |     -104.863000 |      +8.604e+12
```

## Exact Algebraic Starting Point

1. **3D $\alpha$-Simplex Coordination Bond Count $N_{\mathrm{bonds}}^{(3\mathrm{D})}(Z, N)$:**
   In $H_{3A}(q_0)$, each 4-nucleon $SU(4)$ singlet cell $(1^4)$ forms a tetrahedral 3-simplex with $\binom{4}{2} = 6$ edges (3.0 bonds/nucleon interior), while inter-cell face sharing in a 3D close-packed lattice saturates at coordination $z_{\mathrm{bulk}} = 6$ (3 bonds/nucleon) minus the geometric boundary surface deficit $z_{\mathrm{surf}} A^{2/3}$:
   $$N_{\mathrm{bonds}}^{(3\mathrm{D})}(A) = 3 A \left(1 - A^{-1/3}\right) \quad (\text{exact at } A=1: 0\text{ bonds; } A=4: 6(1 - 4^{-1/3}) \text{ or } \binom{A}{2}\text{ for } A \le 4).$$
2. **Pauli / Young-Diagram Isospin-Asymmetry Penalty from $H_{3A}(q_0)$ Content Sum:**
   For $(Z, N)$ with $I_3 = (N - Z)/2$, the 4-row $SU(4)$ ground-state partition $\lambda(Z,N)$ has quadratic content-sum excess over the symmetric $Z = N$ partition:
   $$\Delta C_2(\lambda(Z,N)) = \sum_{\square\in\lambda(Z,N)} c(\square) - \sum_{\square\in\lambda(A/2,A/2)} c(\square) = \frac{9}{4}\frac{(N - Z)^2}{A} + O(1),$$
   which produces a positive Pauli symmetry penalty $-a_{\mathrm{sym}}(q_0) \frac{(N-Z)^2}{A}$ instead of the spurious attractive $f_{nn} = z_D - h_0$ factor.
3. **Deliverables:**
   - Derive the closed-form 3D simplex coordination operator and Pauli content-sum asymmetry term directly from the $H_{3A}(q_0)$ confinement SDP / Wedderburn trace without free parameters.
   - Formalize the content-sum isospin quadratic identity in Lean and verify across the full 10-nuclide table (`2H`..`238U`).
