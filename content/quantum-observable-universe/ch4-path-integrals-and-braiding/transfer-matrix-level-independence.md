Let $H = [K_1, \ldots, K_n]_c \bowtie \mathcal{L}$ be a hadron
with composite knot $K_H = \hat{\beta}_H$.  Let $\mathcal{T}(H)$
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
     P_{K_H}(q).
   $$

2. **Path independence on $E_p$.**  Two braiding operations
   $T_1, T_2$ on $H$ that produce isotopy-equivalent
   configurations
   ([isotopy equivalence](#def:bundle-isotopy-equivalence))
   have the same categorical transfer matrix:
   $\mathcal{T}(T_1) = \mathcal{T}(T_2)$.  In particular, the
   specific sequence of crossing changes within the exceptional
   divisor $E_p$ does not affect the result --- only the
   equivalence class of the final configuration matters.

3. **Well-definedness.**  The categorical transfer matrix
   $\mathcal{T}(H)$ depends only on the isotopy class of the
   hadron $H$ and the knot types $K_i$ of its constituents.
   It is independent of:
   - the braid representative $\beta_H$,
   - the PawLei embedding $\iota_{j_i}$ for each constituent,
   - the order of crossings evaluated within $E_p$.
