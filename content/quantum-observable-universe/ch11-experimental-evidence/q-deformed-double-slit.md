The [substrate parameter](#def:substrate-parameter) $q$ is not merely a formal algebraic interpolation between classical and quantum regimes. It encodes a physical deformation of wave propagation through matter: the slit material acts as a defining boundary of the brane, where the Reeb vector field exerts a geometric push on the traversing test particle.

At the categorical level, wave propagation is governed by the
categorical Dirac equation
([categorical Dirac operator](#def:categorical-dirac-operator)):

$$\mathcal{D}_\nabla\,\psi \;=\; 0,$$

where $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$
([variational equations](#prop:variational-equations), equation 3).
The test particle $\psi$ is a photon --- a purely horizontal
$q$-harmonic form ([boson](#def:fermion-boson-decomposition), knot type
$K = \varnothing$) --- propagating on an instanton background
([categorical instanton](#def:categorical-instanton)).

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
\Delta\phi \;=\; \Delta\phi_{\mathrm{classical}} \;+\; \hbar_q \int_{\gamma} \pi_V \circ d,
```

where the second term integrates the vertical Reeb differential along $\gamma$. The magnitude of this correction depends on the torsion intensity of the slit material. A nucleon modeled as a [localized knot](#def:localized-knot) with the topology of the Borromean rings $6_2^3$ determines a specific value of $q$ via the local substrate map, and hence a definite $\hbar_q$. Heavier atoms with more complex knotted configurations produce correspondingly larger deformations, yielding a material-dependent signature in the fringe spacing that is absent in the standard double-slit analysis.

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
