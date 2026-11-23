# Pre-registration: 5-Layer Iterated Confinement Tower, Adiabatic Gap Ratios & Toric Chemical Stoichiometry Probe (`qou-5lct` / `Q-Gap-0`)

Bean: `qou-5lct` (`Q-Gap-0`).
Written and committed prior to running any 80-dps numerical evaluation or Graver / Universal Gröbner enumeration.

## 1. Questions Tested

1. **Adiabatic Confinement Hierarchy (`L_0 -> L_1 -> L_2 -> L_3 -> L_4`):**
   Each layer `L_k` solves a constrained discrete optimization over `ker(A_k)` with unperturbed intra-layer break-up gap `Delta_k > 0`, promoting its confined motifs into the elementary column alphabet of `L_{k+1}`, where residual cross-motif interactions perturb move costs by `||V_{k+1}||`. By the hierarchical gap-stability bound (`hierarchical_confinement_of_gap_gt_perturbation`), no `L_k` motif breaks apart inside `L_{k+1}` whenever the adiabatic ratio
   $$\eta_k := \frac{\|V_{k+1}\|}{\Delta_k} < 1,$$
   whereas external chemical potential / Fermi pressure driving `-\delta V(g) > \Delta_k` (`\eta_k > 1`) triggers a cross-layer binomial rewrite (`cross_layer_flip_of_perturbation_gt_gap`).

2. **Layer-3 Shadow Prices (`chi_Mulliken`, `eta_PP`) and Noble-Gas Shell Closures:**
   For discrete electron-count ground-state energy `E(N)` around neutral atom `N = Z`, the right and left LP shadow slopes `\mu_+(N) = E(N+1) - E(N) = -A_{\mathrm{ea}}(N)` and `\mu_-(N) = E(N) - E(N-1) = -I(N)` satisfy `2 \chi_{\mathrm{M}}(N) = -(\mu_+(N) + \mu_-(N))` and `\eta_{\mathrm{PP}}(N) = \mu_+(N) - \mu_-(N) = E(N+1) - 2E(N) + E(N-1) \ge 0` under Perdew-Parr-Levy-Balduz discrete convexity, peaking at cumulative `2n^2` closures `[2, 10, 18, 36, 54, 86]`.

3. **Layer-4 Toric / Diophantine Stoichiometry (`ker_Z(A_chem)`, Graver & Universal Gröbner Bases, Birch Equilibrium):**
   Freezing Layer-2 nuclear species (`\eta_2 \sim 10^{-6} \ll 1`) turns elemental conservation into the integer matrix `A_{\mathrm{chem}} \in \mathbb{Z}^{E \times M}`. Balanced reactions `v = \nu_+ - \nu_- \in \ker_{\mathbb{Z}}(A_{\mathrm{chem}})` correspond bijectively to pure toric binomials `x^{\nu_+} - x^{\nu_-} \in I_{A_{\mathrm{chem}}}`, Hess's law holds as LP reduced-cost invariance along fibers `A_{\mathrm{chem}} u = b`, zero-temperature enthalpy minimization reduces via Sturmfels-Thomas test sets, and finite-`T` mass-action detailed balance cuts out a unique positive equilibrium `x^* \in \mathbb{R}_{>0}^M` in each stoichiometric compatibility class `A_{\mathrm{chem}} x = b` (Birch's theorem).

## 2. Pre-Registered 80-dps Layer Scales (`q0Anchor = "proton"`, Zero Fitted Parameters)

Evaluated at `mp.dps = 80` from `CAL-1` (`M_E_MEV`), `q_0 = q_at(80)` (proton substrate pin), QOU substrate formulas, and clearly separated NIST CODATA-2022 / AME validation references:

- **`L_0 -> L_1` (Ribbon-braid substrate -> Colour-singlet hadrons):**
  `Delta_0 = m_p(q_0)` (Borromean `V^3` confinement scale) vs QED radiative intra-hadron perturbation `||V_1||_{QED} = \alpha m_p(q_0)` (`\eta_0 = \alpha \approx 7.297 \times 10^{-3}`).
- **`L_1 -> L_2` (Hadrons -> Bound atomic nuclei):**
  `Delta_1 = m_p(q_0)` (and comparison `m_\pi`) vs nuclear binding per nucleon `||V_2|| = B({}^4\mathrm{He})/4` (`7.073915 MeV`, validation) and `B({}^{12}\mathrm{C})/12` (`7.680144 MeV`), testing `\eta_1 \sim 10^{-2}` (EMC regime, no quark deconfinement).
- **`L_2 -> L_3` (Bound nuclei -> Neutral atoms & valence shells):**
  `Delta_2 = B({}^{12}\mathrm{C})/12` (nuclear separation scale) and weak transmutation threshold `\Delta_{np} = m_n - m_p = m_e + Q_\beta` (both QOU-derived `m_e + Q_\beta^{\mathrm{QOU}}(q_0)` and CODATA validation `M_N_MEV_VALIDATION - M_P_MEV_VALIDATION = 1.29333236 MeV`) vs atomic Rydberg scale `||V_3|| = \mathrm{Ry} = \frac{1}{2}\alpha^2 m_e \approx 13.605693\text{ eV}`, testing `\eta_2 \sim 10^{-6}` at ambient density and exact cross-layer flip `E_{F,e}^* = \Delta_{np}` (`\eta_2 = 1`) in neutron-star outer crusts (`n_e^* = (p_{F,e}^* / \hbar c)^3 / (3\pi^2)`).
- **`L_3 -> L_4` (Closed-core atoms -> Covalent molecules & thermal reaction networks):**
  Core-shell vs covalent perturbation (`\Delta_{3,\mathrm{core}} = Z_{\mathrm{eff}}^2 \mathrm{Ry}` for `C 1s` vs covalent bond scale `||V_4||_{\mathrm{cov}} \sim \frac{1}{3}\mathrm{Ry}`) and covalent vs ambient thermal perturbation (`k_B T_{298.15\,\mathrm{K}} / \mathrm{Ry}` and intermolecular dispersion / H-bond scale vs `\mathrm{Ry}`), testing `\eta_3 \sim 10^{-2}`.

## 3. Pre-Registered Exact Diophantine & Toric Chemical Benchmarks

1. **Four 1D-Kernel Canonical Stoichiometric Circuits (`ker_Z` rank 1, primitive `gcd = 1`):**
   - Water synthesis `(H2, O2, H2O)`: `A = [[2,0,2],[0,2,1]]` -> `v = (-2, -1, 2)`.
   - Methane combustion `(CH4, O2, CO2, H2O)`: `A = [[1,0,1,0],[4,0,0,2],[0,2,2,1]]` -> `v = (-1, -2, 1, 2)`.
   - Haber-Bosch ammonia `(N2, H2, NH3)`: `A = [[2,0,1],[0,2,3]]` -> `v = (-1, -3, 2)`.
   - Glucose respiration `(C6H12O6, O2, CO2, H2O)`: `A = [[6,0,1,0],[12,0,0,2],[6,2,2,1]]` -> `v = (-1, -6, 6, 6)`.

2. **Multi-Reaction `3 x 7` C-H-O Network `(C, H2, O2, CO, CO2, H2O, CH4)`:**
   - `A_CHO = [[1,0,0,1,1,0,1], [0,2,0,0,0,2,4], [0,0,2,1,2,1,0]]` (`rank = 3`, `dim ker_Z = 4`).
   - Compute exact Smith Normal Form (`diag(1, 2, 2)` torsion check / saturation of `ker_Z`), Hermite Normal Form, all elementary circuits, the complete Graver basis `G(A_CHO)`, and the Universal Gröbner Basis `UGB(I_{A_CHO})`.
   - Verify Sturmfels-Thomas Gröbner normal-form reduction to the exact LP/IP optimum on fixed inventory `b = (2, 8, 4)` (`2 C + 4 H2 + 2 O2`) under standard molar enthalpy ordering (comparison enthalpy vector, testing reduced-cost fiber invariance `c^T(u - v) = \bar{c}^T(u - v)`).
   - Solve the 80-dps finite-`T` Birch mass-action system `\ln x - \ln x_0 \in \mathrm{rowspace}(A_{\mathrm{CHO}})`, `A_{\mathrm{CHO}} x = b` via Newton iteration in log-dual potentials `y \in \mathbb{R}^3` (`x_j(y) = \exp((A_{\mathrm{CHO}}^T y)_j - g_j / RT)`), verifying strictly convex dual Hessian `A_{\mathrm{CHO}} \mathrm{diag}(x) A_{\mathrm{CHO}}^T \succ 0`, `||A_{\mathrm{CHO}} x^* - b||_\infty < 10^{-70}`, and `|x^{*\nu_+} - K_{\mathrm{eq}} x^{*\nu_-}| < 10^{-70}` across every Graver circuit!

## 4. Acceptance Criteria

- Zero `float64` anywhere (`probe-float64-guard.py --strict --diff` exit 0).
- Exact symbolic/integer certificates (`tolerance = 0`) for all SNF/HNF, circuit, Graver, and Gröbner identities; `< 10^{-70}` residual on 80-dps Birch equilibrium and neutron-star threshold equations.
