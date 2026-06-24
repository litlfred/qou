The chain has three steps:

**Step 1 (Categorical trace $\to$ Frobenius integral).**
The categorical trace
$\mathrm{tr}(f) = \mathrm{ev}_A \circ (f \otimes \mathrm{id}_{A^\vee}) \circ \mathrm{coev}_A$
descends under the fibre functor $\tau$ to the Frobenius integral
$\int_A : A \to R$ — the Jones--Markov trace on $H_n(R, q)$
([RJ interpretation](#rem:rj-inner-product-interpretation)),
satisfying Markov properties I and II
([vertex algebra relations](#prop:vertex-algebra-relations), QU-3).

**Step 2 (Nakayama automorphism = identity).**
The mass involves $\Psi = (\int_A \otimes \mathrm{id}) \circ \Delta$,
the **Nakayama automorphism** of the Frobenius algebra $A$.  For
Frobenius--Hopf algebras, $\Psi = S^2$.  In $H_n(R, q)$ the antipode
$S(\sigma_i) = \sigma_i^{-1}$ gives $S^2(\sigma_i) = \sigma_i$, so $\Psi = \mathrm{id}_A$.

**Step 3 (Mass = trace of cycle).**
Substituting $\Psi = \mathrm{id}$:

$$
  \mathfrak{m}_{q,\mathcal{K}}
  \;=\; \bigl\lVert \mathrm{tr}\bigl(
    \underbrace{(\textstyle\int_A \otimes \mathrm{id}) \circ \Delta}_{= \,\mathrm{id}_A}
    \circ\, \varrho \bigr) \bigr\rVert
  \;=\; \Bigl|\!\int_A\! \rho(\beta_\mathcal{K})\Bigr|.
$$
