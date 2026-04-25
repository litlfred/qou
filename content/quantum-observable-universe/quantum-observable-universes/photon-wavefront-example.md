We trace the wavefront propagation equation
$\mathcal{D}_\nabla\psi = 0$
([wavefront propagation](#rem:wavefront-propagation)) through the
concrete geometry of a double-slit experiment, with the photon as the
test particle.  In the QOU, a photon is not the bare identity
$\mathbf{1}$ but a **photon with color content**
$\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$
([color content](#rem:knot-basis-color-content)), where the Hecke
generators encode polarisation on the exceptional divisor
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$.  The identity
component ($K = \varnothing$, the empty knot) is purely horizontal
([boson](#def:fermion-boson-decomposition): vertical component $\alpha_V = 0$); the color
dressing $\varphi_i\sigma_i$ adds polarisation-dependent Reeb phase.

**Setup.**  A photon source emits a state
$\psi \colon \mathbf{1} \to A$ with $\psi \in \mathcal{H}_{q,H}^k$
(purely horizontal, [boson](#def:fermion-boson-decomposition): $\alpha_V = 0$).
The photon travels through three regions:

1. **Free propagation** (source $\to$ barrier).
   The connection is the flat instanton: $F_\nabla = 0$, so
   $c_2 = 0$.  The Dirac operator reduces to

   $$
     \mathcal{D}_\nabla\psi
     = 
     q^{-1}\nabla\psi + (1-q^{-1})\iota_\xi\nabla\psi
     =  0.
   $$

   Since $\psi$ is horizontal ($\pi_V\psi = 0$), the Reeb contraction
   $\iota_\xi\nabla\psi$ extracts only the vertical part of the
   connection's action on $\psi$.  On a flat background this produces
   a Gaussian spreading: the beam waist $w_0$ is set by $q$ and
   the source geometry.  As $q \to 1$, $\hbar_q \to 0$ and
   $w_0 \to 0$ (ray limit); as $q$ increases, the beam spreads.

2. **Slit interaction** (barrier).
   The barrier material consists of localized knots
   ([localized knot](#def:localized-knot)) with knot type
   $K_{\mathrm{mat}}$ (e.g. Borromean rings $6_2^3$ for nucleons).
   At the slit walls the connection $\nabla$ is no longer flat:
   $F_\nabla \neq 0$, and the instanton condition $\star_q F_\nabla = F_\nabla$
   constrains the curvature to be self-dual with topological charge
   determined by $K_{\mathrm{mat}}$.

   The photon wavefront encounters two openings (slits of width $d$,
   separation $D$).  At each slit wall, the Reeb term
   $(1-q^{-1})\iota_\xi\nabla$ imparts a *torsion phase*:

   $$
     \tau(y)
     = 
     \hbar_q \cdot \mathrm{Vol}(K_{\mathrm{mat}}) \cdot \eta(y)^2 \cdot k w,
   $$

   where $\eta = |y|/(d/2)$ is the normalized slit coordinate,
   $k = 2\pi/\lambda$ is the wavenumber, and $w$ is the slit
   thickness.  This is the $q$-deformed Huygens--Fresnel correction:
   the torsion is strongest at the slit walls ($\eta = 1$) and
   vanishes at center ($\eta = 0$).

3. **Post-slit propagation** (barrier $\to$ screen).
   After passing through the slits, $\psi$ again satisfies
   $\mathcal{D}_\nabla\psi = 0$ on a flat background, but now with
   boundary conditions set by the two slit openings.  The wavefront
   from each slit interferes, producing the intensity pattern

   $$
     I(x)
     = 
     \left|
       \sum_{s=1}^{2}
       \int_{-d/2}^{d/2}
       e^{ik(r_1+r_2)}
       e^{i\tau(y)}
       e^{-y_s^2/w_0^2}
       dy
     \right|^2,
   $$

   where $r_1, r_2$ are the source-to-slit and slit-to-screen
   distances, $y_s$ is the slit coordinate measured from slit center
   $s$, and the Gaussian factor $e^{-y_s^2/w_0^2}$ is the beam
   envelope determined by the free-propagation solution.

**QOU prediction.**  The torsion correction $\tau(y)$ is absent in the
classical ($q = 1$) double-slit formula.  Its magnitude depends on
$\mathrm{Vol}(K_{\mathrm{mat}})$, the hyperbolic volume of the barrier
material's knot type.  Different slit materials (silicon vs. gold vs.
carbon) have different dominant knot types and hence different
$\mathrm{Vol}(K_{\mathrm{mat}})$, producing *material-dependent
fringe shifts* --- a signature absent in standard quantum mechanics,
testable with current technology.

**Color-content correction.**  When the photon carries non-trivial
color content $(\varphi_0, \varphi_1)$, each polarisation mode
$\sigma_i$ acquires its own Hecke eigenvalue ($+q$ or $-q^{-1}$)
weighting the torsion phase $\tau(y)$.  The corrected torsion becomes

$$
  \tau^{(\mathrm{color})}(y)
  = 
  \tau(y)
  + 
  (\varphi_0q - \varphi_1q^{-1})
  \hbar_q \cdot \mathrm{Vol}(K_{\mathrm{mat}}) \cdot \eta(y)^2 \cdot k w,
$$

which reduces to $\tau(y)$ for bare photons ($\varphi_0 = \varphi_1 = 0$).
For linearly polarised light the correction is first order in $\hbar_q$
and depends on the polarisation angle, providing a measurable signature
distinct from classical birefringence.
