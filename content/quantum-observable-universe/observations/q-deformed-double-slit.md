The [substrate parameter](#def:substrate-parameter) $q$ encodes a physical deformation of wave propagation. The slit material acts as a defining boundary of the brane. Here, the Reeb vector field exerts a geometric push on the traversing test particle.

Wave propagation satisfies the categorical Dirac equation ([categorical Dirac operator](#def:categorical-dirac-operator)):

$$\mathcal{D}_\nabla\psi =  0,$$

where $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$ ([variational equations](#prop:variational-equations)). The test particle $\psi$ is a photon with color content $\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$ ([color content](#rem:knot-basis-color-content)). The elements $\sigma_0$ and $\sigma_1$ are the horizontal and vertical polarisation generators. The product $\sigma_0\sigma_1$ is the Hopf link dressing on $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ ([Breit--Wheeler vertex](#rem:breit-wheeler-vertex)). The photon propagates on an instanton background ([categorical instanton](#def:categorical-instanton)). The identity component $\mathbf{1}$ propagates as pure horizontal flux. The generators $\varphi_i\sigma_i$ carry polarisation-dependent phase from the Hecke eigenvalues $+q$ and $-q^{-1}$.

Recall the $q$-deformed differential ([the local substrate proposition](#prop:local-substrate-q)):

$$d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d.$$

As $q \to 1$, the quantum Planck constant $\hbar_q = 1 - q^{-1}$ vanishes, and $d_q \to d$. The vertical component drops out, recovering classical interference. For $q > 1$, the vertical differential $\pi_V \circ d$ introduces a transverse momentum shift that modifies the interference pattern.

The Reeb contraction term $(1-q^{-1})\iota_\xi\nabla$ drives wavefront spreading ([wavefront propagation](#rem:wavefront-propagation)). This term allows a point-source photon to illuminate both slits. The beam width $w_0$ at the barrier is determined by the Green's function of $\mathcal{D}_\nabla$ on the flat instanton background ($F_\nabla = 0$).

The phase difference for a path $\gamma$ grazing the fermionic slit boundary is

```tex
\Delta\phi =  \Delta\phi_{\mathrm{classical}} +  \hbar_q \int_{\gamma} \pi_V \circ d,
```

The integral evaluates the vertical Reeb differential along $\gamma$. This correction depends on the torsion intensity of the slit material. A nucleon modeled as a [localized knot](#def:localized-knot) with the Borromean rings topology $6_2^3$ determines $q$ via the local substrate map. Heavier atoms with complex knotted configurations produce larger deformations. This yields a material-dependent fringe spacing absent in classical diffraction.

On an instanton background, the Lagrangian simplifies ([instanton on-shell](#rem:instanton-on-shell)):

$$\mathcal{L}_q\big|_{\text{instanton}} = c_2(A) + \psi^* \otimes \mathcal{D}_\nabla\psi,$$

The gauge sector is topological ($c_2$ is fixed by the material's knot type). All observable physics resides in $\mathcal{D}_\nabla\psi = 0$. The intensity pattern derivation is given in [the photon wavefront example](#ex:photon-wavefront).

An interactive simulation is available in the [q-deformed double-slit simulator](q-double-slit.html). It provides real-time parameter sweeps against the classical baseline.

## Color content and polarisation-dependent interference

The photon color content $(\varphi_0, \varphi_1)$ modifies the interference pattern in two ways.

**1. Polarisation-weighted phase.**
Each polarisation mode $\sigma_i$ acquires a Reeb phase along path $\gamma_j$ through slit $j$. The total phase for a color-dressed photon is

$$
  \Phi_q^{(\mathrm{color})}(\gamma_j)
  = 
  \Phi_q^{(j)}
  + 
  \varphi_0q\Phi_{\mathrm{Reeb}}^{(j)}
  + 
  \varphi_1(-q^{-1})\Phi_{\mathrm{Reeb}}^{(j)},
$$

where $+q$ and $-q^{-1}$ are the Hecke eigenvalues of $\sigma_0$ and $\sigma_1$ ([Breit--Wheeler vertex](#rem:breit-wheeler-vertex)). The bare-photon phase difference $\Delta\Phi_q$ of the [$q$-deformed path phase](#def:double-slit-q-phase) acquires a polarisation correction

$$
  \Delta\Phi_q^{(\mathrm{color})}
  = 
  \Delta\Phi_q
  + 
  (\varphi_0q - \varphi_1q^{-1})\Delta\phi_\xi,
$$

where $\Delta\phi_\xi$ is the Reeb phase mismatch. For unpolarised light ($\varphi_0 = \varphi_1$), the correction reduces to $\varphi_0(q - q^{-1})\Delta\phi_\xi$.

**2. Cross-color interference.**
When path amplitudes interfere at the detector, the product of the path states in $H_3(q)$ generates cross-color terms $\sigma_0\sigma_1$ and $\sigma_1\sigma_0$. These are the Hopf-link basis elements $L_{\pm}$ ([color content](#rem:knot-basis-color-content)). Their coefficients are $\varphi_0\psi_1$ and $\varphi_1\psi_0$. The color weights $\psi_i$ are imparted by the slit-wall Reeb interaction ([photon wavefront example](#ex:photon-wavefront)). These cross-color terms contribute a linking amplitude that modulates the fringe visibility:

$$
  V_{\mathrm{color}}
  = 
  1 - |\varphi_0\psi_1 - \varphi_1\psi_0|^2.
$$

When the slit material's color axis aligns with the photon's polarisation ($\varphi_0\psi_1 = \varphi_1\psi_0$), the Hopf-link terms cancel and visibility is maximal ($V_{\mathrm{color}} = 1$). Misalignment partially suppresses fringes. This material-dependent decoherence arises from the Hecke algebra structure, not from environmental noise.

**Observable signature.**
The color-content correction is second order in $\hbar_q$ for unpolarised light, but first order for linearly polarised light. A double-slit experiment with controlled linear polarisation exhibits a polarisation-dependent fringe shift proportional to $(\varphi_0 q - \varphi_1 q^{-1})\hbar_q\mathrm{Vol}(K_{\mathrm{mat}})$. This shift depends on the slit material's knot volume, separating it from classical birefringence.
