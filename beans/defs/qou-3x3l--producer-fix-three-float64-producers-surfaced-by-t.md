---
# qou-3x3l
title: 'PRODUCER FIX: three float64 producers surfaced by the q0 refresh (sublemma / toffoli / six-term)'
status: completed
type: task
priority: normal
created_at: 2026-08-24T07:40:43Z
updated_at: 2026-08-24T08:09:02Z
---

Surfaced by the q0-anchor refresh on claude/q0-anchor-flip-tranche-2026-08-19.
Context and the systemic half of the finding: qou-kn46.
Two of the original five were fixed inline (commit bd5a3dc31); these three
need real refactors and were deliberately left, not silenced. No baseline
was widened.

## The three

**computations/sublemma_2_1_alpha_shift_extract.py** (47 -> 82 fields)
numpy end-to-end -- `M @ sol`, `np.abs`, `np.max`. Line 153:
`"value_re": float(sol[p].real), "value_im": float(sol[p].imag)`.
The regression is 35 `value_im` fields going `0` -> `-0.0` (a signed-zero
artifact). `value_re` was already float64 and already in the baseline, so
fixing only `value_im` would be incoherent -- the whole solve has to move
to mpmath, or the alpha_shift block has to serialize via `_precision.fmt`
as a pair of strings. Note line 238-239 reads `info["value_re"]` /
`info["value_im"]` back for display, so a string switch needs that too.

**computations/toffoli-lp-stability.py** (203 -> 211)
numpy end-to-end -- `gram_matrix(Q0).tolist()`, `toffoli_diagonal(q)`,
`q_and_amplitude(q)`. The eight flipped fields are `0 -> 0.0`,
`1 -> 1.0`, `2 -> 2.0` at exactly-representable scan points and at the
q=1 classical limit. Same shape of fix: mpmath, or serialize exactly.

**computations/sweeps/paper_six_term_shadow_price_sweep.py** (71 -> 79)
This is the closest to a clean fix and the most annoying to land.
The compute is ALREADY mpmath (`mp.mpf`, `w_lambda`, `tau_lambda`), and
line 230 collapses it: `"C_lambda": float(c_lambda), "S_lambda": float(S),
"contribution": float(contrib)`, then `return float(total), contributions`.
The eight flipped fields are `S_lambda` = the mass number A (2 for D, 4 for
He4) -- exact integers.
Two obstacles: (i) `contributions.sort(key=lambda r: abs(r["contribution"]))`
reads the serialized value back, so sorting must happen on the mpf before
serialization; (ii) `float(total)` is consumed numerically by
`isospin_mirror_test` and the sweep's callers, so the return type change
ripples. No live consumer reads the WITNESS payload (only
computations/_deprecated/iterative_tower_unified_mass.py and three audit
docs), so the serialized side is free to become `_precision.fmt` strings.

## Why not fixed inline

The branch is a q0-anchor migration. Two of the five were one-line exactness
fixes with no schema change and no consumer risk, so they landed. These three
change either the arithmetic backend or the witness schema, which is a
different tranche and wants its own review.


## CLOSED 2026-08-24 — all three fixed on claude/q0-anchor-flip-tranche-2026-08-19

Sized the work and it was smaller than this bean assumed. All three landed;
ratchet REGRESSED 5 -> 0, and the branch now drains 59 files / +3,058 fields.

- six-term (7ed6b608c) — sort on the mpf, serialize once at the boundary.
  The witness had been recording a 65-dps compute at float64 width.
- toffoli (dcde98f93) — mp.matrix + mp.eigsy for np.zeros + np.linalg.eigvalsh;
  `json.dump(..., default=float)` was rounding every mpf on the way out.
- sublemma — mp.qr_solve for np.linalg.lstsq, rank from mp.svd singular values.

**The one that nearly shipped a worse defect than it fixed.** The first
sublemma conversion passed `q_parameter.Q` to `chi_lambda_fast_mp`, whose
docstring says *"q_val MUST be an mpmath.mpf"*. `Q` is a Python **float**;
`Q_MP` is the mpf. So the mpmath matrices were seeded with 53 bits and
`fmt()` padded the result to 51 digits:

    1.00544843335356137714597934973426163196563720703125000000000

which round-trips EXACTLY to a float64 — the "reads as measured while
carrying float64 precision" failure `_precision`'s own docstring warns about.
The true value is `1.00544843335356114987624598904593140794462037424206635479002`,
diverging at digit 17. Caught by testing `Decimal(float(s)) == Decimal(s)`
on every long decimal string in the witness. **Run that test after any
float64 -> mpmath conversion**; a conversion that reaches an mpmath API with a
float argument produces output that looks fixed and is not.

That test also has the int-vs-float blindness qou-kn46 describes: it flagged
9 toffoli + 10 six-term values that are exact dyadic rationals at q=1
(0.5, 0.375, 1.125, 2.625) and exact T(T+1)/A ratios (0.75). Genuine values,
not padding.
