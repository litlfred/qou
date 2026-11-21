Let $\beta = \sigma_{i_1} \cdots \sigma_{i_N}$ have Gröbner–Shirshov normal form $\mathrm{NF}_{\mathrm{GS}}(\beta) = e_{j_1} \cdots e_{j_M}$. Unlike the Markov locality of [prop:trace-locality-meets-gs-non-locality](#prop:trace-locality-meets-gs-non-locality), the reduction to normal form is non-local. This is an informal observation; no precise statement of it is proved here.

The Gröbner–Shirshov reduction algorithm on the Hecke algebra applies three rewriting rules:

- *Hecke quadratic relation:*
  $\sigma_i^2 \to (q - q^{-1}) \sigma_i + 1$ (eliminates squared
  generators).
- *Braid relation:*
  $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$
  (Yang–Baxter / commutation).
- *Far-commutativity:*
  $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $\lvert i - j \rvert
  \geq 2$.

The braid relation acts on a window of three consecutive generators,
and successive applications can propagate changes across the entire
braid word. Therefore the normal form depends non-locally on the
input — flipping a single generator in $\beta$ can require rewriting
many generators in $\mathrm{NF}_{\mathrm{GS}}(\beta)$.

**Reconciliation.** Markov locality and this non-locality concern different operations.
The first is a property of the trace and the second a property of the
reduction to normal form, so they do not conflict: the composite
$\beta \mapsto \mathrm{tr}_M(\rho(\beta))$ passes through the
non-local map $\beta \mapsto \mathrm{NF}_{\mathrm{GS}}(\beta)$, and the
trace is then evaluated on the normal form.

Whether the trace of the normal form factorises over its letters is discussed in [the product-factorisation check](#rem:trace-locality-product-factorisation-check).
