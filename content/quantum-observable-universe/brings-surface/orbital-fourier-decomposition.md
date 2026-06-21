*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark)).**
Let $\varrho: S^1 \hookrightarrow \Sigma_4$ be the trefoil
$T_{2,3}$ embedded in the Bring's surface, and let
$N = N_{\varrho/\Sigma_4}$ be the normal bundle.  The four
quantum numbers $(n, \ell, m, s)$ arise from the Fourier
decomposition of sections $\sigma \in \Gamma(N)$ as follows.

**The normal bundle.**

The trefoil $\varrho(S^1)$ is a smooth closed curve in the
$3$-dimensional Bring's surface $\Sigma_4$ (viewed locally as a
real $3$-manifold via the spatial realization functor).  The
normal bundle $N$ is a rank-$2$ real vector bundle over
$S^1$:

$$
  N_p =  T_p \Sigma_4 / T_p \varrho
  \qquad\text{for } p \in \varrho(S^1).
$$

At each point of the trefoil, $N_p \cong \mathbb{R}^2$ — two
independent transverse directions.  A section
$\sigma \in \Gamma(N)$ is a smooth choice of transverse
displacement at each point of the trefoil.

**Parametrisation.**

Let $\varTheta \in [0, 2\pi)$ parametrise the trefoil
$\varrho(\varTheta)$.  A section decomposes as

$$
  \sigma(\varTheta)
  = 
  \sum_{\ell=0}^{\infty}
  \bigl(
    a_\ell \cos(\ell\varTheta) + b_\ell \sin(\ell\varTheta)
  \bigr)
  \hat{n}_1(\varTheta)
  + 
  \sum_{\ell=0}^{\infty}
  \bigl(
    c_\ell \cos(\ell\varTheta) + d_\ell \sin(\ell\varTheta)
  \bigr)
  \hat{n}_2(\varTheta)
$$

where $\hat{n}_1(\varTheta), \hat{n}_2(\varTheta)$ are an
orthonormal frame for $N_{\varrho(\varTheta)}$ that rotates
smoothly as $\varTheta$ varies.

The **total framing twist** is

$$
  k =  \mathrm{tw}(\sigma)
  = 
  \frac{1}{2\pi} \oint_{S^1}
  \kappa(\sigma, \hat{n}_1)  d\varTheta
$$

where $\kappa$ is the rotation angle of $\sigma$ relative to
the Seifert framing.  The shell number is
$n = k/2 + 1$ ([Reidemeister
invariance](#conj:reidemeister-mass-invariance)).

**The four quantum numbers.**

**(1) Principal quantum number $n$.**

The total twist $k = 2(n-1)$ is the **global R-I count** —
the self-linking number relative to the Seifert framing.  It
constrains the total energy:

$$
  E_n =  -\frac{E_{\mathrm{ion}}}{n^2}.
$$

The twist $k$ is the norm-squared of $\sigma$ in the $L^2$
sense:

$$
  k = 
  \sum_{\ell=0}^{\infty}
  \ell  (a_\ell^2 + b_\ell^2 + c_\ell^2 + d_\ell^2).
$$

At fixed $k = 2(n-1)$, only finitely many Fourier modes can
be nonzero.

**(2) Angular momentum quantum number $\ell$.**

The $\ell$-th Fourier mode is the **$\ell$-th resonance
frequency** of the trefoil's transverse vibration.  Mode
$\ell$ has wavelength $L/\ell$ on the trefoil (where $L$ is
the trefoil length) and eigenvalue
$\lambda_\ell = [\ell]_q [\ell + 1]_q$ under the
**$q$-Laplacian** $\Delta_q$, where

$$
  [\ell]_q =  \frac{q^\ell - q^{-\ell}}{q - q^{-1}}
$$

is the $q$-integer.  At $q = 1$, this recovers the classical
eigenvalue $\ell(\ell + 1)$.  At $q = q_0$, the
$q$-deformation shifts the eigenvalues:

| $\ell$ | $\ell(\ell+1)$ | $[\ell]_q [\ell+1]_q$ | Shift |
|-------:|------:|------:|------:|
| 0 | 0 | 0 | 0 |
| 1 | 2 | 2.012 | $+0.6\%$ |
| 2 | 6 | 6.139 | $+2.3\%$ |
| 3 | 12 | 12.55 | $+4.6\%$ |

The shifts are of order $(q - 1)^2 \sim \alpha^2$, producing
the **fine-structure splitting** between sub-shells at the
same $n$.

The energy constraint at shell $n$ admits modes
$\ell = 0, 1, \ldots, n-1$ only: modes $\ell \geq n$ require
more twist than available at framing $k = 2(n-1)$.

**(3) Magnetic quantum number $m$.**

At each Fourier mode $\ell$, the section $\sigma$ vibrates in
the $2$-dimensional normal plane $N_p$.  The trefoil is
embedded in $\Sigma_4 \hookrightarrow \mathbb{R}^3$ (via
spatial realization), so the normal plane is embedded in
$\mathbb{R}^3$.  The vibration at mode $\ell$ can be
**oriented** in the ambient space.

The $\mathrm{SO}(3)$ rotation group acts on $\mathbb{R}^3$
and hence on the normal-bundle sections.  Under this action,
the mode-$\ell$ sections transform as the **irreducible
representation $V_\ell$** of $\mathrm{SO}(3)$, with
dimension $2\ell + 1$.  The magnetic quantum number
$m = -\ell, \ldots, +\ell$ labels the weight spaces of
$V_\ell$ relative to the Reeb axis
([categorical Reeb](#def:categorical-reeb)):

$$
  V_\ell = 
  \bigoplus_{m=-\ell}^{+\ell} \mathbb{C} \cdot Y_\ell^m
$$

where $Y_\ell^m$ is the spherical harmonic — the restriction
of the mode-$\ell$ vibration pattern to the unit sphere
around the proton.

**Why $V_\ell$ and not some other representation.**  The
Fourier mode $\ell$ on $S^1$, transported to $\mathbb{R}^3$
by the embedding $\varrho$, generates a function on the
sphere $S^2$ surrounding the proton (the time-averaged orbit
of the trefoil).  This function is a **homogeneous harmonic
polynomial of degree $\ell$** restricted to $S^2$, which is
by definition a spherical harmonic.  The space of degree-$\ell$
spherical harmonics is $V_\ell$ with $\dim V_\ell = 2\ell + 1$.

**(4) Spin quantum number $s$.**

The fiber adjoint involution
([fiber adjoint involution](#prop:fiber-adjoint-involution))
acts on the normal bundle by exchanging the two orientations
of the Hopf link between the electron and proton.  This is
an involution $\sigma \mapsto -\sigma$ on $\Gamma(N)$ that
commutes with the Laplacian and the $\mathrm{SO}(3)$ action.

Each orbital $(n, \ell, m)$ splits into two states under this
involution:

$$
  s = +\tfrac{1}{2}: \quad
  \sigma  \text{in the } (+1)\text{-eigenspace},
  \qquad
  s = -\tfrac{1}{2}: \quad
  \sigma  \text{in the } (-1)\text{-eigenspace}.
$$

This doubles the orbital count: each of the $n^2$ orbitals
holds $2$ states, giving $2n^2$ states per shell.

**Summary.**

$$
  \Gamma(N)\big|_{k=2(n-1)}
   \cong 
  \bigoplus_{\ell=0}^{n-1}
  \bigoplus_{m=-\ell}^{+\ell}
  \bigoplus_{s=\pm 1/2}
  \mathbb{C}
  \qquad
  \text{(dimension } 2n^2\text{)}
$$

| Quantum number | Fourier origin | Representation |
|:-:|---|---|
| $n$ | Total framing twist $k = 2(n-1)$ | Energy shell |
| $\ell$ | Fourier mode on $S^1$ | $\mathrm{SO}(3)$ irreducible $V_\ell$ |
| $m$ | Weight in $V_\ell$ (Reeb projection) | Spherical harmonic $Y_\ell^m$ |
| $s$ | Fiber adjoint involution eigenvalue | Spin $\pm 1/2$ |
