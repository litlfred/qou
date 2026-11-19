The energy cost of converting an electron into a positron depends on
what "convert" means. The QOU framework distinguishes three energy
scales.

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
   \approx  -3 \times 0.9009
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
   through the unknot, but the trefoil is
   [topologically stable](#rem:trefoil-vortex-chirality-flip).  In the
   observable sector ($q$ real, $\theta = 0$), no finite energy can
   accomplish this: the trefoil and its mirror are in different
   connected components of knot space.

3. **Complex-$q$ rotation (pre-observable).**  In the
   [complex aether](#rem:complex-substrate-interpretation)
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
  rotation is free but inaccessible to measurement).

The crossing energy gap $3(q + q^{-1})$ in Skein units sets the
*algebraic* distance between the two chiralities. Its physical
manifestation is the decomposition
into symmetric binding ($\cosh$) and antisymmetric Coulomb ($\sinh$)
channels rather than a single energy threshold.
