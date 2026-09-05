---
# qou-a5jk
title: The row cap leaves exactly three self-conjugate partitions, so the Wigner mechanism has none past level 4
status: completed
type: task
priority: normal
created_at: 2026-09-05T12:15:23Z
updated_at: 2026-09-05T12:22:37Z
---


Branch `claude/q407-self-assuming-projections-2026-08-21`. Opened while looking
for "which object outside the bond graph carries `(N-Z)^2/A`" — and the first
finding is that **the corpus already has one**.

## The symmetry energy DOES have a derived route, in the MASS channel

`mass-theory` carries the Wigner energy `-Delta_W . T(T+1)/A`, built from
SELF-CONJUGATE shadow prices:

- `unified-iterative-correction-proof.md`: *"Wigner energy (k >= 5, dedicated
  `-Delta_W . T(T+1)/A`): the k = 4, 5 self-conjugate shadow prices
  (`lambda = (2,2)` and `(3,1,1)`)"*
- `figure-eight-branching-rule-proof.md`: *"self-conjugate partitions contribute
  isospin Casimir terms (`T(T+1)/A`, `T(T+1)(T+2)/A^2`, etc.)"*
- `mass-coefficient-shadow-price-proof.md`: the scaling function is set by the
  content sum — `c(lambda) > 0` volume-type, `c(lambda) < 0` charge-type,
  **`c(lambda) = 0` isospin-type `T(T+1)/A^p`**.

So the binding arc's "the symmetry energy is a named gap with NO available
route" was wrong about the corpus, not merely about the bond-graph mechanism.
That is a SECOND supersession of it, independent of `qou-i01a`'s AM-GM result.
Landed on the synthesis audit and `qou-q7ga`.

## The tension

`QOU/Hecke/RowCap.lean` proves the fibre-dimension cap: a column of height >= 3
has no injective filling into a 2-dimensional fibre, so `l(lambda) > 2 =>
y_lambda = 0` under convention D.

| lambda | k | self-conj | ell | c | fate |
|---|---:|---|---:|---:|---|
| **(2,2)** | 4 | yes | 2 | 0 | **survives** |
| **(3,1,1)** | 5 | yes | 3 | 0 | `y_lambda = 0` |

And it is not one shape. **Self-conjugacy forces `l(lambda) = lambda_1`** — the
diagram has as many rows as its first row has columns — so `l <= 2` puts the
whole diagram in a 2x2 box. Enumerated to n = 30:

    (1)     n = 1
    (2,1)   n = 3
    (2,2)   n = 4

**and none at any n >= 5.** Self-conjugate partitions do not stop existing —
2 at n = 8, 3 at n = 12 — they simply all have three or more rows. All three
survivors have `c(lambda) = 0`, i.e. they are all of the isospin-sensitive type;
there are just three of them.

## 🛑 TENSION, NOT REFUTATION — and the difference is the point

The shadow prices `C_lambda` are q-integer products of hooks, contents and
Frobenius coordinates. `y_lambda` enters the same construction SEPARATELY, as
the budget constraint `sum_lambda d_lambda y_lambda = 1`. **Whether
`y_lambda = 0` forces `C_lambda = 0` is not established anywhere in the corpus,
and nothing here assumes it.** Asserting it would be exactly the "declaring
refuted" failure AGENTS.md warns about.

Every theorem in `QOU/Hecke/SelfConjugateRowCap.lean` is about partition shapes
and list lengths, with no dependency on the LP — so the enumeration stands
whichever way the implication goes.

## THE SUCCESSOR — one well-posed question

**Does `y_lambda = 0` force `C_lambda = 0` in the shadow-price construction?**

- If YES: the Wigner mechanism is capped at `k = 4` (only `(2,2)`), and the
  symmetry energy needs a non-self-conjugate source.
- If NO: the mechanism is intact and the binding arc simply had the wrong
  channel all along.

Either answer is worth having, and it is a much smaller question than the one
this bean opened under.

## Artifacts

`content/quantum-observable-universe/lean/QOU/Hecke/SelfConjugateRowCap.lean`,
registered in `QOU.lean`: 7 decls. The four enumeration theorems depend only on
`[propext, Quot.sound]` — no `Classical.choice` — and the three concrete shape
checks (`selfConj_two_one`, `selfConj_two_two`, `not_selfConj_three_one`) depend
on **no axioms at all**. `lean`-direct exit 0.
`computations/qbeta/qbeta_self_conjugate_row_cap_probe.py` (5/5).
