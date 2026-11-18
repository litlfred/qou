import QOU.BraidKnot.wedderburn_trace_identity
import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Group.Finset.Defs

/-!
# Keystone — the standard-representation q-dimension identity `d_q(n−1,1) = [n−1]_q` (all `n`)

This file **generalizes to all `n ≥ 2`** the `n = 5`-only shape lemma
`shape_41` of `QOU.BraidKnot.Keystone` (in
`KeystoneQBesselRadialTarget.lean`), which established the single instance
`d_q(4,1) = [4]_q`.  The general statement is the **standard-representation
family** of the symmetric group / Iwahori–Hecke algebra:

> For the two-row hook shape `λ = (n−1, 1)` (`n ≥ 2`), the q-hook-length
> dimension is `d_q(λ) = [n−1]_q`.

This is the structural content flagged in the Step-1 WRT-gate refutation
(`docs/audits/2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md`): the
`SU(2)` character `[2j+1]_q` matches the Hecke q-dimension `d_q` *only* on
the standard representation `(n−1,1)` — this lemma pins exactly the family
where the two agree.  No fit; pure q-combinatorics.

## Multiplicative form (division-free)

To avoid nonvanishing hypotheses we state the identity multiplicatively,
matching the `shape_*` convention of `KeystoneQBesselRadialTarget.lean`.
The hooks of `(n−1, 1)` are `{n} ∪ {n−2, …, 1}` in row 0 and `{1}` in row 1,
so their product is `[n]_q · [n−2]_q! · [1]_q`, and

  `[n]_q!  =  [n−1]_q · ([n]_q · [n−2]_q! · [1]_q)`.

Dividing, `d_q(n−1,1) = [n]_q! / ∏hooks = [n−1]_q`.  The multiplicative
identity follows from the q-factorial recursion
`[n]_q! = [n]_q · [n−1]_q!` applied twice, together with `[1]_q = 1` and
commutativity (`ring`).

Base ring: generic `[Field R]` throughout (matches
`QOU.BraidKnot.qIntGeo` / `qFactorial`; no archimedean construct — §7c).

-- Ref: [leitner2026] KeystoneQBesselRadialTarget.lean `shape_41` (the `n = 5` instance)
-- Ref: [macdonald1995] Symmetric Functions and Hall Polynomials, I.3 (q-hook-length formula)
-/

namespace QOU.BraidKnot.Keystone

open scoped BigOperators
open QOU.BraidKnot (qIntGeo qFactorial)

variable {R : Type*} [Field R]

/-- `[1]_q = 1` (the unbalanced q-integer `[k]_q = ∑_{i<k} q^i`). -/
theorem qIntGeo_one' (q : R) : qIntGeo q 1 = 1 := by
  simp [qIntGeo]

/-- **q-factorial recursion** `[n+1]_q! = [n]_q! · [n+1]_q`. -/
theorem qFactorial_succ (q : R) (n : ℕ) :
    qFactorial q (n + 1) = qFactorial q n * qIntGeo q (n + 1) := by
  simp only [qFactorial, Finset.prod_range_succ]

/-- **The standard-representation q-dimension identity, for all `n ≥ 2`**
(multiplicative form, division-free):

  `[n]_q!  =  [n−1]_q · ([n]_q · [n−2]_q! · [1]_q)`,

where the parenthesized factor is the hook-length product of the two-row
hook shape `λ = (n−1, 1)` — hooks `{n} ∪ {n−2, …, 1}` in row 0, `{1}` in
row 1.  Equivalently `d_q(n−1, 1) = [n]_q! / ∏hooks = [n−1]_q`.

This **generalizes `shape_41`** (the `n = 5` case `d_q(4,1) = [4]_q`) to the
whole standard-representation family. -/
theorem qFactorial_standard_hook (q : R) (n : ℕ) (hn : 2 ≤ n) :
    qFactorial q n
      = qIntGeo q (n - 1) * (qIntGeo q n * qFactorial q (n - 2) * qIntGeo q 1) := by
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 2 := ⟨n - 2, by omega⟩
  have e1 : m + 2 - 1 = m + 1 := rfl
  have e2 : m + 2 - 2 = m := rfl
  have e3 : m + 1 + 1 = m + 2 := rfl
  rw [e1, e2, qIntGeo_one', qFactorial_succ, qFactorial_succ, e3]
  ring

/-- Subtracting the hook-product factorisation from the n-th geometric q-factorial yields zero. -/
theorem qFactorial_standard_hook_sub_eq_zero (q : R) (n : ℕ) (hn : 2 ≤ n) :
    qFactorial q n
      - qIntGeo q (n - 1) * (qIntGeo q n * qFactorial q (n - 2) * qIntGeo q 1) = 0 := by
  rw [qFactorial_standard_hook q n hn, sub_self]

end QOU.BraidKnot.Keystone
