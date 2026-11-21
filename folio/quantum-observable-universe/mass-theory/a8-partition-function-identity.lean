import Mathlib.Algebra.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Combinatorics.Enumerative.Partition
import Mathlib.Tactic

/-!
# a_8 partition-function identity

The top-shared (m=8) Habiro coefficient `a_8(u)` of the proton and
neutron (identified empirically in PR #1579, audit
`docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md`)
is

```
a_8(u) = u^4 + 2·u^3 + 3·u^2 + 5·u + 7
```

whose coefficient sequence `(1, 2, 3, 5, 7)` matches the **integer
partition function** values `(p(1), p(2), p(3), p(4), p(5))` —
i.e. Hardy–Ramanujan `p(n)`, OEIS A000041.

Closed form:

```
a_8(u) = Σ_{n=1..5} p(n) · u^(5-n).
```

This is convention-stable: it is a combinatorial property of the
coefficient counting at the m=8 shell of the Habiro tower, not an
algebraic-expansion-shape property.

## Mathlib API note

Mathlib's `Mathlib.Combinatorics.Enumerative.Partition` defines
`Nat.Partition n` as the type of integer partitions of `n` (a
`Fintype`). The Hardy–Ramanujan partition function `p(n)` is
`Fintype.card (Nat.Partition n)`. (Mathlib does *not* ship a
top-level `Nat.partition : ℕ → ℕ` function; the convention is to
work via `Fintype.card`.)

To make the identity `a_8 = Σ p(n) X^(5-n)` provable by `decide` /
`rfl`, we define a local `partitionCount n` synonym whose value
table for `n = 1..5` is `(1, 2, 3, 5, 7)`. The bridge to Mathlib's
`Fintype.card (Nat.Partition n)` is `partitionCount_eq_fintype_card_partition_small`
below, which remains an **axiom**.

**Corrected 2026-09-04.** This paragraph used to claim the five values
"are reflexive identities since the `Nat.Partition` enumeration is
decidable for small `n`". **That is false as stated, and the boundary
is sharp: `decide` proves `Fintype.card (Nat.Partition 1) = 1` and
gets STUCK at `n = 2`** — reduction halts on
`(partitionCount 2).beq (Fintype.card (Nat.Partition 2))` after
unfolding two dozen instances including `Nat.instDecidableEqPartition`.

`Decidable` in the typeclass sense is not the same as kernel-reducible.
The instance exists, so the proposition typechecks as decidable; it
simply does not evaluate, because `Nat.Partition` is a structure over a
`Multiset` and the `Fintype` instance is not built from a computable
enumeration the kernel can unfold.

So closing this axiom is real combinatorial work — an explicit
`Nat.Partition n ≃ Fin (p n)`, or a `Finset` enumeration with a
cardinality lemma — not a tactic call. `native_decide` would discharge
it but adds `Lean.ofReduceBool` to the axiom list, i.e. trades one
axiom for another, and is banned by AGENTS.md besides.

## References

-- Ref: [hardy-ramanujan1918] G. H. Hardy and S. Ramanujan,
--      "Asymptotic formulae in combinatory analysis",
--      Proc. London Math. Soc. (2) 17 (1918), 75-115.
-- Ref: [andrews1976] G. E. Andrews, "The Theory of Partitions",
--      Encyclopedia of Mathematics and its Applications 2,
--      Addison-Wesley 1976.
-- Ref: [habiro2000] https://doi.org/10.2140/gt.2000.4.227
-- Ref: [leitner2026] docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md
-/

namespace QOU.BraidKnot.A8Partition

open Polynomial

/-- The concrete integer partition function values for `n = 1..5`:
    `(p(1), p(2), p(3), p(4), p(5)) = (1, 2, 3, 5, 7)`.

    This is the value table needed for the `a_8` identity; the
    bridge to Mathlib's `Fintype.card (Nat.Partition n)` is given
    by `partitionCount_eq_fintype_card_partition` below. -/
def partitionCount : ℕ → ℕ
  | 0 => 1
  | 1 => 1
  | 2 => 2
  | 3 => 3
  | 4 => 5
  | 5 => 7
  | _ => 0  -- extended only as far as the a_8 identity needs

/-- **The a_8 Habiro coefficient polynomial** (shared exactly by
    proton and neutron in the canonical Habiro-witness convention):

      `a_8(X) = X^4 + 2·X^3 + 3·X^2 + 5·X + 7`. -/
noncomputable def a_8_poly : ℤ[X] := X ^ 4 + C 2 * X ^ 3 + C 3 * X ^ 2 + C 5 * X + C 7

/-- Concrete values of the partition function for `n = 1..5`. -/
theorem partitionCount_values :
    partitionCount 1 = 1 ∧ partitionCount 2 = 2 ∧
    partitionCount 3 = 3 ∧ partitionCount 4 = 5 ∧
    partitionCount 5 = 7 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> rfl

/-- **Main identity (closed form).**  The a_8 Habiro coefficient
    polynomial equals the partition-function-weighted sum:

      `a_8(X) = Σ_{n=1..5} p(n) · X^(5-n)`.

    Coefficient-by-coefficient match (descending in X-degree):
      `X^4 ↔ p(1) = 1, X^3 ↔ p(2) = 2, X^2 ↔ p(3) = 3,
       X^1 ↔ p(4) = 5, X^0 ↔ p(5) = 7`. -/
theorem a_8_eq_partition_sum :
    a_8_poly =
      ∑ n ∈ Finset.Icc 1 5, (partitionCount n : ℤ) • X ^ (5 - n) := by
  -- Expand the Icc 1 5 sum, evaluate each partitionCount, and
  -- match coefficients via `ring`.
  unfold a_8_poly
  rw [show (Finset.Icc 1 5 : Finset ℕ) = {1, 2, 3, 4, 5} from by decide]
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide),
      Finset.sum_insert (by decide), Finset.sum_insert (by decide),
      Finset.sum_singleton]
  -- After expanding the explicit sum the goal becomes:
  --   X^4 + 2•X^3 + 3•X^2 + 5•X + C 7
  --     = 1 • X^4 + 2 • X^3 + 3 • X^2 + 5 • X^1 + 7 • X^0
  -- which `ring` closes (smul on ℤ-action coincides with C-mult
  -- on polynomial coefficients).
  norm_num [partitionCount]
  ring

/-- **Alternative form (ascending degree).**  Re-indexing the sum
    by `k = 5 - n` gives:

      `a_8(X) = Σ_{k=0..4} p(5-k) · X^k`. -/
theorem a_8_eq_partition_sum_ascending :
    a_8_poly =
      ∑ k ∈ Finset.range 5, (partitionCount (5 - k) : ℤ) • X ^ k := by
  unfold a_8_poly
  rw [show (Finset.range 5 : Finset ℕ) = {0, 1, 2, 3, 4} from by decide]
  rw [Finset.sum_insert (by decide), Finset.sum_insert (by decide),
      Finset.sum_insert (by decide), Finset.sum_insert (by decide),
      Finset.sum_singleton]
  norm_num [partitionCount]
  ring

/-! ### Bridge to Mathlib's `Nat.Partition`

The local `partitionCount` function above is a value-table
definition; the genuine Hardy–Ramanujan partition function is
`Fintype.card (Nat.Partition n)` from
`Mathlib.Combinatorics.Enumerative.Partition`.

The bridge — `partitionCount n = Fintype.card (Nat.Partition n)`
for `n = 1..5` — holds by decidability of the small enumeration,
but the kernel-level proof requires Mathlib's `Nat.Partition`
fintype instance, which is computationally heavy. We record the
bridge as a `sorry`'d theorem with a bibliographic reference; once
Mathlib's partition-enumeration API stabilises (or once a more
efficient `decide` is available for `Fintype.card`), the bridge
becomes a one-line `decide` / `rfl`.

The downstream content (the a_8 identity above) does NOT depend on
this bridge: the proof goes through `partitionCount` directly,
which is a concrete `ℕ → ℕ` function with no `Fintype` content.
The bridge theorem records the *semantic* link to Mathlib's
canonical partition function. -/

/-- **Bridge to Mathlib's `Nat.Partition` (semantic link).**

    The local `partitionCount n` equals `Fintype.card (Nat.Partition n)`
    for the five values used in the `a_8` identity.

    This is the standard Hardy–Ramanujan partition-function table:
    `p(1) = 1, p(2) = 2, p(3) = 3, p(4) = 5, p(5) = 7` (OEIS A000041).

    Axiomatised pending a uniform Mathlib `decide`-route for
    `Fintype.card (Nat.Partition n)`; the values themselves are standard and
    uncontested (OEIS A000041: `p(1..5) = 1, 2, 3, 5, 7`).  Verified 2026-08-21
    that `decide` currently **fails** on the Mathlib `Nat.Partition` Fintype
    instance (`Tactic decide failed`), so this remains a cited external fact
    rather than a discharged lemma; resolution is a one-line `decide` once that
    instance becomes `Decidable`-friendly at small `n`. -/
-- Ref: [leitner2026] a8-partition-function-identity — semantic bridge; partition values are the standard Hardy–Ramanujan table (OEIS A000041)
axiom partitionCount_eq_fintype_card_partition_small :
    ∀ n ∈ Finset.Icc 1 5,
      partitionCount n = Fintype.card (Nat.Partition n)

end QOU.BraidKnot.A8Partition
