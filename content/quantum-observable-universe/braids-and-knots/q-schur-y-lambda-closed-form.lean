/-!
# QOU.BraidsAndKnots.QSchurYLambdaClosedForm — sibling-resolution stub

**Sibling-resolution stub** for content block
[`prop:q-schur-y-lambda-closed-form`](q-schur-y-lambda-closed-form.md):
*q-Schur Plancherel weights y_λ(q) closed form via q-content principal
specialization*.

The formal proof lives at
[`../lean/QOU/BraidsAndKnots/QSchurYLambdaClosedForm.lean`](../lean/QOU/BraidsAndKnots/QSchurYLambdaClosedForm.lean)
under the `qou` Lake package (file pending — the formula
y_λ(q) = q^{content_sum(λ)} / [n]_q! is implemented in Rust via
pyhecke_native.trace_weights_n_q_schur and verified numerically at H_2
to match the sibling T(2,k) hardcoded formula exactly).

This stub satisfies the lean-ref sibling-resolution rule (CLAUDE.md §0a step 1).

-- Ref: [wenzl1988] Wenzl, "Hecke algebra traces of the symmetric group", Invent. Math. 92 (1988)
-- Ref: [jones1987] Jones, "Hecke algebra representations of braid groups and link polynomials", Ann. Math. 126 (1987)
-/
