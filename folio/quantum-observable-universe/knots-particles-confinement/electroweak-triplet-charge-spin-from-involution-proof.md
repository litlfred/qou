## The provable half — bar-parity of the even-twist carriers

The even-twist carrier $T(2,2k)$ occupies the two-dimensional sym/alt Hecke block with eigenvalues $(q^{2k}, q^{-2k})$. The spin involution acts on this block as the swap $\sigma(x,y) = (y,x)$. This is precisely the bar involution $q \mapsto q^{-1}$ sending $q^{2k} \leftrightarrow q^{-2k}$. Its projections split the carrier:

1. **bar-even part** $a_+ \in A_+$, $\sigma$-fixed, with neutral (Markov-trace) value $q^{2k} + q^{-2k}$.
2. **bar-odd part** $a_- \in A_-$, $\sigma$-negated, traceless with nonzero skew value $q^{2k} - q^{-2k}$.

The Higgs is the bar-even, self-dual, real-volume carrier; the $W^\pm$ and $Z$ are bar-odd.

## The computed sector label and charge

Let $v_c$ be the sector vector of the carrier $c$: the $\sigma$-even projection of $(a_c, a_c^{-1})$ if $c \in A_+$, and its $\sigma$-odd projection if $c \in A_-$. If $c \in A_+$, then $v_c$ is $\sigma$-fixed, so $2s(c) = 0$, and its skew value is $0$, so $Q(c) = 0$. If $c \in A_-$, then $\sigma v_c = -v_c$. Since $2$ is invertible and $a_c^2 \neq 1$, we have $v_c \neq 0$, hence $\sigma v_c \neq v_c$ and $2s(c) = 2$; its skew value is $a_c - a_c^{-1} \neq 0$, so $Q(c) \neq 0$. For $W^-$, the eigenvalue is $a_{W^+}^{-1}$, so $Q(W^-) = -Q(W^+)$. With $H \in A_+$ and $W^\pm, Z \in A_-$ this gives the statement.

The postulated data are the sector map and the eigenvalues. The isospin table $T_3$ is recorded, not derived. The $\sigma$-parity alone makes $Z$ charged, since $Z \in A_-$.

## Isospin and mixing against the charge

If $2T_3(c) = \lambda Q(c) + \mu$ for all four carriers, then $H$ gives $\mu = 0$ since $Q(H) = 0$; $Z$ gives $\lambda Q(Z) = 0$, so $\lambda = 0$ since $Q(Z) \neq 0$; and $W^+$ gives $1 = 0$. Over an ordered field with $a > 1$ we have $a^{-1} < 1 < a$, so $a - a^{-1} > 0$. Hence $Q(W^+), Q(Z) > 0$ and $Q(W^-) = -Q(W^+) < 0$, and the signs of $Q$ are $0, 1, -1, 1$ on $H, W^+, W^-, Z$.

For the rotation $Z = cW^3 - sB$, $\gamma = sW^3 + cB$ with $c^2 + s^2 = 1$ and a linear charge with $x = Q(W^3)$, $y = Q(B)$:

$$
  c\,Q(Z) + s\,Q(\gamma) = (c^2 + s^2)\,x = x,
  \qquad
  -s\,Q(Z) + c\,Q(\gamma) = (c^2 + s^2)\,y = y.
$$

So $Q(Z) = Q(\gamma) = 0$ forces $x = y = 0$, and $Q(Z)^2 + Q(\gamma)^2 = x^2 + y^2$. With $c = \cot\theta_W \cdot s$ we get $Q(Z) = s(\cot\theta_W \cdot x - y)$, which for $s \neq 0$ vanishes exactly when $\cot\theta_W \cdot x = y$.

## The $\sigma_5^8$ bar-grading is derived from spin

The Weinberg-angle block reads the Hoefsmit slot $\sigma_5^8$ as the $\mathrm{U}(1)_Y$ hypercharge gauge boson $B$. The triplet block reads $\sigma_5^8$ ($= T(2,8)$, strands $5$–$6$) as the Higgs. There is no conflict: $\sigma_5^8$ carries both, bar-graded by the spin involution. The Higgs boson $H$ is the $A_+$ (bar-even, scalar) part; the hypercharge gauge boson $B$ is the $A_-$ (bar-odd, vector) part.

This bar-grading follows from the two carriers' sector labels. The map from sector to label is injective and inverts, so the label determines the sector. Reading the Higgs as scalar and $B$ as vector, as independent inputs, forces $H \in A_+$ and $B \in A_-$. The residual postulate is that both $H$ and $B$ inhabit the one $\sigma_5^8$ slot.
