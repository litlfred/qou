**Definition.**
*For a valid quantum universe $(A, \varTheta)$ over a spectral surface $\mathcal{S}$ with Reeb bundle $\xi$, the **NS obstruction class** is evaluated in the surface realisation ([NS-regular QOU](#def:ns-regular-qou)) as the global Euler class*

$$
  \mathrm{NS}(A) \;=\; e(\xi) \;\in\; H^2(\mathcal{S}, \mathbb{Z}) \cong \mathbb{Z}
$$

*(formerly written in local-cohomology notation as $H^3_{\mathrm{loc}}(A, \varTheta)$ or as the curve restriction $\kappa_0|_\Sigma \in H^2(\Sigma, \mathcal{B})$; the latter vanishes identically because $\dim \Sigma = 1$). It represents the base obstruction $\kappa_0$ of the $q$-Navier--Stokes brane tower at $q = 1$, with degree $\deg e(\xi) = \chi(A)$.*

*Categorically, the NS obstruction is governed by the Euler characteristic $\chi(A)$:*

- *$\mathrm{NS}(A) = 0$ ($\chi(A) = 0$) holds if and only if the quantum universe is categorically [NS-regular](#def:ns-regular-qou).*
- *$\mathrm{NS}(A) \neq 0$ ($\chi(A) \neq 0$) holds if and only if the quantum universe is categorically [NS-singular](#def:ns-regular-qou).*

*Scope (framework model correspondence and unforced setting).* Identifying the internal categorical dichotomy $\mathrm{NS}(A) = 0$ vs $\mathrm{NS}(A) \neq 0$ with global regularity or finite-time blowup of the classical **unforced** 3D incompressible Navier--Stokes equations ($f \equiv 0$, Fefferman's alternatives (A) on $\mathbb{R}^3$ and (B) on $\mathbb{T}^3$) is a framework model correspondence, not a deductive PDE theorem: because $\mathrm{NS}(A) = e(\xi)$ depends only on the topology of $\mathcal{S}$ and uses no property of the 3D advection nonlinearity $B(u, u) = P[(u \cdot \nabla)u]$, it is invariant under Tao's rotational/dyadic averaging (*J. Amer. Math. Soc.* **29** (2016), 601--674) and cannot by itself prove classical 3D regularity. Blowup driven by a smooth external force (alternatives (C) and (D)) is a separate problem and is not what $\mathrm{NS}(A)$ addresses.
