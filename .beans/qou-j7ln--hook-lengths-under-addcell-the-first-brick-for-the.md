---
# qou-j7ln
title: Hook lengths under addCell — the first brick for the arbitrary-z corner identity
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T13:03:43Z
updated_at: 2026-08-24T15:10:01Z
---

## Landed — PR #5645

`QOU/SchurWeyl/HookLengthAddCell.lean`, sorry-free, axiom-clean, pure ℕ × ℕ combinatorics.

- `rowLen_of_isAddableCell` / `colLen_of_isAddableCell` — an addable cell sits at the end of its
  row and the bottom of its column.
- `hookLength_addCell_self` — the added cell's own hook is `1`.
- `hookLength_addCell_of_mem` — every other cell gains `1` **iff** it shares the new cell's row or
  column, `0` otherwise.

**The statement is cleaner than the arm/leg case split I budgeted for.** For `x ∈ ν` the *order*
conditions come free: sharing `s`'s row forces `x.2 < rowLen ν x.1 = s.2` automatically, and
symmetrically for the column. So the hook grows by `1` on exactly the union of `s`'s row and
column, and those meet only at `s`, which is not in `ν` — one `if`, not two cases.

**Corpus-grepped before writing**: no hook-under-`addCell` or hook-under-`eraseCorner` lemma
existed. The `hookLength` infrastructure that does exist (`HookLengthFormula`, `QHookProduct`,
`WenzlSchurElement`, `YoungDiagramCells`) is about the hook-length *formula* and product
identities, not about how a hook moves under a shape change. `qou-68e1` is adjacent (consolidating
`schurElement`'s product form) but a different item; untouched.

### Next brick, and an honest estimate

The weight ratio itself:

    w_{ν+s} / w_ν = N(s) / [ (q²−1) · ∏_{x ∈ arm(s) ∪ leg(s)} (q^{2(h(x)+1)}−1)/(q^{2h(x)}−1) ]

The numerator half is free (per-cell, diagram-independent). The arm/leg product is the work, and it
has **no counterpart in the two-row case** — there `schurPrincipal_twoRow` telescoped the entire
hook-content product, which is exactly the shortcut arbitrary `z` does not get. I am not putting a
timeline on it. Nothing downstream is blocked: convention D is canonical per the 2026-08-15 ruling
and its identification is proved and merged (`91bf8fcb4`).


## Second brick landed — and a scoping finding that changes what "next" means

`QOU/SchurWeyl/OcneanuWeightAddCell.lean`, sorry-free, generic `[Field R]`:
`ocneanuNumProd_addCell` (the numerator gains exactly one factor — `Finset.prod_insert`, nothing
more) and `ocneanuDenProd_addCell` (the denominator gains `q²−1`, and every old factor shifts by
one step iff its cell shares the new cell's row or column).

Named `…Prod` because the corpus already has `ocneanuNumFactor_eq_zero_of_content_neg_two` and
`ocneanuNumFactor_conventionD`, which are about **one cell's** factor. Grepped before writing this
time, having got that order wrong earlier in the arc.

### The Schur route does not generalise, and that is structural

I had been treating arbitrary `z` as "the same proof, harder". It is not. The convention-D proof
went entirely through the bridge to `schurPrincipal 2 (q²)` — Pieri, the two-row telescoping, the
≥3-row vanishing. **That route is unavailable at generic `z`, and the reason is a type:**

    schurPrincipal (r : ℕ) (Q : R) (μ : YoungDiagram)

`r` is the **number of variables** in the principal specialisation, so it is inherently a positive
integer. And the corpus's own parameter relation (`pow_level_mul_eq_of_markovParameter`) pins

    Q^r · (1 − Q + z) = z,   i.e.   Q^r = z / (1 − Q + z)

so a Wenzl level exists only when that element happens to be an **integer** power of `Q`.
Convention D is the case `Q = q²`, `Q^r = q⁴`, `r = 2` (`wenzlLevel_conventionD`). Generic `z` is
off that lattice: there is no `r`, hence no `schurPrincipal r Q` to bridge to, hence no Pieri and
no telescoping.

**So "finish the arbitrary-`z` corner identity" is not one more brick on this pile.** It needs
either a genuinely new hook-level identity (the arm/leg product does *not* telescope for a general
diagram — hooks along a row are not consecutive), or a different route entirely. I am not going to
guess which; recording the obstruction is worth more than a speculative attempt.

What these two bricks *are* good for regardless: they are convention-independent statements about
how the weight moves under `addCell`, so any future route needs them, and neither depends on `z`.


## The obstruction is real but NOT fatal — the library already had the route

Asked whether external literature was needed; ran the corpus-grep checklist's library tier first
(`library/INDEX.md`, 320 briefs). **It was already there**, and it supplies the *route*, not just
background.

`library/arxiv-math-9806163v1` — Orellana, *"Weights of Markov traces on Hecke algebras"*, the
paper AGENTS.md already cites as `[orellana1998]`. In §5 (`sec-019-5-the-weight-formula.md`,
~line 108) it proves its branching identity **at the lattice** `Q = −q^{r₁+m}` and then writes:

> *"Since `W(α,β)(q, Q)` is an **analytic rational function** and the above equation holds for all
> `Q = −q^{r₁+m}`, thus we have that `W(α,β)(q, Q) = Σ W(γ,η)(q, Q)` holds **for all values of
> `Q`**."*

That is **rational continuation from the integer-level lattice**, and it goes straight around the
obstruction I recorded above. I wrote that generic `z` is off the lattice so there is no
`schurPrincipal r Q` to bridge to, and concluded a new identity or a different route was needed.
The different route is: **you never need a bridge at generic `z`.** Prove the corner identity at
*every* integer level `r` — where the Schur route works exactly as it did at `r = 2` — observe both
sides are rational in the parameter, and conclude it identically.

### What that makes the remaining work

1. **Generalise `r = 2` to general `r`.** My convention-D chain (`≥3`-row vanishing, `twoRow`
   branching, the corner identity) becomes `≥(r+1)`-row vanishing and `r`-row branching. The
   corpus is already set up for it: `schurPrincipal` takes `r : ℕ`, and
   `schurPrincipal_eq_zero_iff` is **already general in `r`** — it was only my downstream
   specialisation that fixed `r = 2`.
2. **The transfer.** "Two rational functions agreeing on an infinite set are equal" — real Lean
   work, but a standard shape (a nonzero polynomial has finitely many roots), not a new
   mathematical identity.

### Stated precisely, so nobody over-reads this

The paper demonstrates the technique on **type B** weights `W(α,β)(q, Q)`. Its type-A remark cites
Wenzl `[W1]` only at the specific `z = q^r(1−q)/(1−q^r)`. So the library gives me a **proof
technique on a closely analogous object**, not a ready-made citation for the type-A general-`z`
corner identity. And **Wenzl 1988 itself is not in the library** — searched; only Orellana's
citation of it. That is the one thing worth uploading if the primary is wanted, though the
technique above does not depend on having it.

**Answer to "need lit?": no.** The library had what was needed, which is also the honest reason the
checklist puts the library tier before declaring anything open.


## 2026-08-24 — the general-r route, and how much of it is now proved

Three commits on `claude/general-r-vanishing-branching-2026-08-24` (PR #5662).

**1. Vanishing generalises for free.** `QOU/SchurWeyl/WenzlWeightLevelR.lean`:
`wenzlWeight r Q mu = schurPrincipal r Q mu / [r]_Q^{|mu|}`, and
`wenzlWeight_eq_zero_iff : w_mu = 0 <-> r < mu.colLen 0` at every level.
`schurPrincipal_eq_zero_iff` was already general in `r`; only my #5575
specialisation fixed `r = 2`. Conservativity is proved, not asserted:
`wenzlWeight_two_eq_ocneanuWeight` and `wenzlMarkovParam_conventionD`.

**2. The branching route is NOT the twoRow route, and I found the right one.**
The `twoRow` chain works because `schurPrincipal 2 Q (twoRow m k)` telescopes.
Nothing telescopes at general `r`. The right object is the **Vandermonde /
q-Weyl form**: with `x_i = Q^{mu_i + r - i}`,

    s_mu(1,...,Q^{r-1}) = prod_{i<j} (x_i - x_j) / prod_{i<j} (Q^{r-i} - Q^{r-j})

Adding a box to row `i` sends `x_i -> Q*x_i` and fixes every other `x_j`, so

    s_{mu + box in row i} / s_mu  =  prod_{j != i} (Q*x_i - x_j)/(x_i - x_j)

and branching is the assertion that those ratios sum to `[r]_Q`.

**3. That sum is now PROVED, general r.** `QOU/Mathlib/LagrangeCoeffSum.lean`,
`sum_prod_qratio`, sorry-free, axiom-clean. Route: Lagrange interpolation
read as residue-summing (`sum_eval_div_prod_eq_coeff`, also new — Mathlib has
the interpolation but not this reading), applied twice, to `divX f` and
`divX g` for `f = prod (X - v j)`, `g = prod (Q*X - v j)`.

It disposes of a case analysis the r = 2 chain needed a separate lemma for:
if adding a box to row `i` would break the partition then `Q*x_i = x_{i-1}`
and that summand is **already zero**, so summing over all rows and summing
over addable rows are the same sum. `rowLen_two_addCell_row2` and the
three-rows-vanish argument were the r = 2 shadow of this.

Checked symbolically first (sympy, exact, r = 1..5) before writing any Lean.

## What is left — one named classical fact, not a vague gap

`sum_eq_bracket_mul_of_qratio_scaling` packages branching as a theorem
CONDITIONAL on the box-addition ratio above. The only missing input is that
ratio for `schurPrincipal` — equivalently the q-analogue of the
Frame-Robinson-Thrall hook-length identity, relating `prod_c (1 - Q^{h(c)})`
to the shifted parts `x_i`. Neither it nor Pieri is in Mathlib.

Deliberately NOT stated as a `sorry`: a `sorry` in a library file is
indistinguishable from a proved lemma to every consumer.

Two sub-bricks, in order:
  (a) `prod_{c in mu} (1 - Q^{h(c)}) = prod_i prod_{k<=l_i} (1-Q^k) / prod_{i<j} (1 - Q^{l_i - l_j})`
  (b) the Vandermonde ratio under `x_i -> Q*x_i`, ~150 lines of Finset
      surgery splitting `prod_{i<j}` into pairs containing `i` and pairs not.

(a) is the hard half. #5645's `hookLength_addCell_of_mem` is the local
version of it and should feed the induction.


## Same day, later — sub-brick (a) is half done, and the corpus had the skeleton

**Corpus-grep paid.** I had just written "(a) is the hard half" and budgeted it
as a multi-hour job. `QOU/Mathlib/SYTHookFormulaBeta.lean` already proves,
sorry-free over `N`, the divisor-free per-row FRT identity

    rowHookProd a t * betaGapProd a t = (a + |t|)!

with `rowHookProd a t = prod_{j<a} ((a-j) + cnt t j)` — the row's hook lengths.

**Reading its proof is what mattered.** The arithmetic is incidental: every
step reindexes the *multiset of hook lengths* against `{1,...,a+|t|}`, and the
only numerical moves are `omega` facts about the **arguments**. So the whole
thing generalises to any commutative monoid with each factor `n` replaced by
`f n`. `QOU/Mathlib/SYTHookFormulaBetaMonoid.lean`:

    rowHookProdF_mul_betaGapProdF (f : N -> M) :
      rowHookProdF f a t * betaGapProdF f a t = descFactF f (a + |t|)

and `f n = 1 - Q^n` gives the q-analogue with **no separate proof**
(`rowHookProdF_one_sub_pow`). Conservativity checked, not asserted:
`rowHookProdF_id` / `descFactF_id` / `betaGapProdF_id` recover the `N` originals.

**Correction to the commit message of `51f998b85`.** It says two of the
original `omega`s "had been closing goals over an opaque `cnt` by luck of the
argument shape". That is wrong and I should not have written it — both failing
`omega`s were in tactic steps *I* wrote (`congr 2 <;> omega`), not inherited.
The original proof's `omega`s are fine; what changes in the monoid version is
that the values are `f (...)`, so `congr` peels to a different goal and the
argument has to be rewritten rather than `omega`'d. The code and the result
are unaffected.

### What is still open for sub-brick (a)

Two steps, both shape-preserving rather than arithmetic:

1. **Assemble the rows.** `SYTHookFormulaBetaProd.prodHooks_eq_prod_rowHookProd`
   is the `N` version and looks equally arithmetic-free; generalise it the same
   way.
2. **Recognise the assembled `betaGapProdF (fun n => 1 - Q^n)` as the
   Vandermonde denominator** `prod_{i<j} (1 - Q^{l_i - l_j})`, i.e. as
   `prod_{i<j}(x_i - x_j)` up to a monomial with `x_i = Q^{l_i}`.

Then sub-brick (b) — the Vandermonde ratio under `x_i -> Q*x_i` — feeds
`sum_eq_bracket_mul_of_qratio_scaling` and general-r branching closes.
