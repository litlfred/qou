---
# qou-6a7w
title: 'HOLLOW: the y_lambda Wenzl-bridge content-block Lean is identically ZERO and shadows a real library module'
status: todo
type: bug
priority: high
created_at: 2026-08-26T19:32:35Z
updated_at: 2026-08-26T19:32:35Z
---

Found while starting the general-n Gram determinant (the Schur-element product
formula), which is the binding constraint left after bricks 1-4 of qou-s7z2. I
went to build ON the corpus's Schur-element work and found the content-block
copy is hollow.

## Measured, in Lean, not by reading

Appended adversarial probes to a copy of
`content/quantum-observable-universe/mass-theory/y-lambda-closed-form-wenzl-bridge.lean`
and compiled. ALL FIVE PASS (lean exit 0):

  wenzlSchurElement lam Q X = 0        -- for ALL lam, Q, X, by simp
  wenzlNormalization parts Q X = 0
  yLambdaWenzlBridge parts lam q = 0   -- so y_lambda is identically ZERO
  jonesMarkovTrace q x = 0
  hookDim l1 = hookDim l2 := rfl       -- discards its partition argument

The docstrings say so out loud. `wenzlSchurElement`'s reads: "Content-bearing
placeholder `0 * (Q + X + lam.parts.length)`: structurally references all three
arguments while evaluating to 0 by `zero_mul`." That is a description of
DEFEATING THE VACUITY DETECTOR, written into the file. Per AGENTS.md
"No trivial trues, no tautologies, no laundering" that is a review failure, not
a documented compromise.

`hookDim` is worse than vacuous, it is INCONSISTENT: the docstring says
"Computed via hook-length formula. Concrete model: returns `1`" while the code
returns `n.factorial`. Docstring and code disagree, and neither is the hook
formula.

`macdonald-hook-telescope.lean` additionally carries TWO axioms
(`wenzlNormalizationOfShape`, `wenzlSchurElementValue`).

## Why it matters: it SHADOWS a real implementation

`QOU/MathlibExt/WenzlSchurElement.lean` in the LIBRARY tree is real --
`schurElement`, `contentSum`, `hookLength_pos`, `wenzlNormalisation_ne_zero`,
and a genuine `schurElement_ne_zero` with hypotheses.

The hollow file is the `.lean` SIBLING of the content block
`prop:y-lambda-closed-form-wenzl-bridge`, whose .md asserts "The central
coefficients y_lambda ... admit the closed form". Per AGENTS.md 0a, sibling
resolution is CANDIDATE 1 -- so this stub shadows the real library declaration
for every checker aimed at that block. That is the "No shadowing stubs (STRICT)"
violation verbatim, on a PROPOSITION.

## Blast radius: NARROW, and I nearly reported it as wide

First grep showed 3 downstream "consumers". Checked each: NONE consumes the zero
stubs.
- `LeptonMesonParitySplit.lean` defines its OWN `hookDim n hooks := fact n /
  prodList hooks` -- real, and `dim_2` is `by decide`.
- `y-lambda-recipe-from-partition.lean` defines its OWN `hookDim (lam : List N)`.
- `YoungDiagramCellsBridges.lean`'s `content_eq_wenzlSchurElement` points at
  `QOU.MathlibExt.WenzlSchurElement.cellContent` -- the REAL library module, and
  at cellContent rather than the Schur element.

The name `hookDim` is overloaded across three files and `wenzlSchurElement`
across two. The collisions made a self-contained vacuity look like a spreading
corruption. This is the AGENTS.md hazard "attributes do not transfer across
overloaded symbols" biting a blast-radius estimate.

## Prescribed fix, NOT applied

AGENTS.md 0a states the remedy for exactly this shape: "If the decl lives at
<lakeRoot>/<Decl/Path>.lean (candidate 2), do NOT add a sibling .lean -- let the
ref resolve to the library decl." So the fix is to DELETE the shadowing sibling
and let `prop:y-lambda-closed-form-wenzl-bridge` resolve to
`QOU/MathlibExt/WenzlSchurElement.lean`.

Not applied unilaterally: it is a `prop:` block, deletion changes what the
proposition resolves to, and the two axioms in macdonald-hook-telescope need a
separate decision (prove, demote to conjecture, or cite). Owner's call.

## Consequence for the Gram determinant

The general-n Schur-element product formula cannot be built on the content-block
copy. The library module is the real foundation and is where that work should
start.
