### Proof sketch

1. **Completeness.**  The Rosso–Jones formula decomposes
   $J_{\tau(r,s)}(q) = \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s$ into irreps of $H_r(q)$.  Every
   irrep $\lambda$ is recoverable from the torus knot data
   (by Möbius inversion on the power sums $\omega^s$).  The
   self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ provides
   the inner product.  Hence $\mathcal{E}_g$ spans the
   representation ring at each degree $\leq \lfloor 2g/(g-1) \rfloor$.

2. **Inductive chain construction.**  Each nucleon $k$ is
   added by extending the $2\!\times\!2$ chain matrices:
   $M_j \leftarrow M_j \cdot T_{j {}^j\!\bowtie_k k}(q)$
   for existing positions $j < k$, and
   $M_{k-1} = T_{(k\!-\!1) {}^{k-1}\!\bowtie_k k}(q)$ for the new
   position.  The Hecke reduction $\sigma^2 = (q - q^{-1})\sigma + 1$ is handled within each
   $2\!\times\!2$ chain — zero Yang–Baxter steps, zero Hecke
   steps on the multi-generator element.  The nuclear word
   $\mathcal{N}_{Z,N} = \prod_j (\mathfrak{w}^+_j \sigma_j + \mathfrak{w}^0_j)$ uses
   **distinct generators** and is always in Gröbner--Shirshov normal form.

3. **Shell cancellation.**  Since parent and daughter share
   all chains except those crossing the converting nucleon,
   the log ratio $\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}}) = \sum_j [\log_q \hat{V}_j^{\mathrm{dau}} - \log_q \hat{V}_j^{\mathrm{par}}]$ receives contributions
   only from generators $j$ that interact with the converting
   nucleon.

4. **Pauli projection.**  A fully occupied shell of $n$
   fermions is totally antisymmetric.  Under the Schur–Weyl
   decomposition of $H_3(q)$, the decay operator
   $T_{\beta\text{-decay}}(q)$ is projected onto the alternating irrep
   $(1^3)$ via $e_{(1^3)} \cdot T_{\beta\text{-decay}}(q) \cdot e_{(1^3)}$.
   The symmetric and standard irreps cancel in the fully
   occupied state.

5. **Tower termination.**  The degree-$k$ tower knot
   $\tau(r, s^k)$ requires genus $(r-1)(s^k - 1)/2$.  For
   $g = 4$: degree $1$ admits $4$ knots, degree $2$ admits
   $2$ knots ($\tau(2,9)$ and $\tau(3,4)$), degree $3$
   requires genus $\geq 13$ — so the jet bundle over
   $\Sigma_4$ has **exactly three non-zero levels**
   ($k = 0, 1, 2$).

Degree-$1$ knots are already encoded in $\mathcal{Q}_{\mathrm{bare}}$
through distinct vertex weights ($\mathfrak{p} {}^i\!\oplus_j \mathfrak{p}$, $\mathfrak{n} {}^i\!\oplus_j \mathfrak{n}$, $\mathfrak{p} {}^i\!\oplus_j \mathfrak{n}$ — inter-particle Hopf links with crossing indices $i, j$), so $F = 1$ for shells $1$–$4$.
The active correction comes from degree-$2$ knots only.

### Jet bundle structure

The knot operators form a **jet bundle over the exceptional
divisor chain** of $\Sigma_g$, with jet index given by the
Gröbner--Shirshov class (= degree in the degree tower) of each torus knot.

See [Table 2](#tbl:spectral-decomposition-qvalue-table2-data).

The jet decomposition is **exact and finite** — not by truncation
but by the finite dimensionality of the regular representation of
$H_n(q)$ on $\Sigma_g$.
Completeness follows from the self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ and the Rosso–Jones expansion: every irrep of $H_n(q)$ is
recoverable from the torus knot invariants, so the knots form a
complete orthogonal basis under the Markov trace inner product.
