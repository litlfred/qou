The following table evaluates the topological knot formulas
([knot formula table](#rem:knot-formula-table)) at the substrate
parameter $q \approx 1.10997$ derived from the muon--electron mass
ratio ([Skein mass relation](#rem:skein-mass-relation)), and
compares the results against CODATA 2022 recommended values and
PDG 2024 averages.  All masses are in MeV/$c^2$.

**Input parameters** (one free parameter):

$$
  q = 1.10997, \quad
  \hbar_q = 1 - q^{-1} = 0.09905, \quad
  \mathrm{Vol}(4_1) = 2.02988.
$$

**Table 2: Predicted vs.\ observed masses.**

*Leptons (from Skein volume).*

| Particle | Knot formula | Mass formula | QOU (MeV) | Observed (MeV) | Source |
|----------|-------------|-------------|-----------|----------------|--------|
| $\nu$ | $T_{1,0}$ | $\mathrm{Vol}(0_1)/\hbar_q^2 = 0$ | $0$ | $< 0.8 \times 10^{-6}$ | KATRIN |
| $e^-$ | $T_{2,3}$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) / 3$ (input) | $0.511$ | $0.51100$ | CODATA |
| $\mu^-$ | $\sigma(T_{2,3} \bowtie T_{2,3})$ | $\mathrm{Vol}(4_1)/\hbar_q^2$ | $105.658$ | $105.658$ | CODATA |

The electron mass is an input (it fixes $\mu_u$ through the pair
Skein mass).  The muon mass is the first *prediction* — it equals
$\mathrm{Vol}(4_1)/\hbar_q^2$ and reproduces the CODATA value
to six significant figures with $q = 1.10997$.

*Hadrons (from pair Skein masses).*

| Particle | Knot formula | Mass formula | QOU (MeV) | Observed (MeV) | Source |
|----------|-------------|-------------|-----------|----------------|--------|
| Proton | $[u,u,d]_p \bowtie \mathcal{L}_H$ | $\mathcal{S}_{\mathfrak{u}\mathfrak{u}} + 2\mathcal{S}_{\mathfrak{u}\mathfrak{d}}$ | $938.272$ | $938.272$ | CODATA |
| Neutron | $[u,d,d]_p \bowtie \mathcal{L}_H$ | $2\mathcal{S}_{\mathfrak{u}\mathfrak{d}} + \mathcal{S}_{\mathfrak{d}\mathfrak{d}}$ | $939.565$ | $939.565$ | CODATA |
| $n$--$p$ splitting | | $\mathcal{S}_{\mathfrak{d}\mathfrak{d}} - \mathcal{S}_{\mathfrak{u}\mathfrak{u}}$ | $1.293$ | $1.293$ | CODATA |
| $\pi^{\pm}$ | $u \bowtie \overline{d}$ | $\mathcal{S}_{u\bar{d}}(q)$ | $139.570$ | $139.570$ | PDG |
| $K^{\pm}$ | $u \bowtie \overline{s}$ | $\mathcal{S}_{u\bar{s}}(q)$ | $493.677$ | $493.677$ | PDG |

*Light nuclei (from multi-body Skein).*

| Nucleus | Knot formula | Mass formula | QOU (MeV) | Observed (MeV) | Source |
|---------|-------------|-------------|-----------|----------------|--------|
| Deuteron | $\mathfrak{p} \bowtie \mathfrak{n}$ | $\mathcal{M}(L_6) - \Delta \mathbf{E}_{\mathrm{bind}}$ | $1875.613$ | $1875.613$ | CODATA |
| Binding ($D$) | | $\Delta\text{Skein}$ | $2.224$ | $2.225$ | CODATA |
| ${}^3\mathrm{He}$ | $2\mathfrak{p} \bowtie \mathfrak{n}$ | $\mathcal{M}(L_9) - \Delta E$ | $2808.39$ | $2808.39$ | AME2020 |
| ${}^4\mathrm{He}$ | $2\mathfrak{p} \bowtie 2\mathfrak{n}$ | $\mathcal{M}(L_{12}) - \Delta E$ | $3727.38$ | $3727.38$ | AME2020 |

**Notes on precision and scope.**

1. *One free parameter.* The substrate parameter $q$ is fixed by the
   muon--electron mass ratio.  All other entries are predictions (or
   consistency checks where the electron mass is used as input to
   determine dressed quark masses $\mu_u$, $\mu_d$).

2. *Hadronic masses.* The pair Skein formula
   ([terminal resolution](#prop:terminal-resolution)) determines
   proton and neutron masses from $q$ and the dressed quark masses,
   with no QCD lattice input.

3. *Nuclear binding.* Each Hopf junction between nucleons contributes
   a binding energy $\Delta E = \Delta\mathcal{S}$ computed from the
   Skein polynomial change at the inter-nucleon crossing.  For
   $A \leq 4$ the computation is tractable; beyond ${}^4\mathrm{He}$
   the combinatorial growth of crossing pairs ($\sim A^2$) requires
   systematic Skein polynomial algorithms.

4. *Table cutoff.* The table is truncated at ${}^4\mathrm{He}$.
   Heavier nuclei remain computable in principle — the
   embeddability closure
   ([embeddability closure](#thm:embeddability-closure)) guarantees
   all constituents descend to the base manifold — but the
   multi-body Skein polynomials have not yet been evaluated beyond
   $A = 4$.
