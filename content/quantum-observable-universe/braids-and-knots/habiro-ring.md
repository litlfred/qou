**Definition.**
*The **Habiro ring** is the inverse limit*

$$
  \widehat{\mathbb{Z}[q]}
  \;=\;
  \varprojlim_n \;
  \mathbb{Z}[q] \big/ \bigl((q;q)_n\bigr)
$$

*where $(q;q)_n = (1-q)(1-q^2)\cdots(1-q^n)$ is the
$q$-Pochhammer symbol.  It is the cyclotomic completion
of $\mathbb{Z}[q]$: every element specialises to
$\mathbb{Z}[\zeta]$ at every root of unity $\zeta$.*

The Habiro ring is the natural home for quantum invariants
because:

1. **Universality.**  The colored Jones polynomials
   $J_N(K; q)$ for all $N$ coexist as a single element of
   $\widehat{\mathbb{Z}[q]}$ (Habiro, 2002).  In
   $\mathbb{Z}[q, q^{-1}]$ alone, the $J_N$ are separate
   objects; in $\widehat{\mathbb{Z}[q]}$ they unify.

2. **Embedding.**  The Laurent polynomial ring
   $\mathbb{Z}[q, q^{-1}]$ embeds into
   $\widehat{\mathbb{Z}[q]}$.  The Hecke algebra
   $H_n(R, q) = \mathbb{Z}[q, q^{-1}][B_n] / (\sigma_i^2 -
   H_A\sigma_i - 1)$ and its normal form coefficients
   $c_w \in \mathbb{Z}[q, q^{-1}]$ embed naturally.

3. **The algebraic quantum volume**
   ([algebraic quantum volume](#def:algebraic-quantum-volume))
   $\mathrm{Vol}_q(\beta) = \prod \hat{V}_i(q)$ is a
   finite product of Laurent polynomials, hence already in
   $\mathbb{Z}[q^{1/2}, q^{-1/2}]
   \subset \widehat{\mathbb{Z}[q^{1/2}]}$.

4. **Specialisation to volume.**  At roots of unity
   $q = e^{2\pi i/N}$, the Kashaev invariant recovers the
   hyperbolic volume via:

   $$
     \lvert J_N(K; e^{2\pi i/N}) \rvert
     \;\sim\;
     \exp\!\Bigl(\frac{N}{2\pi}\,
       \mathrm{Vol}(S^3 \setminus K)\Bigr)
   $$

   At $q = q_0$ (our substrate parameter, not a root of
   unity), the evaluation gives the mass via the algebraic
   quantum volume.

The distinction between **nuclear volume** and **particle
volume** is:

- **Nuclear volume**
  $\mathrm{Vol}_q(\mathcal{N}(Z,N)) = \prod_{i=0}^{A-2}
  \hat{V}_i(q)$: a finite product in
  $\mathbb{Z}[q^{1/2}, q^{-1/2}]$.  Already computed
  exactly by the transfer matrix.

- **Particle volume**
  $\mathrm{Vol}_q(K) = \prod_{n=1}^{\infty}
  (\text{tower contribution at level } n)$: an infinite
  product requiring the Habiro completion.  This is the
  categorical version of the Volume Conjecture.
