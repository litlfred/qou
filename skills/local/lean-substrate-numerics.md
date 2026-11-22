---
name: lean-substrate-numerics
roles: [collaborator, owner]
description: >
  Numerical bracket lemmas for the QOU substrate constant
  `substrate_q ≈ 1.1097` and its derived quantities (`Real.sqrt
  substrate_q`, `q^(±1/2)`).  Acts as the canonical entry point
  whenever a Lean goal mentions `Real.sqrt substrate_q`,
  `substrate_q ^ (1/2 : ℝ)`, or related half-power expressions.
allowed-tools: Read Edit Bash Grep Glob
---

# QOU Substrate Numerics Skill

## Role

Provide the standard two-sided brackets on `Real.sqrt substrate_q`
and `q ^ (±1/2)` that close every QOU numeric goal involving the
half-power denominators of `MassDerivation.lean`,
`SkeinMassRelation.lean`, and the q-Planck constant proofs.

The substrate value `q ≈ 1.1097` is constant across QOU; once
bracketed, every dependent `q^(±1/2)` bound discharges by
`linarith` against the bracket.

## When to Use This Skill

- Goal mentions `Real.sqrt substrate_q`.
- Goal contains `substrate_q ^ (1/2 : ℝ)` or
  `substrate_q ^ (-(1/2) : ℝ)`.
- A new mass-bound / Planck-constant proof needs the
  "denominator" `q^(1/2) + q^(-1/2)`.

## Authority commits

| Commit | Lemmas | What they teach |
|--------|--------|-----------------|
| `0e0a14a8` | `sqrt_substrate_q_gt`, `sqrt_substrate_q_lt`, `sqrt_substrate_q_bracket` | Direct `1.05341 < √substrate_q < 1.05342` two-sided bracket |
| `78d28acf` | `Real.lt_sqrt_of_sq_lt`, `Real.sqrt_lt_of_lt_sq` | `MathlibExt` companions that drive the bracket |
| `1f34de8c` | `Real.rpow_half_eq_sqrt`, `Real.rpow_neg_half_eq`, `QOU.MathlibExt.q_half_denom` | Convert `q ^ (±1/2 : ℝ)` to `Real.sqrt q` and `1 / Real.sqrt q` |

## Canonical brackets (already in `QOU/MassDerivation.lean`)

```lean
lemma sqrt_substrate_q_gt :
    (1.05341 : ℝ) < Real.sqrt substrate_q := by
  apply QOU.MathlibExt.Real.lt_sqrt_of_sq_lt
  · norm_num
  · unfold substrate_q; norm_num

lemma sqrt_substrate_q_lt :
    Real.sqrt substrate_q < 1.05342 := by
  apply QOU.MathlibExt.Real.sqrt_lt_of_lt_sq
  · norm_num
  · unfold substrate_q; norm_num
  · unfold substrate_q; norm_num

lemma sqrt_substrate_q_bracket :
    (1.05341 : ℝ) < Real.sqrt substrate_q ∧
    Real.sqrt substrate_q < 1.05342 :=
  ⟨sqrt_substrate_q_gt, sqrt_substrate_q_lt⟩
```

## Recipes

### Convert `q ^ (1/2 : ℝ)` to `Real.sqrt q`

```lean
rw [Real.rpow_half_eq_sqrt q]              -- q ^ (1/2 : ℝ) → Real.sqrt q
rw [Real.rpow_neg_half_eq q hq_pos]        -- q ^ (-(1/2) : ℝ) → 1 / Real.sqrt q
```

### Discharge a denominator bound `q^(1/2) + q^(-1/2) ≈ 2.00228`

```lean
rw [QOU.MathlibExt.q_half_denom q hq_pos]
-- Goal is now in `Real.sqrt q + 1 / Real.sqrt q`.
have ⟨hgt, hlt⟩ := sqrt_substrate_q_bracket
have hsq_pos : Real.sqrt substrate_q > 0 := by linarith
-- Bracket the reciprocal, then `linarith`.
have hrcp_lt : 1 / Real.sqrt substrate_q < 1 / 1.05341 := by
  apply div_lt_div_of_pos_left _ _ hgt; linarith; norm_num
-- ... etc; close with `linarith`.
```

## Mathlib-version drift check

This skill must be re-run after every `lake update` of Mathlib:

```bash
cd folio/quantum-observable-universe/lean
lake build QOU.MassDerivation
```

If the brackets fail to close, it is almost always one of:

1. `Real.sqrt_lt_sqrt` API change — re-derive
   `lt_sqrt_of_sq_lt`/`sqrt_lt_of_lt_sq` from current Mathlib.
2. `inv_lt_one_iff_of_pos` rename — search Mathlib for the
   current `lt_one_iff` for `inv`.
3. `mul_inv_cancel₀` rename — `mul_inv_cancel` vs
   `mul_inv_cancel₀` rotates per release.

## Anti-patterns

- **Do not** redefine `substrate_q` to a tighter or looser value
  to "make a bound work" — `substrate_q` is pinned to a 50-digit
  decimal in `q-pinning.md`; any change must go through that
  block, not through ad-hoc redefinition.
- **Do not** prove a fresh `√substrate_q` bracket with different
  numeric endpoints; reuse `sqrt_substrate_q_bracket` so all
  downstream proofs see the same constants.
- **Do not** call `norm_num` on a `Real.sqrt` goal — `norm_num`
  does not evaluate `Real.sqrt` symbolically; the
  `MathlibExt.Real.lt_sqrt_of_sq_lt` bridge is the only path.

## Cross-references

- `lean-q-substitution.md` — for the symbolic-`q` bounds that
  feed the numeric bracket here.
- `lean-mathlibext-curator.md` — for the `Real.lt_sqrt_of_sq_lt`
  family and `QOU.MathlibExt.q_half_denom`.
- `verify-local-substrate.md` — for the upstream check that
  `substrate_q` is *the* pinned constant.
