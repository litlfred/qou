This table evaluates the topological knot formulas ([knot formula table](#rem:knot-formula-table)) at the substrate parameter $q_0$. $q_0$ is derived from the muon--electron mass ratio ([Skein mass relation](#rem:skein-mass-relation)). The results are compared against CODATA 2022 recommended values and PDG 2024 averages. All masses are in MeV/$c^2$.

**Input parameters** (one free parameter):

$$
  q = q_0, \quad
  \hbar_q = 1 - q^{-1} = 0.09905, \quad
  \mathrm{Vol}(4_1) = {{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}.
$$

**Table 2: Predicted vs.\ observed masses.**

*Leptons (from Skein volume).*

See [Table 1](#tbl:mass-comparison-table-table1-data).

The electron mass is an input. It fixes $\mu_{\mathfrak{u}}$ through the pair Skein mass. The muon mass prediction equals $\mathrm{Vol}(4_1)/\hbar_q^2$. This reproduces the CODATA value to six significant figures at $q = q_0$.

*Hadrons (from pair Skein masses).*

The proton and neutron rows derive from the LO $\rho_K$ assembly. This assembly consumes $m_p$ and $m_n$ as CODATA inputs. It is tautological by construction. The $|\mathrm{tr}_M|$ factor cancels in $\rho_K^{\mathrm{LO}} \cdot m_e \cdot |\mathrm{tr}_M|$, reducing the output to $Z m_p + N m_n$. The FULL framework prediction requires the unified knot mass formula $M(\mathfrak{H}) = \rho \cdot [|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})]$. This formula does not yet extend to the nucleon scale. The $n$–$p$ splitting emerges as a consequence of the FULL $\mathfrak{Q}_\beta$ chain ($\mathfrak{Q}_\beta + m_e \approx 0.9557$ MeV under the ruled convention-D base, against CODATA $1.2933$ MeV).

See [Table 2](#tbl:mass-comparison-table-table2-data).

† **Tautological under the LO chain.** The proton, neutron, and $n$-$p$ split rows return the CODATA inputs because the LO formula collapses to $Z m_p + N m_n$ (no binding correction).

#### FULL $\mathfrak{Q}_\beta$ prediction (framework, no CODATA mass injection)

Per [Symbolic $Q$-value of free neutron decay](../nuclear-interactions/neutron-qvalue-symbolic.md), the framework predicts the $\beta$-decay Q-value using only CAL-1 ($m_e$) and CAL-2 ($q_0$):

$$
\boxed{
\mathfrak{Q}_\beta^{\text{pred}} = \mathfrak{Q}_\beta^{z_D} = \Bigl|\tfrac{h^2}{2} - h\,z_D\Bigr|\,\frac{m_e}{q_0(q_0-1)(1-\hbar_q^2)} \approx 0.4491 \text{ MeV}
}
$$

with $h = q_0 - q_0^{-1}$, $\hbar_q = 1 - q_0^{-1}$ and $z_D = q_0^3/(q_0^2+1)$. The energy scale is the tower-summed $E_0$; the order-zero form $m_e/(q_0(q_0-1))$ gives $0.4447$ MeV. This is the ruled convention-D base: $\varepsilon$ is the Markov trace at $z_D$ (owner ruling 2026-09-08). It compares to the CODATA value of $0.7823$ MeV at $-42.59\%$ ($-333.2$ keV). The convention-D $c_k$ correction ladder that would act on this base is not yet derived, and the factor a cosine phase can supply is capped below $1$ ([cos-resummation](#prop:q-beta-cos-resummation)), so the miss is reported as it stands.

The $n$-$p$ mass split follows: $\mathfrak{m}_n - \mathfrak{m}_p = \mathfrak{Q}_\beta + m_e \approx 0.9557$ MeV. This compares to the CODATA value of $1.2933$ MeV ($-26.11\%$ error, no CODATA $m_n - m_p$ input).

*Retired Form A (historical cross-check only).* The earlier closed form $m_e\,|q_0^2 - 2q_0 - 1|\,(q_0 + 1)/(2 q_0^3) \approx 0.7836$ MeV ($+0.168\%$, giving $m_n - m_p \approx 1.295$ MeV) evaluates $\varepsilon$ at $z = 1$, which is not an admissible Markov parameter under convention D. It is kept for comparison and is not the prediction.

*Light nuclei (from multi-body Skein).* 

All rows below come from the LO $\rho_K$ assembly using CODATA $m_p, m_n$ inputs. The $\Delta$ column equals the CODATA binding energy by construction. The FULL multi-body unified knot mass formula at $H_{3A}$ remains intractable beyond $A = 1$. Binding-energy predictions require resolving the open $\Delta_\lambda$ research question (see [recomputed-low-isotope-mass-table.md:99](../mass-endomorphism/recomputed-low-isotope-mass-table.md)).

See [Table 3](#tbl:mass-comparison-table-table3-data).

† **LO output is constituent sum only.** The full prediction (beyond the constituent sum) is not yet available.

**Notes.** The muon--electron mass ratio fixes the substrate parameter $q$. Hadronic masses follow from the pair Skein formula ([terminal resolution](#prop:terminal-resolution)). Nuclear binding follows from the Hopf-junction Skein change $\Delta E = \Delta\mathcal{S}$. Evaluate the multi-body Skein polynomials up to ${}^4\mathrm{He}$. Polynomials beyond $A = 4$ are computable in principle ([embeddability closure](#thm:embeddability-closure)) but remain unevaluated.

**Sources and scope.** The proton and neutron entries use CODATA 2022 values directly. The nuclear entries use AME2020 binding energies. These entries recombine observed constants. The parameter $q$ predicts mass ratios ($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$), Q-values ($\Delta\mathrm{net} \times E_0$), and half-life ratios via $\log_q(ft)$ spectroscopy. The single external scaling ruler is $m_e = {{ qou.library.codata-2022.electron-mass-energy-equivalent-in-mev | precision: 6 }}\;\text{MeV}$ MeV (CODATA 2022 input). This ruler converts dimensionless $q$-ratios to physical MeV. 

*Isotope-level data (hecke-engine certificates, $A \leq 14$).*

The hecke-engine provides exact Skein polynomial evaluations at $q_0$ for 47 isotopes from ${}^2\mathrm{H}$ through ${}^{60}\mathrm{Co}$. All 47 isotopes have corresponding AME2020 binding-energy data. The certificate fields encode combinatorial crossing structure, not mass directly.

See [Table 4](#tbl:mass-comparison-table-table4-data).

The $F_{\mathrm{Pauli}}$ factor remains $O(1)$ across all isotopes and encodes the Pauli exclusion statistical weight. The $\ln|P|$ column records the transfer matrix Skein polynomial evaluated at $q_0$. Neither field maps linearly to $B/A$ or mass in MeV.

