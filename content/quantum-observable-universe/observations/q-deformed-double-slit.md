The [substrate parameter](#def:substrate-parameter) $q$ is not merely a formal algebraic interpolation between classical and quantum regimes. Instead, it encodes a physical deformation of wave propagation through matter. The slit material acts as a defining boundary of the brane, where the Reeb vector field exerts a geometric push on the traversing test particle.

At the categorical level, wave propagation is governed by the
categorical Dirac equation
([categorical Dirac operator](#def:categorical-dirac-operator)):

$$\mathcal{D}_\nabla\psi =  0,$$

where $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$
([variational equations](#prop:variational-equations), equation 3).
The test particle $\psi$ is a photon --- not a bare identity
$\mathbf{1}$ but a **photon with color content**
$\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$
([color content](#rem:knot-basis-color-content)), where $\sigma_0$
and $\sigma_1$ are the horizontal and vertical polarisation generators
and $\sigma_0\sigma_1$ is the Hopf link dressing
on $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$
([Breit--Wheeler vertex](#rem:breit-wheeler-vertex)) --- propagating
on an instanton background
([categorical instanton](#def:categorical-instanton)).  The identity
component $\mathbf{1}$ (degree $0$) propagates as pure horizontal
flux; the generators $\varphi_i\sigma_i$ (degree $1$) carry
additional polarisation-dependent phase from the Hecke eigenvalues
$+q$ and $-q^{-1}$.

Recall the $q$-deformed differential from [the local substrate proposition](#prop:local-substrate-q):

$$d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d.$$

As $q \to 1$, the quantum Planck constant $\hbar_q = 1 - q^{-1}$ vanishes, and $d_q \to d$. In this limit the vertical component drops out entirely, recovering standard classical interference. For $q > 1$, however, the vertical differential $\pi_V \circ d$ introduces a transverse momentum shift that modifies the interference pattern.

The Reeb contraction term $(1-q^{-1})\iota_\xi\nabla$ in $\mathcal{D}_\nabla$ is
the physical mechanism behind wavefront spreading
([wavefront propagation](#rem:wavefront-propagation)): it is what allows a photon
emitted from a point source to illuminate both slits simultaneously.  The beam
width $w_0$ at the barrier is not a free parameter but is determined by the
Green's function of $\mathcal{D}_\nabla$ on the flat instanton background
($F_\nabla = 0$) between source and barrier.

The accumulated phase difference for a path $\gamma$ grazing the fermionic slit boundary is

```tex
\Delta\phi =  \Delta\phi_{\mathrm{classical}} +  \hbar_q \int_{\gamma} \pi_V \circ d,
```

where the second term integrates the vertical Reeb differential along $\gamma$. The magnitude of this correction depends on the torsion intensity of the slit material. A nucleon modeled as a [localized knot](#def:localized-knot) with the topology of the Borromean rings $6_2^3$ determines a specific value of $q$ via the local substrate map, and hence a definite $\hbar_q$. Consequently, heavier atoms with more complex knotted configurations produce correspondingly larger deformations, yielding a material-dependent signature in the fringe spacing that is absent in the standard double-slit analysis.

On an instanton background the Lagrangian simplifies
([instanton on-shell](#rem:instanton-on-shell)):

$$\mathcal{L}_q\big|_{\text{instanton}} = c_2(A) + \psi^* \otimes \mathcal{D}_\nabla\psi,$$

so the gauge sector is topological ($c_2$ fixed by the barrier material's knot
type) and all observable physics is in $\mathcal{D}_\nabla\psi = 0$.  The
complete derivation of the intensity pattern from $\mathcal{D}_\nabla\psi = 0$,
including the torsion phase profile, is given in
[the photon wavefront example](#ex:photon-wavefront).

An interactive simulation of this effect is available in the
[q-deformed double-slit simulator](q-double-slit.html), which
allows real-time sweeps of $q$, slit geometry, and torsion parameters
against the classical baseline.

## Color content and polarisation-dependent interference

The photon color content $(\varphi_0, \varphi_1)$ modifies the
double-slit analysis in two ways.

**1. Polarisation-weighted phase.**
Each polarisation mode $\sigma_i$ acquires its own Reeb phase along
path $\gamma_j$ through slit $j$.  The total phase for a color-dressed
photon is

$$
  \Phi_q^{(\mathrm{color})}(\gamma_j)
  = 
  \Phi_q^{(j)}
  + 
  \varphi_0q\Phi_{\mathrm{Reeb}}^{(j)}
  + 
  \varphi_1(-q^{-1})\Phi_{\mathrm{Reeb}}^{(j)},
$$

where $+q$ and $-q^{-1}$ are the Hecke eigenvalues of $\sigma_0$ and
$\sigma_1$ respectively
([Breit--Wheeler vertex](#rem:breit-wheeler-vertex)).  The bare-photon
phase difference $\Delta\Phi_q$ of the
[$q$-deformed path phase](#def:double-slit-q-phase) acquires a
polarisation correction

$$
  \Delta\Phi_q^{(\mathrm{color})}
  = 
  \Delta\Phi_q
  + 
  (\varphi_0q - \varphi_1q^{-1})\Delta\phi_\xi,
$$

where $\Delta\phi_\xi$ is the Reeb phase mismatch between the two
paths.  For unpolarised light ($\varphi_0 = \varphi_1$) the correction
reduces to $(\varphi_0)(q - q^{-1})\Delta\phi_\xi$, proportional to
the Hecke parameter $h = q - q^{-1}$.

**2. Cross-color interference (Hopf-link terms).**
When a photon's path amplitudes interfere at the detector, the product
of the two path states in $H_3(q)$ generates cross-color terms
$\sigma_0\sigma_1$ and $\sigma_1\sigma_0$ --- the Hopf-link basis
elements $L_{\pm}$
([color content](#rem:knot-basis-color-content)).  Their coefficients
$\varphi_0\psi_1$ and $\varphi_1\psi_0$ (where $\psi_i$ are the
color weights imparted by the slit-wall Reeb interaction --- the
same torsion mechanism that produces $\tau(y)$ in the
[photon wavefront example](#ex:photon-wavefront)) contribute a
**linking amplitude** that modulates the fringe visibility:

$$
  V_{\mathrm{color}}
  = 
  1 - |\varphi_0\psi_1 - \varphi_1\psi_0|^2.
$$

When the slit material's color axis is aligned with the
photon's polarisation ($\varphi_0\psi_1 = \varphi_1\psi_0$), the
Hopf-link terms cancel and visibility is maximal ($V_{\mathrm{color}} = 1$).
Misalignment between the photon's color content and the slit-wall
dressing partially suppresses fringes --- a **material-dependent
decoherence** arising from the Hecke algebra structure rather than
from environmental noise.

**Observable signature.**
The color-content correction is second order in $\hbar_q$ for
unpolarised light but first order for linearly polarised light.
A double-slit experiment with controlled linear polarisation
(e.g.\ a Wollaston prism before the slits) would exhibit a
polarisation-dependent fringe shift proportional to
$(\varphi_0 q - \varphi_1 q^{-1})\hbar_q\mathrm{Vol}(K_{\mathrm{mat}})$,
distinguishable from any classical birefringence effect because
it depends on the slit material's knot volume, not on its
refractive index.
