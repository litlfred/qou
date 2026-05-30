**Remark.**
*The Frobenius Gram matrix*
$G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$
*of $H_3(R, q)$ on the normal-form basis*
$\{1, \sigma_0, \sigma_1, \sigma_0\sigma_1, \sigma_1\sigma_0,
\sigma_0\sigma_1\sigma_0\}$
*has its six diagonal entries determined symbolically by the Hecke
relation $\sigma_i^2 = h \sigma_i + 1$ (with $h := q - q^{-1}$) and
the Markov axioms*
$\mathrm{tr}_M(1) = 1$, $\mathrm{tr}_M(\sigma_i) = z$,
$\mathrm{tr}_M(x \sigma_n) = z \cdot \mathrm{tr}_M(x)$
*for $x \in H_n$, where*
$z := 1 / (\sqrt{q} + 1/\sqrt{q})$:

| $i$ | $b_i$ | $G_{i,i}$ |
|---:|:---|:---|
| 0 | $1$ | $1$ |
| 1 | $\sigma_0$ | $h z + 1$ |
| 2 | $\sigma_1$ | $h z + 1$ |
| 3 | $\sigma_0 \sigma_1$ | $h^2 z^2 + h z + z^2$ |
| 4 | $\sigma_1 \sigma_0$ | $h^2 z^2 + h z + z^2$ |
| 5 | $\sigma_0 \sigma_1 \sigma_0$ | $h^4 z^2 + 3 h^2 z^2 + h^3 z + 3 h z + 1$ |

**Cross-check at the substrate value.**
*Evaluating at $q = q_0 \approx 1.1099798$ (so $h \approx 0.2084$,
$z \approx 0.4993$) reproduces the numerical values recorded in the
producer witness*
`folio-assistant/computations/gram-matrix-dual.witness.json`:
$G_{0,0} = 1$, $G_{1,1} = G_{2,2} \approx 1.1044$,
$G_{3,3} = G_{4,4} \approx 0.3646$, $G_{5,5} \approx 1.3509$.

**Status.**
*This remark records the six diagonal entries; the fifteen distinct
off-diagonal entries depend on a Halverson–Ram seminormal
normalisation choice and are not yet in Lean. The
$\mathrm{gram\_matrix}\;q$ stub in
[universal-ilp-algorithm](#def:universal-ilp-algorithm) currently
returns $0$, making the Frobenius positivity predicate vacuously
true; a follow-up PR will wire that stub through these definitions
plus the symbolic off-diagonals.*
