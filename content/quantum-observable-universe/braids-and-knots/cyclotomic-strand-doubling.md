**Proposition (Cyclotomic strand-doubling identity).**
*Let $\Phi_n(X) \in \mathbb{Z}[X]$ denote the $n$-th cyclotomic
polynomial. Then over $\mathbb{Z}[X]$:*

$$
  \Phi_8(X) \;=\; \Phi_4(X^2),
$$

*equivalently, $X^4 + 1 = (X^2 + 1) \circ X^2$ where $\circ$ denotes
polynomial composition.*

## Proof

By direct evaluation, $\Phi_4(X) = X^2 + 1$ and
$\Phi_8(X) = X^4 + 1$. Composing $\Phi_4$ with $X^2$ gives
$(X^2)^2 + 1 = X^4 + 1 = \Phi_8(X)$. ∎

## Categorical interpretation

The substitution $X \mapsto X^2$ is the **strand-doubling map**:
it lifts the 2-strand braid group $B_2$ representation (carrying
$\Phi_4(X) = X^2 + 1$ in the single-nucleon Habiro denominator)
to the 4-strand $B_4$ representation (carrying
$\Phi_8(X) = X^4 + 1$ as a factor in the deuteron's
$(\mathfrak{D} - \mathfrak{n})$ Habiro element).

The deuteron carries 2 nucleons × 2 isospin (or color) channels =
4 strands; degree 4 = $\deg \Phi_8$ matches exactly. Furthermore,
$\Phi_8$'s four roots split as two bar-conjugate pairs
$\{\zeta_8, \zeta_8^{-1}\}$ and $\{\zeta_8^3, \zeta_8^{-3}\}$,
which is consistent with the deuteron's isoscalar (I = 0) bound-state
structure (the bar-involution $q \leftrightarrow q^{-1}$ is a
symmetry of the bound state itself).

## Generalisation (conjectural, subject to convention resolution)

The cyclotomic doubling extends through the powers-of-two tower:

$$
  \Phi_{2^{k+1}}(X) \;=\; \Phi_{2^k}(X^2)
  \qquad \text{for } k \geq 1.
$$

Under the strand-doubling categorical hypothesis (see
[`docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md`](https://github.com/litlfred/qou/blob/claude/brave-mendel-FPxFl/docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md)),
this predicts the following cyclotomic prefactors in the
$(\mathrm{atom}_A - \mathrm{atom}_{A-1})$ Habiro element:

| Pair (atomic step) | Predicted cyclotomic | Strand count |
|---|---|---|
| $(\mathfrak{D} - \mathfrak{n})$, A=1 → 2 | $\Phi_8 = X^4 + 1$ (observed) | $2^2$ = 4 |
| $({}^3\mathrm{He} - \mathfrak{D})$, A=2 → 3 | $\Phi_{16} = X^8 + 1$ | $2^3$ = 8 |
| $({}^4\mathrm{He} - {}^3\mathrm{He})$, A=3 → 4 | $\Phi_{32} = X^{16} + 1$ | $2^4$ = 16 |

These predictions are **falsifiable** once the per-isotope Habiro
coefficients for $^3$He and $^4$He land in the canonical convention.
The Lean file [`cyclotomic-strand-doubling.lean`](https://github.com/litlfred/qou/blob/claude/brave-mendel-FPxFl/content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean)
records the general identity as a `sorry`'d theorem citing the
Washington cyclotomic-fields textbook for the standard reduction
$\Phi_{p \cdot n}(X) = \Phi_n(X^p)$ when $p \mid n$.

The convention question (`include_inter=True` Habiro witness vs
Phase 5q canonical) remains open as of 2026-06-01; see
[`docs/audits/2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md`](https://github.com/litlfred/qou/blob/claude/brave-mendel-FPxFl/docs/audits/2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md).
