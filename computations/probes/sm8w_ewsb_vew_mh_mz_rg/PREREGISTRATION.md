# Pre-Registration: Electroweak VEV $v_{\mathrm{EW}}$, Higgs Quartic $m_H$, Sweedler $(q_0^2 - 1)^8$ Weak Suppression, and UV-to-$M_Z$ RG Threshold Running (2026-11-23)

Bean `qou-ewsb` (Epic `qou-sm8w`, `Q-Gap-9`). Written and committed **before** running any numerical evaluation.

## 1. Anti-Fit & Precision Discipline (`NO FITTING EXCEPT CAL-1/2/3`)

- **Working precision:** `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized), zero `float64` imports, literals, or casts.
- **Canonical substrate anchor:** `q0Anchor = "proton"` (`q0 = qou_substrate.constants.q_at(80)`), giving $h_0 = q_0 - q_0^{-1}$, $\hbar_{q_0} = 1 - q_0^{-1}$, and balanced quantum integers $[k]_{q_0} = (q_0^k - q_0^{-k})/h_0$.
- **Calibration inputs (strictly CAL-1/2/3 + Form-B $\alpha_q$):**
  - CAL-1: $m_e$ (`codata("electron mass energy equivalent in MeV")`),
  - Proton validation / `q0` pin: $m_p$ (`codata("proton mass energy equivalent in MeV")`),
  - CAL-3: $m_{\pi^\pm} = 139.57039\;\mathrm{MeV}$,
  - Form-B Bring–Schwinger $\alpha_q^{-1}(q_0)$ (`solve_form_b_alpha_inv(q0)`, zero CODATA $\alpha_{\mathrm{EM}}$ input),
  - Exact Catalan's constant $G = \mathrm{Cl}_2(\pi/2) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)^2}$ (`mp.catalan` at 80 dps, cross-checked against the certified 24-term partial sum $102476291858462752 / 111983464450883025$ in `QOU/Knot/CatalanValueBounds.lean`).
- **Empirical comparison targets (PDG-2024 / CODATA-2022, comparison boundary ONLY — never used to fit any QOU coefficient):**
  - $G_F = 1.1663787(6)\times 10^{-5}\;\mathrm{GeV}^{-2} \implies v_{\mathrm{EW}} = (\sqrt{2}\,G_F)^{-1/2} = 246.219650794(63)\;\mathrm{GeV}$,
  - $M_W = 80.3692(133)\;\mathrm{GeV}$, $M_Z = 91.1876(21)\;\mathrm{GeV}$,
  - $m_H = 125.20(11)\;\mathrm{GeV} \implies \lambda_H^{\mathrm{PDG}} = \frac{m_H^2}{2\,v_{\mathrm{EW}}^2}$,
  - $\sin^2\theta_W(M_Z)_{\overline{\mathrm{MS}}} = 0.23122(4)$, $\alpha_{\mathrm{EM}}^{-1}(M_Z)_{\overline{\mathrm{MS}}} = 127.951(9)$, $\alpha_s(M_Z) = 0.1180(9)$.

---

## 2. Pre-Registered Evaluations

### Part A — Sweedler $(q_0^2 - 1)^k$ Weak Ladder vs Bring–Schwinger $v_{\mathrm{EW}}$ Bridge, $M_W, M_Z$, and Higgs Quartic $\lambda_H$ ($m_H$)

1. **Sweedler $(q_0^2 - 1)^k$ Weak Suppression (`SweedlerWeakDegreeCount.lean`, `#9204`) vs $G_F = \frac{1}{\sqrt{2}\,v_{\mathrm{EW}}^2}$:**
   With single-passage amplitude $\mathcal{A}_1(q_0) = q_0(q_0 - q_0^{-1}) = q_0^2 - 1$:
   - **S1 (4-hop squared-rate identification, `#9204`):** $G_F m_p^2 = (q_0^2 - 1)^8 \iff \frac{v_{\mathrm{EW}}}{m_p} = 2^{-1/4}(q_0^2 - 1)^{-4}$, alongside unnormalized $N_v^{\mathrm{S1,bare}} = (q_0^2 - 1)^{-4}$.
   - **S2 (2-vertex $W$-exchange rate $(q_0^2 - 1)^4 \iff v_{\mathrm{EW}} / m_{\mathrm{model}} \propto (q_0^2 - 1)^{-2}$):**
     Evaluated at $G_F m_{\mathrm{model}}^2 = (q_0^2 - 1)^4 \iff v_{\mathrm{EW}} = 2^{-1/4} m_{\mathrm{model}} (q_0^2 - 1)^{-2}$ (and bare $m_{\mathrm{model}}(q_0^2 - 1)^{-2}$) across all three canonical substrate mass scales:
     * (S2a) Proton scale $m_{\mathrm{model}} = m_p$,
     * (S2b) CAL-3 pion scale $m_{\mathrm{model}} = m_{\pi^\pm}$,
     * (S2c) Full lepton/baryon tower scale $m_{\mathrm{model}} = E_0^{\mathrm{full}} = \frac{m_e}{q_0(q_0 - 1)(1 - \hbar_{q_0}^2)}$ and muon-unit scale $E_0^\mu = \frac{m_e}{(q_0 - 1)^2}$.
   - **S3 (Reconciliation with `ElectroweakBringSchwingerBridge` & `ElectroweakVevGaps.su2_coupling_not_selfConsistent`):**
     Compare the conditional self-consistent Bring–Schwinger cubic root $N_v^{\mathrm{BS}} = 1/\alpha_v^*$ (`1/α_v = T_EW(q_0) - α_v H(q_0)(1 - ℏ_{q_0}^2 α_v)`) against inserting the parameter-free Sweedler loop couplings $\kappa_{\mathrm{S1,bare}} = (q_0^2 - 1)^4$ and $\kappa_{\mathrm{S1,Fermi}} = 2^{1/4}(q_0^2 - 1)^4$ directly into $N(\kappa) = T_{\mathrm{EW}}(q_0) - \kappa H(q_0)(1 - \hbar_{q_0}^2 \kappa)$. Verify $\kappa_{\mathrm{S1}} < 1/30$ (avoiding the $\alpha_2 > 1/30$ contradiction of `su2_coupling_not_selfConsistent`) and report the exact shift $N(\kappa_{\mathrm{S1}}) - N_v^{\mathrm{BS}}$ in ppb alongside the tree-level ratio $N_v^{\mathrm{BS}} / (q_0^2 - 1)^{-4}$.

2. **Electroweak Boson Masses ($M_W, M_Z$) and Higgs Mass / Quartic ($m_H, \lambda_H = \frac{m_H^2}{2 v_{\mathrm{EW}}^2}$):**
   - Torus-link Plancherel polynomials $P_2(h_0), P_3(h_0), P_4(h_0)$ for $\{W = T(2,4), Z = T(2,6), H = T(2,8)\}$ and dressed ratio $(M_Z / M_W)_{\mathrm{torus}} = \frac{P_3(h_0)}{P_2(h_0)}\bigl(\frac{[2]_{q_0}}{2}\bigr)^2$, giving on-shell $\sin^2\theta_W^{\mathrm{torus}} = 1 - (M_W / M_Z)_{\mathrm{torus}}^2$.
   - Absolute $M_W, M_Z$ predictions from $M_W = \frac{e(M_Z)}{2 \sin\theta_W} v_{\mathrm{EW}}$ combining $(v_{\mathrm{EW}}^{\mathrm{BS}}, v_{\mathrm{EW}}^{\mathrm{S1}})$ with both (i) torus $\sin^2\theta_W^{\mathrm{torus}}$ and (ii) RG-evolved $\sin^2\theta_W(\mu)$ from Part B.
   - Higgs mass $m_H$ and implied tree-level quartic $\lambda_H = \frac{m_H^2}{2 v_{\mathrm{EW}}^2} > 0$ evaluated with exact 80-dps `mp.catalan` (replacing the remediated decimal literal in `HiggsCategoricalMassFormula.lean`) across:
     * (H0) Undressed Borromean-$2G$ formula $m_H = M_W \frac{P_4(h_0)}{P_2(h_0)} \frac{6}{5}(1 - 2 G h_0^4)$,
     * (H1) `[2]_{q_0}/2`-dressed tree formula $m_H = M_W \frac{P_4(h_0)}{P_2(h_0)} \frac{6}{5} \frac{[2]_{q_0}}{2}$,
     * (H2) Dressed Borromean-$2G$ formula $m_H = M_W \frac{P_4(h_0)}{P_2(h_0)} \frac{6}{5} \frac{[2]_{q_0}}{2}(1 - 2 G h_0^4)$,
     * (H3) Dressed Bring zero-mode formula $m_H = M_W \frac{P_4(h_0)}{P_2(h_0)} \frac{6}{5} \frac{[2]_{q_0}}{2}\bigl(1 - \frac{2}{3\pi}\hbar_{q_0}^2\bigr)$.

### Part B — Zero-Parameter 1-Loop & 2-Loop SM RG Threshold Running ($\sin^2\theta_W(M_Z)_{\overline{\mathrm{MS}}}$, $\alpha_s(M_Z)$)

1. **Exact Rational Beta Coefficients ($N_{\mathrm{gen}} = 3, N_H = 1$, $\mathrm{SU}(5)$ / Split-Bundle $F = V_2 \oplus W_3^*$ Normalization $\alpha_1 = \frac{5}{3}\alpha_Y$, $\sin^2\theta_W^0 = \frac{3}{8}$):**
   - 1-loop slopes in $\frac{d\alpha_i^{-1}}{d\ln\mu} = -\frac{b_i}{2\pi}$:
     $$(b_1, b_2, b_3) = \left(\frac{41}{10},\; -\frac{19}{6},\; -7\right), \qquad b_{\mathrm{EM}} = \frac{5}{3}b_1 + b_2 = \frac{11}{3}, \qquad b_1 - b_2 = \frac{109}{15}.$$
   - 2-loop gauge-matter rational matrix $b_{ij}$ in $\frac{d\alpha_i^{-1}}{d\ln\mu} = -\frac{b_i}{2\pi} - \sum_{j=1}^3 \frac{b_{ij}}{8\pi^2}\alpha_j$:
     $$b_{ij} = \begin{pmatrix} \frac{199}{50} & \frac{27}{10} & \frac{44}{5} \\[3pt] \frac{9}{10} & \frac{35}{6} & 12 \\[3pt] \frac{11}{10} & \frac{9}{2} & -26 \end{pmatrix}$$
     (plus comparison with leading top-Yukawa 2-loop subtraction $\Delta\beta_{\alpha_i^{-1}}^{\mathrm{top}} = +\frac{c_i^{\mathrm{top}}}{8\pi^2}\alpha_t$ with $c^{\mathrm{top}} = (17/10, 3/2, 2)$ and tree-level top Yukawa $y_t = 1 \implies \alpha_t = 1/(4\pi)$).

2. **Pre-Registered Candidate UV-to-$M_Z$ Log-Ratios $L = \ln(\mu_{\mathrm{UV}} / M_Z)$ (Zero Free Parameters):**
   Starting from unified electroweak/GUT boundary $\sin^2\theta_W(\mu_{\mathrm{UV}}) = \frac{3}{8}$ (with $\alpha_{\mathrm{EM}}^{-1}(M_Z)$ evaluated both via QOU Form-B $\alpha_q^{-1}(q_0)$ evolved from $m_e \to M_Z$ by perturbative 1-loop SM fermion logs and via PDG $\alpha_{\mathrm{EM}}^{-1}(M_Z)_{\overline{\mathrm{MS}}} = 127.951$ as scheme reference):
   - **T1 (Sweedler 4-hop inverse):** $L_4 = -4\ln(q_0^2 - 1)$ ($\mu_{\mathrm{UV}}/M_Z = (q_0^2 - 1)^{-4}$),
   - **T2 (Sweedler 8-power rate inverse):** $L_8 = -8\ln(q_0^2 - 1)$ ($\mu_{\mathrm{UV}}/M_Z = (q_0^2 - 1)^{-8}$),
   - **T3 (Sweedler-Bring higher powers $k \in \{16, 20, 21, 22, 24\}$):** $L_k = -k\ln(q_0^2 - 1)$ for $k = 16$ (`2×8`), $k = 20$ (`lcm(4,5)` Bring face-index), $k = 21$, $k = 22$ (`SU(2) pure-gauge 22`), $k = 24$ (`4|χ(Σ_4)| = 24`),
   - **T4 (Bring / Kashaev geometric thresholds):**
     * (T4a) Kashaev modular S-dual exponent $L_{\mathrm{Kashaev}} = \pi / \hbar_{q_0}$,
     * (T4b) Quarter inverse fine-structure action $L_{\alpha/4} = \alpha_q^{-1}(q_0) / 4$,
     * (T4c) Bring Gauss–Bonnet area $L_{\mathrm{Bring}} = \mathrm{Area}(\Sigma_4) = 12\pi$.
   For every threshold T1–T4, evaluate BOTH 1-loop and 2-loop $\sin^2\theta_W(M_Z)$ and single-scale unified $\alpha_s(M_Z)$, AND report the exact inverse diagnostic $L_{\sin^2\theta_W}^*$ and minimal-SM 3-coupling triangle mismatch $(b_2 - b_3)\alpha_1^{-1} + (b_3 - b_1)\alpha_2^{-1} + (b_1 - b_2)\alpha_3^{-1} \neq 0$ honestly.

3. **Zero-Parameter Infrared QCD Dimensional-Transmutation Bridge $m_p / \Lambda_{\mathrm{QCD}} \to \alpha_s(M_Z)$:**
   Test all four natural parameter-free QOU infrared QCD scale candidates:
   - **Q1 (Sweedler single-passage scale):** $\Lambda_{\mathrm{Q1}} = m_p (q_0^2 - 1)$,
   - **Q2 (Hecke $h_0$ scale):** $\Lambda_{\mathrm{Q2}} = m_p (q_0 - q_0^{-1})$,
   - **Q3 (CAL-3 pion scale):** $\Lambda_{\mathrm{Q3}} = m_{\pi^\pm}$,
   - **Q4 (Habiro $\hbar_{q_0}$ scale):** $\Lambda_{\mathrm{Q4}} = m_p \hbar_{q_0}$,
   under both 1-loop $\alpha_s(M_Z) = \frac{2\pi}{\beta_0^{(5)}\ln(M_Z/\Lambda)}$ and 2-loop exact implicit RG $\ln\frac{M_Z}{\Lambda^{(5)}} = \frac{2\pi}{\beta_0^{(5)}\alpha_s} + \frac{\beta_1^{(5)}}{2(\beta_0^{(5)})^2}\ln\Bigl(\frac{\beta_0^{(5)}\alpha_s}{4\pi + (\beta_1^{(5)}/\beta_0^{(5)})\alpha_s}\Bigr)$ ($\beta_0^{(5)} = \frac{23}{3}$, $\beta_1^{(5)} = \frac{116}{3}$), reporting all hits and misses honestly.
