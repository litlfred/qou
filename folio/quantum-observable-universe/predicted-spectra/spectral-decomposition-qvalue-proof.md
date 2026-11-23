### Proof sketch

1. **Completeness.** The Rosso–Jones formula decomposes $J_{\tau(r,s)}(q) = \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s$ into irreps of $H_r(q)$. Every irrep $\lambda$ is recoverable from the torus knot data by Möbius inversion on the power sums $\omega^s$. The self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ provides the required inner product. Thus, $\mathcal{E}_g$ spans the representation ring at each degree $\leq \lfloor 2g/(g-1) \rfloor$.

2. **Inductive chain construction.** Each nucleon $k$ is added by extending the $2\!\times\!2$ chain matrices: $M_j \leftarrow M_j \cdot T_{j {}^j\!\bowtie_k k}(q)$ for existing positions $j < k$, and $M_{k-1} = T_{(k\!-\!1) {}^{k-1}\!\bowtie_k k}(q)$ for the new position. The Hecke reduction $\sigma^2 = (q - q^{-1})\sigma + 1$ acts strictly within each $2\!\times\!2$ chain. This demands zero Yang–Baxter steps and zero Hecke steps on the multi-generator element. The nuclear word $\mathcal{N}_{Z,N} = \prod_j (\mathfrak{w}^+_j \sigma_j + \mathfrak{w}^0_j)$ employs distinct generators, ensuring it remains in Gröbner--Shirshov normal form.

3. **Shell cancellation.** The parent and daughter nuclei share all chains except those traversing the converting nucleon. The log ratio $\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}}) = \sum_j [\log_q \hat{V}_j^{\mathrm{dau}} - \log_q \hat{V}_j^{\mathrm{par}}]$ therefore accumulates contributions only from generators $j$ that explicitly interact with the converting nucleon.

4. **Pauli projection.** A fully occupied shell of $n$ fermions is completely antisymmetric. Under the Schur–Weyl decomposition of $H_3(q)$, the decay operator $T_{\beta\text{-decay}}(q)$ projects onto the alternating irrep $(1^3)$ via $e_{(1^3)} \cdot T_{\beta\text{-decay}}(q) \cdot e_{(1^3)}$. The symmetric and standard irreps cancel entirely in the fully occupied state.

5. **Tower termination.** The degree-$k$ tower knot $\tau(r, s^k)$ demands genus $(r-1)(s^k - 1)/2$. For $g = 4$: degree $1$ admits $4$ knots, degree $2$ admits $2$ knots ($\tau(2,9)$ and $\tau(3,4)$), and degree $3$ requires genus $\geq 13$. Consequently, the jet bundle over $\Sigma_4$ possesses exactly three non-zero levels ($k = 0, 1, 2$).

Degree-$1$ knots are already encoded in $\mathcal{Q}_{\mathrm{bare}}$ through distinct vertex weights ($\mathfrak{p} {}^i\!\oplus_j \mathfrak{p}$, $\mathfrak{n} {}^i\!\oplus_j \mathfrak{n}$, $\mathfrak{p} {}^i\!\oplus_j \mathfrak{n}$ — inter-particle Hopf links with crossing indices $i, j$), so $F = 1$ for shells $1$–$4$. The active correction comes from degree-$2$ knots only.

### Jet bundle structure

The knot operators form a **jet bundle over the exceptional divisor chain** of $\Sigma_g$. The jet index is the Gröbner--Shirshov class (the degree in the degree tower) of each torus knot.

See [Table 2](#tbl:spectral-decomposition-qvalue-table2-data).

The jet decomposition is exact and finite. This finiteness arises not from truncation, but from the finite dimensionality of the regular representation of $H_n(q)$ on $\Sigma_g$. Completeness follows from the self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ and the Rosso–Jones expansion. Every irrep of $H_n(q)$ is recoverable from the torus knot invariants. Consequently, the knots form a complete orthogonal basis under the Markov trace inner product.

### Shell correction proportions

The product $\prod F(\tau, N)$ reduces to two categorically defined proportions for shells $\geq 5$ ($N > 28$).

**Degree-2 shell factor** ($F_{\mathrm{deg2}}$).
For shells at degree $2$ in the torus knot tower, the two embeddable degree-$2$ knots $\tau(2,9)$ and $\tau(3,4)$ contribute a Rosso--Jones weighted average:

$$
  F_{\mathrm{deg2}}
  = \frac{
      J(\tau(2,9)) \cdot \mathrm{tr}_M(\tau(2,9) \cdot \Delta_\beta)
    + J(\tau(3,4)) \cdot \mathrm{tr}_M(\tau(3,4) \cdot \Delta_\beta)
    }{
      \bigl(J(\tau(2,9)) + J(\tau(3,4))\bigr)
      \cdot \mathrm{tr}_M(\Delta_\beta)
    }
  \approx 3.6844,
$$

where $J(\tau(r,s)) = \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s$ is the Rosso--Jones invariant. This is the quantum-dimension weighted trace of the full twist on each irrep of $H_r(q)$. The operator $\Delta_\beta = T_{\mathrm{mix}} - T_{nn}$ is the beta-decay difference operator. The Rosso--Jones weights form the [canonical inner product on $R(H_r(q))$](#prop:rj-canonical-inner-product). Schur orthogonality forces this structure. They assign each degree-$2$ knot its Rosso--Jones invariant $J(\tau)$ with zero fitting freedom.

At $q = q_0$, with the convention-D dimensions $d_\lambda(q) = \prod_{\square}[2+c(\square)]_q/[h(\square)]_q$ (so $d_{(1^3)} = 0$), $J(\tau(2,9)) \approx 7.3936$ and $J(\tau(3,4)) \approx 16.3851$, and $\tau(3,4)$ receives approximately $2.216\times$ the weight of $\tau(2,9)$. With these weights and the convention-D traces $\mathrm{tr}_M(\tau(2,9)\cdot\Delta_\beta) \approx 0.89764$, $\mathrm{tr}_M(\tau(3,4)\cdot\Delta_\beta) \approx 0.91725$ and $\mathrm{tr}_M(\Delta_\beta) \approx 0.24730$ (for $\Delta_\beta = \sigma_0\sigma_1^{-1}$), the displayed ratio is $F_{\mathrm{deg2}} \approx 3.6844$. It exceeds $1$, so under convention D it is not a proportion and does not act as a suppression. Until 2026-10-10 this paragraph read $F_{\mathrm{deg2}} \approx 0.5904$, $J(\tau(2,9)) \approx 2.167$, $J(\tau(3,4)) \approx 5.794$ and a weight ratio of $2.67$; those are convention-C values, and $0.5904$ was the weighted average of the two traces without the division by $\mathrm{tr}_M(\Delta_\beta)$ shown in the display.

**Kummer tower decomposition.**
The two degree-$2$ knots correspond to the prime factorisation of the Euler characteristic $|\chi(A)| = 6 = 2 \times 3$ through the Kummer tower filtration ([Kummer filtration](#rem:kummer-filtration-obstruction)):

- $\tau(3,4)$ has $s = 4 = 2^2$. This is the $\mu_2$ branch of the Kummer tower (even/odd parity).
- $\tau(2,9)$ has $s = 9 = 3^2$. This is the $\mu_3$ branch (threefold symmetry).

The Chinese Remainder Theorem decomposition $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ produces exactly these two independent components. The Rosso--Jones weights are the quantum dimensions of the corresponding Kummer components. Then $J(\tau(3,4)) > J(\tau(2,9))$, because the $\mu_2$ component (parity) possesses a larger quantum dimension in the degree-$2$ representation ring than the $\mu_3$ component (threefold symmetry).

**Pauli exclusion factor** ($F_{\mathrm{Pauli}}$).
For magic-number neutron shells ($N \in \{2, 8, 20, 28, 50, 82, 126\}$), the filled shell projects onto the alternating irrep $(1^3)$ via the Young symmetrizer $e_{(1^3)}$:

$$
  F_{\mathrm{Pauli}}
  = \frac{|\mathrm{tr}_{\mathrm{alt}}(\Delta_\beta)|}
         {|\mathrm{tr}(\Delta_\beta)|}
  = \frac{|\lambda_{\mathrm{alt}}|}{|\lambda_{\mathrm{sym}}|},
$$

where $\mathrm{tr}_{\mathrm{alt}}$ evaluates each Hecke word $w$ with eigenvalue $(-q^{-1})^{\ell(w)}$ (alternating channel) and $\mathrm{tr}$ uses $q^{\ell(w)}$ (symmetric channel). This evaluates the ratio of alternating to symmetric eigenvalues of $\Delta_\beta$ in the $6 \times 6$ regular representation of $H_3(q)$. These character evaluations do not involve the Markov parameter. For $\Delta_\beta = \sigma_0\sigma_1^{-1}$ both characters equal $1$, so this ratio is $1$; the value $0.6382$ quoted here until 2026-10-10 is not reproduced by this definition, and its producer could not be located. The Markov-trace form of the Pauli case in the corollary vanishes identically under convention D, because the Ocneanu weight of $(1^3)$ is zero at $z = q^3/(q^2+1)$.

**Combined formula.**
For a $\beta^-$ decay with the converting neutron in shell degree $d$ and neutron occupation parity $p$:

$$
  Q
  = \mathcal{Q}_{\mathrm{bare}}
    \times F_{\mathrm{deg2}}^{[d \geq 2]}
    \times F_{\mathrm{Pauli}}^{[N \in \mathrm{magic}]},
$$

where $[\cdot]$ is the Iverson bracket. Whereas the Convention-C trace gave a non-zero combined product $F_{\mathrm{deg2}} \times F_{\mathrm{Pauli}} = 0.5904 \times 0.6382 \approx 0.377$, under Convention D $F_{\mathrm{deg2}} \approx 3.6844$ and the Markov-trace Pauli factor is $0$. The formula was intended for magic-number nuclei in heavy shells. An example is ${}^{137}\mathrm{Cs}$ with $N = 82$.
