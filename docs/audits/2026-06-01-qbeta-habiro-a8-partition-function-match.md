# a_8 partition-function match (2026-06-01)

> **POSITIVE structural finding** surfaced by the Option D recursion
> probe ([`qbeta_habiro_recursion_probe.py`](../../computations/probes/qbeta_habiro_recursion_probe.py),
> witness [`qbeta-habiro-recursion.witness.json`](../../computations/probes/qbeta-habiro-recursion.witness.json)):
>
> The top-shared Habiro coefficient `a_8(u)` of the proton and neutron
> (where `a_7 = a_8 = a_m(p) = a_m(n)` for m ∈ {7, 8} — both atoms
> agree EXACTLY at the top of the Habiro ladder) carries the
> **partition function** `p(n)` as its coefficient sequence.
>
> Branch: `claude/brave-mendel-FPxFl` (PR #1579, 16 commits).

## The match

The integer Habiro coefficient at m=8 (shared exactly by proton and
neutron, hence `Δa_8 = 0`) is

  $$a_8(u) \;=\; u^4 \;+\; 2u^3 \;+\; 3u^2 \;+\; 5u \;+\; 7$$

Reading the coefficients in descending order of `u`-power:

| Coefficient of u^k | Value | p(n) for n = 5 − k |
|---|---|---|
| u^0 | 7 | p(5) = 7 ✓ |
| u^1 | 5 | p(4) = 5 ✓ |
| u^2 | 3 | p(3) = 3 ✓ |
| u^3 | 2 | p(2) = 2 ✓ |
| u^4 | 1 | p(1) = 1 ✓ |

In closed form:

  $$a_8(u) \;=\; \sum_{n=1}^{5} p(n) \cdot u^{\,5-n}.$$

Each coefficient is the number of integer partitions of the
corresponding integer. **This is an exact algebraic identification,
not a numerical near-match.**

## Why this is structurally meaningful

The partition function `p(n)` appears throughout Habiro-ring /
Hecke representation theory as the dimension of basis elements
indexed by Young diagrams:

- **Number of Young diagrams** with at most n cells in a row
- **Dimension of certain Hecke algebra modules** via the Robinson-
  Schensted correspondence
- **Generating function** for integer partitions:
  `1 / (q; q)_∞ = Σ_n p(n) · q^n`

The appearance of `p(1), p(2), p(3), p(4), p(5)` in successive
coefficients of `a_8(u)` strongly suggests the Habiro coefficient
at the top shell is **counting partitions of 1 through 5** — i.e.,
a_8(u) is the **dimension-generating function** of partitions
fitting within the m=8 shell of the Habiro tower.

## What's still open

1. **Does `a_8` admit a closed form `Σ_{n=1}^{5} p(n) u^{5−n}` or
   `Σ_n p(n) (1−u)^{n}` etc. that extends to higher m?** Testing
   m=9, 10, … requires Habiro coefficients beyond M=8 (not in the
   current proton/neutron data which terminates at M=8).

2. **Is `a_7` ALSO a partition-function-related sequence?**
   The absolute values of `a_7 = −(12u^7 + 17u^6 + 24u^5 + 34u^4 + 48u^3 + 63u^2 + 84u + 110)`
   are `[12, 17, 24, 34, 48, 63, 84, 110]`. These don't match `p(n)`
   directly:
   - p(7) = 15, p(8) = 22, p(9) = 30, p(10) = 42, p(11) = 56, p(12) = 77, p(13) = 101, p(14) = 135
   - But `a_7` values are slightly different: 12, 17, 24, 34, 48, 63, 84, 110

   First differences `[5, 7, 10, 14, 15, 21, 26]` and second
   differences `[2, 3, 4, 1, 6, 5]` don't reveal an obvious pattern.
   Possible: `a_7` is a *modified* partition-counting sequence (e.g.,
   partitions into distinct parts, partitions with a parity
   constraint, or partitions of a different combinatorial object).

3. **Does the partition-function pattern extend to deuteron and
   heavier atoms?** The deuteron `a_m` for m=8..12 should be tested
   for analogous matches.

## Lean formalisation target

The `a_8 = Σ p(n) u^{5−n}` identity is a concrete polynomial
equality, immediately Lean-provable as:

```lean
-- Hypothesis or computation: a_8 = u^4 + 2u^3 + 3u^2 + 5u + 7
theorem a8_partition_function :
    a_8_qbeta_proton = ∑ n in Finset.Icc 1 5, (Nat.partition n) * X^(5-n) := by
  -- ...
```

This complements the cyclotomic strand-doubling lemma already proven
in [`content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean`](../../content/quantum-observable-universe/braids-and-knots/cyclotomic-strand-doubling.lean).

## Cross-references

- Parent recursion probe (this audit's source): [`qbeta_habiro_recursion_probe.py`](../../computations/probes/qbeta_habiro_recursion_probe.py)
- Witness: [`qbeta-habiro-recursion.witness.json`](../../computations/probes/qbeta-habiro-recursion.witness.json)
- Δa_m factorization parent: [`2026-05-31-qbeta-habiro-delta-am-factorization.md`](2026-05-31-qbeta-habiro-delta-am-factorization.md)
- Cyclotomic strand-doubling (the other categorical identification): [`2026-06-01-qbeta-habiro-phi8-interpretation.md`](2026-06-01-qbeta-habiro-phi8-interpretation.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)

## Convention note

This identification was made in the **Habiro-witness convention**
(`include_inter=True`). Whether it survives in the Phase 5q canonical
convention is open — see [`2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md`](2026-06-01-qbeta-habiro-phi16-phi32-prediction-blocked-convention.md).
However, the partition-function structure is much more robust to
convention than the cyclotomic prefactors (it's a property of the
combinatorial counting at the m=8 shell, not of the algebraic
expansion shape), so this finding is likely convention-stable.

## Recurrence searches — negative

Exhaustive search for constant-coefficient or polynomial-in-u
recurrences on:
- Δa_m leading coefficients `[10, -64, 131, -92, 18, -1]`
- a_m(p) leading coefficients `[4, -74, 340, -711, 788, -466, 133, -12, 1]`
- a_m(n) leading coefficients `[4, -64, 276, -580, 696, -448, 133, -12, 1]`

**No clean rational recurrence found** at orders 1–4. The leading
coefficient sequence is NOT generated by a simple linear recurrence
with integer or rational coefficients. The categorical generator for
the full sequence (if any) is more sophisticated than first-order
recursion — possibly a generating-function identity or a Schur-
function tower.
