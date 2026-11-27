# Pre-Registration: Non-Zero Unknot $0_1$ Neutrino Mass Lift, Sweedler Weak See-Saw Scaling, & Dirac vs Majorana Framing (`qou-nu01`)

Beans: `qou-nu01`, `qou-qydm`, `qou-sm8w` (`Q-Gap-10`).
Lean companion: `folio/quantum-observable-universe/lean/QOU/StandardModel/NeutrinoUnknotSweedlerMassLift.lean`.

Written and committed **strictly prior** to running any numerical evaluation at $q_0$.

## 1. Fixed Substrate Inputs (`NO FITTING EXCEPT CAL-1/2/3`)

- **Working precision:** `mpmath` `workdps = 80` (`_precision.set_compute_dps()`, zero `float64` on any computation or witness path).
- **Substrate pin:** Proton anchor `q_0 = q_at(80)` (`q0Anchor = "proton"`), with $\hbar_q = 1 - q_0^{-1}$, $h_0 = q_0 - q_0^{-1}$, and single Sweedler weak-passage amplitude factor $s_0 = q_0 h_0 = q_0^2 - 1$ (`SweedlerWeakDegreeCount.singlePassageAmp_eq`).
- **Mass anchor (CAL-1):** Electron mass `m_e` (`M_E_MEV_STR` from `qou_substrate.constants`, converted to $\mathrm{eV}$ via exact $10^6$).
- **Derived proton mass:** `m_p(q_0)` from the exact Borromean substrate identity solved by `q_at(80)` (`derived_mp_mev(q_0, m_e, dps=80)`).
- **Derived electroweak vev ratio $N_v(q_0) = v_{\mathrm{EW}}(q_0) / m_p(q_0)$:** Unique root in $(0, 2/T_{\mathrm{EW}})$ of the Bring–Schwinger cubic (`ElectroweakVevFixedPointDecomposition.ewShapeCubic_existsUnique_root`)
  $$\frac{1}{\alpha_v} = q_0 \frac{[2]_{q_0}}{2}[4]_{q_0}[6]_{q_0}[8]_{q_0} + \frac{1}{\pi} - \alpha_v \frac{[2]_{q_0}}{8\pi}\bigl(1 - \hbar_q^2 \alpha_v\bigr), \qquad N_v(q_0) = \frac{1}{\alpha_v(q_0)}, \quad v_{\mathrm{EW}}(q_0) = N_v(q_0) m_p(q_0).$$
- **Derived electromagnetic and weak couplings:**
  - $\alpha_{\mathrm{EM}}(q_0)$ solving $\alpha_{\mathrm{EM}}^{-1} = q_0 [9]_{q_0}[10]_{q_0} + \frac{2}{3\pi} + \alpha_{\mathrm{EM}} \frac{[2]_{q_0}}{8\pi}(1 - \hbar_q^2 \alpha_{\mathrm{EM}})$.
  - Parameter-free substrate Weinberg ratios from `TorusLinkElectroweakSchurRatio.lean`:
    1. Irrep-weighted Wenzl–Higman Schur `M4` on $(T(2,4) \in H_2, T(3,5) \in H_3)$: $\sin^2\theta_W^{\mathrm{M4}}(q_0) = 1 - \bigl(\mathcal{M}_4(T_{2,4}) / \mathcal{M}_4(T_{3,5})\bigr)^2$, giving $\alpha_W^{\mathrm{M4}}(q_0) = \alpha_{\mathrm{EM}}(q_0) / \sin^2\theta_W^{\mathrm{M4}}(q_0)$.
    2. Same-rank torus-link pair $(T(2,4), T(2,6)) \subset H_2(q_0)$: $\sin^2\theta_W^{24/26}(q_0) = 1 - \bigl(\mathrm{tr}_M^D(\beta_{2,4}) / \mathrm{tr}_M^D(\beta_{2,6})\bigr)^2$, giving $\alpha_W^{24/26}(q_0) = \alpha_{\mathrm{EM}}(q_0) / \sin^2\theta_W^{24/26}(q_0)$.
- **Weak vertex $T(3,5)$ Convention-D Markov trace (`WeakVertexT35.weakVertexTrace`):**
  $$W_{T(3,5)}(q_0) = \frac{q_0^2 (q_0^{12} + q_0^8 - 1)}{(q_0^2 + 1)^2}.$$

## 2. Pre-Registered Zero-Parameter Candidate Families for $m_\nu(q_0)$

Because `ParticleKnots.Neutrino` assigns the neutrino the unknot $0_1$ with $\mathrm{Vol}(0_1) = 0$ (`volumeMass me 0 rho hbar = 0`), any nonzero mass scale must arise outside the hyperbolic volume–density chain (`neutrino_mass_volume_exclusion.py`). On the 2-state lepton doublet $(0 = \nu_L, 1 = e_L^-)$, the charged-current self-energy sandwich $E \cdot \mathrm{diag}(0, m_e) \cdot F = m_e E_{00}$ projects strictly onto the neutral $\nu_L$ slot even when $m_\nu^{\mathrm{tree}}(0_1) = 0$, while Sweedler's order-4 antipode ($S^2(X) = -X$) and unbroken $(2T_3, Y)$ forbid a bare $\Delta L = 2$ bilinear and select either a $\Delta L = 0$ Dirac mass on $\mathbb{Z}$-framed $(0_1, \pm 1)$ or the quadratic dimension-5 Weinberg singlet $\mathcal{O}_W = \varepsilon(L, H)^2$.

We pre-register four zero-parameter scale families:

1. **Family A — Pure Sweedler Weak-Jet Suppression Powers ($k \in \{8, 10, 12, 14, 16\}$):**
   $$m_{\nu,\mathrm{A}}^{(k)}(q_0) = m_e \cdot (q_0^2 - 1)^k.$$
2. **Family B — Two-Vertex $T(3,5)$ Weak Self-Energy Dressed Sweedler Powers ($k \in \{8, 10, 12, 14, 16\}$):**
   $$m_{\nu,\mathrm{B}}^{(k)}(q_0) = m_e \cdot W_{T(3,5)}(q_0)^2 \cdot (q_0^2 - 1)^k.$$
3. **Family C — Dimension-5 Weinberg See-Saw Scales $v_{\mathrm{EW}}(q_0)^2 / M_{\mathrm{UV}}(q_0)$ (Zero Hand-Picked Scales):**
   - **C-Sw (`2m` Sweedler inverse ladder, $2m \in \{16, 18, 20, 22\}$):** $M_{\mathrm{UV}}(q_0) = m_p(q_0) / (q_0^2 - 1)^{2m} \implies m_\nu = \frac{v_{\mathrm{EW}}(q_0)^2}{m_p(q_0)} (q_0^2 - 1)^{2m} = N_v(q_0)^2 m_p(q_0) (q_0^2 - 1)^{2m}$.
   - **C-Nv ($N_v$-tower powers, $r \in \{5, 6, 7, 8\}$):** $M_{\mathrm{UV}}(q_0) = m_p(q_0) N_v(q_0)^r \implies m_\nu = m_p(q_0) N_v(q_0)^{2 - r}$.
   - **C-Exp (non-perturbative Schwinger/Planck-like $\exp(1/(2\alpha_{\mathrm{EM}}))$):** $M_{\mathrm{UV}}(q_0) = m_e \exp\bigl(1 / (2\alpha_{\mathrm{EM}}(q_0))\bigr) \implies m_\nu = v_{\mathrm{EW}}(q_0)^2 / M_{\mathrm{UV}}(q_0)$.
4. **Family D — Radiative 2-Loop $(\alpha_W(q_0) / \pi)^2 m_e (q_0^2 - 1)^k$ Scales:**
   Evaluated for both $\alpha_W^{\mathrm{M4}}(q_0)$ and $\alpha_W^{24/26}(q_0)$ across $k \in \{8, 10, 12, 14, 16\}$ (primary pre-registered range) plus control exponents $k \in \{0, 2, 4, 6\}$ to test whether $(\alpha_W/\pi)^2$ compounds or double-counts the Sweedler $(q_0^2 - 1)^k$ weak loop suppression.

## 3. Pre-Registered 3-Generation $S_3 \supset S_2$ Splitting Ratios & Hierarchy Observables

In the 3-generation $S_3 \supset S_2$ neutral perturbation algebra $M_\nu(a, b, \epsilon) = a I_3 + b J_3 + \epsilon B_{12}$ with exact eigenvalues $(\lambda_1, \lambda_2, \lambda_3) = (a, a + 6\epsilon, a + 3b)$:
- **Minimal Normal Hierarchy (`NH`, $a = 0$, $m_1 = 0 < m_2 = 6\epsilon < m_3 = 3b$):**
  $\Delta m_{21}^2 / \Delta m_{31}^2 = (2\epsilon / b)^2$, $\Delta m_{21}^2 / \Delta m_{32}^2 = \frac{(2\epsilon/b)^2}{1 - (2\epsilon/b)^2}$, $\sum m_\nu = m_2 + m_3$.
  We pre-register the four zero-parameter deformation-step candidates for $2\epsilon / b$:
  $$\frac{2\epsilon}{b} \in \bigl\{q_0^2 - 1,\; (q_0^2 - 1)^2,\; \hbar_q,\; \hbar_q^2\bigr\}.$$
- **Minimal Inverted Hierarchy (`IH`, $m_3 = 0 < m_1 = a < m_2 = a + 6\epsilon$):**
  For matched atmospheric scale $m_2$ and solar ratio $r_{21} = \Delta m_{21}^2 / |\Delta m_{32}^2|$, $m_1 = m_2 \sqrt{1 - r_{21}}$, $\sum m_\nu^{\mathrm{IH}} = m_1 + m_2 > m_2 + m_3^{\mathrm{NH}\text{-matched}}$ (proved algebraically in Lean), and we record the implied $\sum m_\nu$ and TBM-benchmark $|m_{\beta\beta}|$ ($u_{e1}^2 = 2/3, u_{e2}^2 = 1/3, u_{e3}^2 = 0$) for every order-of-magnitude survivor ($1\;\mathrm{meV} \le m_{\mathrm{atm}} \le 200\;\mathrm{meV}$).

## 4. Post-Evaluation Empirical Comparison Boundary (Zero Fitting)

Strictly **after** computing all pre-registered substrate numbers at `80` dps, each candidate is compared against:
- **PDG-2024 oscillation parameters:**
  - $\Delta m_{21}^2 = 7.53 \times 10^{-5}\;\mathrm{eV}^2 \implies \sqrt{\Delta m_{21}^2} = 8.677557\ldots\;\mathrm{meV}$,
  - $|\Delta m_{32}^2| = 2.453 \times 10^{-3}\;\mathrm{eV}^2 \implies \sqrt{|\Delta m_{32}^2|} = 49.527770\ldots\;\mathrm{meV}$,
  - Ratio $\Delta m_{21}^2 / |\Delta m_{32}^2| = 0.030697105\ldots$
- **Planck 2018 + BAO cosmological bound:** $\sum m_\nu < 0.12\;\mathrm{eV}$.

**Reporting rule:** Every candidate in Families A–E is emitted in the witness JSON and console table — both natural order-of-magnitude hits (within $[0.2\times, 5\times]$ of $\sqrt{|\Delta m_{32}^2|}$ or $\sqrt{\Delta m_{21}^2}$) and multi-order-of-magnitude misses — with zero post-hoc pruning or parameter adjustment.
