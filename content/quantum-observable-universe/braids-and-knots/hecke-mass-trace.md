Let $(\mathbf{C}, A, \tau)$ be a QOU, let $\varrho \colon \mathbf{1} \to A$
be a vortex with braid representative $\beta \in B_n$, and let
$\Phi_{\mathrm{mass}}(\beta) \in H_n(R, q)$ be its Hecke mass element
([Hecke mass element](#def:hecke-mass-element)).

**Proposition.**  The categorical mass
([mass identity](#def:mass-identity)) equals the norm of the Markov
trace of the Hecke mass element:

$$
  \mathfrak{m}(\varrho_\beta)
  \;=\;
  \bigl\lvert
    \mathrm{tr}_M\!\bigl(\Phi_{\mathrm{mass}}(\beta)\bigr)
  \bigr\rvert.
$$

Moreover, the topological decomposition
([topological mass](#thm:topological-mass)) descends to $H_n(R, q)$:

$$
  \mathrm{tr}_M\!\bigl(\Phi_{\mathrm{mass}}(\beta)\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\Phi^{\mathrm{desc}}(\beta)\bigr)
  \;+\;
  \sum_{i=1}^{N}
  \mathrm{tr}_M\!\bigl(\Phi^{\mathrm{trans}}_i(\beta)\bigr).
$$

*Proof.*  The fibre functor $\tau$ is exact and monoidal, so it
commutes with $\Delta$, $\int_A$, and the categorical trace:

1. **Particle image.**  $\tau(\varrho) = \rho(\beta) \in H_n(R, q)$
   by the Hecke quotient.

2. **Frobenius--comultiplication image.**  Since $\tau$ preserves
   monoidal structure, $\tau\bigl((\int_A \otimes \mathrm{id})
   \circ \Delta\bigr)$ is an $\mathrm{SU}_q(2)$-equivariant
   endomorphism of $V^{\otimes n}$, hence an element of $H_n(R, q)$
   by quantum Schur--Weyl duality.

3. **Trace correspondence.**  The categorical trace
   $\mathrm{tr} \colon \mathrm{End}_{\mathbf{C}}(A) \to R$
   maps under $\tau$ to the Markov trace
   $\mathrm{tr}_M \colon H_n(R, q) \to k$
   ([Jones--Markov trace](#thm:jones-markov-trace), uniqueness).

4. **Norm preservation.**  Working over the same ground ring $R$,
   $\lVert \cdot \rVert$ is preserved.

Combining: $\mathfrak{m}(\varrho) =
\lVert\mathrm{tr}(\alpha_\varrho)\rVert =
\lVert\mathrm{tr}_M(\tau(\alpha_\varrho))\rVert =
\lvert\mathrm{tr}_M(\Phi_{\mathrm{mass}}(\beta))\rvert$.

The decomposition follows because $\tau$ is exact: it preserves the
idempotent splitting $\hat{\tau}_n$, and the Markov trace is linear.

In the archimedean realisation, this gives the closed form
([topological mass formula](#prop:topological-mass-formula)):

$$
  \bigl\lvert
    \mathrm{tr}_M\!\bigl(\Phi_{\mathrm{mass}}(\beta)\bigr)
  \bigr\rvert
  \;=\;
  \frac{\mathrm{Vol}(K_\beta)}{\hbar_q^{2}}.
$$
