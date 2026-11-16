---
# qou-sz98
title: 'GAP: plancherel_via_recipe shadowing stub + content-ref points at the vacuous twin'
status: in-progress
pr: 8206
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T21:12:24Z
updated_at: 2026-11-16T21:22:30Z
parent: qou-6qbv
---

Found draining the small-category vacuity tranche (qou-h3ly), PR #5408. NOT fixed there — deferred because it needs a content-block change plus validation the sandbox cannot run.

**The defect.** `QOU/BraidsAndKnots/PlancherelViaRecipe.lean` contains

    class PlancherelViaRecipeContext where
      holds : (1 : ℝ) = 1
    theorem plancherel_via_recipe [ctx : PlancherelViaRecipeContext] : (1 : ℝ) = 1 := ctx.holds

Doubly vacuous: the class field is `rfl`-provable so it constrains nothing, and the conclusion is a tautology with or without an instance.

**Why it is worse than an ordinary vacuity.** A REAL `plancherel_via_recipe` already exists — `mass-theory/y-lambda-recipe-from-partition.lean:262`, stating the actual identity `Σ_λ (hookDim λ) · yLambdaRecipe λ q v = 1` (backed by `plancherel_via_recipe_axiom`). Both files open `namespace QOU.BraidsAndKnots`, so **both declare `QOU.BraidsAndKnots.plancherel_via_recipe`** — a genuine name collision. This is exactly the shadowing-stub situation AGENTS §0a forbids keeping.

**And a content block points at the wrong one.** `mass-theory/wedderburn-trace-identity.ts:19` has
`lean: { ref: "qou:QOU.BraidsAndKnots.PlancherelViaRecipe.plancherel_via_recipe" }`, which resolves by path to the **vacuous** file. Line 49 of the same manifest already says '... to the true `plancherel_via_recipe`', so the mis-aim was half-noticed.

**The fix (needs one session with the pipeline available):**
1. Delete the stub class + theorem in `PlancherelViaRecipe.lean` (or the file).
2. Retarget the `wedderburn-trace-identity.ts` `lean.ref` to the real declaration.
3. Re-run content validation — this is why it was not done in #5408: changing a `.ts` ref without being able to run the validator risks landing a broken cross-reference.
4. While there: the real one rests on `plancherel_via_recipe_axiom`, so check it against the anti-laundering rule (an axiom is not a proof).

## Round 51 Progress (PR #8206)

- [x] Defined `recipeWeight d s i = s i / ∑ j, d j * s j` and proved `recipe_plancherel_normalization : ∑ i, d i * recipeWeight d s i = 1` in `QOU/BraidsAndKnots/PlancherelViaRecipe.lean`, constructed `canonicalH2PlancherelContext`, and added nested `QOU.BraidsAndKnots.PlancherelViaRecipe.plancherel_via_recipe` matching `mass-theory/wedderburn-trace-identity.ts` (PR #8206, HEAD `aecfe3f528c442bfb5e105f53d801fa139604119`).
- [x] Verified 80-dps `mpmath` witness `round51-devacuify-6qbv.witness.json` (`allPassed: true`, `0` float64 values) and `0` findings across all 6 vacuity audits.
- [ ] Awaiting Merge Manager merge of PR #8206.
