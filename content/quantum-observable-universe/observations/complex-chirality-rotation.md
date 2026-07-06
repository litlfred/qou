Let $q = |q|e^{i\theta}$ be a complex substrate parameter with $|q| > 1$ and $\theta \in (-\pi, \pi]$, as described in the [complex substrate interpretation](#rem:complex-substrate-interpretation).

**Conjecture.**
In the pre-observable sector (prior to imposing the dagger positive-definiteness axiom), the phase $\theta$ governs the particle-antiparticle distinction:

1. **Crossing energy acquires a phase.** For a torus knot $T_{p,k}$ with [crossing energy](#def:crossing-energy) $\mathcal{S}_c(T_{p,k}; q)$, the complex extension satisfies

   $$
     \mathcal{S}_c(T_{p,k}; |q|e^{i\theta})
     = 
     \mathcal{S}_c(T_{p,k}; |q|)e^{in_c\theta},
   $$

   where $n_c$ denotes the crossing number. The mirror image $T_{p,k}^{\sigma}$ carries crossing number $-n_c$, yielding $\mathcal{S}_c(T_{p,k}^{\sigma}) = \mathcal{S}_c(T_{p,k}; |q|)e^{-in_c\theta}$.

2. **Chirality interpolation.** Define the chirality operator $\mathcal{X}_\varphi \colon \theta \mapsto \theta + \varphi$ acting on the phase of $q$. Then:
   - At $\varphi = 0$: the operation acts as the identity.
   - At $\varphi = \pi / n_c$: crossing energies of particle and antiparticle equalize in magnitude and oppose in phase.
   - At $\varphi = \pi$: full chirality reversal occurs ($q \mapsto |q|e^{i(\theta + \pi)}$).
   
   The discrete electron/positron flip detailed in the [chirality remark](#rem:chirality-trefoil-electron-positron) emerges as the endpoint $\varphi = \pi$ of this continuous rotation.

3. **CPT as $\mathbb{Z}_2$ quotient.** The observable sector ($\theta = 0$) accesses only the $\mathbb{Z}_2$ quotient of this $\mathrm{U}(1)$ action. Charge conjugation C operates as the residue of the continuous chirality rotation, modulo the observability constraint. Parity P and time reversal T descend from continuous operations in the pre-observable sector. The CPT theorem asserts that the total rotation $\mathcal{X}_\pi \circ P \circ T$ acts as a symmetry of the categorical action ([categorical action](#def:categorical-action)).

**Experimental discriminant.** Any residual signature of the pre-observable phase $\theta$ surviving projection to the observable sector manifests as a CP-violating phase in crossing-energy ratios. For the electron-positron system:

$$
  \delta_{\mathrm{CP}}
  = 
  \frac{|\mathcal{S}_c(T_{2,3})| - |\mathcal{S}_c(T_{2,3}^{\sigma})|}{|\mathcal{S}_c(T_{2,3})| + |\mathcal{S}_c(T_{2,3}^{\sigma})|}
   \sim 
  \mathcal{O}(\theta^2).
$$

This vanishes to first order, aligning with the near-exact equality of electron and positron masses. It contributes at second order to CP violation in hadronic systems where multiple crossing numbers interact.
