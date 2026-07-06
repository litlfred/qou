The [internal Poisson object](#def:poisson-object) makes explicit a
structure that is already implicit in the paper's deformation theory.
Concretely, over $\mathbf{C} = \mathrm{Mod}(\mathbb{F}_p)$ with
$A = \mathcal{O}(H)$ that object is the $p$-truncated skew-Poisson
biderivation $\pi_<$ of
[skew-Poisson integration](#prop:skew-poisson-integration) — the image
under the fibre functor $\tau$ of the bivector $\pi$ constructed below.
The remainder of this block builds that bivector from the Hochschild
picture and recovers $\pi_<$ as its shadow.

**From Hochschild to bivectors.**
The first-order deformation $\phi_1 \in HH^2(\mathcal{U}_q, \mathrm{Ad})$
of the Frobenius--Hopf algebra
([classical limit obstruction](#def:classical-limit-obstruction))
maps under the Hochschild--Kostant--Rosenberg isomorphism to a
bivector field:

$$
\mathrm{HKR} \colon HH^2(A, A)
\xrightarrow{ \sim }
\Gamma\!\bigl(\Lambda^2 T_A\bigr)
= 
\mathrm{Hom}_{\mathbf{C}}\!\bigl(\mathbf{1},
  \Lambda^2(\Omega^1(A)^{\vee})\bigr).
$$

The image $\pi := \mathrm{HKR}(\phi_1)$ is precisely a global section
of the bivector object $\Pi$ from the
[Poisson object definition](#def:poisson-object).  The Jacobi identity
on $\pi$ corresponds to the Maurer--Cartan equation
$[\phi_1, \phi_1] = 0$ in the Hochschild complex.

**Internal vs.\ external.**
The classical approach defines the Poisson bracket on $A$ by
passing through $\tau$ to the vector-space level and invoking HKR
there.  The internal definition avoids this detour: the bivector
$\pi \colon \mathbf{1} \to \Pi$ into the bivector object $\Pi$ and the
contraction
$\langle \pi, {-} \rangle$ live entirely inside $\mathbf{C}$, using
only the Frobenius self-duality $A \cong A^{\vee}$ and the
differential calculus $\Omega^{\bullet}(A)$.

**Model: skew-Poisson integration.**
When $\mathbf{C} = \mathrm{Mod}(\mathbb{F}_p)$ and $A = \mathcal{O}(H)$
for a commutative formal group $H$, the internal Poisson object
specialises to the skewed-Poisson structure $\pi_<$ of
[skew-Poisson integration](#prop:skew-poisson-integration): the
biderivation $\pi_<$ is the image of $\pi$ under $\tau$, and the
$p$-truncated Jacobi condition is the shadow of the internal Jacobi
identity modulo $p$-th powers.  The integration theorem then lifts
$(H, \pi_<)$ to a non-commutative formal group $G / \mathbb{Z}_p$
whose distribution algebra deforms $\mathrm{Dist}(H)$ while
preserving the Frobenius relation.
