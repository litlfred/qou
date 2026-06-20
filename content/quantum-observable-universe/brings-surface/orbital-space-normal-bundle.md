*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**
Let $T_{2,3} \hookrightarrow \Sigma_4$ be the trefoil embedded
in the Bring's surface, and let $N = N_{T_{2,3}/\Sigma_4}$ be its
normal bundle.  At shell $n$ (framing twist $k = 2(n-1)$
relative to the Seifert framing), the space of orbital states is

$$
  \mathcal{O}_n
  = 
  \bigl\{
    \sigma \in \Gamma(N)  : 
    \mathrm{tw}(\sigma) = k, \quad
    \Delta_{T}\sigma = \lambda\sigma, \quad
    \lambda \leq \lambda_{n-1}
  \bigr\}
$$

where $\mathrm{tw}(\sigma)$ is the total twist (self-linking
relative to the Seifert framing), $\Delta_T$ is the Laplacian
on $T_{2,3}$ induced by the ambient metric, and $\lambda_\ell$
is the $\ell$-th eigenvalue.

*Claim:* $\dim \mathcal{O}_n = n^2$.

**Setup.**

The trefoil $T_{2,3}$ is a smooth closed curve of length $L$
in the Bring's surface $\Sigma_4$.  The normal bundle $N$ is a
rank-$2$ real vector bundle over $T_{2,3} \cong S^1$.  A
section $\sigma \in \Gamma(N)$ describes a transverse
displacement of the trefoil — a vibration.

The total twist $\mathrm{tw}(\sigma) = k$ constrains the
winding of $\sigma$ around the trefoil: it is the self-linking
number of the displaced curve $T_{2,3} + \epsilon\sigma$
relative to the Seifert surface.  This is the global R-I count
([Reidemeister invariance](#conj:reidemeister-mass-invariance)).

**The $q$-Laplacian on the trefoil.**

The $q$-Laplacian $\Delta_q$ on $T_{2,3} \cong S^1$ has
eigenvalues

$$
  \lambda_\ell =  [\ell]_q  [\ell + 1]_q,
  \qquad \ell = 0, 1, 2, \ldots
$$

where $[\ell]_q = (q^\ell - q^{-\ell})/(q - q^{-1})$ is the
$q$-integer.  At $q = 1$ this recovers $\ell(\ell + 1)$.
The eigenfunctions are $q$-deformed exponentials on the
circle.  Each eigenvalue $\lambda_\ell$ for $\ell \geq 1$ has
**multiplicity $2$** (cosine and sine modes).

**From $S^1$ modes to $S^2$ harmonics.**

The normal bundle $N$ is rank $2$: at each point of the
trefoil, the transverse displacement has **two independent
directions** (the two normal directions in the $3$-dimensional
ambient space of the Bring's surface).  A section $\sigma$ with
Fourier mode $\ell$ along the trefoil and direction $\hat{n}$
in the normal plane gives a vibration pattern:

$$
  \sigma(\varTheta)
  = 
  A_\ell  e^{i\ell\varTheta}  \hat{n}(\varTheta)
$$

The direction $\hat{n}(\varTheta)$ rotates as we go around the
trefoil (the normal bundle may be twisted).  The combined
mode — Fourier mode $\ell$ on $S^1$ times direction in the
normal plane — parametrises the same space as a **spherical
harmonic** $Y_\ell^m$ on the unit sphere surrounding the
proton.

This identification works because the trefoil orbits the
proton (spinning around the Borromean anchor).  The time
average of the vibrating trefoil sweeps out a sphere.  A
mode-$\ell$ vibration on the trefoil, averaged over the
trefoil's orbit, projects to the spherical harmonic
$Y_\ell^m$ on this sphere.  The magnetic quantum number
$m = -\ell, \ldots, +\ell$ labels the $2\ell + 1$
orientations of the mode relative to the Reeb axis
([categorical Reeb](#def:categorical-reeb)).

**Proof of $\dim \mathcal{O}_n = n^2$.**

At shell $n$, the energy constraint admits modes
$\ell = 0, 1, \ldots, n-1$ (modes $\ell \geq n$ have
eigenvalue $\lambda_\ell > \lambda_{n-1}$ and cost more
energy than the shell can provide).

For each mode $\ell$:
- On $S^1$: multiplicity $2$ (cosine and sine), except
  $\ell = 0$ which has multiplicity $1$.
- In the normal plane: direction $\hat{n}$ adds another
  factor.
- Combined with the $\mathrm{SO}(3)$ action on the ambient
  space: the mode-$\ell$ section space transforms as the
  irreducible representation $V_\ell$ of dimension $2\ell + 1$.

The total orbital dimension is

$$
  \dim \mathcal{O}_n
  = 
  \sum_{\ell=0}^{n-1} \dim V_\ell
  = 
  \sum_{\ell=0}^{n-1} (2\ell + 1)
  =  n^2.
  \qquad\square
$$

**The critical step.**

The non-trivial claim is that **mode $\ell$ on the trefoil
curve transforms as the irreducible $\mathrm{SO}(3)$
representation $V_\ell$ of dimension $2\ell + 1$** when
embedded in the Bring's surface.

This follows from two facts:

1. The trefoil $T_{2,3}$ orbits the proton
   ($\mathcal{B}_3$), sweeping out a topological $S^2$ in
   the time average.  The $\mathrm{SO}(3)$ symmetry of
   this $S^2$ acts on the normal-bundle sections.

2. A Fourier mode $\ell$ on $S^1$, embedded in $\mathbb{R}^3$
   via the trefoil map $\gamma: S^1 \to \Sigma_4 \hookrightarrow \mathbb{R}^3$, transforms under $\mathrm{SO}(3)$ rotations
   of the ambient space as $V_\ell$.  This is because the
   $\ell$-th Fourier mode of a curve in $\mathbb{R}^3$, when
   restricted to the unit sphere, is a degree-$\ell$ spherical
   harmonic.

**The cutoff $\ell \leq n - 1$.**

The energy of mode $\ell$ at shell $n$ is

$$
  E_\ell
  = 
  \frac{[\ell]_q  [\ell + 1]_q}{[n]_q^2} \cdot E_{\mathrm{ion}}
$$

where $E_{\mathrm{ion}} = 13.6$ eV and $[\ell]_q [\ell+1]_q$
is the $q$-Laplacian eigenvalue (centrifugal barrier).  At
$q = 1$ this reduces to $\ell(\ell+1)/n^2$.

For the mode to fit within shell $n$, we need
$[\ell]_q [\ell+1]_q \leq [n]_q [n-1]_q$, which gives
$\ell \leq n - 1$ (since $[\cdot]_q$ is monotone for
$q > 0$).
