<!-- FILE_START: descartes-theorem-intro.md -->
The atomic and nuclear spectra derived previously are consequences of a single structural choice: $\chi(A) = -6$. The Descartes theorem formalizes this observation into a uniqueness statement, proving that among quantum observable universes satisfying the Descartes condition, Bring's surface is the terminal object.
<!-- FILE_END: descartes-theorem-intro.md -->

<!-- FILE_START: descartes.md -->
Let $\mathbf{C}_{-6}$ denote the category of quantum observable universes over $R$ satisfying the Descartes condition $\chi(A) = -6$, with morphisms given by QOU maps that preserve the Euler characteristic. Bring's surface $\Sigma_4$ is a terminal object in $\mathbf{C}_{-6}$: for every Descartes universe $(\mathbf{C}, A, \tau)$ in $\mathbf{C}_{-6}$, there exists a unique morphism to the Bring's QOU.
<!-- FILE_END: descartes.md -->

<!-- FILE_START: terminal-morphism-brings.md -->
We construct the unique terminal morphism from any Descartes universe $(\mathbf{C}, A, \tau)$ in $\mathbf{C}_{-6}$ to Bring's QOU $(\mathbf{C}_B, A_B, \tau_B)$.

**Step 1: Match the substrate parameters.** 
Both source and target have $\chi(A) = -6$, so the Descartes condition determines $q + q^{-1} = -6$ in both. By constructive extraction, both algebras are defined over $\mathbb{Z}[q, q^{-1}]/(q^2 + 6q + 1)$. The specialisation maps $\iota, \iota_B \colon \mathbb{Z}[q, q^{-1}] \to k$ agree, yielding an isomorphism of base rings. We define $\phi_0 \colon k \to k$ as the identity.

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
<!-- FILE_END: terminal-morphism-brings.md -->

<!-- FILE_START: universality-general.md -->
For any admissible Euler characteristic $\chi$, the category $\mathbf{C}_{\chi}$ of $\mathbb{C}$ quantum observable universes with $\chi(\mathcal{S}) = \chi$ should admit a terminal object determined by the unique maximally symmetric Riemann surface of the corresponding genus. Bring's curve distinguishes the Descartes case $\chi = -6$, but analogous universal objects are expected at other values of $\chi$.
<!-- FILE_END: universality-general.md -->

<!-- FILE_START: archimedean-yekutieli.md -->
Bring's surface satisfies QU-to-QOU lifting with $\chi(A) = -6$. The non-vanishing Yekutieli classes $\kappa_n \neq 0$ obstruct smooth lifting at every level, creating twisted sectors that control inertial mass and the three lepton generations. These correspond to the three pairs of branch points under $S_3 \subset S_5$.

In the realization tower of the motivic substrate, the perpetual non-vanishing $\kappa_n \neq 0$ implies that the Frobenius character of Bring's surface is non-trivial at every finite place $p \nmid 6$. The three lepton generations then correspond to the orbits of the cyclotomic Galois group on the six branch points. The fact that there are exactly three generations is a Galois-theoretic statement, not an analytic count.
<!-- FILE_END: archimedean-yekutieli.md -->

<!-- FILE_START: observation-brings.md -->
On Bring's surface, the observation morphism $\mathfrak{O} \colon A \to A$ acts fibrewise on the state bundle $\mathcal{S} \to M$ and perturbs the substrate parameter $q(p)$, shifting the non-commutative geometry. The two-observer parallelogram applies directly: two independent observations of a fermion on Bring's surface produce a discrepancy controlled by the local Planck constant $\hbar_q(p)$.
<!-- FILE_END: observation-brings.md -->

