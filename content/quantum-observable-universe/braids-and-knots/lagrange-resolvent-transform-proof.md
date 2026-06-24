The Lagrange resolvent transform is the discrete Fourier transform on the cyclic group $C_n$; the claim is that it diagonalises the $C_n$-action while converting the invariant constraints into spectral form. We argue the two formalised parts and indicate how the $n=5$ constraint transforms follow.

**Setup.** Fix a primitive $n$-th root of unity $\zeta$. For $n=5$ the Lean records $\zeta$ via `QOU.BringsSurface.ζ` with $\zeta^5 = 1$ (`ζ_pow_five`), $\zeta \neq 0$ (`ζ_ne_zero`), $\zeta^4 = \zeta^{-1}$ (`ζ_pow_four_eq_inv`), reducing every power mod $5$. Write $w_k = \tfrac{1}{\sqrt n}\sum_j \zeta^{kj} x_j$ (`lagrangeResolvent`) and $\sigma\colon x_j \mapsto x_{j+1 \bmod n}$ (`cyclicPerm`).

**Part 1 — $w_0 = 0$.** At $k=0$ every $\zeta^{0\cdot j}=1$, so $w_0 = \tfrac{1}{\sqrt n}\sum_j x_j$. The $C_n$-invariant linear constraint $\sum_j x_j = 0$ sends $w_0 \to 0$ — exactly `lagrange_resolvent_w0_vanishes`.

**Part 2 — diagonal action.** Applying $\sigma$ relabels $j \mapsto j+1$:
$$
  \sigma(w_k) = \frac{1}{\sqrt n}\sum_j \zeta^{kj} x_{j+1}
  = \frac{1}{\sqrt n}\sum_j \zeta^{k(j-1)} x_j
  = \zeta^{-k} w_k,
$$
the wrap-around term absorbed by $\zeta^{kn}=1$. Each Fourier mode is an eigenvector of $\sigma$ with eigenvalue $\zeta^{-k}$ — the $C_n$ symmetry as a phase rotation. For $n=5$ this is `lagrange_resolvent_diagonal_action` (rewrite $\zeta^{-1}=\zeta^4$, expand the five-term sums, reduce powers mod $5$, close by `ring`).

**Constraint transforms (consequence).** Since $w_k$ transforms by the character $\zeta^{-k}$, a monomial $\prod_a w_{k_a}$ is $C_n$-invariant iff $\sum_a k_a \equiv 0 \pmod n$. Imposing this on the Bring power-sum constraints at $n=5$ gives, degree by degree: the linear one becomes $w_0 = 0$; the quadratic the Hermitian quadric $w_1 w_4 + w_2 w_3 = 0$; the cubic the index-balanced $w_1^2 w_3 + w_4^2 w_2 + w_2^2 w_1 + w_3^2 w_4 = 0$. Only the linear projection and the underlying diagonalisation are carried out in the Lean witness; the higher-degree transforms are recorded as the spectral form of the constraints, not yet formalised.

The two formalised claims — $w_0 = 0$ and $\sigma(w_k) = \zeta^{-k} w_k$ — establish that the transform diagonalises $C_5$ on the Bring surface. $\qquad\blacksquare$
