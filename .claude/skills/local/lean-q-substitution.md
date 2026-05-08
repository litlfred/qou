---
name: lean-q-substitution
roles: [collaborator, owner]
description: >
  Discharge QOU substrate-window polynomial inequalities in `q` and
  `q⁻¹` using the universal `s := q + q⁻¹` substitution and the
  AM-GM rewrite `q + q⁻¹ - 2 = (q - 1)² / q`.  Standard tactic
  ladder for `qIntReal`, `qFactReal`, and Hecke-eigenvalue bounds
  on the substrate interval `q ∈ (1, 3/2)`.
allowed-tools: Read Edit Bash Grep Glob
---

# QOU `q + q⁻¹` Substitution Skill

## Role

Convert polynomial inequalities in `(q, q⁻¹)` over the QOU substrate
window `q ∈ (1, 3/2)` into single-variable polynomial inequalities
in `s := q + q⁻¹ ∈ [2, 13/6]` so that `nlinarith` can close them
with a small, predictable hint set.

This is QOU's most reusable Lean tactic: every quantitative bound
that appears in `QOU/Descartes/QHookBound.lean`,
`QOU/Interactions/*`, `QOU/Descartes/HeckeRep.lean`, and the
`q^(±1/2)` denominators of `MassDerivation.lean` is a symmetric
function of `(q, q⁻¹)`, hence a polynomial in `s`.

## When to Use This Skill

- Goal mentions `qIntReal q m`, `qFactReal q k`, `q⁻¹`, or
  `(q - q⁻¹)^2`.
- Existing proof reaches for `nlinarith` against a hint list of
  more than 4 entries and times out.
- A new `theorem` / `instance` body needs to bound a Laurent
  polynomial in `(q, q⁻¹)` against a polynomial in `(q - q⁻¹)`.

## Authority commits

| Commit | Lemma closed | What it teaches |
|--------|--------------|-----------------|
| `9b423397` | `qIntRatioBoundSmall_three` | The `[3]_q = q² + 1 + q⁻²` and `q² + q⁻² - 2 = (q − q⁻¹)²` rewrites |
| `81a4e3f1` | `qIntRatioBoundSmall_one`, `_two` | Base-case structure |
| `eaaef6de` | `qFactRatioBound_two` | AM-GM rewrite for `q + q⁻¹ - 2 ≥ 0` |
| `fa298f92` | `qFactRatioBound_three` | The full `s := q + q⁻¹` ladder |
| `c2dfca50` | `qIntRatioBoundSmall_four` | Cubic-in-`s` discharge with the `(s - 2)(13/6 - s) ≥ 0` hint |

## Standard preamble (emit at the top of every q-substrate proof)

```lean
have hq_ne_one  : q ≠ 1   := ne_of_gt hq
have hq_pos     : q > 0   := by linarith
have hq_ne      : q ≠ 0   := ne_of_gt hq_pos
have hq_inv_pos : q⁻¹ > 0 := inv_pos.mpr hq_pos
have hq_inv_lt  : q⁻¹ < 1 := by rwa [inv_lt_one_iff_of_pos hq_pos]
have h_diff_pos : q - q⁻¹ > 0 := by linarith
have h_diff_ne  : q - q⁻¹ ≠ 0 := ne_of_gt h_diff_pos
have h_qq_inv   : q * q⁻¹ = 1 := mul_inv_cancel₀ hq_ne
```

## Tactic ladder (try in order)

When the goal is a Laurent-polynomial inequality in `(q, q⁻¹)` over
`q ∈ (1, 3/2)`:

| Step | Tactic | When |
|------|--------|------|
| 1 | `field_simp; ring` | Pure algebraic identity (no inequality) |
| 2 | AM-GM rewrite + `positivity` | Goal is `q + q⁻¹ - 2 ≥ 0` or `≥ 0` after rewrite |
| 3 | `nlinarith [sq_nonneg (q - 1), hq_pos]` | Quadratic-in-`q` after AM-GM |
| 4 | `s := q + q⁻¹` substitution + cubic `nlinarith` | Anything cubic or higher |

### AM-GM one-liner

```lean
have h_amgm : q + q⁻¹ - 2 ≥ 0 := by
  have : q + q⁻¹ - 2 = (q - 1)^2 / q := by field_simp; ring
  rw [this]; positivity
```

### Full `s`-substitution ladder

```lean
-- Step 1: package the ratio in `s`.
set s := q + q⁻¹ with hs_def
have hs_ge : s ≥ 2 := by linarith [h_amgm]
have hs_le : s ≤ 13/6 := by
  -- f(q) = q + 1/q is monotone on (1, 3/2]; max 13/6 at q = 3/2.
  -- Standard subgoal — see QOU/Descartes/QHookBound.lean for the
  -- full discharge.
  sorry
have h_diff_sq : (q - q⁻¹)^2 = s^2 - 4 := by
  nlinarith [h_qq_inv]
have h_lhs_in_s : <LHS in q,q⁻¹> = <poly in s> := by
  nlinarith [h_qq_inv, sq_nonneg q, sq_nonneg q⁻¹]

-- Step 2: rewrite the goal in terms of s.
rw [h_lhs_in_s, h_diff_sq]

-- Step 3: discharge the polynomial-in-s inequality.
nlinarith [hs_ge, hs_le,
           sq_nonneg (s - 2), sq_nonneg (s - 13/6),
           mul_nonneg (by linarith : s - 2 ≥ 0)
                      (by linarith : (13/6 : ℝ) - s ≥ 0),
           sq_nonneg s, sq_nonneg (s + 1)]
```

The `mul_nonneg (s - 2) (13/6 - s)` hint is the **single most
important** entry — it forces `nlinarith` to use the substrate-
window bracket multiplicatively, which is how every cubic-in-`s`
QOU bound discharges.

## Substrate-window constants

```
s_min = 2          (= q + q⁻¹ at q = 1, by AM-GM)
s_max = 13/6       (= q + q⁻¹ at q = 3/2)
q_min = 1          (open lower bound on the substrate)
q_max = 3/2        (open upper bound; widening fails the cubic-in-s bounds)
```

The bound `q < 3/2` is **tight** — the cubic-in-`s` discharge
needs `s² + 2s + 2` and `3s² - 2s - 10` to share a sign on the
interval, and the larger root of `3s² - 2s - 10` is `(1 + √31)/3
≈ 2.19`, just above `13/6 ≈ 2.17`.  Widening to `q < 2` breaks
this hint set.

## Anti-patterns

- **Do not** call `nlinarith` directly on a Laurent polynomial in
  `(q, q⁻¹)` without the `h_qq_inv` hint — it can't infer the
  multiplicative inverse relationship.
- **Do not** widen `hq2 : q < 3/2` to `q < 2` to "match"
  `qFactRatioBound_two` (which uses `q < 2`) without re-deriving
  `hs_le` for the new interval.  These two ratio bounds use
  different intervals on purpose.
- **Do not** introduce `s := q + q⁻¹` for a *quadratic* goal —
  the AM-GM one-liner (Step 2) is shorter.

## Cross-references

- `lean-substrate-numerics.md` — for the `Real.sqrt substrate_q`
  brackets that close `q^(±1/2)` denominators.
- `lean-mathlibext-curator.md` — for `MathlibExt` companion lemmas
  (`Real.lt_sqrt_of_sq_lt`, `q_half_denom`).
- `formalizer.md` §"QOU tactic ladder (QS18)".
