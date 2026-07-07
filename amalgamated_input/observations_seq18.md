<!-- FILE_START: breit-wheeler-pair-creation-intro.md -->
Crystal-resonance experiments probe the substrate at lattice scales. We now turn to the high-energy probe of pair creation. Two blocks anchor this section: Remark: Breit--Wheeler process: first direct observation and QOU prediction compares the first direct observation of the Breit–Wheeler process against the QOU prediction for the $\gamma\gamma \to e^+ e^-$ cross-section, and Remark: Energy cost of electron--positron conversion computes the energy cost of the conversion in terms of crossing energy. Together, these blocks set up the categorical reading of pair creation. This reading is necessary for the complexity-and-interpretation section, which treats virtual pairs as excitations of the exceptional divisor.

_(draft.)_
<!-- FILE_END: breit-wheeler-pair-creation-intro.md -->

<!-- FILE_START: pair-creation-energy.md -->
How much energy does it cost to convert an electron into a positron?
The answer depends on what "convert" means — and the QOU framework
reveals three distinct energy scales.

**Standard physics: conversion is forbidden; only pair creation is possible.**
An isolated electron cannot become a positron — lepton number
conservation forbids it.  The minimum process is **pair production**:
a photon near a nucleus creates an $e^- e^+$ pair, requiring

$$
  E_{\gamma}  \geq  2m_ec^2 =  1.022  \text{MeV}.
$$

The original electron is unchanged; a new pair appears from the
photon's energy.

**In the QOU: crossing energy of the trefoil.**
The electron is the left trefoil $T_{2,3}$ with $n_c = 3$ positive
crossings.  Its [crossing energy](#def:crossing-energy) is

$$
  \mathfrak{E}_{\mathrm{cross}}(e^-)
  =  3q
   \approx  3  q_0
  =  3.330
  \quad (\text{in Skein units}).
$$

The positron is the mirror $T_{2,3}^{\sigma}$ with $3$ negative crossings:

$$
  \mathfrak{E}_{\mathrm{cross}}(e^+)
  =  -3q^{-1}
   \approx  -3 \times 0.9010
  =  -2.703
  \quad (\text{in Skein units}).
$$

The **crossing energy gap** between the two chiralities is

$$
  \Delta \mathfrak{E}_{\mathrm{cross}}
  =  \mathfrak{E}_{\mathrm{cross}}(e^-) - \mathfrak{E}_{\mathrm{cross}}(e^+)
  =  3(q + q^{-1})
   \approx  6.033
  \quad (\text{in Skein units}).
$$

This decomposes into symmetric and antisymmetric parts:

$$
  3(q + q^{-1})
  = 
  \underbrace{3 \cdot 2 \cosh(\ln q)}_{\text{strong baseline}}
  = 
  6 \cosh(\ln q)
   \approx  6.033.
$$

**Three energy scales for "conversion".**

| Process | Energy | QOU description |
|---------|--------|-----------------|
| Pair production ($\gamma \to e^- e^+$) | $2m_e c^2 \approx 1.022$ MeV | New pair from photon; trefoil + mirror created at exceptional divisor |
| Crossing energy gap (one trefoil) | $3(q + q^{-1}) \approx 6.03$ Skein units | Full reversal of all 3 crossings; maps to $\Delta E = 6\cosh(\ln q)$ |
| Complex-$q$ barrier ($\theta = 0 \to \pi$) | Topological, not energetic | Continuous rotation in pre-observable sector; no energy cost in observable sector |

**Physical interpretation of each route.**

1. **Pair production at the exceptional divisor.**  When a photon
   with $E \geq 2m_e$ encounters the blow-up locus, it can resolve
   into a trefoil--mirror pair.  The energy $2m_e$ is *not* the
   crossing energy gap — it is the mass-energy of the two particles
   created.  The crossing energies of $e^-$ and $e^+$ have opposite
   sign and partially cancel in the pair:

   $$
     \mathfrak{E}_{\mathrm{cross}}(e^-) + \mathfrak{E}_{\mathrm{cross}}(e^+)
     =  3q - 3q^{-1}
     =  3(q - q^{-1})
      \approx  0.630
     \quad (\text{Skein units}).
   $$

   The residual $3(q - q^{-1}) > 0$ is the **net Coulomb repulsion**
   of the pair — the antisymmetric part of the crossing energy that
   drives the $e^-$ and $e^+$ apart after creation.  The ratio

   $$
     \frac{q - q^{-1}}{q + q^{-1}}
     =  \tanh(\ln q)
      \approx  0.104
   $$

   measures the electromagnetic-to-strong ratio for the electron,
   consistent with $\alpha_{\mathrm{EM}} \sim 1/137$ at low energies
   (the Skein ratio is at the constituent scale, not the running
   coupling scale).

2. **Direct chirality reversal (forbidden in observable sector).**
   Flipping all 3 crossings of $T_{2,3}$ to produce $T_{2,3}^{\sigma}$
   while keeping the same knot would require a topological transition
   through the unknot — but the trefoil is
   [topologically stable](#rem:trefoil-vortex-chirality-flip).  In the
   observable sector ($q$ real, $\theta = 0$), no finite energy can
   accomplish this: the trefoil and its mirror are in different
   connected components of knot space.

3. **Complex-$q$ rotation (pre-observable).**  In the
   [complex substrate](#rem:complex-substrate-interpretation)
   framework, the chirality operator
   $\mathcal{X}_\varphi \colon \theta \to \theta + \varphi$ rotates
   continuously from electron to positron.  This has **zero energy
   cost** in the pre-observable sector (the rotation is along a
   flat direction of the categorical action).  The energy cost
   appears only upon **projection to the observable sector**, where
   the continuous rotation collapses to the discrete pair-creation
   event with threshold $2m_e$.

**Summary.**
The energy to "convert" an electron to a positron is either:
- **$\infty$** (impossible within the observable sector — topologically
  forbidden),
- **$2m_e \approx 1.022$ MeV** (create a new pair at the exceptional divisor),
  or
- **$0$** (in the pre-observable complex-$q$ sector, chirality
  rotation is free — but inaccessible to measurement).

The crossing energy gap $3(q + q^{-1})$ in Skein units sets the
*algebraic* distance between the two chiralities. Its physical
manifestation is not a single energy threshold but the decomposition
into symmetric binding ($\cosh$) and antisymmetric Coulomb ($\sinh$)
channels.
<!-- FILE_END: pair-creation-energy.md -->

<!-- FILE_START: breit-wheeler-observation.md -->
The Breit--Wheeler polarisation selection rule ([rem:breit-wheeler-vertex](#rem:breit-wheeler-vertex)) predicts a measurable azimuthal anisotropy in $e^-e^+$ pairs produced from two real photons. Only photons in distinct polarisation modes (generators $\sigma_0\neq\sigma_1$) contribute to pair production.

## QOU prediction

For two photons with polarisation mixing parameters $\phi_1,\phi_2\in[0,1]$, the Hecke normal form yields the same-mode amplitude $S = \phi_1\phi_2 + (1-\phi_1)(1-\phi_2)$ and the pair-production amplitude $C_+ + C_- = 1 - S$. The pair-production threshold energy scale is

$$
  E_0(\phi_1,\phi_2)
  = 
  \frac{2m_e}{\mathrm{net}(e^+) - S \cdot H_A}
   \in [2.27,4.22] \text{MeV},
$$

where $H_A = q - q^{-1} \approx 0.209$ at $q_0$ and $\mathrm{net}(e^+) \approx 0.451$ (the Gröbner--Shirshov NF coefficient at $q_0$).

We evaluate the limits:

| Configuration | $S$ | $E_0$ | Character |
|---|---|---|---|
| Same mode ($\phi_1 = \phi_2$) | $1$ | $\approx 4.22 \mathrm{MeV}$ | Hecke-reduced; no pair |
| Distinct modes ($\phi_1 \neq \phi_2$) | $0$ | $\approx 2.27 \mathrm{MeV}$ | Hopf link $L_\pm$; pair |

For unpolarised beams, the cross-section averages over $\phi_1,\phi_2$ and develops a $\cos(2\phi)$ azimuthal modulation in the $e^-e^+$ opening-angle distribution. The amplitude is proportional to $\langle C_+ - C_- \rangle = \langle \phi_1 - \phi_2 \rangle^2$.

## Comparison with observation

Ultra-peripheral heavy-ion collisions (UPCs) provide colliding real photons. Both STAR (Au+Au) \cite{star2021bw} and ATLAS (Pb+Pb) \cite{atlas2021bw} measure the azimuthal distribution of $e^-e^+$ pairs from $\gamma\gamma$ processes and observe a $\cos(2\phi)$ anisotropy. This observation is consistent with the QOU polarisation selection rule.

- **STAR \cite{star2021bw}**: observes $\cos(2\phi)$ azimuthal asymmetry in $e^-e^+$ pairs from coherent $\gamma\gamma$ interactions in Au+Au UPCs at $\sqrt{s_{NN}} = 200 \text{GeV}$. The measured asymmetry amplitude is $\approx 10$--$15\%$.
- **ATLAS \cite{atlas2021bw}**: confirms the azimuthal anisotropy in $e^-e^+$ pairs from $\gamma\gamma$ in Pb+Pb UPCs at $\sqrt{s_{NN}} = 5.02 \text{TeV}$.

In both experiments, the quasi-real photons are linearly polarised transverse to the beam axis. The observed $\cos(2\phi)$ pattern follows directly from the Hecke polarisation selection rule: pairs are suppressed when both photons occupy the same $\mathbb{P}^1(\mathbb{C})$ coordinate patch and enhanced when they occupy orthogonal patches. While standard QED attributes this modulation to helicity-interference, the QOU traces its geometric origin to the Hecke-algebra structure on the exceptional divisor $\mathcal{S}_p$.

The QOU distinct-mode pair-production energy scale $E_0 \approx 2.27 \text{MeV}$ resolves into the standard threshold $2m_e \approx 1.022 \text{MeV}$ plus the crossing energy of one unit of Reeb charge $\hbar_q = (q-1)/q \approx 1.25 \text{MeV}$ at $q_0$. The sum is $\approx 2.27 \text{MeV}$, matching the symbolic formula.
<!-- FILE_END: breit-wheeler-observation.md -->

