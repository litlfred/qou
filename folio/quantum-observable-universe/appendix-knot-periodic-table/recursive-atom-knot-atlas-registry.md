The [recursive atom-knot atlas](#prop:recursive-atom-knot-atlas) organizes confined particles and atomic nuclei at the aether parameter $q_0$ into four hierarchical levels $\ell \in \{0, 1, 2, 3\}$. At each level, composite operators are assembled from lower-level normal forms in the Iwahori--Hecke tower $H_n(q_0)$ ([confined particle](#def:confined-particle); [confinement SDP](#prop:confinement-sdp)) without empirical fitting. Absolute mass figures in $\mathrm{MeV}$ render dimensionless ratios $\mathfrak{m}/m_e$ against the electron calibration scale $m_e = 0.51099895\;\mathrm{MeV}$; the parameter-free predictive content resides in the dimensionless mass ratios, nucleon mass splitting, nuclear binding energies, magic separation jumps, and isobaric $\beta$-stability minima.

## Algebraic notation and canonical braid closures

Each braid generator $\sigma_i \in B_n$ ($1 \leq i \leq n - 1$) satisfies the quadratic Hecke relation $(\sigma_i - q_0)(\sigma_i + q_0^{-1}) = 0$ in $H_n(q_0)$, and $\widehat{\beta}$ denotes the Markov closure of $\beta \in B_n$ in $S^3$. Six canonical closures generate the elementary and composite building blocks of the atlas ([fermions are knots, bosons are links](#prop:fermion-boson-knot-link)):

| Closure | Braid word | Carrier | Topological type | $\mathrm{Vol}_{\mathrm{hyp}}$ | Physical sector |
|:-------:|:-----------|:-------:|:-----------------|:-----------------------------:|:----------------|
| $0_1$ | $\mathbf{1}_{B_1}$ | $H_1(q_0)$ | Unknot ($T_{1,0}$) | $0$ | Neutrino ($\nu$, vacuum drag) |
| $4 \cdot 0_1$ | $\mathbf{1}_{B_4}$ | $H_4(q_0)$ | Four disjoint unknots | $0$ | Photon ($\gamma$, polarization $\times$ chirality) |
| $\mathcal{L}_H$ | $\sigma_1^2$ | $H_2(q_0)$ | Hopf torus link ($T_{2,2}$) | $0$ | Gluon and pairwise nuclear interface |
| $3_1$ | $\sigma_1^3$ | $H_2(q_0)$ | Left trefoil ($T_{2,3}$) | $0$ | Electron ($e^-$; mirror $3_1^\sigma$ for $e^+$) |
| $4_1$ | $(\sigma_1 \sigma_2^{-1})^2$ | $H_3(q_0)$ | Amphichiral figure-eight | ${{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}$ | Scalar mass-generation complement |
| $\mathcal{B}_3$ | $(\sigma_1 \sigma_2^{-1})^3$ | $H_3(q_0)$ | Three-component Borromean link | $8G = 7.327725\ldots$ | Nucleons $\mathfrak{p} = \mathcal{B}_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$, $\mathfrak{n} = \mathcal{B}_3(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ |

Here $G = \sum_{k=0}^{\infty} (-1)^k / (2k + 1)^2 = 0.91596559\ldots$ is Catalan's constant.

## Levels $\ell = 0$ and $\ell = 1$: Elementary braids, leptons, and Borromean nucleons.

At $\ell = 0$ (vacuum and confined sub-hadronic strands) and $\ell = 1$ (single leptons and three-quark Borromean baryons, [Borromean baryon](#def:borromean-baryon)), the two-term categorical Lagrangian trace at $q_{2\mathrm{t}} = 1.10997860\ldots$ fixes the free-constituent masses entering every composite atom.

| Entry | Level | Carrier | Canonical Hecke word $T_w$ | Closure $\widehat{T_w}$ | Derived value (MeV) | Experimental reference (MeV) |
|:-----:|:-----:|:-------:|:---------------------------|:-----------------------:|--------------------:|-----------------------------:|
| $\nu$ | $\ell = 0$ | $H_1(q_0)$ | $\mathbf{1}$ | $0_1$ | $0$ | $< 10^{-6}$ |
| $\gamma$ | $\ell = 0$ | $H_4(q_0)$ | $\mathbf{1}_{B_4}$ | $4 \cdot 0_1$ | $0$ | $0$ |
| $\mathfrak{q}$ | $\ell = 0$ | $H_1(q_0)$ | $\sigma_0$ (confined) | — | confined | confined |
| $e^-$ | $\ell = 1$ | $H_2(q_0)$ | $\sigma_1^3$ | $T_{2,3} = 3_1$ | $0.51099895$ (scale) | $0.51099895$ |
| $\mathfrak{p}$ | $\ell = 1$ | $H_3(q_0)$ | $(\sigma_1 \sigma_2^{-1})^3_{\mathfrak{u}\mathfrak{u}\mathfrak{d}}$ | $\mathcal{B}_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ | $938.27209$ | $938.27209$ |
| $\mathfrak{n}$ | $\ell = 1$ | $H_3(q_0)$ | $(\sigma_1 \sigma_2^{-1})^3_{\mathfrak{u}\mathfrak{d}\mathfrak{d}}$ | $\mathcal{B}_3(\mathfrak{u}\mathfrak{d}\mathfrak{d})$ | $939.56556$ | $939.56542$ |
| $\delta m_{\mathfrak{n}\mathfrak{p}}$ | $\ell = 1$ | $H_3(q_0)$ | $Q_\beta^{N=2,2\mathrm{t}}(q_{2\mathrm{t}}) + m_e$ | $\mathcal{B}_3(\mathfrak{u}\mathfrak{d}\mathfrak{d}) \to \mathcal{B}_3(\mathfrak{u}\mathfrak{u}\mathfrak{d})$ | $1.29347$ | $1.29335$ |

## Level $\ell = 2$: Few-nucleon cells ($A \leq 4$), $H_4(q_0)$ full-twist $\alpha$-closure, and the Hoyle threshold.

Unfactored Specht representations of $H_{3A}(q_0)$ scale as $\dim H_{3A} = (3A)!$ across $p(3A)$ partitions ($p(12) = 77$ at ${}^{4}\mathrm{He}$, $p(36) = 17{,}977$ at ${}^{12}\mathrm{C}$, and $p(120) = 1{,}844{,}349{,}560$ at ${}^{40}\mathrm{Ca}$). Standard Convention-D Markov trace evaluation annihilates all partitions with $\ell(\lambda) \geq 3$, leaving only $\lfloor 3A/2 \rfloor + 1$ two-row partitions and omitting three- and four-body nuclear correlations. Inductive Gröbner--Shirshov block reduction ([Gröbner--Shirshov engine](#sec:groebner-engine)) compresses pairwise interfaces to $\binom{A}{2}$ $2 \times 2$ transfer steps. Geer--Patureau-Mirand--Turaev (GPMT) modified traces on $H_4(q_0)$ then supply the non-vanishing three- and four-body cumulants $(w_3, w_4^{(H_4)})$ on the five partitions of $4$ ($\lambda \in \{(4), (3,1), (2,2), (2,1,1), (1,1,1,1)\}$, full-twist exponents $2\kappa_\lambda \in \{+12, +4, 0, -4, -12\}$).

On few-nucleon $A \leq 4$ systems, zero-parameter Hecke evaluation replaces ad hoc hyperbolic-volume matching by algebraic trace channels ($b_2 = E_0 \ln(1/z_D) = 2.051\;\mathrm{MeV}$ in Convention D, $b_2^{gg} = E_0 \ln(1/z_{gg}) = 2.834\;\mathrm{MeV}$ in the double-twist $gg$ channel, and the closed-shell $H_4(q_0)$ full-twist Casimir on ${}^{4}\mathrm{He}$).

| Nuclide | $A$ | $3A$ strands | $p(3A)$ | $\binom{A}{2}$ steps | Algebraic channel at $q_0$ | $B_{\mathrm{QOU}}$ (MeV) | $B_{\mathrm{AME}}$ (MeV) | $\Delta B/B$ |
|:-------:|:---:|:------------:|--------:|---------------------:|:---------------------------|-------------------------:|-------------------------:|-------------:|
| ${}^{2}\mathrm{H}$ | 2 | 6 | 11 | 1 | Single Convention-D bond ($b_2$ bare / tower) | $2.051\;/\;2.071$ | $2.225$ | $-7.82\%\;/\;-6.90\%$ |
| ${}^{3}\mathrm{H}$ | 3 | 9 | 30 | 3 | $K_3$ triangle + $w_3$ ($gg$ bare) | $9.185$ | $8.482$ | $+8.29\%$ |
| ${}^{3}\mathrm{He}$ | 3 | 9 | 30 | 3 | $K_3$ triangle + $w_3 - E_{\mathrm{C}}$ ($gg$ bare) | $8.338$ | $7.718$ | $+8.03\%$ |
| ${}^{4}\mathrm{He}$ | 4 | 12 | 77 | 6 | $H_4(q_0)$ full-twist Wigner singlet (bare / tower) | $26.426\;/\;26.695$ | $28.296$ | $-6.61\%\;/\;-5.66\%$ |

**Borromean $3\alpha$ Hoyle threshold.** Across $A = 4k_\alpha$ multi-$\alpha$ complexes, two $\alpha$-particles (${}^{8}\mathrm{Be}$, $k_\alpha = 2$) form a single inter-$\alpha$ edge with zero $3\alpha$ 2-simplices ($f_2^\alpha(2) = 0$). Coulomb repulsion therefore overcomes residual pair attraction ($\Delta B_{2\alpha} = B({}^{8}\mathrm{Be}) - 2B({}^{4}\mathrm{He}) = -0.0918\;\mathrm{MeV} < 0$), leaving ground-state ${}^{8}\mathrm{Be}$ $\alpha$-unbound. At $k_\alpha = 3$ (${}^{12}\mathrm{C}$), the first Borromean $3\alpha$ triangle ($f_2^\alpha(3) = 1$) activates three-body attraction ($\Delta B_{3\alpha} = +7.275\;\mathrm{MeV}$), with the $0_2^+$ Hoyle resonance $+0.379\;\mathrm{MeV}$ above the $3\alpha$ threshold at $E_x = 7.654\;\mathrm{MeV}$. At $k_\alpha = 4$ (${}^{16}\mathrm{O}$, $f_2^\alpha(4) = 4$, $f_3^\alpha(4) = 1$), four-body tetrahedral saturation yields $\Delta B_{4\alpha} = +14.437\;\mathrm{MeV}$ ($\Delta B_{4\alpha}/\Delta B_{3\alpha} = 1.984$).

## Level $\ell = 3$: Three-dimensional simplicial synthesis across all 3,558 AME2020 nuclides

Stacked Apollonian 3-trees embed every vertex on the outer boundary ($f_1 = 3A - 6$, $f_2 = 3A - 8$, $f_3 = A - 3$), omitting interior coordination and $A^{2/3}$ surface scaling ($40.27\%$ median $|\Delta B/B|$ across AME2020). Replacing the 3-tree by compact three-dimensional simplicial balls — the face-centered-cubic $K_4$-clique ball, the coordinate-verified Freudenthal--Kuhn 3-ball ($f_1 \sim 6A$, $f_2 \sim 10A$, $f_3 \sim 5A$), and the close-packed Mackay nuclear shell ball ($f_1 = A + f_3 + f_0^\partial - 3 \sim 7A - O(A^{2/3})$, $f_2 = 2f_3 + f_0^\partial - 2 \sim 12A - O(A^{2/3})$, $f_3 \sim 6A - O(A^{2/3})$, [nuclear binding regimes](#sec:nuclear-binding)) — restores interior three-dimensional coordination and $-A^{2/3}$ surface tension.

**Global accuracy across all $3{,}556$ bound AME2020 nuclides ($A \geq 2$, $Z = 1\text{--}118$) at $q_0$.**

| Parameter-free simplicial model | All $A \geq 2$ med.\ $|\Delta B/B|$ | $\mathrm{RMSE}(B/A)$ (MeV) | $16 \leq A < 100$ med.\ | $100 \leq A < 200$ med.\ | $A \geq 200$ med.\ |
|:--------------------------------|------------------------------------:|---------------------------:|------------------------:|-------------------------:|-------------------:|
| Apollonian 3-tree baseline ($E_0^{\mathrm{tower}}$, $\ln z_D^{-1}$) | $40.27\%$ | $3.125$ | $34.91\%$ | $41.44\%$ | $42.09\%$ |
| 3D FCC $K_4$-clique ball ($H_3$ GPMT, $\ln z_D^{-1}$) | $10.68\%$ | $0.957$ | $13.99\%$ | $10.07\%$ | $8.97\%$ |
| 3D Freudenthal--Kuhn ball ($H_4$ GPMT + Fermi sym., $\ln z_D^{-1}$) | $2.14\%$ | $0.654$ | $2.03\%$ | $2.03\%$ | $2.20\%$ |
| **3D close-packed shell ball ($H_4$ GPMT + sym.\ HO + Fermi, $\ln z_D^{-1}$)** | **$1.02\%$** | **$0.582$** | **$1.27\%$** | **$0.59\%$** | **$1.70\%$** |
| 3D close-packed shell ball (Borromean $q$-dilogarithm bond $b_2^{\mathrm{Bor}}$) | $1.51\%$ | $0.582$ | $1.33\%$ | $1.20\%$ | $2.63\%$ |
| 3D close-packed shell ball (discrete FCC vertex-pair Coulomb sum) | $2.67\%$ | $0.591$ | $1.98\%$ | $2.41\%$ | $3.67\%$ |

Evaluating at the two-term Borromean anchor $q_{2\mathrm{t}}$ yields an identical $1.02\%$ median $|\Delta B/B|$ across all $3{,}556$ bound nuclides.

**Canonical benchmark nuclides across mass regimes ($q_0$, total binding $B$ in MeV).**

| Nuclide | $(Z, N)$ | $(f_1, f_2, f_3)_{\mathrm{shell}}$ | Shell ball ($\ln z_D^{-1}$) | Shell ball ($b_2^{\mathrm{Bor}}$) | Kuhn 3-ball ($\ln z_D^{-1}$) | Discrete FCC Coulomb | $B_{\mathrm{AME}}$ |
|:-------:|:--------:|:----------------------------------:|----------------------------:|----------------------------------:|-----------------------------:|---------------------:|-------------------:|
| ${}^{12}\mathrm{C}$ | $(6, 6)$ | $(38, 44, 17)$ | $79.36\;(-13.89\%)$ | $79.83\;(-13.38\%)$ | $78.66\;(-14.65\%)$ | $81.02\;(-12.09\%)$ | $92.16$ |
| ${}^{16}\mathrm{O}$ | $(8, 8)$ | $(57, 72, 30)$ | $119.92\;(-6.04\%)$ | $120.62\;(-5.48\%)$ | $108.53\;(-14.96\%)$ | $122.26\;(-4.20\%)$ | $127.62$ |
| ${}^{56}\mathrm{Fe}$ | $(26, 30)$ | $(259, 368, 164)$ | $477.91\;(-2.91\%)$ | $481.12\;(-2.26\%)$ | $500.47\;(+1.67\%)$ | $487.15\;(-1.04\%)$ | $492.26$ |
| ${}^{208}\mathrm{Pb}$ | $(82, 126)$ | $(1141, 1752, 818)$ | $1652.41\;(+0.98\%)$ | $1666.52\;(+1.84\%)$ | $1638.88\;(+0.15\%)$ | $1682.19\;(+2.80\%)$ | $1636.43$ |
| ${}^{238}\mathrm{U}$ | $(92, 146)$ | $(1321, 2039, 955)$ | $1834.73\;(+1.83\%)$ | $1851.07\;(+2.74\%)$ | $1855.05\;(+2.96\%)$ | $1866.89\;(+3.62\%)$ | $1801.69$ |
| ${}^{294}\mathrm{Og}$ | $(118, 176)$ | $(1657, 2575, 1211)$ | $2116.26\;(+1.68\%)$ | $2136.76\;(+2.67\%)$ | $2147.07\;(+3.16\%)$ | $2160.23\;(+3.80\%)$ | $2081.23$ |

On open-shell actinides such as ${}^{238}\mathrm{U}$ ($30$ valence nucleons above $(Z, N) = (82, 126)$, spherical Coulomb energy $E_{\mathrm{C}}^{(0)} = 825.56\;\mathrm{MeV}$, Compton oscillator spacing $\hbar\omega_0 = 6.817\;\mathrm{MeV}$), volume-preserving Nilsson quadrupole splitting breaks spherical $(2j + 1)$ degeneracy against Rayleigh--Bohr--Wheeler Coulomb-plus-surface stiffness while vanishing identically at doubly magic ${}^{208}\mathrm{Pb}$.

**Mayer--Jensen magic separation jumps and the isobaric $\beta$-stability valley.**

* **Magic shell closures**: Two-nucleon separation-energy jumps $\Delta_{2n}(Z, N) = S_{2n}(Z, N) - S_{2n}(Z, N + 2)$ and $\Delta_{2p}(Z, N) = S_{2p}(Z, N) - S_{2p}(Z + 2, N)$ are strictly positive across every harmonic-oscillator and spin--orbit intruder closure $2, 8, 20, 28, 50, 82, 126$ (and neutron closure $184$), verified on ${}^{16}\mathrm{O}$ ($N, Z = 8$), ${}^{40}\mathrm{Ca}$ ($N, Z = 20$), ${}^{48}\mathrm{Ca}$ ($N = 28$), ${}^{58}\mathrm{Ni}$ ($Z = 28$), ${}^{88}\mathrm{Sr}$ ($N = 50$), ${}^{120}\mathrm{Sn}$ ($Z = 50$), ${}^{132}\mathrm{Sn}$ ($N = 82$), and ${}^{208}\mathrm{Pb}$ ($Z = 82, N = 126$).
* **Isobaric $\beta$-stability valley ($A = 4\text{--}238$, $235$ chains)**: Minimizing total nuclear mass $Z m_{\mathfrak{p}} + (A - Z)m_{\mathfrak{n}} - B_{\mathrm{QOU}}(Z, A - Z)$ using the parameter-free splitting $\delta m_{\mathfrak{n}\mathfrak{p}}^{\mathrm{QOU}}(q_0) = 1.29347\;\mathrm{MeV}$ ([beta-stability closure](#sec:beta-stability-closure)) reproduces the empirical $\beta$-stable charge $Z_{\mathrm{exp}}(A)$ **exactly** on $140 / 235$ chains ($59.6\%$). Residual agreement holds within $|\Delta Z| \leq 1$ on $193 / 235$ chains ($82.1\%$) and within $|\Delta Z| \leq 2$ on $234 / 235$ chains ($99.6\%$), with mean absolute residual $0.587$ charge units (including exact $\Delta Z = 0$ on $A = 4, 12, 16, 56, 120$).

Per-element ground-state nuclear cluster formulas, electronic shells, binding energies per nucleon, and neutral atomic masses for all $118$ elements ($Z = 1\text{--}118$) appear in [knot-periodic table of the elements](#prose:knot-periodic-table).
