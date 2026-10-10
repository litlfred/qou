---
# qou-qbg9
title: 'Attack vectors for the resurgence-arc Lean gaps, TIERED by kind (not by file)'
status: scrapped
type: task
priority: high
created_at: 2026-08-08T12:05:00Z
updated_at: 2026-08-08T12:55:00Z
---

Survey 2026-08-08 of real `sorry`s in the resurgence arc (grep corrected to
exclude the phrase "sorry-free", which inflates naive counts):

    Mathlib/ArgumentPrinciple.lean          2
    Mathlib/BorelResummation.lean           4
    Mathlib/EllipticDivisorDegree.lean      2
    Mathlib/HadamardFactorization.lean      4
    Mathlib/IdentityIHLFBridge.lean         1
    Mathlib/QGevreyOrder.lean               4
    Mathlib/RSKBridge.lean                  1
    Mathlib/SYTBranchingRecursion.lean      3
    Mathlib/SYTHookGNW.lean                 3
    Resurgence/StokesMatrixDescent.lean     1

**These are not one kind of gap and must not be attacked as one.** Tiering:

## TIER 1 — hard Mathlib gaps. NOT session-closeable. Do not start casually.

`ArgumentPrinciple`, `EllipticDivisorDegree`, `HadamardFactorization`,
`BorelResummation`.

`EllipticDivisorDegree`'s cited sorry says it outright: *"needs the argument
principle (Σ ord = (1/2πi)∮ f'/f) from complex analysis"*, absent from Mathlib
v4.24.0. Hadamard factorization and Borel resummation are the same shape: real
analytic theorems missing upstream. These belong to the existing epic `qou-08a2`
(keystone de-abstraction, hard Mathlib-gap infra), not to an afternoon.

**Honest note against my own session's work.** The `det A` argument in
`qou-qbe9x` -- that C1's third singular site is non-removable because
`deg div(det A)|_{C*} = -1` is gauge-invariant -- leans on exactly the
sum-of-orders fact that `EllipticDivisorDegree` cannot yet formalise. The
argument is correct mathematics and standard, but it is **not** Lean-backed, and
this bean records that so nobody cites it as if it were.

## TIER 2 — algebraic, plausibly closeable. START HERE.

`Resurgence/StokesMatrixDescent.lean` (1 sorry): block-diagonalisation (A.i) of
an `S_n`/Wedderburn-equivariant Stokes matrix. The neighbouring lemma is already
a clean `calc` over orthogonal idempotents (`e i * S * e j = 0` from
`hf.ortho`), so the missing step looks like idempotent bookkeeping rather than
analysis. **Assess first; if it is genuinely algebraic, close it.**

`Mathlib/IdentityIHLFBridge.lean` (1), `Mathlib/RSKBridge.lean` (1): single
sorries in bridge files -- cheap to at least CLASSIFY (algebraic vs analytic)
even if not to close.

## TIER 3 — combinatorial, off the resurgence critical path.

`SYTBranchingRecursion` (3), `SYTHookGNW` (3). Standard-Young-tableaux
combinatorics. Likely tractable with effort, but they do not gate the alien-
calculus work; do not let them absorb the arc's budget.

## TIER 4 — the analytic residual of q-Gevrey order.

`Mathlib/QGevreyOrder.lean` (4). Read the file's own header before touching it:
the **algebraic heart is already proved sorry-free** -- product adds order, bar
involution negates it, geometric sequences have order 0, and the dominant-balance
inequality `s k² + t j² <= E(s,t)(k+j)²` (a completing-the-square argument per
regime). What remains is the **Cauchy-convolution order law** (MI-2): the ε-δ
assembly into the order LIMIT, plus a lower bound needing a non-cancellation
hypothesis on leading coefficients.

That residual is real analysis, not bookkeeping -- but it is the most *on-arc* of
the analytic gaps, since q-Gevrey order is exactly the growth class the new
`QGevreyTaming.lean` works in. If any Tier-1-flavoured gap is worth the
investment, it is this one.

## Method

1. Classify before attacking. A "sorry" in an analytic file and a "sorry" in an
   algebraic one are different tasks; the counts above deliberately do not rank
   files by sorry-count, which would put `BorelResummation` (4, hard) above
   `StokesMatrixDescent` (1, plausibly easy).
2. Tier 2 first, then re-assess. Closing one algebraic sorry is worth more than
   half-finishing an analytic one.
3. Anything Tier 1 that is attempted must go through `qou-08a2`, and must record
   which Mathlib theorem is missing rather than working around it with an axiom
   (§"Axiomatization is NOT a Proof").

## ⚠ CORRECTION 2026-08-08 (same session): the survey above was WRONG

The counts that produced the tiering were **false positives**. Docstrings in this
corpus say the word constantly -- "sorry-free", "no `sorry`, no axiom",
"a cited `sorry`", "-- SORRY: needs ..." -- and every grep refinement I tried
still matched them (`-w` matches inside "sorry-free" because `-` is a word
boundary; excluding "sorry-free" still matches the backticked forms; excluding
backticks still matches the `-- SORRY:` markers).

Re-measured by stripping Lean comments first (`scripts/real-sorry-scan.py`):

| file | tiering above claimed | ACTUAL |
|---|---|---|
| `Mathlib/ArgumentPrinciple` | 2 | **0** |
| `Mathlib/BorelResummation` | 4 | **0** |
| `Resurgence/StokesMatrixDescent` | 1 | **0** |
| `Mathlib/SYTBranchingRecursion` | 3 | **0** |
| `Mathlib/SYTHookGNW` | 3 | **0** |
| `Mathlib/RSKBridge` | 1 | **0** |
| `Mathlib/IdentityIHLFBridge` | 1 | **0** |
| `Mathlib/EllipticDivisorDegree` | 2 | 1 |
| `Mathlib/HadamardFactorization` | 4 | 2 |
| `Mathlib/QGevreyOrder` | 4 | 1 |

**Whole QOU tree: 18 real sorries across 1611 files.** Naive `grep -c sorry` over
the same tree reports **2193** -- a 60x overcount.

### What this does to the tiering

* **TIER 2 does not exist.** `StokesMatrixDescent` is already sorry-free; its
  block-diagonalisation is proved. So is every other file I called "plausibly
  closeable". There is **no cheap algebraic sorry to close in the resurgence arc.**
* **TIER 3 does not exist.** The SYT files are clean.
* **TIER 1 shrinks** to `EllipticDivisorDegree` (1) + `HadamardFactorization` (2),
  and `ArgumentPrinciple`/`BorelResummation` are already clean.
* **TIER 4 is one sorry**, `QGevreyOrder.lean:269` -- verified a genuine bare
  `sorry` (the `-- SORRY:` marker on the line above is a comment and is correctly
  ignored).

### The honest answer to "what can be closed in the arc"

**Almost nothing, because the arc is already essentially clean.** The resurgence
arc carries **3** real sorries, all genuinely hard analysis:

1. `EllipticDivisorDegree` -- needs the argument principle, absent from Mathlib
   v4.24.0.
2. `HadamardFactorization` (2) -- Hadamard factorization.
3. `QGevreyOrder:269` -- the Cauchy-convolution order law: dominant balance /
   Laplace method for discrete convolutions with q-Gevrey bounds.

That is a good-news finding, not a bad one -- but it means the right move is
**not** to hunt for cheap sorries here. Effort should go to the analytic gaps via
`qou-08a2`, or to new content (as `QGevreyTaming.lean` did) rather than to
closing a backlog that is mostly imaginary.

### Tooling

`scripts/real-sorry-scan.py` now exists so this cannot recur. It blanks comments
in place (preserving line alignment) rather than deleting them -- an earlier draft
deleted them, which desynchronised the line mapping and double-counted every hit
(reported 36 instead of 18). Use it instead of grep.

## ⚠ SUPERSEDED 2026-08-08 — this bean DUPLICATED existing coverage

Rebasing onto main (153 commits) revealed the corpus already had a bean for every
gap tiered here, several with more analysis than I wrote:

    qou-6e88 [todo]      cauchyMul_order -- statement may need strengthening
                         (= my "Tier 4"; now SETTLED, see that bean)
    qou-dgtf [todo]      elliptic_divisor_degree_zero -- blocked on the argument
                         principle (= my "Tier 1", same diagnosis)
    qou-c3if [todo]      exponent of convergence <= order (Hadamard PI-4)
    qou-bp5n [todo]      Jensen + Nevanlinna are ALREADY in Mathlib -- wire, do
                         not reprove
    qou-8cwi [completed] Borel-Caratheodory inequality
    qou-7y3g [todo]      Vol(4_1), Vol(B_3) numerical only

**Use those, not this.** They are better scoped and already carry the per-gap
detail. This bean is kept only for the two things it contributed that are not in
them: the corrected sorry census (18 real, vs 2193 by naive grep) and
`scripts/real-sorry-scan.py`. Both are recorded in the correction section above.

**Method note.** I ran the corpus-grep for RSZ/alien-calculus content but not for
"is there already a bean for this Lean gap" before tiering. That is the same
checklist, skipped one step earlier. Grep the beans too.
