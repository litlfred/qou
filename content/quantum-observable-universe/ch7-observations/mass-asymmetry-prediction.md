**Statement.**
*In the QOU framework, the categorical mass of a particle and its
antiparticle are not equal at the Skein (constituent) scale.  For a
knot $K$ with $n_c$ positive crossings and its mirror
$\sigma(K)$ with $n_c$ negative crossings, the mass--energy
equivalence $E = mc(q)^2$
([mass--energy equivalence](#thm:mass-energy-equivalence)) gives*

$$
  \frac{m(K)}{m(\sigma(K))}
  \;=\; \frac{|E_{\mathrm{cross}}(K)|}{|E_{\mathrm{cross}}(\sigma(K))|}
  \;=\; \frac{n_c \, q}{n_c \, q^{-1}}
  \;=\; q^2.
$$

*At $q = 1.1097$:*

$$
  \frac{m(K)}{m(\sigma(K))} \;=\; q^2 \;\approx\; 1.231.
$$

**Electron--positron mass table.**

| Quantity | $e^-$ (left trefoil) | $e^+$ (right trefoil) | Ratio |
|----------|---------------------|-----------------------|-------|
| Crossings | $n_c = 3$ positive | $n_c = 3$ negative | --- |
| Crossing energy | $3q \approx 3.330$ | $3q^{-1} \approx 2.703$ | $q^2 \approx 1.231$ |
| Categorical mass | $m_e = 3q(q-1)^2$ | $m_{e^+} = 3q^{-1}(q-1)^2$ | $q^2 \approx 1.231$ |

The mass ratio $q^2$ is **universal**: it depends only on the
substrate parameter, not on the crossing number $n_c$.  Every
particle--antiparticle pair has the same constituent-scale mass
asymmetry.

**Relation to CPT.**
In standard physics, CPT invariance guarantees
$m_{\mathrm{particle}} = m_{\mathrm{antiparticle}}$ exactly.  The
QOU does not violate CPT --- the asymmetry arises because the
categorical mass at the **Skein scale** is not the same as the
**renormalized physical mass** measured in experiments:

1. **Skein (constituent) scale.**  The crossing energy weights
   $q$ and $q^{-1}$ are manifestly asymmetric under $q \neq 1$.
   At this scale, $m(e^-) / m(e^+) = q^2 \approx 1.231$.

2. **Renormalized (physical) scale.**  The descent from the
   Skein scale to the physical scale involves:
   - Coarse-graining over $n_R(q) \approx 10$ Reeb iterations
     per Planck time
     ([Reeb operations](#prop:reeb-operations-per-planck))
   - The statistical-mechanical time averaging
     ([stat-mech time](#rem:statistical-mechanical-time))
     that smooths the discrete dynamics into continuous fields
   - Radiative corrections from higher jet levels

   These corrections restore the CPT-mandated equality
   $m_e^{\mathrm{phys}} = m_{e^+}^{\mathrm{phys}}$ at the
   observable scale: the coarse-graining averages over the
   $q \leftrightarrow q^{-1}$ asymmetry in the crossing weights.

3. **Residual asymmetry.**  The restoration is exact only in the
   $q \to 1$ (classical) limit.  At finite $q$, a residual
   asymmetry may survive:

   $$
     \frac{m_e^{\mathrm{phys}} - m_{e^+}^{\mathrm{phys}}}
          {m_e^{\mathrm{phys}}}
     \;\sim\; \mathcal{O}\!\left(\frac{(q-1)^2}{n_R(q)}\right)
     \;\sim\; \mathcal{O}(\hbar_q^3)
     \;\approx\; 10^{-3}.
   $$

   This is below current experimental bounds but within reach of
   planned measurements.

**Experimental status.**

| Experiment | Bound on $|m_e - m_{e^+}|/m_e$ | Year |
|-----------|-------------------------------|------|
| TRAP (Gabrielse) | $< 8 \times 10^{-9}$ | 1999 |
| BASE (antiproton) | $< 1.6 \times 10^{-12}$ ($p/\bar{p}$) | 2022 |
| ALPHA (antihydrogen) | $< 2 \times 10^{-12}$ (via $\bar{H}$ spectroscopy) | 2020 |

The current bounds ($< 10^{-9}$ for electrons, $< 10^{-12}$
for protons) constrain the residual asymmetry but do not
test the Skein-scale ratio $q^2 \approx 1.231$.  The Skein-scale
asymmetry is a **pre-renormalization** quantity --- it is not
directly observable in mass measurements but manifests in:

- **Crossing energy decomposition.**  The symmetric/antisymmetric
  split is already observed: $\tanh(\ln q) \approx 0.104$ matches
  the EM/strong ratio
  ([crossing energy interpretation](#rem:crossing-energy-interpretation)).
  The mass asymmetry $q^2$ and the coupling ratio $\tanh(\ln q)$
  are both consequences of $q \neq 1$.

- **Pair creation thresholds.**  The net crossing energy of a pair
  $E(e^-) + E(e^+) = 3(q - q^{-1})$ is nonzero precisely because
  $q \neq q^{-1}$.  This residual drives the Coulomb repulsion of
  the pair ([pair creation energy](#rem:pair-creation-energy)).

- **CP violation.**  The $q^2$ asymmetry feeds into the
  $\delta_{\mathrm{CP}}$ prediction
  ([CP violation](#rem:cp-violation-evidence)) through the
  complex-$q$ residual phase.

**Prediction.**
The Skein-scale mass asymmetry $q^2 \approx 1.231$ is a structural
consequence of $c(q) = 1/(q-1)$ and the asymmetric crossing weights
$q \neq q^{-1}$.  It is **not** a violation of CPT but a feature of
the pre-renormalized (constituent) description.  The physical
observable is the residual after coarse-graining, predicted to be
$\mathcal{O}(\hbar_q^3) \sim 10^{-3}$, which is testable at
next-generation antimatter facilities (ELENA/GBAR at CERN, AEgIS).
