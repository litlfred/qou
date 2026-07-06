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

See [Table 1](#tbl:mass-comparison-table-table1-data).

The electron mass is an input (it fixes $\mu_{\mathfrak{u}}$ through the pair
Skein mass).  The muon mass is the first *prediction* — it equals
$\mathrm{Vol}(4_1)/\hbar_q^2$ and reproduces the CODATA value
to six significant figures with $q = q_0$.

*Hadrons (from pair Skein masses).*

The proton and neutron rows currently come from the **LO ρ_K
assembly** which consumes $m_p$ and $m_n$ as CODATA inputs (per
[`atomic-mass-via-rho-k.witness.json`](../../../computations/atomic-mass-via-rho-k.witness.json)).
Per owner directive ("do not use LO — use full"), this
is tautological by construction (the $|\mathrm{tr}_M|$ factor
cancels in $\rho_K^{\mathrm{LO}} \cdot m_e \cdot |\mathrm{tr}_M|$,
reducing $\mathcal{M}_\text{pred}$ to $Z m_p + N m_n$). The FULL
framework prediction for atomic masses requires the unified knot
mass formula
$M(\mathfrak{H}) = \rho \cdot [|\mathrm{tr}_M(T_w)| + \mathrm{tower}(T_w) + \mathrm{tr}_M(C_{\dim_q})]$
which is **not yet wired** at the nucleon scale (Workplan 0b
Phase 0b.4 + Workplan 2 + open Δ_λ derivation; see
[handoff](../../../docs/audits/-workplan-0b-script-rewire-handoff.md)).
The $n$–$p$ splitting is a *consequence* of the FULL $\mathfrak{Q}_\beta$ chain
($\mathfrak{Q}_\beta + m_e \approx 1.293$ MeV) — see the framework prediction
panel after this table.

See [Table 2](#tbl:mass-comparison-table-table2-data).

† **Tautological under the LO chain.** The proton, neutron, and
$n$-$p$ split rows read back the CODATA inputs because the LO
formula collapses to $Z m_p + N m_n$ identically (no binding
correction). FULL framework prediction below.

#### FULL $\mathfrak{Q}_\beta$ prediction (framework, no CODATA mass injection)

Per [`prop:neutron-qvalue-symbolic`](../../particle-interactions/neutron-qvalue-symbolic.md)
the framework predicts the β-decay Q-value from CAL-1 ($m_e$) and
CAL-2 ($q_0$) only via the closed form:

$$
\boxed{
\mathfrak{Q}_\beta^{\text{pred}} = \frac{m_e \cdot |q_0^2 - 2q_0 - 1| \cdot (q_0 + 1)}{2 q_0^3} \approx 0.7836 \text{ MeV}
}
$$

vs CODATA $0.7823$ MeV — **+0.168% / +1.31 keV framework prediction**.
At single wrap the $L_\pm$ and $e^-$ contributions cancel exactly
between proton and neutron, so $\Delta(\mathrm{net}) = h(h-2)/2$
with $h = q_0 - q_0^{-1}$, and the entire $Q$-value lives in the
$\gamma + \sigma_0 + \sigma_1$ channels.

The $n$-$p$ mass split follows: $\mathfrak{m}_n - \mathfrak{m}_p = \mathfrak{Q}_\beta + m_e \approx 1.295$ MeV
(vs CODATA $1.293$, same $0.17\%$ framework error, no CODATA $m_n - m_p$
input).

The +1.31 keV residual is the **brane-tower truncation** — the
derived $E_0$ uses the single-level Planck-tick approximation;
exact tower-summed $E_0$ closes it (Workplan 2 Phase 2). The
typed-crossings 6-term form gives a looser +0.747% prediction
(0.7882 MeV) — kept in the witness only for cross-check, not used
for production. Witness:
[`q-beta-predicted.witness.json`](../../../computations/q-beta-predicted.witness.json).

*Light nuclei (from multi-body Skein).* All rows below come from
the **LO ρ_K assembly** with CODATA $m_p$, $m_n$ inputs — same
discipline caveat as the proton/neutron rows above. The $\Delta$
column equals the CODATA binding energy by construction, not a
genuine framework prediction. The FULL multi-body unified knot
mass formula at $H_{3A}$ is not yet tractable beyond $A = 1$
(the $n$-$p$ split through $\mathfrak{Q}_\beta$ is the only mass-domain framework
prediction wired today; binding-energy predictions await closure
of the open Δ_λ research question per
[recomputed-low-isotope-mass-table.md:99](../braids-and-knots/recomputed-low-isotope-mass-table.md)).

See [Table 3](#tbl:mass-comparison-table-table3-data).

† **LO output is constituent sum only.** Genuine FULL prediction
not yet wired (see Workplan 0b §FULL chain status). Witness:
[`atomic-mass-via-rho-k.witness.json`](../../../computations/atomic-mass-via-rho-k.witness.json).

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
$m_e = :val[m_e_MeV]{precision=6, witness=computations/codata-masses.witness.json}$ MeV (CODATA 2022 experimental input, not a
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

See [Table 4](#tbl:mass-comparison-table-table4-data).

The $F_{\mathrm{Pauli}}$ factor is $O(1)$ for all isotopes and
encodes the Pauli exclusion statistical weight. The $\ln|P|$ column
is the transfer matrix Skein polynomial evaluated at $q_0$. Neither
field maps linearly to $B/A$ or mass in MeV. The full validation is
in `certificate-to-mass.witness.json`.
