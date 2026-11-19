The [internal Poisson object](#def:poisson-object) makes explicit a structure implicit in the deformation theory. Over $\mathbf{C} = \mathrm{Mod}(\mathbb{F}_p)$ with $A = \mathcal{O}(H)$, this object specialises to a $p$-truncated skew-Poisson biderivation $\pi_<$.

**From Hochschild to bivectors.** The first-order deformation $\phi_1 \in HH^2(\mathcal{U}_q, \mathrm{Ad})$ of the Frobenius--Hopf algebra maps under the Hochschild--Kostant--Rosenberg isomorphism to a bivector field:

$$
\mathrm{HKR} \colon HH^2(A, A)
\xrightarrow{ \sim }
\Gamma\!\bigl(\Lambda^2 T_A\bigr)
= 
\mathrm{Hom}_{\mathbf{C}}\!\bigl(\mathbf{1},
  \Lambda^2(\Omega^1(A)^{\vee})\bigr).
$$

The image $\pi := \mathrm{HKR}(\phi_1)$ is a global section of the bivector object $\Pi$. The Jacobi identity on $\pi$ corresponds to the Maurer--Cartan equation $[\phi_1, \phi_1] = 0$.

**Internal vs. external.** The classical approach defines the Poisson bracket by passing through $\tau$ to the vector-space level and invoking HKR. The internal definition avoids this detour. The bivector $\pi \colon \mathbf{1} \to \Pi$ and the contraction live entirely inside $\mathbf{C}$.

**Model: skew-Poisson integration.** When $\mathbf{C} = \mathrm{Mod}(\mathbb{F}_p)$ and $A = \mathcal{O}(H)$, the internal Poisson object specialises to the skewed-Poisson biderivation $\pi_<$ developed in the skew-Poisson integration theory of the finite-characteristic deformation chapter. The $p$-truncated Jacobi condition is the shadow of the internal Jacobi identity modulo $p$-th powers, and skew-Poisson integration lifts $(H, \pi_<)$ to a non-commutative formal group $G / \mathbb{Z}_p$.
