---
# qou-m45w
title: per_generator_V_hat_3A re-buckets the interleaved nucleon word by generator; v_p = V0·V1 is the grouped-word trace
status: todo
type: bug
priority: high
tags:
    - compute-accuracy
created_at: 2026-11-27T20:31:47Z
updated_at: 2026-11-27T20:31:47Z
parent: qou-myts
---

## Finding (2026-11-27, PR #9670)

`computations/mass_at_3A_proper.py::per_generator_V_hat_3A` buckets each word's
factors by generator (`word_by_gen[g].append((c, d))`) and then multiplies each
bucket into a single `α_i σ_i + β_i`. So `V̂_i` is computed on the **grouped** word.
`binding_block_multiplicative.py` then uses `v_p = V^p_0 · V^p_1` and
`v_n = V^n_0 · V^n_1`.

Under convention D, `V̂_i = α_i z + β_i`. Lean (`QOU.BraidKnot.tr_block_word`, PR
#9670) proves that `V̂_0 V̂_1` is the Markov trace of the **ascending regrouped**
block word `W_0 W_1`, not of the interleaved word. The interleaving matters:
`tr(σ₁σ₂σ₁σ₂) − tr(σ₁²σ₂²) = z² − hz − 1 = −(q⁴+q²+1)/(q²+1)²`, which is never zero.
The intra-nucleon word was fixed to be built interleaved in `nucleon_word_letters`
(bean `qou-hu1f`, 2026-09-05; the comment there gives 82 % at q₀ for `σ₀³σ₁⁻³`
against `(σ₀σ₁⁻¹)³`). The per-generator V̂ path re-buckets that interleaved word,
which undoes the fix on this path. This is the same kind of artifact that
`qou-4383` hunted, at a site that audit's fingerprints do not cover.

## Fix (derived, no fitting)

Replace `v = V̂_0 V̂_1` by the Markov trace of the block's interleaved word,
`tr(wordVal 0 w)` (Lean `tr_blockProd_pn`: the vacuum trace is
`tr(w_p)^Z · tr(w_n)^N` with each block read at offset 0). Then re-run
`binding_block_multiplicative.py`, `binding_via_interface_knot.py` and the
witnesses downstream, and report how far the numbers move.

Measure first: compute `tr(w_p)` exactly (sympy ℚ(q), or mpf at q₀) against the
grouped `V̂_0 V̂_1`. A difference of zero would mean the words commute
generator-wise. That is not expected.
