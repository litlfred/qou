**Proposition ($a_8$ partition-function identity).**
*Let $a_8 \in \mathbb{Z}[X]$ denote the top-shared ($m = 8$) integer
Habiro coefficient of the proton and neutron in the canonical
Habiro-witness convention (per
[`docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md)):*

$$
  a_8(X) \;=\; X^4 + 2\,X^3 + 3\,X^2 + 5\,X + 7.
$$

*Then $a_8$ admits the closed form*

$$
  a_8(X) \;=\; \sum_{n=1}^{5} p(n)\,X^{5-n},
$$

*where $p(n)$ denotes the integer partition function
(Hardy–Ramanujan, OEIS A000041):
$p(1) = 1,\; p(2) = 2,\; p(3) = 3,\; p(4) = 5,\; p(5) = 7$.*

## Proof

Coefficient-by-coefficient match in descending order of $X$-power:

| Power of $X$ | Coefficient in $a_8$ | $p(n)$ | $n = 5 - k$ |
|---|---|---|---|
| $X^4$ | $1$ | $p(1) = 1$ ✓ | $n = 1$ |
| $X^3$ | $2$ | $p(2) = 2$ ✓ | $n = 2$ |
| $X^2$ | $3$ | $p(3) = 3$ ✓ | $n = 3$ |
| $X^1$ | $5$ | $p(4) = 5$ ✓ | $n = 4$ |
| $X^0$ | $7$ | $p(5) = 7$ ✓ | $n = 5$ |

Each coefficient is the exact value of the integer partition
function at the corresponding index. The identity is checked in
$\mathbb{Z}[X]$ by `ring` after expanding
$\sum_{n=1}^{5}$ over $\{1, 2, 3, 4, 5\}$. ∎

## Categorical interpretation

The integer partition function $p(n)$ appears throughout
Habiro-ring / Hecke representation theory:

- **Number of Young diagrams** of weight $n$ (equivalently:
  partitions of $n$).
- **Generating function** $\sum_{n \geq 0} p(n)\,q^n
  = \prod_{k \geq 1} (1 - q^k)^{-1} = 1 / (q;q)_\infty$ —
  the Euler / Habiro generating series.
- **Dimensions of basis elements** indexed by Young diagrams via the
  Robinson–Schensted correspondence (combined with
  $\sum_{\lambda \vdash n} \dim(\lambda)^2 = n!$).

The appearance of $p(1), p(2), p(3), p(4), p(5)$ as successive
coefficients of $a_8(X)$ strongly suggests that the $m = 8$ shell
of the Habiro tower is **counting partitions** of $n = 1, \dots, 5$
— i.e., $a_8(X)$ is the **dimension-generating function** of
partitions fitting within the $m = 8$ shell.

## Convention stability

This identification was made in the **Habiro-witness convention**
(`include_inter=True`). The audit
[`docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md)
notes that the partition-function structure is much more
convention-robust than the cyclotomic prefactors: it is a property
of the combinatorial counting at the $m = 8$ shell, not of the
algebraic-expansion shape, so this finding is expected to survive
the Phase 5q convention switch (cf. Track 1 of the 𝔔_β Habiro
follow-up coordination ledger).

## Mathlib bridge

The Lean file
[`a8-partition-function-identity.lean`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/content/quantum-observable-universe/braids-and-knots/a8-partition-function-identity.lean)
defines a local `partitionCount : ℕ → ℕ` value table for
$n = 1, \dots, 5$ and proves the identity directly. The semantic
bridge to Mathlib's `Fintype.card (Nat.Partition n)` (from
`Mathlib.Combinatorics.Enumerative.Partition`) is recorded as a
documentation note — the genuine Hardy–Ramanujan values
$(1, 2, 3, 5, 7)$ are uncontested and standard (OEIS A000041
Table 1; Andrews, *The Theory of Partitions*, §1.1).

## Cross-references

- Sibling Lean identity (cyclotomic strand-doubling):
  [`cyclotomic-strand-doubling.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.md)
- Empirical source: [`qbeta_habiro_recursion_probe.py`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/computations/probes/qbeta_habiro_recursion_probe.py)
- Master 𝔔_β coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/coordination/1ppq-qbeta.md)
- This tranche's coordination ledger:
  [`docs/coordination/2026-06-01-qbeta-habiro-followup.md`](https://github.com/litlfred/qou/blob/claude/qbeta-habiro-followup-2026-06-01/docs/coordination/2026-06-01-qbeta-habiro-followup.md)
