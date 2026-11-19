**Substrate layer.** In the substrate layer of the [unit layers](#def:qns-unit-layers), the viscosity $\nu_q$ is the derived ladder quantity, which vanishes as $q \to 1^+$. In this layer the classical limit is a *vanishing-viscosity* (Euler-type) limit.

**Physical layer.** The physical-layer coordinates are a rescaling by an existing derived scale, introducing no new degree of freedom. Under this map $k_{\mathrm{phys}} = (q-1)\,k_{\mathrm{sub}}$ (the ladder becomes a continuum grid of spacing $q-1$), enstrophies convert by $(q-1)^2$, and the viscosity becomes

$$
  \nu_{\mathrm{phys}} \;=\; c_q\,\nu_q \;=\; \frac{1}{2q},
$$

exactly — an algebraic identity, with $\tfrac12 - \nu_{\mathrm{phys}} \leq (q-1)/2$. In this layer the classical limit is a *fixed-viscosity* Navier–Stokes limit, the setting of the Clay formulation.

**Never straddle the layers (strict).** A single computed quantity, estimate, or claim must not mix substrate-layer and physical-layer inputs; every fluid-dynamics statement about the classical limit names its layer, and cross-layer comparisons go through the conversion identities above. The two layers can give different answers to the same-sounding question: the spectral pile-up question of the uniformity reduction is answered *negatively* in the substrate layer (tail enstrophy above a fixed band grows without bound as $q \to 1^+$, the receding dissipation range filling in) and *affirmatively* in the physical layer (the converted tail vanishes), per the witness `qns-tail-pileup-probe.witness.json`.
