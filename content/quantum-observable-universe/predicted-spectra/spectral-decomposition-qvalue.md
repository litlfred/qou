## Corollary (spectral decomposition of the $Q$-value)

*This is a direct consequence of the [cohomological embedding](#prop:cohomological-embedding) (completeness of the torus knot basis on $\Sigma_g$) applied to the beta decay [transfer matrix](#prop:beta-decay-transfer-matrix).*

*Let $\Sigma_g$ be a genus-$g$ surface and $\mathcal{E}_g = \{\tau(r,s) : \tfrac{(r-1)(s-1)}{2} \leq g\}$ the set of torus knot labels embeddable on $\Sigma_g$. For $\beta^-$ decay $\mathcal{N}_{Z,N} \to \mathcal{N}_{Z+1,N-1}$, the $Q$-value admits the spectral decomposition:*

$$
  Q
  = 
  \underbrace{
    \Bigl|\log_q\frac{P_{\mathrm{dau}}(q)}{P_{\mathrm{par}}(q)}\Bigr|
    \cdot \hbar_q \cdot \frac{m_e}{3}
  }_{\displaystyle\mathcal{Q}_{\mathrm{bare}}}
   \times 
  \underbrace{
    \prod_{\tau(r,s) \in \mathcal{E}_g}
    F\!\bigl(\tau(r,s), N\bigr)
  }_{\displaystyle\text{knot operator product}},
$$

*where:*

**(i)** *$P(q) = \prod_{j=0}^{A-2} \hat{V}_j(q)$ is the Skein polynomial from the inductive chain construction ([transfer matrix](#prop:beta-decay-transfer-matrix)). Each chain $\hat{V}_j = z \cdot M_j[0][0] + M_j[1][0]$ (with $z = (q^{1/2} + q^{-1/2})^{-1}$ the Markov parameter) is pre-reduced via the $2\!\times\!2$ matrix recurrence. This requires zero Hecke steps, ensuring $\mathcal{N}_{Z,N}$ is in Gröbner--Shirshov normal form at every inductive stage.*

**(ii)** *$\log_q(x) = \ln x / \ln q$ is the $q$-natural logarithm. It counts exceptional divisor levels along the color tube fiber of $\Sigma_g$. The constant $\hbar_q = (q - 1)/q$ is the quantum Planck constant (action per divisor step). The factor $m_e/3$ is the mass per crossing of the trefoil $\mathcal{K}_e = \mathcal{K}_{\tau(2,3)}$, because the electron has $3$ crossings. The product $\hbar_q \cdot m_e / 3$ replaces the intermediate notation $\mathfrak{E} \cdot \mu_0$; these cancel algebraically.*

**(iii)** *$F(\tau(r,s), N)$ is the **knot operator** of $\tau(r,s)$ acting on the converting neutron's shell:*

$$
  F(\tau(r,s), N)
  = 
  \begin{cases}
    1
    & \tau(r,s) \notin \mathcal{E}_g
     \text{ (null: zero action on $\Sigma_g$)} \\[4pt]
    1
    & \text{shell unchanged by decay (cancels in ratio)} \\[4pt]
    \mathrm{tr}_M\!\bigl(
      \tau(r,s) \cdot T_{\beta\text{-decay}}(q)
    \bigr)
    & \text{active shell, partially filled} \\[4pt]
    \dfrac{\bigl|\mathrm{tr}_M\!\bigl(
      e_{(1^3)} \cdot \tau(r,s) \cdot
      T_{\beta\text{-decay}}(q) \cdot e_{(1^3)}
    \bigr)\bigr|}{\bigl|\mathrm{tr}_M\!\bigl(T_{\beta\text{-decay}}(q)\bigr)\bigr|}
    & \text{active shell, fully filled (Pauli)}
  \end{cases}
$$

*with $T_{\beta\text{-decay}}(q) = \sigma_0 \sigma_1^{-1} \in H_3(q)$ the beta decay operator ([beta decay](#def:beta-decay-skein)), and $e_{(1^3)}$ the alternating Young symmetrizer of $H_3(q)$ ([glossary](#rem:y-lambda-sign-pattern)).*

**(iv)** *The product over $\mathcal{E}_g$ **collapses to a single term**. Only the converting neutron's shell knot $\tau(k^*)$ is active; all other shells cancel between parent and daughter. Non-embeddable knots contribute $F = 1$.*

**(v)** *The decomposition is **exact**. The embeddable torus knots form a complete basis for the representation ring of $H_n(q)$ restricted to $\Sigma_g$. This follows from the self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ and the Rosso–Jones completeness of torus knot invariants ([cohomological embedding](#prop:cohomological-embedding)). No higher-order corrections exist. The tower terminates definitively at degree $\lfloor 2g/(g-1) \rfloor$.*

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
  \approx 0.5904,
$$

where $J(\tau(r,s)) = \sum_{\lambda \vdash r} d_\lambda(q) \cdot \omega_\lambda^s$ is the Rosso--Jones invariant (the quantum-dimension weighted trace of the full twist on each irrep of $H_r(q)$), and $\Delta_\beta = T_{\mathrm{mix}} - T_{nn}$ is the beta-decay difference operator. The Rosso--Jones weights are the [canonical inner product on $R(H_r(q))$](#prop:rj-canonical-inner-product). Schur orthogonality forces this structure; they assign each degree-$2$ knot its Rosso--Jones invariant $J(\tau)$ with zero fitting freedom.

At $q = q_0$, $J(\tau(2,9)) \approx 2.167$ and $J(\tau(3,4)) \approx 5.794$ (computed from the Rosso--Jones expansion $J(\tau(r,s)) = \sum_\lambda d_\lambda(q_0)\omega_\lambda^s$). Thus, $\tau(3,4)$ receives approximately $2.67\times$ the weight of $\tau(2,9)$.

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
  = \frac{|\lambda_{\mathrm{alt}}|}{|\lambda_{\mathrm{sym}}|}
  \approx 0.6382,
$$

where $\mathrm{tr}_{\mathrm{alt}}$ evaluates each Hecke word $w$ with eigenvalue $(-q^{-1})^{\ell(w)}$ (alternating channel) and $\mathrm{tr}$ uses $q^{\ell(w)}$ (symmetric channel). This evaluates the ratio of alternating to symmetric eigenvalues of $\Delta_\beta$ in the $6 \times 6$ regular representation of $H_3(q)$.

**Combined formula.**
For a $\beta^-$ decay with the converting neutron in shell degree $d$ and neutron occupation parity $p$:

$$
  Q
  = \mathcal{Q}_{\mathrm{bare}}
    \times F_{\mathrm{deg2}}^{[d \geq 2]}
    \times F_{\mathrm{Pauli}}^{[N \in \mathrm{magic}]},
$$

where $[\cdot]$ is the Iverson bracket. The combined proportion $F_{\mathrm{deg2}} \times F_{\mathrm{Pauli}} = 0.5904 \times 0.6382 \approx 0.377$ applies to magic-number nuclei in heavy shells (e.g. ${}^{137}\mathrm{Cs}$ with $N = 82$).

### Error structure

Let $\varepsilon = \delta q / q \approx 1.2 \times 10^{-8}$ (CODATA). The parametric error is $O(\varepsilon)$, which is negligible. The structural errors ($2$–$10\%$) are $O(1)$ relative to $\varepsilon$. These arise from nucleon ordering in $\mathcal{Q}_{\mathrm{bare}}$, degree-$2$ Rosso--Jones weighting over two knots, and the degree tower truncation. These errors do not stem from missing spectral components; the decomposition is strictly complete.
