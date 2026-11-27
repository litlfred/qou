# Pre-Registration Index — Active Pre-Registered Probes

## W10 / `qou-awxv` Item 1 (`L_cal` Route 1): Self-Consistent Intra-Nucleon Borromean EM Self-Energy (`Δ_EM = α · m_model · f`, NO `m_π` Unit)

- **Beans:** `qou-awxv` (item 1), `qou-37y0`, `qou-mjo7`, `qou-pzsi`, `qou-17mq`, `qou-zp6a`, `qou-99qc`.
- **Canonical probe pre-registration:** [`computations/probes/w10_continuum_ecat_intranuc_em/PREREGISTRATION.md`](probes/w10_continuum_ecat_intranuc_em/PREREGISTRATION.md).
- **Lean companion:** `folio/quantum-observable-universe/lean/QOU/QBeta/ContinuumECatIntraNucleonEM.lean` (zero empirical inputs, `0 sorry`, `0` custom axioms, §7c generic).
- **Locked Route-1 specification (committed prior to numerical evaluation):**
  $$\Delta_{\mathrm{EM}}(p - n) = \alpha_q(q_0) \cdot m_{\mathrm{model}}(q_0) \cdot f,$$
  with derived Form-B $\alpha_q(q_0) = (q_0 [9]_{q_0} [10]_{q_0} + \frac{2}{3\pi})^{-1}$, self-consistent nucleon mass
  $m_{\mathrm{model}}(q_0) = m_e \left(2 \frac{\mathrm{Vol}(4_1)}{\hbar_q^2} F_{\mathrm{Bor}}(q_0) - 12\right)$ (**NO $m_\pi$ unit**),
  and ten parameter-free dimensionless shape factors $f$ from pure 3-strand $H_3(q_0)$ algebra and Borromean $6_3^3$ (`L6a4`, $\mathrm{Vol}(\mathcal{B}_3) = 8 G$) geometry:
  1. `f_R1_1a = 1 / 9` (3-strand equal-partition constituent Compton `1/3` × pairwise charge split `+1/3`);
  2. `f_R1_1b = 1 / (3 [3]_{q_0})` (`q`-deformed `(2,1)` Schur `[3]_{q_0}` constituent Compton × `+1/3`);
  3. `f_R1_1c = 1 / 6` (3-strand constituent Compton `1/3` × coherent `(1s)^3` self+pair `+1/2`);
  4. `f_R1_2a = (1/9) (coth(R_{B_3}/2) - c_0(B_3))` (O2 zero-mean `H^3` Green's kernel on `S^3 \ B_3` at half-ball separation `R_{B_3}/2`);
  5. `f_R1_2b = 1 / (24 G)` (`(1/3) / Vol(B_3)`);
  6. `f_R1_2c = Vol(4_1) / (24 G)` (`(1/3) · Vol(4_1) / Vol(B_3)`);
  7. `f_R1_3a = 1 / (3 q_0 √(2 Vol(4_1) F_Bor(q_0) - 12 ℏ_q^2))` (`(1/3) √(E_osc / m_model)` with `E_osc = m_e / (q_0 - 1)^2`, `m_e`- and `m_π`-free);
  8. `f_R1_3b = (1/3) √(2/π) √(E_osc / m_model)` (`(1s)^2` spherical HO Slater pairwise `+1/3`);
  9. `f_R1_3c = (1/2) √(2/π) √(E_osc / m_model)` (`(1s)^3` spherical HO Slater coherent self+pair `+1/2`);
  10. `f_R1_3d = |tr_conn(p, V^3)|` and `f_R1_3e = ℏ_q / 3` (pure Hecke `O(ℏ_q^4)` and `O(ℏ_q)` suppression controls).

All pre-registered candidates are evaluated at `workdps = 80` and reported without selection, including misses against `f_emp ≈ 0.111–0.146`.
