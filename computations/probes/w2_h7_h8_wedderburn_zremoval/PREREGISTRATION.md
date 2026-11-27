# Pre-Registration: All-`q` `H_7(q), H_8(q)` Two-Row Wedderburn Cross-Nucleon Pair Identities, Coideal Killing-Norm Hypercharge Slope `1/2`, & Separated-Hadron `Z`-Channel Removal (`W2`: `qou-20sx`, `qou-vudb`, `qou-fbrp`)

Beans: `qou-20sx`, `qou-vudb`, `qou-fbrp` (Workstream `W2`).
Lean companion: `folio/quantum-observable-universe/lean/QOU/QBeta/CrossNucleonPairWedderburnZRemoval.lean`.
Written and committed prior to running any `80`-dps probe evaluation.

---

## 1. Fixed Zero-Parameter & Calibration Inputs (`workdps = 80`, `q0Anchor = "proton"`)

- **Substrate anchor:** `q_0 = q_at(80)` solved at `80` decimal digits from the proton substrate identity (`qou_substrate.constants`), with `h_0 = q_0 - q_0^-1`, Convention-D Markov parameter `z_D = q_0^3 / (q_0^2 + 1)`, and inverse-crossing Markov parameter `z_D_bar = z_D - h_0 = 1 / (q_0 (q_0^2 + 1))`.
- **Derived EM coupling & lepton/pion scales:** Form-B Bring-surface coupling `alpha_q(q_0) = (q_0 [9]_{q_0} [10]_{q_0} + 2 / (3 pi))^-1`, CAL-1 `m_e` (`M_E_MEV_STR`), exact SI-2019 `h, c, e` (`qou_substrate.codata`) defining `hbar * c` in `MeV * fm`, and pion mass benchmarks `m_{pi^+-}` (`M_PI_PM_MEV_VALIDATION`), `m_{pi^0}` (`M_PI_0_MEV_VALIDATION`), and isospin average `m_{pi_bar} = (2 m_{pi^+-} + m_{pi^0}) / 3`.
- **Electroweak `Z`-scale comparison benchmarks (zero fitting):**
  1. PDG `Z`-pole validation benchmark `M_Z = 91187.6 MeV` at pion Compton separations `r_{pi^+-} = hbar c / m_{pi^+-}`, `r_{pi_bar} = hbar c / m_{pi_bar}`, `r_{pi^0} = hbar c / m_{pi^0}`, and nominal nuclear pion spacing `r = 1.418 fm` (`M_Z r / (hbar c) approx 655`).
  2. Tree-level electroweak comparison scales from `G_F` (`codata("Fermi coupling constant")`) + `alpha_q(q_0)` at unrenormalized `sin^2 theta_W^0 = 3/8` (`qou-fbrp`) and NIST on-shell `sin^2 theta_W` (`codata("weak mixing angle")`).

---

## 2. Pre-Registered Analytical Predictions & Falsification Criteria (`tol = 1e-75 .. 1e-78` at `80 dps`)

### P1 — Convention-D Radical Truncation & Two-Row Catalan Block Reduction (`H_7(q_0), H_8(q_0)`)
1. On `H_7(q_0)` (`7! = 5,040`, `p(7) = 15`), all `11` partitions with `ell(lambda) >= 3` satisfy `ocneanuWeight(q_0, z_D, lambda) = 0` identically, leaving only the `4` two-row blocks `lambda in {(7,0), (6,1), (5,2), (4,3)}` of ballot dimensions `(1, 6, 14, 14)` (`sum d_lambda^2 = 429 = C_7`).
2. On `H_8(q_0)` (`8! = 40,320`, `p(8) = 22`), all `17` partitions with `ell(lambda) >= 3` satisfy `ocneanuWeight(q_0, z_D, lambda) = 0` identically, leaving only the `5` two-row blocks `lambda in {(8,0), (7,1), (6,2), (5,3), (4,4)}` of ballot dimensions `(1, 7, 20, 28, 14)` (`sum d_lambda^2 = 1,430 = C_8`).
3. Every two-row Ocneanu weight satisfies the closed quantum-multiplicity identity
   `ocneanuWeight(q_0, z_D, (N - k, k)) = [N - 2k + 1]_{q_0} / (q_0 + q_0^-1)^N`
   and normalized trace sum `sum_{k=0}^{floor(N/2)} d_{(N-k, k)} w_{(N-k, k)}(q_0, z_D) = 1` to `< 10^-78`.

### P2 — Exact Hoefsmit Seminormal Character Traces Across `pp`, `pn`, `nn` Cross-Cluster Dressings
1. Square-root-free Hoefsmit seminormal generator matrices `rho_lambda(sigma_i)` (`d_lambda <= 28`) satisfy Hecke quadratic, braid, and far-commutation relations to `< 10^-78` across all two-row blocks of `H_7(q_0)` and `H_8(q_0)`.
2. For two Borromean nucleon cores `C_A, C_B` dressed by `pp` (`sigma`), `nn` (`sigma^-1`), `pn` (`(sigma + sigma^-1)/2`), and double-crossing monodromy (`sigma^2`) across `L7e`, `L7s`, `L8e`, `L8s`, the weighted two-row Hoefsmit character sums `sum_{ell(lambda) <= 2} w_lambda(q_0, z_D) Tr(rho_lambda(W_tau))` match the closed rational Markov-stabilization formulas in `z_D`, `z_D_bar`, and `tr_M(beta_Bor) = (4 + h_0^2 - 3 h_0^4 - h_0^6)/(h_0^2 + 4)` to `< 10^-78`.
3. Under symmetric `pn` bond averaging, the skein cross-cluster split satisfies `pp - nn != 0` while `pp - 2 pn + nn = 0` to `< 10^-78` (purely isovector, zero `Q_A Q_B` Coulomb curvature; `qou-vudb`).

### P3 — Sector-Projected `(pp, pn, np, nn)` Readouts & Iterated Left/Right Chain Factorization
1. Right-spectator stabilization (`L7e`, `L8e`) collapses by exact scalars `q_0^{+- 2m}` (`Delta E^{(7)} = z_D^{(+-)} Delta E^{(6)}`, `Delta E^{(8)} = z_D^{(eps_5)} z_D^{(eps_6)} Delta E^{(6)}`), preserving the rational six-strand pair parameters `(alpha_6(q_0), beta_6(q_0))` with `alpha_6(q_0) + beta_6(q_0) = 1` and `beta_6(q_0) = alpha_6(q_0^-1)` to `< 10^-78`.
2. Between-spectator left chains (`L7s`, `L8s`) collapse on the leading strand of block `B` to the rank-2 diagonal weight-counting operator `L_m(q_0) = I_2 + (q_0^2 + 1)(q_0^{2m-2} - q_0^-2) E_{00}`, obeying the exact linear dependence `L_2(q_0) = (q_0^2 + 1) L_1(q_0) - q_0^2 I_2`, pinning `alpha_8(q_0) = alpha_7(q_0) = alpha_6(q_0) != 0`, and excluding `1 : 0 : 0` Coulomb on Hecke insertions to `< 10^-78`.

### P4 — Coideal Killing-Norm Hypercharge Slope `1/2` & `Z`-Channel Yukawa Removal (`lambda(r_pi) < 10^-280`)
1. Traceless `su(5)` centralizer on `F = V_2 (+) W_3^*` fixes `y_3 = -(2/3) y_2`, `Tr_F((2 T_3)^2) = 2` (`Tr_G(T_3^2) = 2`), `Tr_F((Y/2)^2) = 5/6` (`Tr_G((Y/2)^2) = 10/3`), unrenormalized Weinberg ratio `3/8`, and Gell-Mann-Nishijima slope `alpha_Y = 1/2` (`(q_u, q_d) = (2/3, -1/3)`).
2. Evaluating `CoulombNeedsZRemoval.exch(g^2, g'^2, lambda(r), T_3, T_3')` at `lambda(r_pi) = exp(-M_Z r_pi / (hbar c))` yields `M_Z r_pi / (hbar c) > 650` and `0 < lambda(r_pi) < 10^-280` across all pion Compton benchmarks (`pi^+-`, `pi_bar`, `pi^0`, and `1.418 fm`), suppressing `|pn - nn| / e^2`, `|nn| / e^2`, and `|(pp - e^2) / e^2|` below `10^-280` and isolating `pp : pn : nn = 1 : 0 : 0` to `> 280` decimal digits.
