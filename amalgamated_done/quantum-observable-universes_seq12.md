<!-- FILE_START: archimedean-intro.md -->
We specialise the categorical framework to the archimedean setting, where the base ring is an archimedean field $K$ and the quantum universe is realised by CR geometry on a contact manifold. The abstract categorical structures acquire concrete geometric meaning as differential-geometric objects on a CR manifold equipped with a pseudo-Hermitian structure. 
<!-- FILE_END: archimedean-intro.md -->

<!-- FILE_START: c-quantum-universe.md -->
Let $K$ be an archimedean field. A quantum universe over $K$ is realised by the $4$-tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$, where $\varTheta$ is a contact form on a CR manifold $M$, $G = \mathrm{SU}(2)$ is the gauge group, and $\mathcal{S}$ is the state bundle carrying the quantum degrees of freedom. 

Specifically:
1. $M$ is a CR manifold of hypersurface type with non-degenerate Levi form of signature $(r,s)$.
2. $\varTheta$ is a pseudo-Hermitian structure on $M$, determining the Levi distribution $H = \ker\varTheta$, the Reeb vector field $\xi$, the Webster metric $g_\varTheta$, and the Levi form $L_\varTheta$.
3. $G = \mathrm{SU}(2)$.
4. $\mathcal{S} = P \times_G \mathbb{P}^1(\mathbb{C}) \to M$ is the associated state bundle, where $P \to M$ is the principal $G$-bundle.

The monoidal category is $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$, the Frobenius--Hopf object is $A = \mathcal{O}_q(\mathrm{SU}(2))$ with Frobenius form given by the Haar state, and the fibre functor $\tau$ is the forgetful functor to $K\text{-}\mathrm{Mod}$.
<!-- FILE_END: c-quantum-universe.md -->

<!-- FILE_START: notation-special-cases.md -->
The symbol $\varTheta$ denotes the contact form in the archimedean $4$-tuple $(\mathbf{C}, \varTheta, G, \mathcal{S})$. When the category $\mathbf{C}$ is understood, we abbreviate to $(\varTheta, G, \mathcal{S})$. The strictly pseudoconvex case corresponds to signature $(n,0)$, yielding a positive-definite Webster metric $g_\varTheta$ and a well-defined Hodge star. 
<!-- FILE_END: notation-special-cases.md -->

<!-- FILE_START: c-quantum-observable-universe.md -->
An archimedean quantum observable universe is an archimedean quantum universe $(\mathbf{C}, \varTheta, G, \mathcal{S})$ satisfying the vanishing conditions:

$$
  H^0(M, \mathrm{Ad}(P)) = 0
  \qquad\text{and}\qquad
  \Gamma_c(M, \mathcal{S}) = 0.
$$

These analytic conditions are the archimedean realisation of the categorical observability conditions. The Frobenius non-degeneracy of the Haar state on $\mathcal{O}_q(\mathrm{SU}(2))$ and the irreducibility of the instanton connection force $H^0(M, \mathrm{Ad}(P)) = 0$. The section-vanishing $\Gamma_c(M, \mathcal{S}) = 0$ follows from the non-existence of $A$-equivariant sections of the associated $\mathbb{P}^1(\mathbb{C})$-bundle.
<!-- FILE_END: c-quantum-observable-universe.md -->

<!-- FILE_START: archimedean-realisations.md -->
In the archimedean setting, categorical structures specialise to geometric objects:

1. **Volume constraint:** The Levi form $L_\varTheta = -id\varTheta|_{H \times H}$ is non-degenerate on the rank-$4$ distribution $H = \ker\varTheta$, realising the categorical volume form $\epsilon \colon \Lambda^2 V \to \mathbf{1}$. The induced Hodge star forces the structure group to be $\mathrm{SU}(2)$.
2. **Involution:** The categorical involution $\sigma$ becomes the identification $\mathbb{P}^1(\mathbb{C}) \cong S^2 \subset \mathfrak{su}(2)$.
3. **Variational equations:** The categorical Einstein equation reduces to $\mathrm{Ric}_{g_\varTheta} = T^{(q)}$. The transport equation reduces to the Schrodinger equation $J\hbar_q\iota_{\xi_q} D_A \psi = \hat{H}_q \psi$.
<!-- FILE_END: archimedean-realisations.md -->

<!-- FILE_START: affine-light-cone-figure.md -->
The affine light-cone wedge over the brane locus sits in the spacetime affine chart $z = x_0/x_1 \in \mathbb{CP}^1$.

The brane curve is the locus $\{(z, X_{\mathrm{real}}(z)) : z \in [-1.5, 2.5]\}$ where $X_{\mathrm{real}}(z)$ is the real root of the canonical Bring chiral cubic

$$
  X^3 + (z+1)\, X^2 + (z^2+z+1)\, X + (z^3 + z^2 + z + 1) = 0.
$$

The cubic's discriminant has six complex zeros; the real interval $z \in [-1.5, 2.5]$ avoids these branch points, making $X_{\mathrm{real}}$ a single-valued smooth function. Two lines bound a wedge opening from the vertex $(-1.5, X_{\mathrm{real}}(-1.5)) \approx (-1.5, 0.811)$ toward the horizon at $z = 2.5$. The wedge is a 2D bounded region of the spacetime-affine-chart $(z, X)$-plane.

The observer sits at the substrate point $q_0 \approx 1.1099786$ on the brane at $(q_0, X_{\mathrm{real}}(q_0)) \approx (1.110, -1.743)$. The Euler-characteristic constraint $\chi(A) = -6$ fixes the algebraic substrate's topology.
<!-- FILE_END: affine-light-cone-figure.md -->
