The [Descartes theorem](#thm:descartes) asserts that for every
Descartes universe $(\mathbf{C}, A, \tau)$ in $\mathbf{C}_{-6}$,
there exists a *unique* morphism to the
[Bring's QOU](#prop:brings-is-qou). We construct this morphism
step by step.

**Setup.** Let $(\mathbf{C}, A, \tau)$ be any QOU with
$\chi(A) = -6$ and $(\mathbf{C}_B, A_B, \tau_B)$ be Bring's QOU
with $A_B = \mathcal{O}_q(\mathrm{SU}(2))$,
$\mathbf{C}_B = \mathrm{Rep}(\mathrm{SU}_q(2))$, and $\tau_B$ the
forgetful functor.

**Step 1: match the substrate parameters.** Both source and target
have $\chi(A) = -6$, so the Descartes condition determines
$q + q^{-1} = -6$ in both. By the
[constructive extraction](#ex:substrate-parameter-brings), both
algebras are defined over
$\mathbb{Z}[q, q^{-1}]/(q^2 + 6q + 1)$. The specialisation maps
$\iota, \iota_B \colon \mathbb{Z}[q, q^{-1}] \to k$ agree, giving an
isomorphism of base rings. Define $\phi_0 \colon k \to k$ as the
identity.

**Step 2: construct the :refterm[monoidal functor]{#monoidal-functor}.** The fibre functor
$\tau \colon \mathbf{C} \to \mathrm{Vect}_k$ is exact, faithful,
and monoidal. By Tannaka–Krein reconstruction
([constructive reconstruction](#ex:tannaka-krein-su2)), the
source algebra $A$ is recovered as
$\mathrm{coend}(\tau^\vee \otimes \tau)$. Since both $A$ and $A_B$
satisfy the same Hecke relation $(T - q)(T + q^{-1}) = 0$ with the
*same* $q$, the reconstructed Hopf algebras are isomorphic. Define:

$$
  F \colon \mathbf{C} \xrightarrow{\tau} \mathrm{Vect}_k
  \xleftarrow{\tau_B} \mathbf{C}_B.
$$

The :refterm[monoidal functor]{#monoidal-functor} $\Phi = \tau_B^{-1} \circ \tau$ (well-defined
up to natural isomorphism by Tannaka equivalence) is the desired
morphism on categories.

**Step 3: construct the algebra map.** The functor $\Phi$ induces
a Hopf algebra homomorphism $\phi \colon A \to A_B$ by applying
$\Phi$ to the regular representation. Concretely, $\phi$ maps
the generators of $A$ to those of $A_B$:

$$
  \phi(\alpha_A) = \alpha_B, \quad
  \phi(\beta_A) = \beta_B, \quad
  \phi(\bar\alpha_A) = \bar\alpha_B, \quad
  \phi(\bar\beta_A) = \bar\beta_B,
$$

where both sets of generators satisfy the same
$\mathcal{O}_q(\mathrm{SU}(2))$ relations (since $q$ is the same).
The Frobenius forms are compatible:
$\int_{A_B} \circ\, \phi = \int_A$ because both are Haar states.

**Step 4: verify uniqueness.** Suppose $\phi'$ is another such
morphism. Then $\tau_B \circ \Phi' \cong \tau_B \circ \Phi \cong \tau$
as monoidal functors. By Tannaka–Krein rigidity (the automorphism
group of $\tau_B$ is $G_q$ acting by inner automorphisms), there
exists $g \in G_q$ with $\Phi' = \mathrm{Ad}(g) \circ \Phi$. But
morphisms in $\mathbf{C}_{-6}$ must preserve the Haar state, and the
Haar state is $G_q$-invariant
([vacuum state uniqueness](#prop:vacuum-state)), so
$\int_{A_B} \circ\, \phi' = \int_{A_B} \circ\, \phi$. This forces
$\phi' = \phi$ as Frobenius-algebra homomorphisms. $\square$

**Summary.** The terminal morphism is constructed in four steps:
(1) match substrate parameters via the Descartes condition,
(2) build a :refterm[monoidal functor]{#monoidal-functor} via Tannaka–Krein,
(3) extract the Hopf algebra map on generators,
(4) verify uniqueness via Haar-state rigidity.
Every step is algorithmic — no non-constructive choices are made.
