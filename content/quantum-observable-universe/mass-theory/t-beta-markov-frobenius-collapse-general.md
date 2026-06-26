**Proposition (Min-Frobenius-norm collapse — general unital R-algebra).**
*Let $R$ be a strict-ordered field (typeclass `[Field R] [LinearOrder R] [IsStrictOrderedRing R]`), $A$ a unital $R$-algebra, and
$\tau : A \to R$ an $R$-linear normalised trace ($\tau(1) = 1$,
$\tau(xy) = \tau(yx)$).  Assume $\tau$ is positive-semi-definite
on squares: $0 \le \tau(X \cdot X)$ for every $X \in A$.  Then for
any $S \in R$ and any $X \in A$ satisfying the linear constraint
$\tau(X) = S$,*

$$
S^2 \;\le\; \tau(X \cdot X).
$$

*If, additionally, $\tau$ is non-degenerate on squares ($\tau(Y \cdot Y) = 0
\implies Y = 0$), the lower bound is attained iff $X = S \cdot 1_A$.*
## Relation to the substrate-model version

This proposition **lifts** [`prop:t-beta-markov-frobenius-collapse`](t-beta-markov-frobenius-collapse.md) from the substrate model ($A = R$, $\tau = \mathrm{id}$, where the theorem reduces to the trivial $X = S \Rightarrow X^2 = S^2$) to the **general unital $R$-algebra setting** where $A$ may be non-commutative and infinite-dimensional.

| Block | Setting | Used by |
|-------|---------|---------|
| `prop:t-beta-markov-frobenius-collapse` | substrate model ($A = R$, $\tau = \mathrm{id}$) | scalar $\mathfrak{Q}_\beta$ identities |
| `prop:t-beta-markov-frobenius-collapse-general` (this block) | any unital $R$-algebra with normalised trace + PSD + non-deg | Hecke-algebra applications |

## Proof

The Lean proof in [`t-beta-markov-collapse-general-lift.lean`](t-beta-markov-collapse-general-lift.lean) follows the same Lagrangian / completing-the-square argument as the substrate-model version, lifted to the general algebra:

1. **Algebra identity** (`completing_the_square_general`): for any $X \in A$, $S \in R$,
   $$\tau(X \cdot X) = \tau\!\big((X - S \cdot 1)(X - S \cdot 1)\big) + 2 S \cdot \tau(X) - S^2.$$
   Mechanical expansion using centrality of $S \cdot 1_A$ (`Algebra.commutes`) plus $R$-linearity of $\tau$.
2. **Constraint substitution** ($\tau(X) = S$, $\tau(1) = 1$):
   $$\tau(X \cdot X) = \tau\!\big((X - S \cdot 1)^2\big) + S^2.$$
3. **PSD bound** (`PSDTrace.psd`): $\tau\!\big((X - S \cdot 1)^2\big) \ge 0 \Rightarrow \tau(X \cdot X) \ge S^2$.
4. **Equality case** (`markov_frobenius_min_norm_uniqueness`, using `NonDegTrace.nondeg`): $\tau\!\big((X - S \cdot 1)^2\big) = 0 \Leftrightarrow X - S \cdot 1 = 0$.

## Application to the Iwahori–Hecke algebra

For $A = H_n(R, q)$ at generic $q > 0$ with $\tau = \tau_M$ (the Jones–Markov trace), this proposition gives the **canonical SDP-min-Frobenius-norm operator** for the constraint $\tau_M(T_\beta) = S$:

$$
T_\beta^{\mathrm{Markov}} \;=\; S \cdot 1_H.
$$

This is the Markov-trace collapse (substrate model) lifted to the genuine non-commutative Hecke algebra.

The L2-Euclidean coordinate-norm picture (PR #1739: 6-channel $A_i x_i^{L2}$ SHAPE $\times$ S decomposition) and the Markov-Frobenius picture (this proposition: $T_\beta = S \cdot 1$) are **two different operators** inside $H_n(R, q)$ that **both reproduce the SDP constraint** $\tau_M(T_\beta) = S$. The observable $c_k$ Taylor coefficients of $\mathfrak{Q}_\beta(q)$ are L2/Markov-invariant: see [PR #1750](https://github.com/litlfred/qou/pull/1750) Step 4 diagnostic.

## References

- PR #1750 (merged) — substrate-model proof + paper proof + accuracy diagnostic + audit doc.
- [PR #1761](https://github.com/litlfred/qou/pull/1761) (merged) — general-lift Lean infrastructure + this content block.
- [`docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`](../../../docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md) — structural finding + numerical verification at $q_0$.
- [`prop:markov-trace-frobenius-selection`](markov-trace-frobenius-selection.md) — Wenzl–Jones uniqueness theorem (the source of $\tau_M$'s non-degeneracy).
- Jones 1987 — Markov-trace existence + uniqueness.
- Wenzl 1988 — non-degeneracy of the Markov trace.
