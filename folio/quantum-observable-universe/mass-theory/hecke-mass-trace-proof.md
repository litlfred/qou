*Argument sketch.*  The fibre functor $\tau$ is exact and monoidal, so it
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
   $\lVert \cdot \rVert$ is taken to be preserved. This step is
   asserted, not proved, and it is one reason the statement is a
   conjecture.

Combining: $\mathfrak{m}(\varrho) =
\lVert\mathrm{tr}(\alpha_\varrho)\rVert =
\lVert\mathrm{tr}_M(\tau(\alpha_\varrho))\rVert =
\lvert\mathrm{tr}_M(\Phi_{\mathrm{mass}}(\beta))\rvert$.

The trace-level split follows because $\tau$ is exact: it preserves the
idempotent splitting $\hat{\tau}_n$, and the Markov trace is linear.
This step is a theorem once the element splits. It does not give the
norm-level decomposition of the mass, which is
[conj:topological-mass](#conj:topological-mass).

In the archimedean realisation, the conjectured closed form is
([topological mass formula](#conj:topological-mass-formula)):

$$
  \bigl\lvert
    \mathrm{tr}_M\!\bigl(\Phi_{\mathrm{mass}}(\beta)\bigr)
  \bigr\rvert
  \;=\;
  \frac{\mathrm{Vol}(K_\beta)}{\hbar_q^{2}}.
$$
