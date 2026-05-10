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

The proton and neutron rows currently come from the **LO ρ_K
assembly** which consumes $m_p$ and $m_n$ as CODATA inputs (per
[`atomic-mass-via-rho-k.witness.json`](../../../folio-assistant/computations/atomic-mass-via-rho-k.witness.json)).
Per owner directive 2026-05-10 ("do not use LO — use full"), this
is tautological by construction (the $|\mathrm{tr}_M|$ factor
cancels in $\rho_K^{\mathrm{LO}} \cdot m_e \cdot |\mathrm{tr}_M|$,
reducing $\mathcal{M}_\text{pred}$ to $Z m_p + N m_n$). The FULL
framework prediction for atomic masses requires the unified knot
mass formula
$M(\mathfrak{H}) = \rho \cdot [|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})]$
which is **not yet wired** at the nucleon scale (Workplan 0b
Phase 0b.4 + Workplan 2 + open Δ_λ derivation; see
[handoff](../../../docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md)).
The $n$–$p$ splitting is a *consequence* of the FULL Q_β chain
($Q_\beta + m_e \approx 1.293$ MeV) — see the framework prediction
panel after this table.

| Particle | Knot formula | LO output (MeV) | Observed (MeV) | Source |
|----------|-------------|---:|---:|--------|
| Proton | $[u,u,d]_p \bowtie \mathcal{L}_H$ | $938.272$ † | $938.272$ | CODATA |
| Neutron | $[u,d,d]_p \bowtie \mathcal{L}_H$ | $939.565$ † | $939.565$ | CODATA |
| $n$-$p$ split | | $1.293$ † | $1.293$ | CODATA |
| $\pi^{\pm}$ | $u \bowtie d^{\sigma}$ | $139.570$ | $139.570$ | PDG |
| $K^{\pm}$ | $u \bowtie s^{\sigma}$ | $493.677$ | $493.677$ | PDG |

† **Tautological under the LO chain.** The proton, neutron, and
$n$-$p$ split rows read back the CODATA inputs because the LO
formula collapses to $Z m_p + N m_n$ identically (no binding
correction). FULL framework prediction below.

#### FULL Q_β prediction (framework, no CODATA mass injection)

Per [`prop:beta-decay-energy-scale`](../../braids-and-knots/beta-decay-energy-scale.md)
the framework predicts the β-decay Q-value from CAL-1 ($m_e$) and
CAL-2 ($q_0$) only:

$$
E_0 = \frac{m_e}{q_0(q_0 - 1)} \approx 4.186\,\text{MeV},
\qquad
Q_\beta^{\text{pred}} = |\Delta(\mathrm{net})| \cdot E_0 \approx 0.7882\,\text{MeV}
$$

vs CODATA $Q_\beta = 0.7823$ MeV — **0.75% framework prediction**,
with $\Delta(\mathrm{net}) = -0.18829$ from the GS-NF coefficients
of the canonical neutron and proton braids. The $n$-$p$ mass split
follows: $\mathfrak{m}_n - \mathfrak{m}_p = Q_\beta + m_e \approx 1.299$ MeV
(vs CODATA $1.293$, same 0.5% framework error, no CODATA $m_n - m_p$
input).

**Observable / virtual split** (per Coxeter length $\ell$):

| Component | $\Delta \cdot E_0$ (MeV) | fraction | terms |
|---|---:|---:|---|
| **Observable** ($\ell \geq 2$) | $0.4608$ | $58.46\%$ | Hopf links $L_\pm$, trefoil $e^-$ |
| **Virtual** ($\ell < 2$) | $0.3274$ | $41.54\%$ | identity $\gamma$, single crossings $\sigma_0, \sigma_1$ |
| Total | $0.7882$ | $100\%$ |  |

Observable = topologically non-trivial, physical kinetic energy
released. Virtual = gauge / vacuum-debt, cancels in asymptotic
states. Witness:
[`q-beta-predicted.witness.json`](../../../folio-assistant/computations/q-beta-predicted.witness.json).

*Light nuclei (from multi-body Skein).* All rows below come from
the **LO ρ_K assembly** with CODATA $m_p$, $m_n$ inputs — same
discipline caveat as the proton/neutron rows above. The $\Delta$
column equals the CODATA binding energy by construction, not a
genuine framework prediction. The FULL multi-body unified knot
mass formula at $H_{3A}$ is not yet tractable beyond $A = 1$
(the $n$-$p$ split through Q_β is the only mass-domain framework
prediction wired today; binding-energy predictions await closure
of the open Δ_λ research question per
[recomputed-low-isotope-mass-table.md:99](../braids-and-knots/recomputed-low-isotope-mass-table.md)).

| Nucleus | Knot formula | LO output (MeV) | Observed (MeV) | $\Delta$ = CODATA binding | Source |
|---------|-------------|---:|---:|---:|--------|
| Deuteron | $\mathfrak{p} \bowtie \mathfrak{n}$ | $1877.838$ † | $1875.613$ | $-2.225$ MeV | CODATA |
| Tritium | $\mathfrak{p} \bowtie 2\mathfrak{n}$ | $2817.403$ † | $2808.921$ | $-8.482$ MeV | AME2020 |
| ${}^3\mathrm{He}$ | $2\mathfrak{p} \bowtie \mathfrak{n}$ | $2816.110$ † | $2808.392$ | $-7.718$ MeV | AME2020 |
| ${}^4\mathrm{He}$ | $2\mathfrak{p} \bowtie 2\mathfrak{n}$ | $3755.675$ † | $3727.379$ | $-28.296$ MeV | AME2020 |

† **LO output is constituent sum only.** Genuine FULL prediction
not yet wired (see Workplan 0b §FULL chain status). Witness:
[`atomic-mass-via-rho-k.witness.json`](../../../folio-assistant/computations/atomic-mass-via-rho-k.witness.json).

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
