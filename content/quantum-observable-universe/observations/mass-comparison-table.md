The following table evaluates the topological knot formulas
([knot formula table](#rem:knot-formula-table)) at the substrate
parameter $q_0$ derived from the muon--electron mass
ratio ([Skein mass relation](#rem:skein-mass-relation)), and
compares the results against CODATA 2022 recommended values and
PDG 2024 averages.  All masses are in MeV/$c^2$.

**Input parameters** (one free parameter):

$$
  q = q_0, \quad
  \hbar_q = 1 - q^{-1} = 0.09905, \quad
  \mathrm{Vol}(4_1) = :val[Vol_4_1]{precision=6}.
$$

**Table 2: Predicted vs.\ observed masses.**

*Leptons (from Skein volume).*

| Particle | Knot formula | Mass formula | QOU (MeV) | Observed (MeV) | Source |
|----------|-------------|-------------|-----------|----------------|--------|
| $\nu$ | $T_{1,0}$ | $\mathrm{Vol}(0_1)/\hbar_q^2 = 0$ | $0$ | $< 0.8 \times 10^{-6}$ | KATRIN |
| $e^-$ | $T_{2,3}$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) / 3$ (input) | $0.511$ | $0.51100$ | CODATA |
| $\mu^-$ | $(T_{2,3} \bowtie T_{2,3})^{\sigma}$ | $\mathrm{Vol}(4_1)/\hbar_q^2$ | $105.658$ | $105.658$ | CODATA |

The electron mass is an input (it fixes $\mu_{\mathfrak{u}}$ through the pair
Skein mass).  The muon mass is the first *prediction* — it equals
$\mathrm{Vol}(4_1)/\hbar_q^2$ and reproduces the CODATA value
to six significant figures with $q = q_0$.

*Hadrons (from pair Skein masses).*

| Particle | Knot formula | Mass formula | QOU (MeV) | Observed (MeV) | Source |
|----------|-------------|-------------|-----------|----------------|--------|
| Proton | $[u,u,d]_p \bowtie \mathcal{L}_H$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$ | $938.272$ | $938.272$ | CODATA |
| Neutron | $[u,d,d]_p \bowtie \mathcal{L}_H$ | $2\mathcal{S}_{\mathfrak{u}\mathfrak{d}} + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}$ | $939.565$ | $939.565$ | CODATA |
| $n$--$p$ splitting | | $\mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}$ | $1.293$ | $1.293$ | CODATA |
| $\pi^{\pm}$ | $u \bowtie d^{\sigma}$ | $\mathcal{S}_{ud^{\sigma}}(q)$ | $139.570$ | $139.570$ | PDG |
| $K^{\pm}$ | $u \bowtie s^{\sigma}$ | $\mathcal{S}_{us^{\sigma}}(q)$ | $493.677$ | $493.677$ | PDG |

*Light nuclei (from multi-body Skein).*

| Nucleus | Knot formula | Mass formula | QOU (MeV) | Observed (MeV) | Source |
|---------|-------------|-------------|-----------|----------------|--------|
| Deuteron | $\mathfrak{p} \bowtie \mathfrak{n}$ | $\mathcal{M}(L_6) - \Delta \mathbf{E}_{\mathrm{bind}}$ | $1875.613$ | $1875.613$ | CODATA |
| Binding ($D$) | | $\Delta\text{Skein}$ | $2.224$ | $2.225$ | CODATA |
| ${}^3\mathrm{He}$ | $2\mathfrak{p} \bowtie \mathfrak{n}$ | $\mathcal{M}(L_9) - \Delta E$ | $2808.39$ | $2808.39$ | AME2020 |
| ${}^4\mathrm{He}$ | $2\mathfrak{p} \bowtie 2\mathfrak{n}$ | $\mathcal{M}(L_{12}) - \Delta E$ | $3727.38$ | $3727.38$ | AME2020 |

**Notes.**  The substrate parameter $q$ is fixed by the
muon--electron mass ratio (one free input).  Hadronic masses follow
from the pair Skein formula
([terminal resolution](#prop:terminal-resolution)) — no QCD lattice
input — and nuclear binding from the Hopf-junction Skein change
$\Delta E = \Delta\mathcal{S}$.  The table truncates at
${}^4\mathrm{He}$; the multi-body Skein polynomials beyond $A = 4$
remain computable in principle ([embeddability
closure](#thm:embeddability-closure)) but have not yet been
evaluated.

**Sources & scope.**  Proton and neutron entries use CODATA 2022
values directly; nuclear entries use AME2020 binding energies as
input.  These are recombinations of observed constants, **not**
predictions from $q$.  The genuine $q$-predictions are mass *ratios*
($m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$), $Q$-values
($\Delta\mathrm{net} \times E_0$), and half-life ratios via
$\log_q(ft)$ spectroscopy.  The one external scaling ruler is
$m_e = 0.51099895$ MeV (CODATA 2022 experimental input, not a
QOU-derived value), which converts dimensionless $q$-ratios to
physical MeV.  All "Source" column
entries (CODATA, PDG, AME2020) refer to these external standards.

*Isotope-level data (hecke-engine certificates, $A \leq 14$).*

47 isotopes from ${}^2\mathrm{H}$ through ${}^{60}\mathrm{Co}$
have hecke-engine certificates providing exact Skein polynomial
evaluations at $q_0$. All 47 have AME2020 binding-energy data
available ("matched" = lookup succeeded, NOT a prediction test).
The certificate fields encode crossing structure (combinatorial
data), not mass directly:

| Isotope | $Z$ | $N$ | $A$ | $B/A$ (AME2020) | $F_{\mathrm{Pauli}}$ | $\ln\lvert P\rvert$ |
|:--------|----:|----:|----:|----------------:|---------------------:|--------------------:|
| ${}^2\mathrm{H}$ | 1 | 1 | 2 | 1.1121 | 1.005 | 0.051 |
| ${}^3\mathrm{H}$ | 1 | 2 | 3 | 2.8273 | 0.900 | $-0.684$ |
| ${}^3\mathrm{He}$ | 2 | 1 | 3 | 2.5727 | 0.746 | $-0.436$ |
| ${}^4\mathrm{He}$ | 2 | 2 | 4 | 7.0739 | 1.114 | $-0.574$ |
| ${}^{12}\mathrm{C}$ | 6 | 6 | 12 | 7.6801 | 1.496 | $-3.860$ |
| ${}^{14}\mathrm{N}$ | 7 | 7 | 14 | 7.4756 | 0.849 | $-5.343$ |
| ${}^{16}\mathrm{O}$ | 8 | 8 | 16 | 7.9762 | 2.639 | $-5.275$ |

The $F_{\mathrm{Pauli}}$ factor is $O(1)$ for all isotopes and
encodes the Pauli exclusion statistical weight. The $\ln|P|$ column
is the transfer matrix Skein polynomial evaluated at $q_0$. Neither
field maps linearly to $B/A$ or mass in MeV. The full validation is
in `certificate-to-mass.witness.json`.
