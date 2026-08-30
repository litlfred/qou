## Proof

1. **Algebraic stratification exists.** For each $S$, $\beta_S$ is
   a well-defined element of the braid group $B_n$ (skein-smoothing
   commutes with the braid-group structure). The image
   $\rho(\beta_S)$ in $H_n(R, q)$ is an explicit Laurent polynomial
   in the Hecke generators. *Direct from the definition of
   skein smoothing.*

2. **The mass formula sums over levels.** Per the
   [mass endomorphism tower](#prop:mass-endomorphism-tower)
   formula, the categorical mass equals
   $\bigl\lvert\prod_i \hat V_i\bigr\rvert + \sum_i \Phi_q(|\hat V_i|) + z^2 \sum_{(i,j)} \Phi_q(|\hat V_i \hat V_j|)$.
   The first term corresponds to $\beta_\emptyset$ (level 0); the
   singleton sum to $\beta_{\{i\}}$ (level 1); the pair sum to
   $\beta_{\{i,j\}}$ (level 2). Identification term-by-term. *Direct.*

3. **No level $\geq 3$ contribution at fixed jet level $n$.** Per
   pentagon ascension
   ([jet-tower remark](#rem:mass-endomorphism-jet-tower) §"Pentagon
   ascension"), any would-be order-3 contribution
   $\Phi_q(|\hat V_i \hat V_j \hat V_k|)$ rewrites via the pentagon
   identity as a product of order-$\leq 2$ factors at level $n$
   plus a residual that ascends to level $(n+1)$ as a new singleton
   or pair. Iteration covers all higher orders.

4. **Each summand is in $\mathbb{Z}[q^{\pm 1/2}]$.** $\hat V_S$ is a
   Laurent polynomial in $q^{1/2}$ with integer coefficients
   ([algebraic quantum volume](#def:algebraic-quantum-volume)); the
   quantum dilogarithm $\Phi_q$ is given as a formal product
   $\prod_{n \geq 0} (1 - q^n \cdot x)$ in $\mathbb{Z}[q]\![[x]\!]$
   and reduces to a polynomial when truncated at the GB-filtration
   level appropriate for the partition data. **No convergence
   condition on $|q|$ is required for the algebraic-side statement.**

$\square$

## Relation to the JSJ archimedean bridge

The conjecture
[Φ$_q$-tower JSJ archimedean bridge](#rem:phi-q-tower-jsj-bridge)
states that under $\tau_{\mathrm{arch}}$ each algebraic stratum $S$
maps to a JSJ piece of $\widehat\beta$, with the algebraic value
$\Phi_q(|\hat V_S|)$ τ-realising to $\rho_q \cdot \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K_S)$.
That conjecture **interprets** the algebraic stratification on the
3-manifold side; the algebraic stratification itself is unconditional.

In terms of the strict Archimedean wall:

* The **statement** of the mass formula uses the algebraic
  stratification (this proposition); 3-manifold language does not
  appear.
* The **interpretation** as a JSJ-piecewise sum is a τ-image
  conjecture, on the right side of τ.
* No **proof** anywhere in the algebraic engine invokes JSJ /
  hyperbolic-volume / Mostow / Thurston as a derivation input.
