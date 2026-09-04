---
# qou-18b6
title: 'GAP: chi_v21_matrix_trace_identity — the 11-crossing Hoefsmit matrix-product trace is stated, not proved'
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T04:40:15Z
updated_at: 2026-09-04T12:42:45Z
---

## What is open

`content/quantum-observable-universe/mass-endomorphism/chi-v21-hoefsmit-matrix-derivation.lean`

    theorem chi_v21_matrix_trace_identity (q : ℝ) (hq : q ≠ 0) :
        chi_v21_on_word q beta_n_word_v21
          - chi_v21_on_word q beta_p_word_v21
          = chi_V21_difference_factored q

The trace of the Hoefsmit V_(2,1) matrix product over the canonical 11-crossing
typed-B₃ word for β_n − β_p equals `-(q⁴+1)(q²-1)/(4q³)`.

**Empirically verified** via sympy (`q_character_on_braid_word` + `cancel` +
`factor`) in `computations/probe_per_wedderburn_block_ck.py`; the bit-exact
closed form is in `per-wedderburn-block-ck.witness.json`. It is the Lean proof
that is missing, not the result.

## Why the old state was worse than a `sorry`

The file carried a tactic script that **did not prove it and could not be seen
to fail**: elaboration hit the 200 000-heartbeat `whnf` timeout before reaching
the failing step, so the file read as "proof present, environment too slow".
Raised to 4 000 000, it completes in 28 s and reports the real error:

    rewrite failed: Did not find an occurrence of the pattern
      √(hoefsmit_v21_b_sq q) ^ 2

— `ring_nf` had already normalised the square away, so `rw [h_sqrt]` never
applied. Now `sorry` + `-- Ref:` (AGENTS.md §Zero-sorry default, state-and-queue).

A second, independent defect in the same file: `hoefsmit_v21_b_sq_rational` was
declared at the END of the file and consumed at line 247, so Lean reported
`Unknown identifier hoefsmit_v21_b_sq_rational`. **A forward reference and a
missing declaration are indistinguishable from that error text.** Moved up;
that error is gone.

## How far the proof gets — start here, not from scratch

With `b := √(hoefsmit_v21_b_sq q)` `set` before unfolding:

    simp only [List.foldl, Matrix.trace_fin_two]   -- the rest of the old
                                                   -- simp set is unused
    field_simp

reduces the goal to a **polynomial identity in `q` and `b` modulo the single
quadratic relation**

    b² = (q⁴ + q² + 1) / (q² + 1)²          (`hoefsmit_v21_b_sq_rational`)

Missing: the elimination step. `nlinarith [h_sqrt, sq_nonneg b, sq_nonneg q]`
does not close it, and `linear_combination` needs the polynomial coefficient of
that relation, which is not hand-guessable at degree 11.

## The tractable route

The file's own `@[deprecated]` notice on `sigma1_v21_legacy` already names it:
restate over `sigma1_v21_gen d1 d2 b` with `b² = d1·d2 + 1` as an **explicit
hypothesis** (Tier 2 of `docs/audits/2026-06-01-hoefsmit-tier2-migration-plan.md`).
Then `b` is a free variable, the identity is polynomial in `(q, b)`, and the
relation applies by `ring`-level rewriting rather than by search.

## Do NOT

- Weaken the statement until it becomes provable — the claim is exactly the one
  sympy verifies.
- Assume it as a class field and project it out (§3b-cond item 5).
- Re-add a tactic script whose failure mode is a heartbeat timeout; if you try
  something, raise `maxHeartbeats` first so a failure is a *failure* and not a
  timeout.

## State after PR #6540

lean-direct: **0 errors**, 3 warnings — 2 deliberate deprecation-use warnings
(the legacy Hoefsmit form is used pending exactly this Tier-2 migration) and the
`declaration uses 'sorry'` marker. Was 1 error + 21 warnings. Also fixed in
passing: two `@[deprecated]` attributes missing `(since := ...)`, an unused
`hq` on `sigma1_v21_param_sq_trace` (an unused hypothesis overstates what the
statement needs), and three unused simp arguments.
