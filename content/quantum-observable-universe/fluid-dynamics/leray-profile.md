> **Summary.** Near the blowup time $T^*$, the singular NS
> solution approaches a self-similar Leray profile $V(\xi)$ on
> the rescaled coordinate $\xi = (x-x_0)/\sqrt{T^*-t}$.  The QOU
> representation theory constrains this profile to a finite-
> dimensional ansatz: $V$ is a sum of weight-$j$ matrix entries
> of $\mathrm{SU}_q(2)$ representations, with coefficients fixed
> by the singular gerbe data $(\Sigma, n^*, \kappa_{n^*})$.

Near the blowup time $T^*$, the
[NS-singular solution](#thm:ns-singularity-descartes) approaches
a self-similar profile.  The QOU representation theory constrains
this profile to a finite-dimensional ansatz.

**The Leray rescaling.**
Set $\tau = -\ln(T^* - t)$ and
$\xi = (x - x_0)/\sqrt{T^* - t}$.  The velocity field
$v(x, t) = (T^* - t)^{-1/2}V(\xi)$ satisfies the
**Leray equations**:

$$
  -\frac{1}{2}V
  - \frac{1}{2}(\xi \cdot \nabla)V
  + (V \cdot \nabla)V
  = 
  -\nabla P + \nu\Delta V,
  \qquad
  \nabla \cdot V = 0.
$$

These are a time-independent elliptic PDE for the profile
$(V, P)$ on $\mathbb{R}^3$.  A self-similar blowup occurs iff
a nontrivial solution exists with $V \in L^2(\mathbb{R}^3)$.

**The $\mathrm{SU}_q(2)$ decomposition.**
By the [Peter--Weyl theorem](#thm:quantum-peter-weyl), the
profile decomposes into matrix coefficients:

$$
  V(\xi)
  = 
  \sum_{j \geq 0}
  \sum_{m,n=-j}^{j}
  c^j_{mn}D^j_{mn}(\hat\xi)R_j(|\xi|),
$$

where $\hat\xi = \xi/|\xi|$, $D^j_{mn}$ are the spin-$j$
matrix coefficients on the unit sphere, and $R_j(r)$ is the
radial profile at spin $j$.

The Leray equations decompose by spin:

$$
  -\frac{1}{2}R_j
  - \frac{1}{2}rR_j'
  + \sum_{j_1, j_2}
    N^j_{j_1 j_2}R_{j_1}R_{j_2}'
  = 
  \nu\!\left(R_j'' + \frac{2}{r}R_j'
    - \frac{[j]_q[j+1]_q}{r^2}R_j\right),
$$

where $N^j_{j_1 j_2}$ are the nonlinear coupling coefficients,
determined by the Clebsch--Gordan decomposition
$V_{j_1} \otimes V_{j_2} = \bigoplus_J V_J$.

**Truncation by the discrete spectrum.**
The [discrete vortex spectrum](#prop:discrete-vortex-spectrum)
shows that the eigenvalues $[j]_q[j+1]_q$ grow exponentially
in $j$.  The centrifugal barrier $[j]_q[j+1]_q/r^2$ in the
radial equation suppresses high-spin components: for $j$
large, $R_j(r) \sim r^{[j]_q}$ near $r = 0$, which vanishes
faster than any power.

At the physical value $q \approx 1.110$, the
[Planck--Reynolds analysis](#rem:planck-reynolds) gives
$k_{\max} \approx 4$ active modes.  The self-similar profile
is effectively a **finite sum**:

$$
  V(\xi)
   \approx 
  \sum_{j=0}^{2}
  \sum_{m,n}
  c^j_{mn}D^j_{mn}(\hat\xi)R_j(|\xi|),
$$

with spins $j = 0, 1/2, 1, 3/2, 2$.  This is a
finite-dimensional ansatz with
$\sum_{j=0}^{2}(2j+1)^2 = 1 + 4 + 9 + 16 + 25 = 55$
angular coefficients and 5 radial functions.

**The truncated Leray system.**
Substituting the truncated ansatz into the Leray equations
gives a system of 5 coupled ODEs for
$(R_0, R_{1/2}, R_1, R_{3/2}, R_2)$ in the radial variable $r$:

For each $j \in \{0, 1/2, 1, 3/2, 2\}$:

$$
  \nu\!\left(R_j'' + \frac{2}{r}R_j'
    - \frac{\lambda_j}{r^2}R_j\right)
  + \frac{1}{2}R_j
  + \frac{1}{2}rR_j'
  = 
  \sum_{\substack{j_1, j_2 \\ j \in j_1 \otimes j_2}}
  N^j_{j_1 j_2}R_{j_1}R_{j_2}',
$$

where $\lambda_j = [j]_q[j+1]_q$ and
$N^j_{j_1 j_2} \neq 0$ only when $j$ appears in the
Clebsch--Gordan decomposition of $V_{j_1} \otimes V_{j_2}$.

**Boundary conditions.**

- $r \to 0$: regularity requires
  $R_j(r) \sim r^{\ell_j}$ where $\ell_j$ is the smallest
  non-negative integer with
  $\ell_j(\ell_j + 1) \geq \lambda_j$.  For $q \approx 1.110$:
  $\ell_0 = 0$, $\ell_{1/2} = 1$, $\ell_1 = 1$,
  $\ell_{3/2} = 2$, $\ell_2 = 3$.

- $r \to \infty$: $V \in L^2$ requires
  $R_j(r) = O(r^{-5/2})$ (faster than the self-similar
  decay $r^{-1}$).

**The nonlinear coupling matrix.**
The coefficients $N^j_{j_1 j_2}$ encode which spin interactions
drive the blowup.  The fusion rules
$V_{j_1} \otimes V_{j_2} = \bigoplus_J V_J$ constrain:

| $j_1 \otimes j_2$ | Contains $j$ | Coupling |
|---|---|---|
| $\frac{1}{2} \otimes \frac{1}{2}$ | $0, 1$ | Electron-electron |
| $\frac{1}{2} \otimes 1$ | $\frac{1}{2}, \frac{3}{2}$ | Electron-photon |
| $1 \otimes 1$ | $0, 1, 2$ | Photon-photon |
| $\frac{1}{2} \otimes \frac{3}{2}$ | $1, 2$ | Generation mixing |

The dominant interaction driving the blowup is the
$j = 1/2 \otimes 1/2 \to 0$ channel: two fundamental vortices
(the anti-parallel pair) fuse into the trivial representation
(annihilation), releasing their energy into the radial
compression.

**The fundamental profile ($j = 1/2$ only).**
The simplest nontrivial ansatz retains only $j = 1/2$:

$$
  V(\xi) = cD^{1/2}_{mn}(\hat\xi)R(|\xi|),
$$

with a single radial ODE:

$$
  \nu\!\left(R'' + \frac{2}{r}R'
    - \frac{[1/2]_q[3/2]_q}{r^2}R\right)
  + \frac{1}{2}R + \frac{1}{2}rR'
  = 
  N^{1/2}_{1/2,1/2}RR'.
$$

This is a second-order nonlinear ODE with two boundary
conditions ($R \sim r$ at $r = 0$, $R = O(r^{-5/2})$ at
$r = \infty$).  The nonlinear eigenvalue problem has a
discrete spectrum of solutions parametrised by the number
of zeros of $R$ — exactly the
[vortex intensity levels](#prop:discrete-vortex-spectrum).

**What remains.**
The existence of a nontrivial solution to the truncated
Leray ODE with the specified boundary conditions is a
**finite-dimensional shooting problem**: find the initial slope
$R'(0)$ such that the solution decays at infinity.  This is
numerically tractable (standard boundary-value ODE solvers).
An analytical proof of existence would use topological methods
(Leray--Schauder degree theory) on the finite-dimensional
system.

The QOU contribution is the **finite truncation**: the classical
Leray equations are an infinite-dimensional elliptic PDE.  The
$\mathrm{SU}_q(2)$ representation theory reduces it to a
finite system of 5 coupled radial ODEs, or in the simplest case
a single nonlinear ODE.  This is where the constructive
counter-example becomes feasible.
