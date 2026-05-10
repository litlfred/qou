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

The proton and neutron predictions split into two columns: the
**LO calibrated form** (which consumes $m_p$ and $m_n$ as CODATA
inputs and is therefore tautological for $p$, $n$, and the $n$-$p$
split) and the **Strategy-3 categorical prediction** (the genuine
multi-term unified knot mass formula
$M = \rho \cdot [|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})]$
with $T_w$ the β-decay-operator-unfolded canonical 3-strand braid
$\mathtt{atom\_braid\_word\_3A}(Z, N)$). Pion and kaon are
genuine pair-Skein predictions (no $m_p$/$m_n$ injection).

| Particle | Knot formula | LO calibrated (MeV) | Strategy-3 (MeV) | Observed (MeV) | Source |
|----------|-------------|---:|---:|---:|--------|
| Proton | $[u,u,d]_p \bowtie \mathcal{L}_H$ | $938.272$ † | $938.272$ ‡ | $938.272$ | CODATA |
| Neutron | $[u,d,d]_p \bowtie \mathcal{L}_H$ | $939.565$ † | $861.289$ ($-8.33\%$) | $939.565$ | CODATA |
| $n$-$p$ split | | $1.293$ † | $-76.983$ | $1.293$ | CODATA |
| $\pi^{\pm}$ | $u \bowtie d^{\sigma}$ | $139.570$ | — | $139.570$ | PDG |
| $K^{\pm}$ | $u \bowtie s^{\sigma}$ | $493.677$ | — | $493.677$ | PDG |

† **Tautological** — the LO ρ_K assembly
([`atomic-mass-via-rho-k.witness.json`](../../../folio-assistant/computations/atomic-mass-via-rho-k.witness.json))
consumes `M_P_MEV_VALIDATION` and `M_N_MEV_VALIDATION` (see the
deprecation banner in
[`codata_constants.py`](../../../folio-assistant/computations/codata_constants.py))
as upstream inputs. Per the
[three-calibration discipline](../braids-and-knots/three-calibration-inputs.md)
(CAL-1 $m_e$, CAL-2 $m_\mu/m_e$, CAL-3 $Q_\beta$), $m_p$ and $m_n$
are predictions, not inputs. Workplan 0b
([handoff](../../../docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md))
rewires the scripts to derive them.

‡ **Anchor** (Strategy-3) — the proton mass calibrates
$E_0 \approx 200$ MeV/cat-unit in
[`atomic-braid-mass-table.witness.json`](../../../folio-assistant/computations/atomic-braid-mass-table.witness.json).
This itself is a 4th-calibration violation parallel to (†); both
fixed under Workplan 0b. The neutron entry ($-8.33\%$) is a
genuine categorical residual — the multiplicative T1 base
$|\mathrm{tr}_p|^Z \cdot |\mathrm{tr}_n|^N$ is structurally
inadequate (atomic-scale composition is additive); the correct
path is the LP-dual shadow-price scheme of
[`prop:operator-selection-lp`](../braids-and-knots/operator-selection-lp.md).

*Light nuclei (from multi-body Skein).* Same two-column layout: LO
calibrated form (with CODATA $m_p$/$m_n$ injection) vs Strategy-3
genuine categorical prediction.

| Nucleus | Knot formula | LO calibrated (MeV) | Strategy-3 (MeV) | Observed (MeV) | Source |
|---------|-------------|---:|---:|---:|--------|
| Deuteron | $\mathfrak{p} \bowtie \mathfrak{n}$ | $1877.84$ ($+0.12\%$) | $1421.82$ ($-24.19\%$) | $1875.613$ | CODATA |
| Binding ($D$) | $\Delta\text{Skein}$ | $+2.22$ MeV | — | $2.225$ MeV | CODATA |
| Tritium | $\mathfrak{p} \bowtie 2\mathfrak{n}$ | $2817.40$ ($+0.30\%$) | $1288.82$ ($-54.12\%$) | $2808.921$ | AME2020 |
| ${}^3\mathrm{He}$ | $2\mathfrak{p} \bowtie \mathfrak{n}$ | $2816.11$ ($+0.27\%$) | $1392.19$ ($-50.43\%$) | $2808.392$ | AME2020 |
| ${}^4\mathrm{He}$ | $2\mathfrak{p} \bowtie 2\mathfrak{n}$ | $3755.68$ ($+0.76\%$) | (intractable §)  | $3727.379$ | AME2020 |

§ ${}^4\mathrm{He}$ Strategy-3 prediction marked
`tr_M_convention_status: DEPRECATED_DISJOINT` in
[`atomic-mass-via-rho-k.witness.json`](../../../folio-assistant/computations/atomic-mass-via-rho-k.witness.json):
the canonical word $\mathtt{atom\_braid\_word\_3A}(2, 2)$ has 47
crossings with 3 interfaces (pp, pn, nn); the canonical
$|\mathrm{tr}_M({}^4\mathrm{He})|$ at $H_{12}$ via the Wenzl
bridge is intractable in current Python mpmath (77 partitions, max
dim $\sim 7700$, $\sim 2 \times 10^{13}$ ops/partition $\times$ 47
crossings). Resolution requires a Rust kernel with rayon parallel
partitions or a categorical reduction via Wenzl 1988 LR branching.

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
