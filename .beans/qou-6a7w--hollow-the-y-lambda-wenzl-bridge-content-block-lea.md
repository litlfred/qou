---
# qou-6a7w
title: 'HOLLOW: the y_lambda Wenzl-bridge content-block Lean is identically ZERO and shadows a real library module'
status: completed
type: bug
priority: high
created_at: 2026-08-26T19:32:35Z
updated_at: 2026-08-27T05:35:37Z
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


## CORRECTION 2026-08-26 — "shadows a real library module" is WRONG; retracted

The section above classifies this as an AGENTS.md 0a SHADOWING STUB and
prescribes deleting the sibling so the ref resolves to
QOU/MathlibExt/WenzlSchurElement.lean. **That is wrong.** Caught before acting on
it, by checking what the ref actually resolves to rather than trusting my own
diagnosis.

  prop ref:  qou:QOU.BraidsAndKnots.y_lambda_closed_form_wenzl_bridge

That declaration exists ONLY in the content-block sibling. grep over the entire
library tree returns nothing. The library module is namespace
QOU.MathlibExt.WenzlSchurElement carrying `schurElement (Q X : R) (lam :
Partition)` -- a DIFFERENT declaration, in a DIFFERENT namespace, over a
DIFFERENT Partition type (QPartitionCombinatorics' list-based one, versus the
sibling's `structure Partition (n : N)`).

0a shadowing means the sibling occludes a real library declaration the ref would
OTHERWISE RESOLVE TO. Candidate 2 here
(<lakeRoot>/QOU/BraidsAndKnots/y_lambda_closed_form_wenzl_bridge.lean) does not
exist. So the sibling shadows NOTHING, and deleting it would leave the prop's
lean.ref UNRESOLVABLE -- strictly worse than the status quo.

**How I got it wrong.** I saw a real module whose name matched the topic
(WenzlSchurElement) and inferred it was the same object under a different path.
It is not. Same failure shape as the blast-radius error recorded above -- name
similarity standing in for declaration identity -- committed twice in one
investigation, the second time in the fix rather than the diagnosis.

## What actually stands

The MEASUREMENT is unaffected and was independently verified: wenzlSchurElement
= 0, wenzlNormalization = 0, yLambdaWenzlBridge = 0, jonesMarkovTrace = 0,
hookDim discarding its argument, all by Lean probes compiling exit 0. The
docstring still states the evasion technique. hookDim's docstring still
contradicts its body. macdonald-hook-telescope.lean still carries two axioms.

Correct classification: **vacuous / laundered formalisation** (AGENTS.md 1a
"No audit-dodging", "No trivial trues"), NOT a shadowing stub.

## Honest dispositions -- 1a's three, plus a fourth that is available here

1. Prove it: implement the real Schur element. Large.
2. Queue it: state the REAL proposition with `sorry` + a `-- Ref:` citation.
3. Demote the block to `conjecture`.
4. **DELEGATE** -- newly available, and the cheapest honest option: the library
   module's `schurElement` is real, and the sibling's `Partition (n)` structure
   carries `.parts : List N`, which is exactly the library's Partition type. So
   `wenzlSchurElement lam Q X := WenzlSchurElement.schurElement Q X lam.parts`
   is a genuine delegation, replacing zero with the real definition and leaving
   the ref resolving where it already resolves.

Route 4 is what I am attempting. If the type bridge does not hold up, route 2
(honest sorry + Ref) is the fallback -- NOT a return to zero.

Corrected on PR #5857, in the coordination ledger, and on the one sibling PR
(#5352) where the wrong advice was load-bearing:
https://github.com/litlfred/qou/pull/5352#issuecomment-5430258333


## ROUTE 4 ATTEMPTED AND IT FAILS -- informatively. The theorem is 0 = 0.

Delegated `wenzlSchurElement` to the real library `schurElement` (the type
bridge DOES hold: library `Partition` is `abbrev Partition := List N`, and the
sibling's `structure Partition (n)` carries `.parts : List N`, so
`schurElement Q X lam.parts` typechecks). The file then FAILS TO COMPILE, at
exactly one place -- line 172, the block's main theorem:

  theorem y_lambda_closed_form_wenzl_bridge ... :
    jonesMarkovCoefficient q lam = yLambdaWenzlBridge parts lam q

Residual goal with the real Schur element in place:

  0 = schurElement (wenzlQ q) (wenzlX q) lam.parts / (sum over parts ...)

So the theorem was provable ONLY because BOTH sides are definitionally zero:
`jonesMarkovCoefficient = 0 * q` on the left, and `0/0 = 0` on the right. Make
either side real and the statement is FALSE for generic q.

**This is stronger than "vacuous".** The declaration the prop's lean.ref points
at is `0 = 0`, while its docstring reads: "Numerically verified to 10^-16 for
all 270 partitions of n = 2, ..., 12 in y-lambda-wenzl-bridge-symbolic-witness.json
and gb-filtration-gauge-invariance.witness.json." The docstring describes a
verified nontrivial identity; the Lean states an identity between two zeros. The
witnesses may well be real -- that is a separate question, and nothing here
impugns them -- but the THEOREM does not state what the docstring says was
verified.

## Why route 4 alone cannot fix it

Delegating the Schur element makes the RIGHT side real. The LEFT side is
`jonesMarkovCoefficient`, the actual Markov-trace central coefficient -- the hard
object, with no library replacement. Fixing one side without the other converts a
vacuous truth into a falsehood. So the cascade is: real Schur element REQUIRES a
real jonesMarkovCoefficient, which is the very thing the arc is trying to reach.

Edit REVERTED; the file compiles again as committed (exit 0). I am not leaving a
broken tree, and not landing a change that turns 0 = 0 into a false statement.

## Honest dispositions now, narrowed to two

1. **Route 2 -- state the real proposition with `sorry` + `-- Ref:`.** The
   citations are already in the file (wenzl1988, chlouveraki2016 Thm 6.20). The
   honest form states `jonesMarkovCoefficient = yLambdaWenzlBridge` with BOTH
   sides real and a cited `sorry`, and the block's derived status becomes
   `has_sorry` -- the honest "stated, not yet proved" marker.
2. **Route 3 -- demote the block from `proposition` to `conjecture`.** Per 3b
   this is defensible: the statement depends on the Markov trace being the hard
   unformalised object.

Both are substantive changes to a `prop:` block. OWNER'S CALL -- and route 4 was
worth attempting precisely because its failure narrows the choice to these two
and shows why neither is avoidable.


### 2026-08-26 — (P)'s bookkeeping is complete; (P) itself is not

PR #5857, twelve commits.

**The hook-length update rule is proved** (`hookLength_addBoxRow_of_ne_corner`):
adding a box to row `r` raises the hook length by exactly 1 on the arm cells of
row `r` and the leg cells of column `λ_r` above row `r`, and leaves every other
cell alone. The new box itself is excluded — its hook is 1 only by the
weakly-decreasing property, which the bare `List ℕ` carrier does not have.

**`schurElement` is now a product** (`schurElement_eq_prod`), not a fold. That
was a real obligation, not a rewriting convenience: nothing cell-by-cell can be
said about a fold. Cross-checked at λ=(2,1), Q=2, X=3 against the value
`telescope_three_needs_multiplicity` derives independently: both 10/7.

**All three box-addition cases for the row factor are proved** — below (equal),
the receiving row (`List.range_succ` split), and above (product surgery at one
interior index, via `Finset.mul_prod_erase`; stated division-free because
`cellFactor`'s denominator may vanish).

**What is left is (P) itself**: the sum over addable corners. Everything above
is its bookkeeping. Do not read "all three cases proved" as "(P) proved" — the
per-shape ratio is in place, the identity is not.

Corpus-grep before claiming this open: `udmw` is a *different* telescope
(AJFigureEight / Andersen–Kashaev), not this one.


### CORRECTION to the entry above — "every ingredient of the per-shape ratio is
### now in place" was WRONG

I wrote that one commit ago. It is not right, and the distinction changes the
scoping.

`rowFactor_addBoxRow_same_row` gives the receiving row as a product over
**shifted** hooks, `∏_{j<λ_r} (1 − X·Q^{c(r,j)}) / (1 − Q^{h_λ(r,j)+1})`. That
is not expressible in terms of `rowFactor Q X λ r`, which is the same product
over **unshifted** hooks. Relating them means evaluating
`∏_j (1 − Q^h)/(1 − Q^{h+1})` over row `r`, which collapses only because of what
a row's hook lengths actually are — the hook-walk. **That is the substance of
(P), not its bookkeeping.**

So the remaining work is TWO things, not one:

1. the hook-shift collapse over a row, and
2. the sum over addable corners.

What landed (§5, §6 of the PR) is genuinely reusable and is less of (P) than I
claimed. `nLambda_addBoxRow : n(λ + box in row r) = n(λ) + r` is the prefactor's
share and is complete; the denominators are not.

Recording it here rather than only in the PR body because this bean is what a
later agent greps, and "all the ingredients are in place" would send them in
expecting an assembly job.


### CORRECTION TO THE CORRECTION — measured, 2026-08-26

I over-corrected the entry above. `computations/y_lambda_pieri_step_probe.py`
(exact sympy, no floats, no witness) measures what I had been asserting:

- **(P) holds with X FREE** at eight shapes, up to `(3,2,1)` with four addable
  corners.
- **The per-shape ratio HAS a closed form** and it needs no collapse:
  `s_{λ+□(r)}/s_λ = Q^r · (1 − X·Q^{λ_r−r})/(1 − Q^{h_μ(r,λ_r)}) ·
  ∏_{h ∈ arm ∪ leg} (1−Q^h)/(1−Q^{h+1})`. The arm and leg sets are exactly what
  the Lean update rule moves; `Q^r` is `nLambda_addBoxRow`.
- **The shift product does NOT collapse** — `(Q²+Q+1)/((Q+1)³(Q²+1))` at
  `λ=(3,2,1), r=1`; `1/(Q²+Q+1)` at `(3,1), r=1`.

So the previous entry's "relating them is the hook-walk, the substance of (P)"
is **wrong**. There is nothing to collapse. The per-shape ratio is reachable
from what has landed, which is closer to my ORIGINAL claim than to the
correction of it. **The sum over corners is the hard part, and always was.**

That is three successive mischaracterisations of the same piece of mathematics,
each stated confidently, none measured until now. The probe exists so the next
one is checked rather than recalled.

### A real gap in the Lean, found by the same probe

`addBoxRow` is `List.set`, which is a **no-op out of range**. So
`addBoxRow λ (length λ) = λ`, **not** `λ ++ [1]`. The new-bottom-row corner is
not expressible by `addBoxRow` and needs its own operation — and every shape
in the probe has exactly one such corner. Any attempt at (P) must add it.


### The new-bottom-row corner now exists in Lean (2026-08-26)

The gap recorded above is closed. `addBoxNewRow lam = lam ++ [1]`, with the kit
mirroring `addBoxRow`'s: length, both `getElem?` cases, `drop`, the hook-length
response, and `nLambda`. Plus `addBoxRow_at_length : addBoxRow lam lam.length =
lam` — the trap stated as a theorem so it cannot be re-discovered by accident.

Two ways the last row is EASIER than an interior corner, both worth carrying
forward:

- **Only column 0 changes.** The new row holds one cell, so its entry `1`
  exceeds `j` exactly when `j = 0`; every other column's leg count is blind to
  it.
- **The new cell's hook is `1` unconditionally.** Nothing lies below the last
  row, so no order hypothesis is needed — unlike the interior corner, which
  `hookLength_addBoxRow_of_ne_corner` must exclude precisely because the bare
  `List ℕ` carrier does not carry weak decrease.

`nLambda_addBoxNewRow : n(λ ++ [1]) = n(λ) + ℓ(λ)`, checked against the probe
(`[3,2,1] → [3,2,1,1]`, `n` going `4 → 7`).

Guard rc=0 on 149. What is left for (P) is now exactly the sum over corners.


### (P) now holds in Lean at TWO shapes, and the second one is the engine test

`pieri_one` is (P) at `λ=(1)`, whose two corners are both trivial — a single row
and a single column, neither with a cell above or below the new box. It cannot
distinguish the three row cases.

`pieri_two_one` is (P) at `λ=(2,1)`, whose three corners are one of each kind:
`(3,1)` a box with a row **below**; `(2,2)` a box with a row **above** in the
changed column (the interior case needing product surgery); `(2,1,1)` a **new
bottom row**, which `addBoxRow` cannot express. First shape where every moving
part is in play at once — the (P) analogue of `telescope_three`.

Sharp at `Q=2, X=3`: total `20/7`, summands `22/9`, `40/63`, `−2/9`. The
summands are recorded separately because a sum identity whose summands were
equal, or all of one sign, is a much weaker check than it looks. One is
negative.

Guard rc=0 on 152.

**What remains for (P) is the induction over addable corners.** Every ingredient
is in Lean, and the statement now has two independent confirmations there.

**Discipline note, second instance this session.** I wrote `−4/7` for the total
from memory, into a theorem whose entire purpose is to check a constant.
`norm_num` rejected it; the computed value is `20/7`. Compute, do not recall.


### CLOSED — PR #5857 merged 2026-08-27 05:15 (6f4d0d2a3a)

Everything this bean tracked is on main: the prefactor bug and its fix, the
telescope at n=1,2,3 with two degeneracy guards, the hook-length update rule,
schurElement as a product, all three row-factor cases, addBoxNewRow, and (P)
at (1) and (2,1).

Follow-up work continues on PR #5871 (a NEW PR — a merged PR is finished):
addableCorners plus (P) stated in general, with both proved cases shown to be
instances of it. What remains is the induction over corners, tracked there.
