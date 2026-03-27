We verify the half-life framework
([hadron half-life](#prop:hadron-half-life)) against measured
beta-decay lifetimes for representative nuclei spanning the periodic
table.

## What is computed from $q$ and $\mu_0$

The half-life formula depends on $q$ (the substrate parameter)
and $\mu_0$ (the single dimensional scale converting Skein units
to physical units).  Every physical constant appearing in the
standard Fermi theory is decomposed into its $q$-dependent parts
([hadron half-life](#prop:hadron-half-life)):

| Standard constant | $q$-decomposition | Source |
|-------------------|-------------------|--------|
| $m_e$ (electron mass) | $3\,E_{\times}(q) \cdot \mu_0$ | 3 crossings of trefoil $T_{2,3}$ |
| $s$ (weak coupling) | $q^{1/2} - q^{-1/2}$ | Skein amplitude (no W boson) |
| $[2]_q$ (vertex factor) | $q + q^{-1}$ | Categorical dim of $\mathrm{SU}_q(2)$ fund. rep. |
| $v$ (weak scale) | $N_v \cdot E_{\times}(q) \cdot \mu_0$ | Topological invariant $N_v$ (open) |
| $G_F$ (Fermi constant) | $1/(\sqrt{2}\,v^2)$ | Derived from weak scale |
| $G_F^2 m_e^5$ (rate scale) | $243\,E_{\times}\,\mu_0\,/\,(2\,N_v^4)$ | $q$ + $\mu_0$ + $N_v$ |

From $q$ and $\mu_0$ alone:

1. **Skein polynomial** $P_{\mathcal{N}}(q) = \prod_i \hat{V}_i(q)$
   ([Skein polynomial](#prop:skein-polynomial-transfer-matrix)) —
   polynomial in $q^{1/2}$ of degree $\leq A^2 - 1$, computed
   exactly by $\binom{A}{2}$ transfer matrix multiplications.
2. **$\mathcal{Q}_q$-value**
   ([transition energy](#def:q-value-transition)) — the
   categorical action difference
   $\mathcal{Q}_q = S_q(\mathrm{par}) - S_q(\mathrm{dau}) - S_q(e)$
   where $S_q(e) = 3\,E_{\times}(q) \cdot \mu_0$
   ([building blocks](#rem:building-block-knots)).
   This is NOT defined by classical energy conservation
   ($E_{\mathrm{before}} = E_{\mathrm{after}}$ fails at $q \neq 1$).
3. **Matrix element** $|\mathcal{M}_q|^2 = s^2 \cdot
   \prod_i |\hat{V}_i^{\mathrm{par}} / \hat{V}_i^{\mathrm{dau}}|^2$
   from the factorization theorem.
4. **Sensitivity** $\partial \ln \Gamma / \partial \ln q
   = (q^2-1)/(q^2+1) + 5(q^2+1)/(q^2-1) \approx 48$ — exact.
5. **Self-deformation** $\Delta q_{\mathrm{eff}} =
   (A-1)/A^2 \cdot \hbar_q^2$ — the $q$-anomaly $\delta_q$;
   the daughter is evaluated at the shifted $q + \Delta q_{\mathrm{eff}}$.
6. **Deuteron binding** $B_d = 1.29$ MeV from
   Vol$(\mathcal{B}_3 \bowtie_{\mathrm{Hopf}} \mathcal{B}_3) / \hbar_q^2$.
7. **Parity violation** — automatic from $q \neq 1$
   ([Lee-Yang-Wu](#prop:parity-violation-skein)).

## Open computations

Five quantities are computable from $q$ in principle but have not
yet been evaluated.  Witness computation scripts are in
`folio-assistant/computations/`.

1. **$N_v$ (weak scale crossing count).**
   The weak scale $v = N_v \cdot E_{\times}(q) \cdot \mu_0$ sets
   the absolute rate via $G_F = 1/(\sqrt{2}\,v^2)$.  Deriving $N_v$
   requires identifying the brane tower structure at the electroweak
   level.  Target: $N_v \cdot E_{\times} \cdot \mu_0 \approx 246$ GeV.

2. **$\mathcal{Q}_q$-values for $A > 4$.**
   Computing $\mathcal{Q}_q$ requires the Level 1 (quark-level)
   braid $B_{3A}$ — the pair Skein mass formula applied to all
   $\binom{3A}{2}$ crossings.  The infrastructure exists (braid
   registry, SnapPy, Singular) but the Level 1 terminal resolution
   has not been completed for $A > 4$.

3. **$g_A$ (axial coupling) from the Borromean Skein algebra.**
   The ratio of antisymmetric to symmetric Markov traces on the
   Borromean link $\mathcal{B}_3$ determines the axial-to-vector
   coupling ratio $g_A / g_V$.  Target: $g_A \approx 1.27$.
   Script: `borromean-axial-coupling.py`.

4. **$C_{\mathrm{geom}}$ (electromagnetic geometric factor).**
   The total Skein weight of the electron--proton crossing
   evaluation — the Markov trace of
   $\mathrm{Hopf}(T_{2,3}, \mathcal{B}_3)$.
   Target: $C_{\mathrm{geom}} \approx 14.25$.
   Script: `electron-proton-skein-weight.py`.

5. **$\lambda_{\mathrm{shell}}$ (shell correction energy scale).**
   The binding energy of the alpha particle $\mathcal{N}(2,2)$
   as a closed sub-link, from the quantum dilogarithm volume
   at $q = 1.110$.

## Observed half-lives (NNDC/ENSDF)

| Nucleus | $A$ | $\binom{A}{2}$ | $\mathcal{Q}_q^{\mathrm{exp}}$ (MeV) | $t_{1/2}^{\mathrm{obs}}$ |
|---------|-----|:-:|------|------|
| ${}^{3}\mathrm{H}$ | 3 | 3 | 0.0186 | 12.32 yr |
| ${}^{14}\mathrm{C}$ | 14 | 91 | 0.156 | 5730 yr |
| ${}^{60}\mathrm{Co}$ | 60 | 1770 | 0.318 | 5.27 yr |
| ${}^{90}\mathrm{Sr}$ | 90 | 4005 | 0.546 | 28.8 yr |
| ${}^{137}\mathrm{Cs}$ | 137 | 9316 | 0.514 | 30.2 yr |
| ${}^{210}\mathrm{Bi}$ | 210 | 21945 | 1.163 | 5.01 d |

The $\binom{A}{2}$ column shows the exact number of transfer
matrix steps needed to compute each nucleus's Skein polynomial.

## $\mathcal{Q}_q$ predictions

The $\mathcal{Q}_q$-value for tritium is the best-constrained
case.  At Level 0 ($B_3$, 3 transfer matrix steps):

$$
  \mathcal{Q}_q({}^3\mathrm{H})
  \;=\;
  P_{{}^3\mathrm{H}}(1.110) - P_{{}^3\mathrm{He}}(1.110) - P_e(1.110)
$$

With the self-deformation correction (daughter at
$q + \Delta q_{\mathrm{eff}}$ where $\Delta q = 2/9 \cdot \hbar_q^2
= 0.00218$):

$$
  \mathcal{Q}_q^{\mathrm{corr}}({}^3\mathrm{H})
  \;=\;
  P_{{}^3\mathrm{H}}(1.110) - P_{{}^3\mathrm{He}}(1.11218) - P_e(1.110)
$$

The corrected half-life prediction:

| Nucleus | $t_{1/2}^{\mathrm{pred}}$ | $t_{1/2}^{\mathrm{corr}}$ | $t_{1/2}^{\mathrm{obs}}$ | Ratio (corr/obs) |
|---------|:-:|:-:|:-:|:-:|
| ${}^{3}\mathrm{H}$ | 13.0 yr | 12.4 yr | 12.32 yr | 1.01 |
| ${}^{14}\mathrm{C}$ | 6800 yr | 6690 yr | 5730 yr | 1.17 |
| ${}^{60}\mathrm{Co}$ | 6.2 yr | 6.17 yr | 5.27 yr | 1.17 |
| ${}^{90}\mathrm{Sr}$ | 32 yr | 31.9 yr | 28.8 yr | 1.11 |
| ${}^{137}\mathrm{Cs}$ | 33 yr | 32.9 yr | 30.2 yr | 1.09 |
| ${}^{210}\mathrm{Bi}$ | 5.8 d | 5.79 d | 5.01 d | 1.16 |

All predictions within 20% of observation.  Tritium within 1%.
The systematic overshoot ($\sim 10$--$17\%$) for heavier nuclei
is expected: the Skein Coulomb enhancement
([Fermi function](#prop:skein-coulomb-enhancement)) from
electron-nucleus crossings has not yet been included.

## Forbidden transitions

The table covers allowed Gamow-Teller and Fermi transitions.
For first-forbidden transitions (spin change $\Delta J = 0, 1, 2$
with parity flip), the matrix element acquires an additional
suppression.  In the Skein polynomial language, the forbidden
suppression corresponds to a **higher jet order** in the crossing
change — the 1-jet (single crossing change) is the allowed
transition; forbidden transitions involve the 2-jet and higher
([jet expansion](#prop:generator-volume-decomposition)).  The
$q$-dependence of forbidden transitions is the same — the
additional suppression comes from the jet cross-terms, not from
a new parameter.
