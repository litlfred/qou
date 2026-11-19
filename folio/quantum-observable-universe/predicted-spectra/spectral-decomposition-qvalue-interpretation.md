The torus knots embeddable on $\Sigma_4$ form a **complete, self-dual basis** for the regular representation of the Iwahori--Hecke algebra $H_n(q)$. The $Q$-value of beta decay is the spectral decomposition of the decay operator in this basis. The decomposition is **exact and finite**. It terminates at degree $2$ because the embeddability bound on $\Sigma_4$ kills all higher jets.

### The six embeddable torus knots on $\Sigma_4$

See [Table 1](#tbl:spectral-decomposition-qvalue-table1-data).

Degree-$1$ knots are already encoded in $\mathcal{Q}_{\mathrm{bare}}$ through distinct vertex weights ($\mathfrak{p} {}^i\!\oplus_j \mathfrak{p}$, $\mathfrak{n} {}^i\!\oplus_j \mathfrak{n}$, $\mathfrak{p} {}^i\!\oplus_j \mathfrak{n}$ — inter-particle Hopf links with crossing indices $i, j$), so $F = 1$ for shells $1$–$4$. The active correction comes from degree-$2$ knots only.

### Jet bundle structure

The knot operators form a **jet bundle over the exceptional divisor chain** of $\Sigma_g$. The jet index is the Gröbner--Shirshov class (the degree in the degree tower) of each torus knot.

See [Table 2](#tbl:spectral-decomposition-qvalue-table2-data).

The jet decomposition is exact and finite. This finiteness arises not from truncation, but from the finite dimensionality of the regular representation of $H_n(q)$ on $\Sigma_g$. Completeness follows from the self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ and the Rosso–Jones expansion. Every irrep of $H_n(q)$ is recoverable from the torus knot invariants. Consequently, the knots form a complete orthogonal basis under the Markov trace inner product.

### Geometric interpretation

Each factor in $Q$ reads geometrically:

See [Table 3](#tbl:spectral-decomposition-qvalue-table3-data).

The ratio $\hbar_q / \ln q = 0.9496$ is the **discretisation correction**. The exceptional divisors are $q$-spaced (discrete), not $e$-spaced (continuous).

### Shell correction proportions

The product $\prod F(\tau, N)$ reduces to two categorically defined proportions for shells $\geq 5$ ($N > 28$):

**Degree-2 shell factor** ($F_{\mathrm{deg2}}$).
For shells at degree $2$ in the torus knot tower, the two embeddable degree-$2$ knots $\tau(2,9)$ and $\tau(3,4)$ contribute a **Rosso--Jones weighted average**:

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

where $J(\tau(r,s)) = \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s$ is the Rosso--Jones invariant (the quantum-dimension weighted trace of the full twist on each irrep of $H_r(q)$), and $\Delta_\beta = T_{\mathrm{mix}} - T_{nn}$ is the beta-decay difference operator. The Rosso--Jones weights are the [canonical inner product on $R(H_r(q))$](#prop:rj-canonical-inner-product). Schur orthogonality forces this structure; they assign each degree-$2$ knot its Rosso--Jones invariant $J(\tau)$ with zero fitting freedom.

At $q = q_0$, with the convention-D dimensions $d_\lambda(q) = \prod_{\square}[2+c(\square)]_q/[h(\square)]_q$ (so $d_{(1^3)} = 0$), $J(\tau(2,9)) \approx 7.3936$ and $J(\tau(3,4)) \approx 16.3851$, and $\tau(3,4)$ receives approximately $2.216\times$ the weight of $\tau(2,9)$. With these weights and the convention-D traces $\mathrm{tr}_M(\tau(2,9)\cdot\Delta_\beta) \approx 0.89764$, $\mathrm{tr}_M(\tau(3,4)\cdot\Delta_\beta) \approx 0.91725$ and $\mathrm{tr}_M(\Delta_\beta) \approx 0.24730$ (for $\Delta_\beta = \sigma_0\sigma_1^{-1}$), the displayed ratio is $F_{\mathrm{deg2}} \approx 3.6844$. It exceeds $1$, so under convention D it is not a proportion and does not act as a suppression. <!-- literal-source: unnormalised Rosso-Jones average at z = q^{1/2}/(q+1) --> Until 2026-10-10 this paragraph read $F_{\mathrm{deg2}} \approx 0.5904$, $J(\tau(2,9)) \approx 2.167$, $J(\tau(3,4)) \approx 5.794$ and a weight ratio of $2.67$; those are convention-C values, and $0.5904$ was the weighted average of the two traces without the division by $\mathrm{tr}_M(\Delta_\beta)$ shown in the display.

**Kummer tower decomposition.**
The two degree-$2$ knots correspond to the prime factorisation of the Euler characteristic $|\chi(A)| = 6 = 2 \times 3$ through the Kummer tower filtration ([Kummer filtration](#rem:kummer-filtration-obstruction)):

- $\tau(3,4)$ has $s = 4 = 2^2$. This is the **$\mu_2$ branch** of the Kummer tower (even/odd parity).
- $\tau(2,9)$ has $s = 9 = 3^2$. This is the **$\mu_3$ branch** (threefold symmetry).

The Chinese Remainder Theorem decomposition $\mathbb{Z}/6\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ produces exactly these two independent components. The Rosso--Jones weights are the quantum dimensions of the corresponding Kummer components. $J(\tau(3,4)) > J(\tau(2,9))$ because the $\mu_2$ component (parity) possesses a larger quantum dimension in the degree-$2$ representation ring than the $\mu_3$ component (threefold symmetry).

**Pauli exclusion factor** ($F_{\mathrm{Pauli}}$).
For magic-number neutron shells ($N \in \{2, 8, 20, 28, 50, 82, 126\}$), the filled shell projects onto the alternating irrep $(1^3)$ via the Young symmetrizer $e_{(1^3)}$:

$$
  F_{\mathrm{Pauli}}
  = \frac{|\mathrm{tr}_{\mathrm{alt}}(\Delta_\beta)|}
         {|\mathrm{tr}(\Delta_\beta)|}
  = \frac{|\lambda_{\mathrm{alt}}|}{|\lambda_{\mathrm{sym}}|},
$$

where $\mathrm{tr}_{\mathrm{alt}}$ evaluates each Hecke word $w$ with eigenvalue $(-q^{-1})^{\ell(w)}$ (alternating channel) and $\mathrm{tr}$ uses $q^{\ell(w)}$ (symmetric channel). This evaluates the ratio of alternating to symmetric eigenvalues of $\Delta_\beta$ in the $6 \times 6$ regular representation of $H_3(q)$. These character evaluations do not involve the Markov parameter. For $\Delta_\beta = \sigma_0\sigma_1^{-1}$ both characters equal $1$, so this ratio is $1$; <!-- literal-source: nominal Pauli suppression parameter in 6x6 regular-representation ansatz --> the value $0.6382$ quoted here until 2026-10-10 is not reproduced by this definition, and its producer could not be located. The Markov-trace form of the Pauli case in the corollary vanishes identically under convention D, because the Ocneanu weight of $(1^3)$ is zero at $z = q^3/(q^2+1)$.

**Combined formula.**
For a $\beta^-$ decay with the converting neutron in shell degree $d$ and neutron occupation parity $p$:

$$
  Q
  = \mathcal{Q}_{\mathrm{bare}}
    \times F_{\mathrm{deg2}}^{[d \geq 2]}
    \times F_{\mathrm{Pauli}}^{[N \in \mathrm{magic}]},
$$

<!-- literal-source: unnormalised Rosso-Jones average at z = q^{1/2}/(q+1) and nominal Pauli parameter -->
where $[\cdot]$ is the Iverson bracket. Whereas the Convention-C trace gave a non-zero combined product $F_{\mathrm{deg2}} \times F_{\mathrm{Pauli}} = 0.5904 \times 0.6382 \approx 0.377$, under Convention D $F_{\mathrm{deg2}} \approx 3.6844$ and the Markov-trace Pauli factor is $0$. The formula was intended for magic-number nuclei in heavy shells (e.g. ${}^{137}\mathrm{Cs}$ with $N = 82$).

### Convention-D $Q$-values

The bare term and the combined formula, evaluated under the proton calibration $q_0$ with $z = q^3/(q^2+1)$, the normalisation $|\log_q(P_{\mathrm{dau}}/P_{\mathrm{par}})|\cdot\hbar_q\cdot m_e/3$ of the corollary, and nucleons ordered protons first. $F_{\mathrm{deg2}} \approx 3.6844$ is applied for converting-neutron shells $\geq 5$; for ${}^{137}\mathrm{Cs}$ ($N = 82$, a filled shell $\geq 5$) the Pauli factor is $0$ under convention D. ${}^{3}\mathrm{H}$ ($N = 2$) and ${}^{14}\mathrm{C}$ ($N = 8$) also fill a shell, but lie in shells $1$–$4$, where $F = 1$; read literally, part (iii) of the corollary would give $Q = 0$ for them as well.

| Decay | $N$ | Shell | $\mathcal{Q}_{\mathrm{bare}}$ (MeV) | Error | Combined $Q$ (MeV) | Error | $Q_{\mathrm{exp}}$ (MeV) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ${}^{3}\mathrm{H}$ | $2$ | $1$ | $\approx 0.03675$ | $+97.5\%$ | $\approx 0.03675$ | $+97.5\%$ | $0.01861$ |
| ${}^{14}\mathrm{C}$ | $8$ | $2$ | $\approx 0.14379$ | $-8.1\%$ | $\approx 0.14379$ | $-8.1\%$ | $0.15648$ |
| ${}^{60}\mathrm{Co}$ | $33$ | $5$ | $\approx 0.08553$ | $-73.1\%$ | $\approx 0.31514$ | $-1.0\%$ | $0.31817$ |
| ${}^{90}\mathrm{Sr}$ | $52$ | $6$ | $\approx 0.05482$ | $-90.0\%$ | $\approx 0.20198$ | $-63.0\%$ | $0.54590$ |
| ${}^{137}\mathrm{Cs}$ | $82$ | $6$ | $\approx 0.15314$ | $-70.2\%$ | $0$ | $-100\%$ | $0.51400$ |
| ${}^{210}\mathrm{Bi}$ | $127$ | $8$ | $\approx 0.52314$ | $-55.0\%$ | $\approx 1.92747$ | $+65.8\%$ | $1.16270$ |

The bare term misses by $8$–$98\%$ and the combined formula by $1$–$100\%$. The single close entry (${}^{60}\mathrm{Co}$) sits among misses of tens of percent on both sides and is not evidence for the formula. The same computation reproduces Table 1 and the values of $J$ and $F_{\mathrm{deg2}}$ above.

### Error structure

Let $\varepsilon = \delta q / q \approx 1.2 \times 10^{-8}$ (CODATA). The parametric error is $O(\varepsilon)$, which is negligible. The structural errors are $O(1)$ relative to $\varepsilon$: under convention D they are $8$–$98\%$ for $\mathcal{Q}_{\mathrm{bare}}$ and $1$–$100\%$ for the combined formula (table above). Until 2026-10-10 this paragraph quoted $2$–$10\%$; that range was measured under the excised convention C, and no producer of it was located. These errors arise from nucleon ordering in $\mathcal{Q}_{\mathrm{bare}}$, degree-$2$ Rosso--Jones weighting over two knots, the degree tower truncation, and, for filled shells, the vanishing of the Pauli branch under convention D. Whether the decomposition is complete is a separate claim; these residuals do not test it.
