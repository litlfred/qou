**The Leray rescaling.**
In Leray's similarity variables $y = (x - x_0)/\sqrt{T^* - t}$, $s = -\log(T^* - t)$, the velocity profile satisfies the Leray system. A *continuous* self-similar blowup would require a time-independent ($s$-independent) profile $(V, P)$ on $\mathbb{R}^3$ with $V \in L^2(\mathbb{R}^3)$; every such nontrivial finite-energy profile is trivial \cite{necas-ruzicka-sverak1996}, a no-go extended to local-energy estimates \cite{tsai1998}. The admissible profile is therefore **discretely self-similar** — periodic in $s$ — with period fixed by the root-of-unity scaling $\lambda_\kappa$.

**The $\mathrm{SU}_q(2)$ decomposition.**
By the Peter--Weyl theorem, the profile decomposes into matrix coefficients. The Leray equations decompose by spin. The nonlinear coupling coefficients are determined by the Clebsch--Gordan decomposition.

**Truncation by the discrete spectrum.**
The discrete vortex spectrum eigenvalues grow exponentially in $j$. The centrifugal barrier suppresses high-spin components. At the physical value $q \approx 1.110$, $k_{\max} \approx 4$ active modes. The discretely self-similar profile is a finite sum.

**The truncated Leray system.**
Substituting the truncated ansatz gives a system of 5 coupled ODEs in the radial variable $r$, the $s$-periodicity being carried by the ansatz coefficients.

**Boundary conditions.**
Regularity at $r \to 0$ requires $R_j(r) \sim r^{\ell_j}$. Square-integrability at $r \to \infty$ requires $R_j(r) = O(r^{-5/2})$.

**The nonlinear coupling matrix.**
The fusion rules constrain which spin interactions drive the blowup. The dominant interaction is the $j = 1/2 \otimes 1/2 \to 0$ channel: two fundamental vortices fuse into the trivial representation, releasing energy into radial compression.

**The fundamental profile ($j = 1/2$ only).**
The simplest nontrivial ansatz retains only $j = 1/2$. This yields a second-order nonlinear ODE with two boundary conditions. The nonlinear eigenvalue problem has a discrete spectrum of solutions.

**Open question.**
The existence of a nontrivial discretely self-similar solution to the truncated Leray ODE is a finite-dimensional shooting problem; the continuous ($s$-independent) case is excluded \cite{necas-ruzicka-sverak1996}, so any solution must carry genuine $s$-periodicity. The QOU contribution is the finite truncation: the classical Leray equations are infinite-dimensional, but $\mathrm{SU}_q(2)$ representation theory reduces them to a finite system of ODEs.
