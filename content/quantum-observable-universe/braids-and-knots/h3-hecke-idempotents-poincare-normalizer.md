## Explicit projector normalization — the $S_3$ Poincaré polynomial

The carrier-level construction of the two one-dimensional projectors
(in the upstreamable module `QOU.Mathlib.HeckeAlgebra`, declarations
`H3.blockSym3` / `H3.blockAlt3`) fixes the normalization convention:

$$
  e_{(3)} = \frac{1}{P(q)} \sum_{w \in S_3} q^{\ell(w)}\, T_w,
  \qquad
  e_{(1^3)} = \frac{1}{P(q^{-1})} \sum_{w \in S_3} (-q^{-1})^{\ell(w)}\, T_w,
$$

where $P(q) = \sum_{w \in S_3} q^{2\ell(w)} = 1 + 2q^2 + 2q^4 + q^6
= (1+q^2)(1+q^2+q^4)$ is the Poincaré polynomial of $S_3$ in the
Hecke parameter (declaration `H3.poincare`). The normalizer is forced
by the eigenvalue table above: $T_w\, e_{(3)} = q^{\ell(w)} e_{(3)}$,
so squaring the sum multiplies it by $\sum_w q^{2\ell(w)}$, and
idempotency pins the denominator to $P(q)$ exactly; the sign block has
$T_w\, e_{(1^3)} = (-q^{-1})^{\ell(w)} e_{(1^3)}$, pinning $P(q^{-1})$.

Two practical consequences:

1. **No genericity hypothesis.** $P(q) \geq 1 > 0$ for every real
   $q$ (even powers, positive coefficients), so idempotency and
   orthogonality of the blocks hold with only $q \neq 0$ (which
   clears the $q - q^{-1}$ structure constants) — there is no
   vanishing locus to avoid on the real line.
2. **Relation to the balanced $q$-factorial.** With the balanced
   convention $[k]_q = (q^k - q^{-k})/(q - q^{-1})$ one has
   $P(q) = q^{\ell(w_0)}\, [3]_q!$ with $\ell(w_0) = 3$ the longest
   element, and $P(q^{-1}) = q^{-\ell(w_0)}\, [3]_q!$ by
   bar-invariance of $[3]_q!$. The two normalizers differ by
   $q^{2\ell(w_0)} = q^6$; using the bare balanced factorial for
   *both* blocks makes neither projector idempotent.
