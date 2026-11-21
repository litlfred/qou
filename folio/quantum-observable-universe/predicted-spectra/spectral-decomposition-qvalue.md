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

**(i)** *$P(q) = \prod_{j=0}^{A-2} \hat{V}_j(q)$ is the Skein polynomial from the inductive chain construction ([transfer matrix](#prop:beta-decay-transfer-matrix)). Each chain $\hat{V}_j = z \cdot M_j[0][0] + M_j[1][0]$ (with $z = q^3/(q^2+1)$ the convention-D Markov parameter, $z \approx 0.612688037$ at $q_0$) is pre-reduced via the $2\!\times\!2$ matrix recurrence. This requires zero Hecke steps. It ensures $\mathcal{N}_{Z,N}$ is in Gröbner--Shirshov normal form at every inductive stage.*

*Under the canonical Convention-D parameter $z_D = q^3/(q^2+1)$, each transfer matrix $\hat{V}_j$ and hence $P(q)$ has coefficients in $\mathbb{Q}(q)$ (unlike the Convention-C parameter $z_C = (q^{1/2} + q^{-1/2})^{-1} \approx 0.4993203342$, which introduces $\mathbb{Q}(q^{1/2})$); the numerical evaluations of $\mathcal{Q}_{\mathrm{bare}}$ are tabulated in the [interpretation](#rem:spectral-decomposition-qvalue-interpretation).*

**(ii)** *$\log_q(x) = \ln x / \ln q$ is the $q$-natural logarithm. It counts exceptional divisor levels along the color tube fiber of $\Sigma_g$. The constant $\hbar_q = (q - 1)/q$ is the quantum Planck constant. This is the action per divisor step. The factor $m_e/3$ is the mass per crossing of the electron word $\sigma_0\sigma_1\sigma_0$ ([electron](#def:electron-knot)), which has $3$ letters. (The backup trefoil electron $\mathcal{K}_{\tau(2,3)}$ also has $3$ crossings, so the factor is the same in both readings.) The product $\hbar_q \cdot m_e / 3$ replaces the intermediate notation $\mathfrak{E}_{\mathrm{int}} \cdot \mu_0$. These cancel algebraically.*

**(iii)** *$F(\tau(r,s), N)$ is the knot operator of $\tau(r,s)$ acting on the converting neutron's shell:*

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

*Under convention D the fourth case is degenerate. The Ocneanu weight of every partition with three rows vanishes at $z = q^3/(q^2+1)$, so $\mathrm{tr}_M\bigl(e_{(1^3)} \cdot x \cdot e_{(1^3)}\bigr) = 0$ for every $x \in H_3(q)$, and the fully filled case gives $F = 0$ and hence $Q = 0$ for every magic-number shell. The Pauli branch of the decomposition, as stated with the Markov trace, does not survive the change of convention; a replacement projection has not been derived. **The corollary is therefore asserted only for decays whose converting shell is not fully filled.** The fully filled (magic-number) case is excluded from its scope, because on that case the formula returns $Q = 0$, which is not a $Q$-value.*

**(iv)** *The product over $\mathcal{E}_g$ collapses to a single term. Only the converting neutron's shell knot $\tau(k^*)$ is active. All other shells cancel between parent and daughter. Non-embeddable knots contribute $F = 1$.*

**(v)** *On the scope fixed in (iii), the decomposition is exact. The embeddable torus knots form a complete basis for the representation ring of $H_n(q)$ restricted to $\Sigma_g$, by the self-duality $\tau(r,s) \leftrightarrow \tau(s,r)$ and the Rosso–Jones completeness of torus knot invariants ([cohomological embedding](#prop:cohomological-embedding)). No higher-order corrections exist; the tower terminates definitively at degree $\lfloor 2g/(g-1) \rfloor$.*
