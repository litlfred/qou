The [aether parameter](#def:substrate-parameter) $q$ physicalizes wave propagation deformation. The slit material defines the brane boundary.

Wave propagation obeys the categorical Dirac equation ([categorical Dirac operator](#def:categorical-dirac-operator)):

$$\mathcal{D}_\nabla\psi =  0,$$

where $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$ ([variational equations](#prop:variational-equations)). The test particle $\psi$ is a photon with color content ([color content](#rem:knot-basis-color-content)). It propagates on an instanton background ([categorical instanton](#def:categorical-instanton)).

The $q$-deformed differential is:

$$d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d.$$

As $q \to 1$, $d_q \to d$. For $q > 1$, the vertical differential introduces transverse momentum shift.

The Reeb contraction drives wavefront spreading ([wavefront propagation](#rem:wavefront-propagation)). The phase difference along path $\gamma$ grazing the slit boundary is

$$
\Delta\phi =  \Delta\phi_{\mathrm{classical}} +  \hbar_q \int_{\gamma} \pi_V \circ d,
$$

The integral depends on the slit material's torsion intensity. The Lagrangian simplifies on an instanton background ([instanton on-shell](#rem:instanton-on-shell)):

$$\mathcal{L}_q\big|_{\text{instanton}} = c_2(A) + \psi^* \otimes \mathcal{D}_\nabla\psi.$$

An interactive simulation provides real-time parameter sweeps against the classical baseline.

## Color content and polarisation-dependent interference

The color content modifies interference via:

**1. Polarisation-weighted phase.**
Each polarisation mode acquires a Reeb phase. The total phase is

$$
  \Phi_q^{(\mathrm{color})}(\gamma_j)
  = 
  \Phi_q^{(j)}
  + 
  \varphi_0q\Phi_{\mathrm{Reeb}}^{(j)}
  + 
  \varphi_1(-q^{-1})\Phi_{\mathrm{Reeb}}^{(j)}.
$$

The bare-photon phase difference acquires a polarisation correction:

$$
  \Delta\Phi_q^{(\mathrm{color})}
  = 
  \Delta\Phi_q
  + 
  (\varphi_0q - \varphi_1q^{-1})\Delta\phi_\xi.
$$

**2. Cross-color interference.**
Interference generates cross-color terms. This modulates fringe visibility:

$$
  V_{\mathrm{color}}
  = 
  1 - |\varphi_0\psi_1 - \varphi_1\psi_0|^2.
$$

Material-dependent decoherence stems from the Hecke algebra structure.

**Observable signature.**
The correction is first order in $\hbar_q$ for linearly polarised light. A double-slit experiment isolates this material-dependent shift.
