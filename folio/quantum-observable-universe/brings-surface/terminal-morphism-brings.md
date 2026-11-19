The unique terminal morphism from any Descartes universe $(\mathbf{C}, A, \tau)$ in $\mathbf{C}_{-6}$ to Bring's QOU $(\mathbf{C}_B, A_B, \tau_B)$ is constructed in four steps.

**Step 1: Match the aether parameters.** 
Both source and target have $\chi(A) = -6$, so the Descartes condition determines $q + q^{-1} = -6$ in both. By constructive extraction, both algebras are defined over $\mathbb{Z}[q, q^{-1}]/(q^2 + 6q + 1)$. The specialisation maps $\iota, \iota_B \colon \mathbb{Z}[q, q^{-1}] \to k$ agree, yielding an isomorphism of base rings. Define $\phi_0 \colon k \to k$ as the identity.

**Step 2: Construct the :refterm[monoidal functor]{#monoidal-functor}.** 
The fibre functor $\tau \colon \mathbf{C} \to \mathrm{Vect}_k$ is exact, faithful, and monoidal. By Tannaka–Krein reconstruction, the source algebra $A$ is recovered as $\mathrm{coend}(\tau^\vee \otimes \tau)$. Since both $A$ and $A_B$ satisfy the Hecke relation $(T - q)(T + q^{-1}) = 0$ with identical $q$, the reconstructed Hopf algebras are isomorphic. Define:
$$
  F \colon \mathbf{C} \xrightarrow{\tau} \mathrm{Vect}_k
  \xleftarrow{\tau_B} \mathbf{C}_B.
$$
The :refterm[monoidal functor]{#monoidal-functor} $\Phi = \tau_B^{-1} \circ \tau$ is the desired morphism on categories.

**Step 3: Construct the algebra map.** 
The functor $\Phi$ induces a Hopf algebra homomorphism $\phi \colon A \to A_B$ by mapping the generators of $A$ to those of $A_B$:
$$
  \phi(\alpha_A) = \alpha_B, \quad
  \phi(\beta_A) = \beta_B, \quad
  \phi(\bar\alpha_A) = \bar\alpha_B, \quad
  \phi(\bar\beta_A) = \bar\beta_B.
$$
Both sets of generators satisfy the $\mathcal{O}_q(\mathrm{SU}(2))$ relations. The Frobenius forms are compatible ($\int_{A_B} \circ\, \phi = \int_A$) because both are Haar states.

**Step 4: Verify uniqueness.** 
Suppose $\phi'$ is another such morphism. Then $\tau_B \circ \Phi' \cong \tau_B \circ \Phi \cong \tau$ as monoidal functors. By Tannaka–Krein rigidity, there exists $g \in G_q$ with $\Phi' = \mathrm{Ad}(g) \circ \Phi$. Because morphisms in $\mathbf{C}_{-6}$ must preserve the Haar state, and the Haar state is $G_q$-invariant, $\int_{A_B} \circ\, \phi' = \int_{A_B} \circ\, \phi$. This forces $\phi' = \phi$ as Frobenius-algebra homomorphisms. 
