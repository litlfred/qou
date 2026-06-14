**Conjecture (graded Baer-* on $\mathcal{H}_q$ across the depth filtration).**

*Let $\mathcal{H}_q$ be the substrate convolution Hopf algebra
([Frobenius–Hopf substrate](#def:frobenius-hopf-substrate)),
filtered by iterated-integral depth
([keystone correspondence](#conj:gb-depth-period-correspondence)):*

$$
  G^{(0)}(\mathcal{H}_q) \;\subseteq\; G^{(1)}(\mathcal{H}_q)
  \;\subseteq\; G^{(2)}(\mathcal{H}_q) \;\subseteq\; \cdots.
$$

*Each filtration piece $G^{(n)}(\mathcal{H}_q)$ is a Baer-*-ring
under the bar involution, and the inclusions $G^{(n)} \hookrightarrow
G^{(n+1)}$ are **Baer-*-morphisms**: they send projections to
projections and preserve the annihilator-generation property.
Equivalently: $\mathcal{H}_q$ admits a system of orthogonal
projections $\{p_n^{(i)}\}_{n,i}$ indexed by depth $n$ and
intra-depth label $i$, with*

- *each $p_n^{(i)}$ self-adjoint under $* \colon q \mapsto q^{-1}$,*
- *$p_n^{(i)} p_m^{(j)} = 0$ when $(n, i) \neq (m, j)$,*
- *$\sum_{i} p_n^{(i)} \cdot \mathrm{id}_{G^{(n)}} = \mathrm{id}_{G^{(n)}}$
  (completeness at each depth).*

### Why this is the right structural statement

Three free consequences if discharged:

1. **Explicit Goncharov-period witnesses.** Each projection
   $p_n^{(i)} \cdot \mathrm{Li}_n^q(z)$ under $\tau_{\mathrm{arch}}$
   generates a *specific* element of $\mathcal{P}_n / \mathcal{P}_{n-1}$
   — naming a real-number period class with a finite algebraic
   label. (Without graded Baer-*, B1 only asserts existence.)
2. **Graded Mikusiński localisation.** The field-of-fractions tower
   $\mathcal{M}_q^{(n)}$ inherits a graded Baer-* structure: each
   $\mathcal{M}_q^{(n)}$ is itself Baer-*, with its "delta at depth
   $n$" $= 1/\omega^n$ on the surreal envelope corresponding to a
   specific projection. The graded Titchmarsh question
   ([keystone §discharge targets](#conj:gb-depth-period-correspondence))
   gets a clean handle: zero divisors at depth $n$ are detected by
   non-trivial $p_n^{(i)} \cdot p_n^{(j)}$ for $i \neq j$.
3. **Bar-involution-equivariant period theory.** Self-adjoint
   $p_n^{(i)}$ generate *real* periods (bar-fixed loci of $\mathcal{P}_n$);
   bar-swapped pairs generate *chirality-twisted* periods (eigenspaces
   of bar with eigenvalue $-1$ — equivalently, periods of motives
   with a Tate twist). See
   [`rem:chirality-period-pairing`](#rem:chirality-period-pairing).

### Reduction to known structure

At depth 0 (scalars + $\exp_q$): Baer-* is trivial — $G^{(0)}$ is a
field.

At depth 1 ($\log_q$ adjoined): the analogue is Baker's theorem
infrastructure — annihilators of $\log\alpha$-relations among
algebraic $\alpha$'s. Baer-* at this depth corresponds to the
*linear independence* of logarithms of multiplicatively
independent algebraics (Baker 1966; Wüstholz). Conjecturally
known.

At depth 2 ($\mathrm{Li}_2^q$ adjoined): reduces to the Hecke
algebra Baer-* result
([`prop:hecke-baer-star-generic`](#prop:hecke-baer-star-generic))
since the depth-2 grouplikes pair with $H_n(q)$-cells via the
Markov trace. The projections are the Hoefsmit $e_\lambda$,
lifted to $\mathcal{H}_q$ via Schur–Weyl duality.

At depth $\geq 3$: open. The depth-3 case requires identifying
projections compatible with the trilog grouplike $\mathrm{Li}_3^q$
— see the depth-3 witness
([`conj:bring-trilog-depth-3-witness`](#conj:bring-trilog-depth-3-witness)).
