Let $q = |q|\,e^{i\theta}$ be a complex substrate parameter with
$|q| > 1$ and $\theta \in (-\pi, \pi]$, as in the
[complex substrate interpretation](#rem:complex-substrate-interpretation).

**Conjecture.**
In the pre-observable sector (before imposing the dagger
positive-definiteness axiom), the particle--antiparticle distinction
is governed by the phase $\theta$:

1. **Crossing energy acquires a phase.**  For a torus knot
   $T_{p,k}$ with [crossing energy](#def:crossing-energy)
   $\mathcal{S}_c(T_{p,k}; q)$, the complex extension satisfies
   $$
     \mathcal{S}_c(T_{p,k};\, |q|\,e^{i\theta})
     \;=\;
     \mathcal{S}_c(T_{p,k};\, |q|)\,e^{i\,n_c\,\theta},
   $$
   where $n_c$ is the crossing number.  The mirror image
   $\sigma(T_{p,k})$ has crossing number $-n_c$, giving
   $\mathcal{S}_c(\sigma(T_{p,k})) = \mathcal{S}_c(T_{p,k};\, |q|)\,e^{-i\,n_c\,\theta}$.

2. **Chirality interpolation.**  Define the chirality operator
   $\mathcal{X}_\varphi \colon \theta \mapsto \theta + \varphi$
   acting on the phase of $q$.  Then:
   - At $\varphi = 0$: identity (same particle).
   - At $\varphi = \pi / n_c$: crossing energies of particle and
     antiparticle become equal in magnitude, opposite in phase.
   - At $\varphi = \pi$: full chirality reversal
     ($q \mapsto |q|\,e^{i(\theta + \pi)}$).
   The discrete electron/positron flip of the
   [chirality remark](#rem:chirality-trefoil-electron-positron) is
   recovered as the endpoint $\varphi = \pi$ of a continuous
   rotation.

3. **CPT as $\mathbb{Z}_2$ quotient.**  The observable sector
   ($\theta = 0$) sees only the $\mathbb{Z}_2$ quotient of
   this $\mathrm{U}(1)$ action: charge conjugation C is the
   residue of the continuous chirality rotation modulo the
   observability constraint.  Parity P and time reversal T
   similarly descend from continuous operations in the
   pre-observable sector, and the CPT theorem becomes the
   statement that the total rotation
   $\mathcal{X}_\pi \circ P \circ T$ is always a symmetry
   of the categorical action
   ([categorical action](#def:categorical-action)).

**Experimental discriminant.**  If the pre-observable phase
$\theta$ leaves a residual signature after projection to
the observable sector, it would appear as a tiny
CP-violating phase in crossing-energy ratios.  For the
electron--positron system:

$$
  \delta_{\mathrm{CP}}
  \;=\;
  \frac{|\mathcal{S}_c(T_{2,3})| - |\mathcal{S}_c(\sigma(T_{2,3}))|}{|\mathcal{S}_c(T_{2,3})| + |\mathcal{S}_c(\sigma(T_{2,3}))|}
  \;\sim\;
  \mathcal{O}(\theta^2),
$$

which vanishes to first order (consistent with the observed
near-exact electron--positron mass equality) but could contribute
at second order to CP violation in hadronic systems where
multiple crossing numbers interact.
