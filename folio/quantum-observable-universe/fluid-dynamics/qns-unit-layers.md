The classical limit $q \to 1^+$ of the internal $q$-Navier–Stokes dynamics may be taken in two unit systems, which differ by the canonical aether scale $c_q = 1/(q-1)$. Every statement about the classical limit of a $q$-fluid quantity carries exactly one of the two layer tags below.

**Aether layer.** Coordinates $(x, t)$ as carried by the aether: wavenumbers are the $q$-integers $[n]_q$, and the viscosity is the derived ladder quantity

$$
  \nu_q \;=\; \frac{q-1}{2q},
$$

which vanishes as $q \to 1^+$. In this layer the classical limit is a *vanishing-viscosity* (Euler-type) limit.

**Physical layer.** Coordinates $(X, T) = (c_q\,x,\; c_q\,t)$ with velocity unrescaled — a rescaling by an existing derived scale, introducing no new degree of freedom. Under this map $k_{\mathrm{phys}} = (q-1)\,k_{\mathrm{sub}}$ (the ladder becomes a continuum grid of spacing $q-1$), enstrophies convert by $(q-1)^2$, and the viscosity becomes

$$
  \nu_{\mathrm{phys}} \;=\; c_q\,\nu_q \;=\; \frac{1}{2q},
$$

exactly — an algebraic identity, with $\tfrac12 - \nu_{\mathrm{phys}} \leq (q-1)/2$. In this layer the classical limit is a *fixed-viscosity* Navier–Stokes limit, the setting of the Clay formulation.

**Never straddle the layers (strict).** A single computed quantity, estimate, or claim must not mix aether-layer and physical-layer inputs; every fluid-dynamics statement about the classical limit names its layer, and cross-layer comparisons go through the conversion identities above. The two layers can give different answers to the same-sounding question: the spectral pile-up question of the uniformity reduction is answered *negatively* in the aether layer (tail enstrophy above a fixed band grows without bound as $q \to 1^+$, the receding dissipation range filling in) and *affirmatively* in the physical layer (the converted tail vanishes).
