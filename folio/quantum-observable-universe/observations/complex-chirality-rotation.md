Let $q = |q|e^{i\theta}$ be a complex aether parameter with $|q| > 1$ and $\theta \in (-\pi, \pi]$ ([complex aether interpretation](#rem:complex-substrate-interpretation)).

**Conjecture.**
In the pre-observable sector (before the dagger positive-definiteness axiom), the phase $\theta$ controls the particle-antiparticle distinction:

1. **Crossing energy phase.** For a torus knot $T_{p,k}$ with [crossing energy](#def:crossing-energy) $\mathcal{S}_c(T_{p,k}; q)$, the complex extension is:

   $$
     \mathcal{S}_c(T_{p,k}; |q|e^{i\theta})
     = 
     \mathcal{S}_c(T_{p,k}; |q|)e^{in_c\theta},
   $$

   where $n_c$ is the crossing number. The mirror $T_{p,k}^{\sigma}$ carries crossing number $-n_c$, so $\mathcal{S}_c(T_{p,k}^{\sigma}) = \mathcal{S}_c(T_{p,k}; |q|)e^{-in_c\theta}$.

2. **Chirality interpolation.** The chirality operator $\mathcal{X}_\varphi \colon \theta \mapsto \theta + \varphi$ acts on the phase of $q$:
   - $\varphi = 0$: Identity action.
   - $\varphi = \pi / n_c$: Particle and antiparticle crossing energies equalize in magnitude and oppose in phase.
   - $\varphi = \pi$: Full chirality reversal ($q \mapsto |q|e^{i(\theta + \pi)}$).
   
   The discrete electron/positron flip ([chirality remark](#rem:chirality-trefoil-electron-positron)) is the endpoint $\varphi = \pi$ of this rotation.

3. **CPT as $\mathbb{Z}_2$ quotient.** The observable sector ($\theta = 0$) detects only the $\mathbb{Z}_2$ quotient of this $\mathrm{U}(1)$ action. Charge conjugation C is the residue of continuous chirality rotation. Parity P and time reversal T descend from pre-observable continuous operations. The CPT theorem means the total rotation $\mathcal{X}_\pi \circ P \circ T$ is a symmetry of the categorical action ([categorical action](#def:categorical-action)).

**Experimental discriminant.** Any pre-observable phase $\theta$ surviving in the observable sector appears as a CP-violating phase in crossing-energy ratios. For the electron-positron system:

$$
  \delta_{\mathrm{CP}}
  = 
  \frac{|\mathcal{S}_c(T_{2,3})| - |\mathcal{S}_c(T_{2,3}^{\sigma})|}{|\mathcal{S}_c(T_{2,3})| + |\mathcal{S}_c(T_{2,3}^{\sigma})|}
   \sim 
  \mathcal{O}(\theta^2).
$$

This vanishes to first order, matching electron-positron mass equality. It contributes at second order to hadronic CP violation, where multiple crossing numbers interact.
