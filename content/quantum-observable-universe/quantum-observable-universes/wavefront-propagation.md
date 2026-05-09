The third variational equation ([variational equations](#prop\:variational-equations))
yields the *:refterm[categorical transport]{#categorical-transport} equation*

$$
  \mathcal{D}_\nabla\psi =  0,
$$

where $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$
is the categorical Dirac operator
([categorical Dirac operator](#def\:categorical-dirac-operator)).
This equation governs the *spatial propagation* of a state
$\psi \colon \mathbf{1} \to A$ through the quantum observable universe:
it is the categorical analog of the classical wave equation.

The two terms of $\mathcal{D}_\nabla$ contribute distinct physical effects:

1. **Parallel transport** ($q^{-1}\nabla$): the state $\psi$ is
   covariantly transported along geodesics of the connection $\nabla$.
   At $q = 1$ this is the only term, and the wavefront propagates
   without transverse spreading --- pure ray optics.

2. **Reeb diffraction** ($(1-q^{-1})\iota_\xi\nabla$): the Reeb
   contraction $\iota_\xi$ couples $\psi$ to the vertical (contact)
   direction.  This term is responsible for *wavefront spreading*:
   the state acquires transverse amplitude proportional to the
   quantum Planck constant $\hbar_q = 1 - q^{-1}$.  As $q$ increases,
   the diffraction effect strengthens.

The spatial extent of the wavefront --- the *beam width* --- is not a free
parameter but a derived quantity: it is determined by the Green's function
of $\mathcal{D}_\nabla$ on the instanton background
([categorical instanton](#def\:categorical-instanton)).  On a flat instanton
($F_\nabla = 0$, free propagation), the Gaussian beam waist $w_0$ is
fixed by $q$ and the source geometry.  At a material boundary (slit wall),
$F_\nabla \neq 0$ and the wavefront diffracts around the edge ---
exactly the mechanism that allows a photon to illuminate both slits
simultaneously.

The Lagrangian ([categorical Lagrangian](#def\:categorical-lagrangian))
packages this as

$$
  \mathcal{L}_q(\nabla, \psi)
  = 
  \underbrace{\mathcal{D}_\nabla^{2}}_{\text{gauge (curvature)}}
  + 
  \underbrace{\psi^* \otimes \mathcal{D}_\nabla\psi}_{\text{matter (propagation)}},
$$

so that the on-shell condition $\mathcal{D}_\nabla\psi = 0$ eliminates
the matter term, leaving only the topological gauge sector
([instanton on-shell](#rem\:instanton-on-shell)).
