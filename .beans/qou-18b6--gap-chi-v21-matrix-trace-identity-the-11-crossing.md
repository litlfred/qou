---
# qou-18b6
title: 'GAP: chi_v21_matrix_trace_identity — the 11-crossing Hoefsmit matrix-product trace is stated, not proved'
status: completed
type: task
priority: normal
created_at: 2026-09-04T04:40:15Z
updated_at: 2026-09-04T13:29:00Z
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


---

## RE-DIAGNOSED 2026-09-04 — this bean was wrong about the nature of the gap

**The statement was FALSE, not merely unproved.** This bean said "It is the
Lean proof that is missing, not the result", and "the claim is exactly the one
sympy verifies". Both are wrong about *these* definitions.

`hoefsmit_v21_d1` and `hoefsmit_v21_d2` were **transposed**. With
`sigma_0 = diag(q, -q⁻¹)` the pair failed the braid relation
`σ₀σ₁σ₀ = σ₁σ₀σ₁`, so it was not a representation of `B_3` and the trace was
of an object that does not exist. Measured: the file's own matrices give
`chi_n - chi_p` larger than the closed form by exactly `(q⁴+q²+1)/q²`,
confirmed at `q = 2`, `3/2` and `1.1099`.

**The closed form was right all along** — expanded at `q = 1+ε` it matches the
witness's ε-coefficients (`0, -1, 1/2, -5/2, 7/2, -5, 27/4, -35/4`); the
transposed matrices give `0, -3, 3/2, -23/2, ...`.

Fixed in PR #6662, with `hoefsmit_v21_braid_relation` added as the guard —
sorry-free, and the cheapest statement that can see a transposition, since
`b²`, the trace, the determinant and the Hecke quadratic are all **symmetric**
in `d_1, d_2`.

## What is still open, and it is a DIFFERENT problem

The identity is now true. The remaining gap is **compute size, measured**: the
proof reaches a fully expanded scalar goal (`simp only` over the definitions
and `List.foldl_cons`, then `Matrix.mul_fin_two` + `Matrix.trace_fin_two`), and
`field_simp` then **exhausts 2 000 000 heartbeats** on it. Not a slow machine,
not a missing lemma — the 11-fold product of 2×2 matrices in `q, q⁻¹, b` is
simply too large to clear.

**So the route this bean recorded — "linear_combination needs the polynomial
coefficient, not hand-guessable at degree 11" — is the wrong route.** No
certificate is needed at all.

## The route that works (verified symbolically, not guessed)

Every index-0 crossing is DIAGONAL:

    σ₀ - (q-q⁻¹)·I   = diag(q⁻¹, -q)            (= σ₀⁻¹)
    σ₀ - (q-q⁻¹)/2·I = ((q+q⁻¹)/2)·diag(1,-1)

so the seven index-0 factors collapse *before* any expansion:

    beta_p index-0 block = ((q+q⁻¹)/2)  · diag(q⁶, -q⁻⁶)
    beta_n index-0 block = ((q+q⁻¹)/2)² · diag(q⁵, -q⁻⁵)

one lemma each. What remains is `trace(D · M)` with `D` diagonal and `M` a
product of only FOUR index-1 factors, i.e. `D₀₀·M₀₀ + D₁₁·M₁₁`. Each index-1
factor is symmetric with off-diagonal `b`, so only EVEN powers of `b` survive
in `M₀₀` and `M₁₁`, and `b² = hoefsmit_v21_b_sq q` eliminates the square root
directly.

Next commit's work.

## Also corrected

The `.md`'s "Not yet formalised" item 2 said the swap was known and that "the
closed-form rational result is invariant under the swap". That parenthetical is
false and is what let the defect stand — `b²`, trace and determinant are
invariant; the result is not.


---

## CLOSED 2026-09-04 — proved sorry-free (PR #6662)

`chi_v21_matrix_trace_identity` is proved. `#print axioms` =
`[propext, Classical.choice, Quot.sound]`; no `sorryAx`. The statement is
byte-identical to the one that carried the `sorry` — only the matrices it is
about were corrected.

**Mutation test:** changing the closed form's `q^4 + 1` to `q^4 + 2` makes the
proof FAIL (exit 1, 4 errors). It is not closing vacuously.

## The one tactic choice that decided it

Use **`Matrix.trace_fin_two_of`**, which rewrites `trace !![a,b;c,d]` straight
to `a + d`. NOT `Matrix.trace_fin_two`, which leaves `M 0 0 + M 1 1` as
*applications* — with that, `field_simp` runs on the un-projected expression
and exhausts 2,000,000 heartbeats. The two lemma names give no hint of this.

Working sequence:

    simp only [defs..., List.foldl_cons, List.foldl_nil, if_true, hif, one_mul]
    simp only [hsm, hsub, Matrix.mul_fin_two, Matrix.trace_fin_two_of]
    generalize Real.sqrt (hoefsmit_v21_b_sq q) = b at hb2 ⊢
    ring_nf
    rw [hb4, hb2]        -- b^4 FIRST; rw [hb2] cannot see inside b^4
    field_simp
    ring

with three local helpers: `hif : ∀ A B, (if (1 : Fin 2) = 0 then A else B) = B`
(by `norm_num` — `reduceIte` does NOT fire on this), `hsm : ∀ c, c • 1 =
!![c,0;0,c]`, and `hsub` for the subtraction of two `!![...]` literals.

## Corrections to my own earlier notes on this bean

1. **"linear_combination needs a coefficient not guessable at degree 11" —
   WRONG, no certificate is needed.** Only EVEN powers of `b` reach the trace:
   each index-1 factor is symmetric with off-diagonal `b`, so a path from a
   diagonal slot back to itself takes an even number of off-diagonal steps.
   Odd powers DO occur — `b^3` appears 20 times in the normalised matrix — but
   only in the OFF-DIAGONAL entries, which the trace discards. Projecting
   first is what makes `b² ↦ (q⁴+q²+1)/(q²+1)²` sufficient alone.
2. **"`ring_nf` re-folds the matrix literals back into `Matrix.mul`" —
   RETRACTED.** I recorded that as a tactic property in a commit message. It
   was an artifact of that run: `if (1 : Fin 2) = 0` was still unreduced, so
   matrices genuinely remained for `ring_nf` to act on. With `hif` in place
   there are none left and `ring_nf` behaves correctly. Do not avoid `ring_nf`
   here — the proof needs it.
3. **The structural decomposition I proposed as "the route that works"
   (collapsing the seven diagonal index-0 factors first) was never needed.**
   It is correct mathematics and would also work, but the flat expansion
   closes once the projection is right. Cheaper to fix the projection than to
   restructure.

## Preceding correction (same PR)

The `sorry` had stood over a FALSE statement: `hoefsmit_v21_d1` and
`hoefsmit_v21_d2` were transposed, failing the braid relation, so the pair was
not a `B_3` representation. See the earlier entry. `hoefsmit_v21_braid_relation`
is now the guard.
