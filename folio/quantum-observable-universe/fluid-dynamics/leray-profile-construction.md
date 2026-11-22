**The Leray rescaling.**
In Leray's similarity variables $y = (x - x_0)/\sqrt{T^* - t}$, $s = -\log(T^* - t)$, the velocity profile satisfies the Leray system. A *continuous* self-similar blowup would require a time-independent ($s$-independent) profile $(V, \Pi)$ on $\mathbb{R}^3$; such a profile with $V \in L^3(\mathbb{R}^3)$ is zero \cite{necas-ruzicka-sverak1996}, a no-go extended to $L^q$, $3 < q \leq \infty$, and to local-energy estimates \cite{tsai1998}. The profile considered here is therefore [discretely self-similar](#def:leray-profile): periodic in $s$ with some period $P > 0$. The Leray system itself does not fix $P$.

**The period.**
An identification of $P$ with the scaling $\lambda_\kappa$ of the root-of-unity ladder $q_\kappa = e^{i\pi/\kappa}$ would require evaluating at a root of unity, which [the substrate parameter](#def:substrate-parameter) excludes. No identification of $P$ is made here.

**The angular decomposition.**
A velocity field on $\mathbb{R}^3$ decomposes in angle into vector spherical harmonics of integer degree $\ell$: the sphere is $S^2 = \mathrm{SU}(2)/\mathrm{U}(1)$, and functions or vector fields on it carry only integer spin. Half-integer components $j = 1/2, 3/2, \ldots$ do not occur in a Navier--Stokes velocity field. The quadratic term $(V \cdot \nabla) V$ couples degrees $\ell_1$ and $\ell_2$ to every degree $\ell$ with $|\ell_1 - \ell_2| \le \ell \le \ell_1 + \ell_2$, so a finite set of degrees is in general not closed under the nonlinearity.

**Truncation.**
Consequently a truncation at finitely many degrees $\ell \le L$ is a Galerkin approximation of the Leray system, not an exact reduction. A discretely self-similar profile depends on $s$ periodically; after expansion in Fourier modes in $s$, the truncated system is a system of ODEs in the radial variable $r$ indexed by both the angular degree and the Fourier mode. A truncation keeping only the zero Fourier mode is $s$-independent and is the steady case excluded above.

**Boundary conditions.**
Each radial coefficient must be regular at $r = 0$, with the vanishing order set by its degree $\ell$ and the type of vector spherical harmonic. At $r \to \infty$ the profile must decay like $r^{-1}$ and no faster. Decay faster than $r^{-1}$ puts a bounded profile in $L^3$, and a discretely self-similar blow-up whose profile is continuous in $s$ with values in $L^3$ is excluded \cite{chae2013adss}; in particular a bounded square-integrable profile lies in $L^3$ and is excluded. Decay slower than $r^{-1}$ makes the velocity field unbounded away from the blow-up point. See [Exclusions for discretely self-similar profiles](#rem:leray-profile-exclusions).

**Open question.**
The coefficients of the truncated system are not specified here. Writing them down from the vector-spherical-harmonic coupling, and then deciding whether a nonzero $s$-periodic solution exists and persists as $L$ grows, is the open content of this construction. Any numerical solution of a truncated system is evidence about the truncation, not about the Leray system.
