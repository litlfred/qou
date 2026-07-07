<!-- FILE_START: variational-equations-intro.md -->
The canonical action $\mathfrak{S}_q$ depends on three
inputs — the Frobenius form $\int_A$, the connection $\nabla$,
and the state $\psi$ — and varying each gives one of the three
classical field equations in categorical form. Proposition: Variational equations of the categorical action, with its proof,
collects all three: varying $\int_A$ yields the **categorical
Einstein equation** $R_{\int} - \tfrac{1}{2}\mathrm{tr}(R_{\int})
\mathrm{id}_A = T_q[\nabla,\psi]$, varying $\nabla$ yields the
**categorical Yang--Mills equation** $\nabla \star_q F_\nabla +
q [F_\nabla, \star_q F_\nabla] = J_\psi$, and varying $\psi$
yields the :refterm[categorical transport]{#categorical-transport}
equation $\mathcal{D}_\nabla \psi = 0$. Remark: Wavefront propagation and the categorical Dirac equation reads the transport
equation as governing the spatial propagation of states, with
the two terms of $\mathcal{D}_\nabla$ contributing parallel
transport ($q^{-1}\nabla$) and Reeb diffraction ($(1-q^{-1})
\iota_\xi\nabla$) — the categorical origin of Gaussian beam
spreading. Example: Continuing example: photon wavefront through a double slit traces this through the explicit
double-slit geometry, predicting a material-dependent torsion
phase shift set by the hyperbolic volume of the barrier knot
type. The next section, **Particles, fermions, bosons, and
observation**, takes the transport equation and asks what kind
of solution counts as a particle.

_(draft.)_
<!-- FILE_END: variational-equations-intro.md -->

<!-- FILE_START: variational-equations.md -->
Let $\mathfrak{S}_q$ be the
([categorical action](#def:categorical-action)).  The three variational
equations are:

1. *Gravity (vary $\int_A$)*:
   $\delta\mathfrak{S}_q / \delta\!\int_A = 0$ yields the
   *categorical Einstein equation*:

   $$
     R_{\int} - \tfrac{1}{2}\mathrm{tr}(R_{\int})\mathrm{id}_A
     =  T_q[\nabla, \psi],
   $$

   where $T_q$ is the stress-energy endomorphism constructed from the
   gauge and matter terms.

2. *Gauge (vary $\nabla$)*:
   $\delta\mathfrak{S}_q / \delta\nabla = 0$ yields the
   *categorical Yang--Mills equation*:

   $$
     \nabla \star_q F_\nabla + q \cdot [F_\nabla, \star_q F_\nabla]
     =  J_\psi,
   $$

   where $J_\psi = \psi^* \otimes D_\nabla\psi - D_\nabla\psi^* \otimes \psi$
   is the matter current.

3. *Matter (vary $\psi$)*:
   $\delta\mathfrak{S}_q / \delta\psi = 0$ yields the
   *:refterm[categorical transport]{#categorical-transport} equation*:

   $$
     D_\nabla\psi =  0.
   $$

```tex
\begin{equation}\label{eq:variational-equations-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathfrak{S}_q \ar[r, "\delta/\delta\!\int_A"]
    \ar[d, "\delta/\delta\nabla"']
    \ar[dr, "\delta/\delta\psi"]
  & R_{\int} - \tfrac{1}{2}\mathrm{tr}(R_{\int})\mathrm{id} = T_q \\
  \nabla \star_q F + q[F, \star_q F] = J_\psi
  & D_\nabla \psi = 0 \ar[from=ul, crossing over]
\end{tikzcd}
\qquad\text{(variational equations)}
\end{equation}
```
<!-- FILE_END: variational-equations.md -->

<!-- FILE_START: wavefront-propagation.md -->
The third variational equation ([variational equations](#prop:variational-equations))
yields the *:refterm[categorical transport]{#categorical-transport} equation*

$$
  \mathcal{D}_\nabla\psi =  0,
$$

where $\mathcal{D}_\nabla = q^{-1}\nabla + (1-q^{-1})\iota_\xi\nabla$
is the categorical Dirac operator
([categorical Dirac operator](#def:categorical-dirac-operator)).
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
([categorical instanton](#def:categorical-instanton)).  On a flat instanton
($F_\nabla = 0$, free propagation), the Gaussian beam waist $w_0$ is
fixed by $q$ and the source geometry.  At a material boundary (slit wall),
$F_\nabla \neq 0$ and the wavefront diffracts around the edge ---
exactly the mechanism that allows a photon to illuminate both slits
simultaneously.

The Lagrangian ([categorical Lagrangian](#def:categorical-lagrangian))
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
([instanton on-shell](#rem:instanton-on-shell)).
<!-- FILE_END: wavefront-propagation.md -->

<!-- FILE_START: photon-wavefront-example.md -->
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
<!-- FILE_END: photon-wavefront-example.md -->

