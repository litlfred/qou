Let $\mathfrak{H}_p = [K_1, \ldots, K_n]_p \bowtie \mathcal{L}$ be a hadron
with composite knot $K_{\mathfrak{H}} = \hat{\beta}_{\mathfrak{H}}$.  Let $\mathcal{T}(\mathfrak{H}_p)$
be the categorical transfer matrix
([categorical transfer matrix](#def:categorical-transfer-matrix)).
Then:

1. **Constituent-composite agreement.**  The Markov trace computed
   by operating on the constituent variables $(z_1, \ldots, z_n)$
   and the Markov trace computed from the composite knot variable
   $z_H$ yield the same Skein polynomial:

   $$
     \prod_{i=0}^{n-2} \hat{V}_i^{\mathrm{const}}(q)
     \;=\;
     \hat{V}^{\mathrm{comp}}(q)
     \;=\;
     P_{K_{\mathfrak{H}}}(q).
   $$

2. **Path independence on $\mathcal{S}_p$.**  Two braiding operations
   $T_1, T_2$ on $\mathfrak{H}$ that produce isotopy-equivalent
   configurations
   ([isotopy equivalence](#def:bundle-isotopy-equivalence))
   have the same categorical transfer matrix:
   $\mathcal{T}(T_1) = \mathcal{T}(T_2)$.  In particular, the
   specific sequence of crossing changes within the exceptional
   divisor $\mathcal{S}_p$ does not affect the result --- only the
   equivalence class of the final configuration matters.

3. **Well-definedness.**  The categorical transfer matrix
   $\mathcal{T}(\mathfrak{H})$ depends only on the isotopy class of the
   hadron $\mathfrak{H}$ and the knot types $K_i$ of its constituents.
   It is independent of:
   - the braid representative $\beta_{\mathfrak{H}}$,
   - the PawLei embedding $\iota_{j_i}$ for each constituent,
   - the order of crossings evaluated within $\mathcal{S}_p$.
