---
# qou-w06d
title: 'Yes: a vanishing Wedderburn weight kills the shadow price, so the Wigner mechanism is capped at k=4'
status: completed
type: task
priority: normal
created_at: 2026-09-05T12:30:48Z
updated_at: 2026-09-05T12:32:40Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Answers the successor
`qou-a5jk` opened: **does `y_lambda = 0` force the shadow price `C_lambda = 0`?**

## YES — and it was already a class field nobody drew the consequence from

`content/quantum-observable-universe/mass-theory/mass-coefficient-shadow-price.lean`
has carried, since the block was written:

    C_eq   : forall lam, C lam = w lam * (h * (1/2))
    factor : forall lam, uStar lam = C lam * S lam

So `w~_lambda = 0` gives `C_lambda = 0` by one `rw`, and `uStar_lambda = 0` by
one more. **No `S_lambda` can rescue a zeroed block — the vanishing is upstream
of the nuclear datum.** Three theorems added to the sibling, all sorry-free:

- `coefficient_eq_zero_of_weight_eq_zero` — `w = 0 -> C = 0`
- `shadow_price_eq_zero_of_weight_eq_zero` — `w = 0 -> uStar = 0`
- `weight_ne_zero_of_shadow_price_ne_zero` — the contrapositive, which is how a
  search uses it: a block that prices anything must have at most two rows.

`qou-8na1` had already observed the instance without stating the rule:
*"`C_[1,1,1] = w~.h/2 = 0` makes `uStar = C.S = 0` consistent rather than
contradictory."* The corpus believed the implication at `H_3`; it just was not
a theorem.

## Joined with the enumeration: the Wigner mechanism is capped at k = 4

`QOU/Hecke/SelfConjugateRowCap.no_selfConj_two_row_of_five_le` (added here) is
the contrapositive of the size bound: **a self-conjugate partition of `n >= 5`
necessarily has `l(lambda) > 2`**, hence `w~ = 0`, hence `uStar = 0`.

So of the two Wigner shadow prices `mass-theory` names, `lambda = (2,2)` at
`k = 4` survives and `(3,1,1)` at `k = 5` prices nothing — **and neither does
any self-conjugate shape at any higher level.** The `T(T+1)/A` route exists, and
convention D leaves exactly one block of it standing.

## The dependency, stated not buried

Lean proves the IMPLICATION. The antecedent — that `w~` (canonical Wedderburn
weight) is the object convention D's row cap zeroes — is the corpus's
identification, taken from `qou-8na1`'s explicit `C_[1,1,1] = w~.h/2 = 0`, **not
inferred here**. If that identification is wrong the implication still stands
and simply does not apply. The two halves also sit in files that cannot import
each other (content siblings live outside the package globs), so the join is
prose in both docstrings rather than a single Lean chain — recorded so nobody
reads it as one theorem.

## What this opens

**Is `(2,2)` alone enough to reproduce `-Delta_W . T(T+1)/A`?** The mechanism
was stated over `k = 4, 5`; one of the two is now known to price nothing. If
`(2,2)` suffices, the Wigner term survives intact and the binding arc simply had
the wrong channel. If it does not, the symmetry energy needs a
non-self-conjugate source — and by the enumeration there is no self-conjugate
one available at any level.

## Gates

Sibling compiles standalone (`lean`-direct exit 0, imports Mathlib only);
`#print axioms` clean on all three; `lean-vacuity-axiom-audit.ts --fail-on
proof-no-trivial-type-mismatch,lean-import-after-content` **0 defect
candidates**; `--check-ledger` clean (so no ledger verdict is required — the
gate fires only on a flagged candidate). Library file `lean`-direct exit 0,
`no_selfConj_two_row_of_five_le` on `[propext, Quot.sound]` only.


## 2026-09-05 (later) — SUCCESSOR ANSWERED: (2,2) alone is what is already used

`qou-ld2a`. The IMPLEMENTED Wigner term
(`derived-mass-formula-light-isotopes.md`) is already `(2,2)`-only:

    Delta_W = -m_e . H_q((2,2)) . min(Z,N)/A

so the row cap leaves it untouched. **What carries `(3,1,1)` is the `T(T+1)/A`
form in `unified-iterative-correction-proof.md`**, whose `k = 5` half this bean
showed prices nothing. Concrete follow-up: that block should be re-stated over
`k = 4` alone, or its `k = 5` term dropped.

And the selection is tighter than "it survives": at the quartet level `n = 4`
the isospin-type class (`c(lambda) = 0`, the corpus's own rule) contains
**exactly one** partition out of five — `(2,2)`. So the Wigner coefficient is
forced, not drawn from a menu, which answers the fit-shape QA objection on that
one row.
