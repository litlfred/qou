---
# qou-8zjc
title: 'Wenzl level-2 collapses the two-nucleon H6 trace to 4 blocks: 3 unbind, (3,3) sign-flips, and NO conjugate pair survives at n=6'
status: in-progress
pr: 8187
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T12:43:11Z
updated_at: 2026-11-16T20:22:00Z
parent: qou-10v9
---


Consumer of the Wenzl epic `qou-otbb` / `5cf16c8f16` (*z_D is Wenzl level r = 2,
exactly*), applied to the two-nucleon H₆ analysis on PR #4973. Not a
re-derivation — the vanishing comes from the corpus's live closed form
`schur_principal_mpmath.y_lambda_at_q0_mpmath`.

## What level 2 does to the two-nucleon trace

`y_λ = 0` for every partition with ≥3 rows, so of 11 blocks at n = 6 only **four**
carry Markov weight:

| λ | rows | `y_λ` | `r_λ` pp / pn / nn |
|---|---|---:|---|
| (6,) | 1 | 0.1153242249 | 1.110 / 1.005 / 0.901 |
| (5,1) | 2 | 0.0789529625 | **3.759 / 4.388 / 6.464** |
| (4,2) | 2 | 0.0460324347 | **3.150 / 2.438 / 1.982** |
| (3,3) | 2 | 0.0151238101 | −0.018 / −0.042 / −0.269 |

**Three of the four unbind in all three systems.**

## It dissolves an obstruction I had filed as blocking

I recorded "7 of 11 blocks have `r_λ < 0`, and they are precisely the channel that
has to come out BOUND" as the obstruction facing any per-block decomposition.
Those 7 blocks are exactly the ≥3-row ones — **`y_λ = 0`, they are not in the
trace at all**. The obstruction was on blocks that do not exist.

One survivor is still sign-flipped: `(3,3)`, the rectangular two-row block. That
is the residue of the obstruction, and it is one block rather than seven.

## Conjugate pairs: safe at n = 2, void at n = 6

The ribbon-twist result rests on `θ_{λ'} = θ_λ⁻¹`, which needs **both** members of
a conjugate pair to carry weight.

* **n = 2** — survivors `(2)` and `(1,1)`; they are conjugates and **both survive**.
  The twist argument is intact exactly where it was used (the interface).
* **n = 6** — survivors `(6,), (5,1), (4,2), (3,3)`; conjugates `(1⁶), (2,1⁴),
  (2,2,1,1), (2,2,2)` **all have `y = 0`**. **No conjugate pair survives.**

So any H₆-*level* conjugation claim is void, while the n=2 interface claim stands.
Worth stating because I nearly made the H₆ version.

## Bonus: μ± ARE the n=2 Wedderburn weights, verified

I asserted this earlier without checking. It is exact:

    y_(2)   = 0.7527021133   =  mu+  (T = 1)
    y_(1,1) = 0.2472978867   =  mu-  (T = 0)

So the projector scalars used throughout the twist analysis are the Markov
weights, not a parallel construction that happens to look like them.

## Open

Why `(3,3)` sign-flips while the other three survivors do not. It is the only
rectangular block among them and the only one whose conjugate is dead — neither
observation is yet an explanation.

## Progress 2026-11-16 (PR #8187)

- [x] Added `conjugate_pair_survives_at_n_two`, `three_le_first_row_of_two_rows_of_five_le`, `conjugate_weight_eq_zero_of_two_lt_colLen_transpose`, and `n_six_three_three_survives_but_conjugate_dies` in `QOU/QBeta/WenzlWeightVanishing.lean` + 80-dps `mpmath` probe (`litlfred/qou#8187`, `28237151a70df9ecb11495b374e141771a7b4a76`).
- [ ] Await review and merge of `litlfred/qou#8187`.
