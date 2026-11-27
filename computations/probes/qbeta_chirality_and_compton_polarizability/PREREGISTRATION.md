# Pre-registration: $Q_\beta$ Chirality Selection & $k \ge 1$ Cottingham–Compton `Ppos` Polarizability Probe (`qou-gtv6`)

Beans: `qou-gtv6`, `qou-qzvs` (`L2 1-ppQ` Gate 1 follow-up on PR `#9203` & `#9198`).
Written and committed prior to evaluating any signed 9-strand readout, $k \ge 1$ transient jet magnitude, or magnetic channel against experiment.

## 1. Fixed Derived & Calibration Inputs (Zero Fitted Parameters)

- Proton substrate pin: `q_0 = q_at(80)` (`q0Anchor = "proton"`, `workdps = 80`, zero `float64`).
- CAL-1 electron mass `m_e` (`M_E_MEV_STR`), QOU derived proton mass `m_p(q_0)` from the proton substrate identity, CAL-3 charged pion mass `m_pi = M_PI_PM_MEV_VALIDATION`.
- Form-B Bring-surface derived fine-structure coupling `alpha_q(q_0) = (q_0 [9]_{q_0} [10]_{q_0} + 2 / (3 pi))^-1`.
- Tower energy scale `E_0^full(q) / m_e = 1 / (q (q - 1) (1 - (1 - q^-1)^2))` and leading scale `E_0^(0)(q) / m_e = 1 / (q (q - 1))`.

## 2. Part A — Left-Coupled Crossing Chirality (`C2_neg` vs `C1_pos`) & Action Readout (`Log` vs `Linear`)

1. **Algebraic Chirality Selection on Left-Lepton $\otimes$ Right-Quark (`strands 5, 6`):**
   - By `WeightedTraceSide.rightTrace_R` / `rightTrace_Rinv`, placing the 6-strand $\gamma\gamma$ lepton block to the right of the 3-strand nucleon $V_{\mathrm{nuc}}^3$ yields a scalar Cartan weight $d_0 = d_1$ on the nucleon, leaving conditioned $Q_\beta$ identical to the isolated 3-strand bound $R(q) \le 3/4$. Non-scalar Cartan dressing therefore forces the $\gamma\gamma$ lepton block onto the **left** (`strands 0..5`) and the nucleon onto the **right** (`strands 6..8`).
   - On the boundary pair `(strand 5 = lepton, strand 6 = nucleon quark)` in basis `(00, 01, 10, 11)` (`0 = u / \nu`, `1 = d / e^-`), $\beta^-$ decay raises the right-hand nucleon quark $d_6 \to u_6$ while lowering the left-hand lepton strand $\nu_5 \to e^-_5$, i.e. $|0_5 1_6\rangle \mapsto |1_5 0_6\rangle$ ($F \otimes E$).
   - Test both strand-tracked boundary crossings $P \check{R}_+ = P \sigma_5$ (`C1_pos`) and $P \check{R}_- = P \sigma_5^{-1}$ (`C2_neg`) under the outgoing right-quark up projector $\Pi_{R,+} = (1 + G_{\mathrm{right}})/2$ and incoming left-lepton up projector $\Pi_{L,+} = (1 + G_{\mathrm{left}})/2$, and verify whether Sweedler's $H_4 \cong K[\mathbb{Z}/2] \ltimes \Omega^1_u$ (`G^2 = 1`, `X^2 = 0`, `X G = -G X`) lifts via `G \mapsto G_{\mathrm{right}}`, `X \mapsto -h(F \otimes E)` uniquely onto `C2_neg`.

2. **Logarithmic Action (`skein-binding-lagrangian.md`, Ruling 28) vs Linear Conditioned Trace (`R_cond`), Signed & Unsigned:**
   - Verify the algebraic additivity defect $\mathcal{E}_{\mathrm{aff}}(\tau_1 \tau_2) - \mathcal{E}_{\mathrm{aff}}(\tau_1) - \mathcal{E}_{\mathrm{aff}}(\tau_2) = E_0(\tau_1 - 1)(\tau_2 - 1)$ for affine-linear trace readouts on split product braids $W_{\mathrm{left}} \otimes W_{\mathrm{nuc}}$ vs exact spectator cancellation in $\mathcal{E}_{\log}(\tau) = -E_0 \ln |\tau|$.
   - Evaluate **signed** (not merely absolute-value) readouts across all left blocks `{bare_spectator, pair_std, pair_refl}` $\times$ boundary couplings `{C0_uncoupled, C1_pos, C2_neg, C3_clasp, C4_vertex}` symbolically as $q \to 1^+$ and numerically at 80 dps at $q_0$:
     - `F3C_signed`: $-E_0^{\mathrm{full}}(q) m_e \ln(\mathrm{tr}_{\mathrm{plain}, n}(W) / \mathrm{tr}_{\mathrm{plain}, p}(W))$ (Placement C, where the $(e^-, \nu)$ weight step cancels the $q^{\pm 1}$ nucleon cell per `BetaVertexBudget.lepton_cancels_cell`).
     - `F3B_signed`: $-E_0^{\mathrm{full}}(q) m_e \ln(\varepsilon_n^{(9)}(W) / \varepsilon_p^{(9)}(W)) - m_e$ (Placement B).
     - `F2_signed`: $+E_0^{\mathrm{full}}(q) m_e (\varepsilon_n^{(9)}(W) - \varepsilon_p^{(9)}(W)) / \tau_D^{(6)}(W_{\mathrm{left}})$ (linear conditioned trace).
   - **Pre-registered sign falsifier:** Determine whether `C2_neg` ($\sigma_5^{-1}$) vs `C1_pos` ($\sigma_5$) yields **positive** signed $Q_\beta^{\mathrm{F3C,signed}} > 0$ ($E_n > E_p$, spontaneous $\beta^-$ decay) or negative ($E_n < E_p$).

## 3. Part B — $k \ge 1$ `Ppos` Transient Jet & Magnetic Spin-Spin Channels in the Two-Term Action

Under QOU's derived quantum-trace two-term weighting $t_X(W_p) = q\,\mathrm{tr}(X_p V_p^3)/[2]_q^3$, $t_X(W_n) = q^{-1}\,\mathrm{tr}(X_n V_n^3)/[2]_q^3$:

1. **Covariant All-Pairs (`Q_pair = Q_12 + Q_23 + Q_13`) vs Adjacent (`Q_adj = Q_12 + Q_23`) Jet Decomposition:**
   - Separate the $k = 0$ static Coulomb part ($-\frac{1}{3}$ on `Q_pair`; $-\frac{2}{9} I_3$ on `Q_adj` neutron) from the $k \ge 1$ `Ppos` connected transient jet (vanishing at $q = 1$) on both the full 3D weight spaces $W_{p,n}$ (`O((q-1)^4)`) and the $I = 1/2$ nucleon-projected sector $e_{(2,1)} W_{p,n}$ (`O((q-1)^2)`).
   - Report exact per-unit-$c_{\mathrm{em}}$ values $\Delta t_X(q_0)$ and parameter-free MeV shifts at $c_{\mathrm{em}} \in \{1,\, \alpha_q(q_0),\, 1 - q_0^{-2},\, (q_0 - q_0^{-1})^2\}$ under both $m_e$ and $E_0^{\mathrm{full}}(q_0) m_e$ scales.
2. **Pointlike Nucleon Dipole ($\mu_n^2 - \mu_p^2$) vs Constituent-Quark Magnetic Hyperfine ($-\sum_{i<j} q_i q_j \vec{\sigma}_i \cdot \vec{\sigma}_j$):**
   - Contrast the negative pointlike Cottingham magnetic dipole difference ($\mu_n^2/\mu_p^2 - 1 = -5/9 < 0$ in $SU(6)$, $([2]_{q_0}/[3]_{q_0})^2 - 1 < 0$ in $SU_q(6)$) with the positive $SU(6)$ $56$-plet constituent-quark Breit–Fermi spin-spin matrix element $\langle -\sum_{i<j} q_i q_j (\vec{\sigma}_i \cdot \vec{\sigma}_j) \rangle_{n - p} = (-1) - (-4/3) = +1/3 > 0$, evaluating both at the QOU derived pion/Compton magnetic recoil scales at 80 dps.

CODATA $Q_\beta$ and $\Delta m_{np}$ are recorded strictly for post-computation comparison; zero parameters are fitted or selected.
