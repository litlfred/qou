**V_(1,1,1) per-irrep character via sign-rep substitution.**

$V_{(1,1,1)}$ constitutes the antisymmetric 1-d irrep of $H_3(q)$. The character is derived directly via scalar arithmetic (analogous to $V_{(3)}$) using the sign-rep action:

  - $\sigma_i \mapsto -q^{-1}$
  - $\sigma_i^{-1} \mapsto -q$
  - averaged $\mapsto -(q + q^{-1})/2$

Applied to the canonical typed-$\mathbf{B}_3$ braids:

  - $\mathcal{B}_p$ (uud): 6$\sigma$ + 3$\sigma^{-1}$ + 2 averaged
  - $\mathcal{B}_n$ (udd): 5$\sigma$ + 4$\sigma^{-1}$ + 2 averaged

yields:

  - $\chi_{(1,1,1)}(\mathcal{B}_p) = (-q^{-1})^6 \cdot (-q)^3 \cdot (-(q+q^{-1})/2)^2 = -q^{-3} \cdot (q+q^{-1})^2/4$
  - $\chi_{(1,1,1)}(\mathcal{B}_n) = (-q^{-1})^5 \cdot (-q)^4 \cdot (-(q+q^{-1})/2)^2 = -q^{-1} \cdot (q+q^{-1})^2/4$

Difference:

$$
  \chi_{(1,1,1)}(\mathcal{B}_n) - \chi_{(1,1,1)}(\mathcal{B}_p)
   = -\frac{(q^2 + 1)^2 (q^2 - 1)}{4 q^5}.
$$

## Conjugate-partition symmetry to V_(3)

The closed forms for V_(3) and V_(1,1,1) share the **same numerator
polynomial** $-(q^2 + 1)^2(q^2 - 1)$; they differ only by the
denominator power ($q$ vs $q^5$). The conjugate-partition quotient identity establishes

$$\chi_{(1,1,1)}\text{-diff}(q) = \chi_{(3)}\text{-diff}(q) \,/\, q^4$$

by direct rational simplification. This is the **conjugate-partition symmetry**: $(3)$ and
$(1,1,1)$ are transpose partitions, and the sign-rep $\leftrightarrow$
trivial-rep duality manifests as the $q \leftrightarrow -q^{-1}$
substitution on the generator level.

## Summary of established identities

| identity | content |
|---|---|
| Factored difference form | V_(1,1,1) char-diff = $-(q^2+1)^2(q^2-1)/(4q^5)$ |
| Conjugate-partition quotient | $\chi_{(1,1,1)}\text{-diff}(q) = \chi_{(3)}\text{-diff}(q) / q^4$ |
| Classical $q = 1$ limit | vanishes at $q = 1$ (isospin invariance) |
| Evaluation at $q = 2$ | numerical cross-check: $-75/128$ at $q = 2$ |

All four identities follow by direct rational and arithmetic simplification.
