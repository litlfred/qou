This table evaluates the topological knot formulas ([knot formula table](#rem:knot-formula-table)) at the substrate parameter $q_0 = {{ qou.computations.master-atlas-80dps.data.anchors.q0_proton_80dps | precision: 13 }}$ (anchored numerically on the proton-to-electron mass ratio $m_{\mathfrak{p}}/m_e$; see [Skein mass relation](#rem:skein-mass-relation)). The results are compared against CODATA 2022 recommended values and PDG 2024 averages. All masses are in MeV/$c^2$.

**Input parameters** (one dimensionless deformation parameter $q_0$):

$$
  q = q_0, \quad
  \hbar_q = 1 - q^{-1} \approx {{ qou.computations.master-atlas-80dps.data.anchors.hbar_q_proton_80dps | precision: 5 }}, \quad
  \mathrm{Vol}(4_1) = {{ qou.computations.master-atlas-80dps.data.anchors.vol_4_1_80dps | precision: 7 }}.
$$

**Table 2: Predicted vs.\ observed masses.**

*Leptons (from Skein volume).*

See [Table 1](#tbl:mass-comparison-table-table1-data).

The electron mass is a physical scale input fixing the MeV energy unit. At the proton-pinned $q_0$, the topological volume ratio $m_e\,\mathrm{Vol}(4_1)/\hbar_{q_0}^2 \approx {{ qou.computations.master-atlas-80dps.data.observables.m_mu_MeV.pred | precision: 9 }}\;\text{MeV}$ agrees with $m_\mu$ to six significant figures in MeV (residual $+{{ qou.computations.master-atlas-80dps.data.observables.m_mu_MeV.rel_ppb | precision: 4 }}\;\text{ppb}$, or ${{ qou.computations.master-atlas-80dps.data.observables.m_mu_MeV.pull_exp | precision: 3 }}\sigma$ against the sub-ppb CODATA uncertainty).

*Hadrons (from pair Skein masses).*

The proton and neutron rows derive from the LO $\rho_K$ assembly. This assembly consumes $m_p$ and $m_n$ as CODATA inputs. It is tautological by construction. The $|\mathrm{tr}_M|$ factor cancels in $\rho_K^{\mathrm{LO}} \cdot m_e \cdot |\mathrm{tr}_M|$, reducing the output to $Z m_p + N m_n$. The FULL framework prediction requires the unified knot mass formula $M(\mathfrak{H}) = \rho \cdot [|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})]$. This formula does not yet extend to the nucleon scale. The $n$–$p$ splitting emerges as a consequence of the FULL $\mathfrak{Q}_\beta$ chain ($\mathfrak{Q}_\beta + m_e \approx {{ qou.computations.master-atlas-80dps.data.observables.delta_m_np_MeV.pred | precision: 4 }}\;\text{MeV}$ on the scored $T^3$ weight-trace split at $z = q_0^3/(q_0^2+1)$, or $0.9601\;\text{MeV}$ on the historical $\Delta$ base, against CODATA ${{ qou.library.codata-2022.neutron-proton-mass-difference-energy-equivalent-in-mev | precision: 5 }}\;\text{MeV}$).

See [Table 2](#tbl:mass-comparison-table-table2-data).

† **Tautological under the LO chain.** The proton, neutron, and $n$-$p$ split rows return the CODATA inputs because the LO formula collapses to $Z m_p + N m_n$ (no binding correction).

#### FULL $\mathfrak{Q}_\beta$ prediction (framework, no CODATA mass injection)

Per [Symbolic $Q$-value of free neutron decay](../nuclear-interactions/neutron-qvalue-symbolic.md), the framework evaluates the $\beta$-decay Q-value from the electron scale $m_e$ and proton-anchored $q_0$ alone:

$$
\boxed{
\mathfrak{Q}_\beta^{\Delta} = \Bigl|\tfrac{h^2}{2} - h\,z\Bigr|\,\frac{m_e}{q_0(q_0-1)(1-\hbar_q^2)} \approx {{ qou.computations.per-observable-100x-status.data.qbeta_ruled_base.Q_beta_MeV_on_superseded_delta_S | precision: 4 }} \text{ MeV}
}
$$

with $h = q_0 - q_0^{-1}$, $\hbar_q = 1 - q_0^{-1}$, and $z = q_0^3/(q_0^2+1) \approx {{ qou.computations.master-atlas-80dps.data.anchors.markov_z_proton_80dps | precision: 6 }}$. Using the tower-summed $E_0$ (the order-zero form $m_e/(q_0(q_0-1))$ gives $0.4447$ MeV), this Markov-trace $\Delta$ evaluation sits at $-42.59\%$ ($-333.2$ keV) relative to CODATA ${{ qou.computations.master-atlas-80dps.data.observables.q_beta_base_MeV.exp | precision: 4 }}$ MeV; no $c_k$ correction ladder at $z = q^3/(q^2+1)$ has yet been derived, and a cosine factor cannot exceed $1$ ([cos-resummation](#prop:q-beta-cos-resummation)).

The scored evaluation applies the $T^3$ weight split of the $z = q_0^3/(q_0^2+1)$ trace to the $\gamma\gamma$ base $V^3 = (\sigma_0\sigma_1^{-1})^3$, giving $\mathfrak{Q}_\beta^{\mathrm{scored}} = |\varepsilon_{\mathrm{flavour}}(V^3)|\,E_0 \approx {{ qou.computations.master-atlas-80dps.data.observables.q_beta_base_MeV.pred | precision: 4 }}$ MeV (${{ qou.computations.per-observable-100x-status.data.qbeta_ruled_base.err_pct | precision: 4 }}\%$) and $\mathfrak{m}_n - \mathfrak{m}_p \approx {{ qou.computations.master-atlas-80dps.data.observables.delta_m_np_MeV.pred | precision: 4 }}$ MeV ($-35.33\%$). On the $\Delta$ evaluation above (${{ qou.computations.per-observable-100x-status.data.qbeta_ruled_base.Q_beta_MeV_on_superseded_delta_S | precision: 4 }}$ MeV), $\mathfrak{m}_n - \mathfrak{m}_p = \mathfrak{Q}_\beta + m_e \approx 0.9601$ MeV ($-25.77\%$ relative to CODATA ${{ qou.library.codata-2022.neutron-proton-mass-difference-energy-equivalent-in-mev | precision: 5 }}$ MeV).

*Coordinate-sum Form A ($z = 1$ comparison).* Evaluating $\varepsilon$ at $z = 1$ gives $m_e\,|q_0^2 - 2q_0 - 1|\,(q_0 + 1)/(2 q_0^3) \approx 0.7836$ MeV ($+0.168\%$, $m_n - m_p \approx 1.295$ MeV); because $z = 1$ does not satisfy $y_{(1^3)}(z) = 0$, it serves only as an algebraic comparison.

*Light nuclei (from multi-body Skein).* 

All rows below come from the LO $\rho_K$ assembly using CODATA $m_p, m_n$ inputs. The $\Delta$ column equals the CODATA binding energy by construction. The FULL multi-body unified knot mass formula at $H_{3A}$ remains intractable beyond $A = 1$. Binding-energy predictions require resolving the open $\Delta_\lambda$ research question (see [Recomputed low-isotope mass table](../mass-endomorphism/recomputed-low-isotope-mass-table.md)).

See [Table 3](#tbl:mass-comparison-table-table3-data).

† **LO output is constituent sum only.** The full prediction (beyond the constituent sum) is not yet available.

**Notes.** The proton--electron mass ratio fixes the substrate parameter $q_0$. Hadronic masses follow from the pair Skein formula once the two dressed quark masses are given; that map is invertible, so the formula alone does not predict them ([nucleon masses under the pair Skein formula](#prop:terminal-resolution)). Nuclear binding follows from the Hopf-junction Skein change $\Delta E = \Delta\mathcal{S}$. Evaluate the multi-body Skein polynomials up to ${}^4\mathrm{He}$. Polynomials beyond $A = 4$ are computable in principle ([embeddability closure](#thm:embeddability-closure)) but remain unevaluated.

**Sources and scope.** The proton and neutron entries use CODATA 2022 values directly. The nuclear entries use AME2020 binding energies. These entries recombine observed constants. The parameter $q$ predicts mass ratios ($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$), Q-values ($\Delta\mathrm{net} \times E_0$), and half-life ratios via $\log_q(ft)$ spectroscopy. The single external scaling ruler is $m_e = {{ qou.library.codata-2022.electron-mass-energy-equivalent-in-mev | precision: 6 }}\;\text{MeV}$ (CODATA 2022 input). This ruler converts dimensionless $q$-ratios to physical MeV. 

*Isotope-level data (hecke-engine certificates, $A \leq 14$).*

The hecke-engine provides exact Skein polynomial evaluations at $q_0$ for 47 isotopes from ${}^2\mathrm{H}$ through ${}^{60}\mathrm{Co}$. All 47 isotopes have corresponding AME2020 binding-energy data. The certificate fields encode combinatorial crossing structure, not mass directly.

See [Table 4](#tbl:mass-comparison-table-table4-data).

The $F_{\mathrm{Pauli}}$ factor remains $O(1)$ across all isotopes and encodes the Pauli exclusion statistical weight. The $\ln|P|$ column records the transfer matrix Skein polynomial evaluated at $q_0$. Neither field maps linearly to $B/A$ or mass in MeV.

