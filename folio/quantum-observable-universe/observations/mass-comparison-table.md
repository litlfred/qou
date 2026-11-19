This table evaluates the topological knot formulas ([knot formula table](#rem:knot-formula-table)) at the canonical proton-pinned substrate parameter $q_0 = {{ qou.computations.m-p-substrate-identity-50dps.q0Value | precision: 12 }}\ldots$ ([local substrate](#prop:local-substrate-q), [Skein mass relation](#rem:skein-mass-relation)). The predictions are compared against CODATA 2022 recommended values and PDG 2024 averages. All masses are in MeV/$c^2$.

**Input parameters** (one dimensionless substrate parameter $q_0$ plus the CAL-1 scale $m_e$):

$$
  q = q_0 = {{ qou.computations.m-p-substrate-identity-50dps.q0Value | precision: 10 }}\ldots, \quad
  \hbar_q = 1 - q^{-1} = {{ qou.computations.q-pinning-50-digit.derived_50_digit.hbar_q | precision: 6 }}, \quad
  \mathrm{Vol}(4_1) = {{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}.
$$

**Table 2: Predicted vs.\ observed masses.**

*Leptons (from Skein volume).*

See [Table 1](#tbl:mass-comparison-table-table1-data).

The electron mass is the CAL-1 scale input. It fixes $\mu_{\mathfrak{u}}$ through the pair Skein mass. Under the proton-mass calibration $q_0$, the one-term muon mass prediction $m_e\mathrm{Vol}(4_1)/\hbar_q^2 = {{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector1_proton_self_energy_and_mup_tension.m_mu_pred_1term_MeV | precision: 9 }}\;\mathrm{MeV}$ sits $+{{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector1_proton_self_energy_and_mup_tension.m_mu_err_1term_ppb | precision: 4 }}\;\mathrm{ppb}$ above CODATA 2022, and subtracting the connected fourth-order Borromean $V^3$ proton QED self-energy $M_p^{\mathrm{QED,conn}} = +{{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector1_proton_self_energy_and_mup_tension.candidates.derived_borromean_V3_plain.M_p_QED_keV | precision: 6 }}\;\mathrm{keV}$ brings the two-term muon prediction to ${{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector1_proton_self_energy_and_mup_tension.candidates.derived_borromean_V3_plain.m_mu_pred_MeV | precision: 9 }}\;\mathrm{MeV}$ ($+{{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector1_proton_self_energy_and_mup_tension.candidates.derived_borromean_V3_plain.m_mu_err_ppb | precision: 3 }}\;\mathrm{ppb} = +0.36\,\sigma$).

*Hadrons (from pair Skein masses).*

The leading-order $\rho_K^{\mathrm{LO}}$ assembly cancels $|\mathrm{tr}_M|$ in $\rho_K^{\mathrm{LO}} \cdot m_e \cdot |\mathrm{tr}_M|$, reducing the constituent baseline to $Z m_p + N m_n$. In the substrate-identity evaluation, $m_p = {{ qou.computations.m-p-substrate-identity-50dps.data.predictions.m_p_MeV | precision: 9 }}\;\mathrm{MeV}$ round-trips the proton calibration while the neutron mass and $n$–$p$ splitting follow from the $\mathfrak{Q}_\beta$ chain without CODATA $m_n$ input.

See [Table 2](#tbl:mass-comparison-table-table2-data).

† **Anchor and constituent conventions.** Under the proton-mass calibration $q_0$, $m_p$ is the CAL-2 calibration anchor round-trip; $m_n$ and the $n$–$p$ split are parameter-free predictions from the Kashiwara $b^2$ + Two-Term QED Borromean $V^3$ chain.

#### FULL $\mathfrak{Q}_\beta$ and Two-Term QED $n$–$p$ splitting predictions (zero CODATA $m_n$ injection)

Using only CAL-1 ($m_e$) and CAL-2 ($q_0$), the framework evaluates the neutron $\beta$-decay $Q$-value and $n$–$p$ mass splitting across three parameter-free Convention-D levels:

1. **One-term Kashiwara $b^2$ Convention-D chain:**
   $$\mathfrak{Q}_\beta^{(1)} = {{ qou.computations.m-p-substrate-identity-50dps.data.predictions.Q_beta_MeV | precision: 7 }}\;\mathrm{MeV} \quad (+{{ qou.computations.m-p-substrate-identity-50dps.data.codata_comparison.Q_beta_residual_ppm | precision: 4 }}\;\mathrm{ppm}), \qquad m_n^{(1)} = {{ qou.computations.m-p-substrate-identity-50dps.data.predictions.m_n_MeV | precision: 9 }}\;\mathrm{MeV} \quad (+{{ qou.computations.m-p-substrate-identity-50dps.data.codata_comparison.m_n_residual_ppm | precision: 4 }}\;\mathrm{ppm}).$$
2. **Two-Term QED connected Borromean $V^3 = (\sigma_1\sigma_2^{-1})^3$ chain:**
   Adding the parameter-free electromagnetic splitting $\Delta m_{\mathrm{QED}}^{\mathrm{conn}} = {{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector2_np_and_qbeta_two_term_splitting.Delta_m_QED_conn_plain_keV | precision: 6 }}\;\mathrm{keV}$ ($-331.70\;\mathrm{eV}$ plain, or ${{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector2_np_and_qbeta_two_term_splitting.Delta_m_QED_conn_q_MeV | precision: 5 }}\;\mathrm{MeV} = -368.18\;\mathrm{eV}$ under Cartan $q_0$ weighting) reduces the neutron residual by $70.4\%$:
   $$\mathfrak{Q}_\beta^{\mathrm{2\text{-}term}} = {{ qou.computations.m-p-substrate-identity-50dps.data.two_term_borromean_qed_diagnostics.Q_beta_two_term_MeV | precision: 7 }}\;\mathrm{MeV} \quad (+{{ qou.computations.m-p-substrate-identity-50dps.data.two_term_borromean_qed_diagnostics.Q_beta_two_term_residual_ppm | precision: 4 }}\;\mathrm{ppm}), \qquad m_n^{\mathrm{2\text{-}term}} = {{ qou.computations.m-p-substrate-identity-50dps.data.two_term_borromean_qed_diagnostics.m_n_two_term_MeV | precision: 9 }}\;\mathrm{MeV} \quad (+{{ qou.computations.m-p-substrate-identity-50dps.data.two_term_borromean_qed_diagnostics.m_n_two_term_residual_ppb | precision: 4 }}\;\mathrm{ppb}\text{ plain},\; +{{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector2_np_and_qbeta_two_term_splitting.substrate_identity_neutron_mass.m_n_2term_q_err_ppb | precision: 4 }}\;\mathrm{ppb}\text{ Cartan }q_0).$$
   With the mirror-projected Convention-D Wedderburn phase $\alpha_D^{\mathrm{proj}} \approx -0.051412$, the one-term $Q$-value reaches $0.782375\;\mathrm{MeV}$ ($+53.2\;\mathrm{ppm}$ vs.\ CODATA ${{ qou.computations.m-p-substrate-identity-50dps.data.codata_comparison.Q_beta_codata_MeV | precision: 7 }}\;\mathrm{MeV}$).
3. **Un-dressed single-crossing base $\mathfrak{Q}_\beta^{z_D}$ and GPMT $(1,1,1)$ sign-block closure ([symbolic neutron $Q$-value](../nuclear-interactions/neutron-qvalue-symbolic.md)):**
   On the unbraided single-wrap difference $\Delta = \tfrac{1}{2}h^2\gamma - \tfrac{1}{2}h(\sigma_0 + \sigma_1)$, the two-dimensional Hoefsmit representation $(2,1)$ has exact opposite eigenvalues $\pm h/2$ ($\mathrm{tr}_{(2,1)}(\Delta) = 0$) while the bare single-crossing Markov trace at $z_D = q_0^3/(q_0^2+1)$ annihilates the antisymmetric baryon sign block $(1,1,1)$ ($y_{(1,1,1)}(z_D) = 0$), giving $\bigl|\tfrac{1}{2}h^2 - h z_D\bigr| E_0^{(\infty)} \approx 0.4491\;\mathrm{MeV}$ ($-42.59\%$) and Path-C $Q_\beta = {{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector2_np_and_qbeta_two_term_splitting.ruled_zD_qbeta_and_path_c_impact.qbeta_ruled_1term_MeV | precision: 6 }}\;\mathrm{MeV}$ ($\Delta m_{np} = {{ qou.computations.two-term-qed-isotope-and-nucleon-compute.data.sector2_np_and_qbeta_two_term_splitting.ruled_zD_qbeta_and_path_c_impact.Delta_pn_path_c_1term_MeV | precision: 6 }}\;\mathrm{MeV}$), or $0.6515\;\mathrm{MeV}$ ($-16.72\%$; $m_n \approx 939.435\;\mathrm{MeV}$, $-139\;\mathrm{ppm}$) after $\{V, V^{-1}, L_+, L_-\}$ reselection. On the 11-crossing Borromean nucleon normal forms, $\chi_{(2,1)}(n - p) < 0$ is non-vanishing and $\chi_{(1,1,1)}(n - p) < 0$ shares the sign of $\chi_{(3)}(n - p) < 0$; restoring $(1,1,1)$ via its positive Geer–Patureau-Mirand–Turaev modified quantum dimension $|d_{\mathrm{mod}}(1,1,1)| = \frac{1}{[2]_q[3]_q}$ together with the closed-form Convention-D generating function $\mathcal{G}_D(u; q)$ and the connected Borromean $V^3$ QED splitting ($\Delta M_{\mathrm{QED}}^{\mathrm{Bor}} = -0.332\;\mathrm{keV}$) yields parameter-free $\mathfrak{Q}_\beta = 0.77065\;\mathrm{MeV}$ ($-1.49\%$; $\Delta m_{np} = 1.28101\;\mathrm{MeV}$, $-0.95\%$) on the interleaved ordering and $\mathfrak{Q}_\beta = 0.78682\;\mathrm{MeV}$ ($+0.57\%$; $0.78616\;\mathrm{MeV}$, $+0.49\%$ before $\mathcal{G}_D$; $\Delta m_{np} = 1.29716\;\mathrm{MeV}$, $+0.30\%$) on the generator-grouped ordering, bracketing CODATA $0.78233\;\mathrm{MeV}$ ($\Delta m_{np} = 1.29333\;\mathrm{MeV}$) to $\sim 0.5\%\text{--}1.5\%$ with zero fitted parameters. The $z = 1$ symbolic specialization (${{ qou.computations.q-beta-predicted.data.q_beta_prediction.Q_beta_pred_MeV | precision: 6 }}\;\mathrm{MeV}$, $+0.168\%$) serves as an algebraic reference point only.

*Light nuclei (from multi-body Skein).* 

All rows below come from the LO $\rho_K$ assembly using CODATA $m_p, m_n$ inputs. The $\Delta$ column equals the CODATA/AME2020 binding energy by construction. The FULL multi-body unified knot mass formula at $H_{3A}$ remains intractable beyond $A = 1$. Binding-energy predictions require resolving the open $\Delta_\lambda$ research question (see [the recomputed low-isotope mass table](../mass-endomorphism/recomputed-low-isotope-mass-table.md)).

See [Table 3](#tbl:mass-comparison-table-table3-data).

† **LO output is constituent sum only.** The full prediction (beyond the constituent sum) is not yet available.

**Notes.** The proton--electron mass ratio (CAL-2) fixes the production substrate parameter $q_0$. Hadronic masses follow from the pair Skein formula ([terminal resolution](#prop:terminal-resolution)). Nuclear binding follows from the Hopf-junction Skein change $\Delta E = \Delta\mathcal{S}$. The multi-body Skein polynomials are evaluated explicitly up to ${}^4\mathrm{He}$; polynomials beyond $A = 4$ are computable in principle ([embeddability closure](#thm:embeddability-closure)) or via the 3D tetrahedral $\alpha$-simplex coordination reduction.

**Sources and scope.** The proton and neutron comparison entries use CODATA 2022 values directly. The nuclear entries use AME2020 binding energies. These entries recombine observed constants. The parameter $q$ predicts mass ratios ($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$), Q-values ($\Delta\mathrm{net} \times E_0$), and half-life ratios via $\log_q(ft)$ spectroscopy. The single external scaling ruler is $m_e = {{ qou.library.codata-2022.electron-mass-energy-equivalent-in-mev | precision: 6 }}\;\text{MeV}$ (CODATA 2022 input). This ruler converts dimensionless $q$-ratios to physical MeV. 

*Isotope-level data (hecke-engine certificates, $A \leq 14$).*

The hecke-engine provides exact Skein polynomial evaluations at $q_0$ for 47 isotopes from ${}^2\mathrm{H}$ through ${}^{60}\mathrm{Co}$. All 47 isotopes have corresponding AME2020 binding-energy data. The certificate fields encode combinatorial crossing structure, not mass directly.

See [Table 4](#tbl:mass-comparison-table-table4-data).

The $F_{\mathrm{Pauli}}$ factor remains $O(1)$ across all isotopes and encodes the Pauli exclusion statistical weight. The $\ln|P|$ column records the transfer matrix Skein polynomial evaluated at $q_0$. Neither field maps linearly to $B/A$ or mass in MeV.

