---
# qou-j7ln
title: Hook lengths under addCell — the first brick for the arbitrary-z corner identity
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T13:03:43Z
updated_at: 2026-08-24T17:21:24Z
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


## Sub-brick (a) is DONE — and the remaining list is longer than I said

Two more commits: `694c4066b` (full FRT hook product in any commutative
monoid) and `4947465a3` (β-gap denominator as the Vandermonde pair product).

    prod_c (1 - Q^{h(c)}) * prod_{i<j} (1 - Q^{b_i - b_j})
      = prod_i prod_{k<=b_i} (1 - Q^k)

sorry-free, axiom-clean, and it cost almost nothing beyond the monoid
generalisation: the assembly is arithmetic-free for the same reason the
per-row step was, and `colLen_eq_succ_add_cnt_drop` / `drop_sorted` /
`drop_le_getD` are facts about **indices**, reused verbatim.

`betaGap_eq_betaNum_sub` is the one place the weak-decrease hypothesis earns
its keep: without `l[j] <= l[i]` the two truncated `N` subtractions part
company.

### Correction to my own scoping

I wrote earlier that after sub-bricks (a) and (b) "general-r branching
closes". **That was too fast.** (a) is the HOOK side only — the denominator.
Four things stand between here and branching for `schurPrincipal`:

1. **The numerator side.** `schurPrincipal` is `Q^{nPart} * prod (1 - Q^{r +
   content}) / prod (1 - Q^{hook})`. I have the denominator; the numerator
   `prod_c (1 - Q^{r + content(c)})` needs its own beta-number form.
2. **List-partition <-> YoungDiagram.** `prodHooks` and the whole
   `SYTBeta` namespace are List-encoded; `schurPrincipal` is YoungDiagram-
   encoded. `hookLength_eq` in `BraidKnot/HookProductHLF.lean` and
   `HookLengthFormula.lean` are the candidate bridges — corpus-grep before
   writing anything.
3. **Sub-brick (b)**, unchanged: the Vandermonde ratio under `x_i -> Q*x_i`.
   Best done as a `Finset` pair product over `range n` with `i < j`, split
   once into pairs containing `a` and pairs not. The signs cancel: for
   `j < a` the pair is `(j,a)` and `(x_j - y)/(x_j - x_a) = (y - x_j)/(x_a -
   x_j)`, same as for `j > a`.
4. Only then does `sum_eq_bracket_mul_of_qratio_scaling` fire.

Estimating (b) at ~100 lines of Finset surgery; (1) and (2) unknown until
grepped.


## Sub-brick (b) done — branching PROVED for the Vandermonde form

`QOU/Mathlib/VandermondeUpdateRatio.lean` (commit `bcf8a5731`), sorry-free,
axiom-clean:

    sum_vandPairProd_scale : sum_a V(x[a -> Q*x_a]) = [n]_Q * V(x)

`sum_prod_qratio` supplied the sum; this file supplies the ratio it was
conditional on. So general-r branching is proved **for the Vandermonde-form
weight**, unconditionally.

`vandPairProd_update_eq_zero` turns the "illegal rows need no special case"
argument into a theorem: adding a box to row `a` is illegal exactly when
`mu_a = mu_{a-1}`, and then `beta_{a-1} = beta_a + 1`, so the updated node
collides with its neighbour and V vanishes.

Stated division-free (any `CommRing`, no non-vanishing hypothesis); the field
ratio is a corollary.

## The remaining bridge — and a simplification worth recording

Only one thing is left: `schurPrincipal r Q mu` = (mu-independent constant)
times the Vandermonde in `x_i = Q^{beta_i}`. Worked out on paper:

* **Denominator** (proved, `prodHooksF_one_sub_pow_pair`):

      prod_c (1 - Q^{h(c)}) = prod_i descFact(beta_i) / prod_{i<j}(1 - Q^{beta_i - beta_j})

* **Numerator** (not yet in Lean). Row `i` has cells of content `j - i`,
  `j < mu_i`, so its factors are `1 - Q^k` for `k = r-i .. r-i+mu_i-1`. Since
  `beta_i = mu_i + r - 1 - i`, the top index **is** `beta_i`:

      prod_{row i} = descFact(beta_i) / descFact(r - 1 - i)

* **So `prod_i descFact(beta_i) CANCELS** between numerator and denominator:

      schurPrincipal r Q mu
        = Q^{nPart mu} * prod_{i<j}(1 - Q^{beta_i - beta_j}) / prod_i descFact(r-1-i)

  and the leftover denominator is `mu`-INDEPENDENT — it is the empty-partition
  Vandermonde at `rho_i = r-1-i`. Everything else is a monomial:
  `prod_{i<j}(1 - Q^{beta_i-beta_j}) = V(x) / prod_{i<j} x_i` with
  `x_i = Q^{beta_i}`.

That cancellation means the **ratio** form needs even less: for
`nu = mu + box in row a`, the `mu`-independent factor drops out entirely, so
only the numerator row-split and the List <-> YoungDiagram bridge remain.

### Left, in order

1. **Numerator row-split** — `prod_{c in row i}(1 - Q^{r + content c})
   = descFact(beta_i) / descFact(r-1-i)`. Same shape as the hook side; should
   generalise the same way.
2. **List-partition <-> YoungDiagram.** `SYTBeta` is List-encoded,
   `schurPrincipal` is YoungDiagram-encoded. Candidates to grep first:
   `BraidKnot/HookProductHLF.hookLength_eq`, `Mathlib/HookLengthFormula`.
3. **Assemble** and discharge `hw` in `sum_eq_bracket_mul_of_qratio_scaling`.

Alternative worth weighing at (3): compute the `schurPrincipal` ratio directly
from #5645's `hookLength_addCell_of_mem` instead of via the closed form. Same
work in different clothes, but it stays inside `YoungDiagram` and skips the
List bridge entirely.


## Bricks 1 and 2 done; a trap found and closed

Three more commits: `6f4f6b712` (content-side block), `300c107b4` (List <->
YoungDiagram hook bridge), `3b08549f7` (zero-padding + the beta trap).

**Brick 1 — content side.** `prod_block_mul_descFactF`: a contiguous block
`f(b)...f(b+m-1)` is a ratio of two `descFactF`s, division-free. Row `i`'s
numerator factors are `f(r - i + j)` for `j < mu_i`, a block at `b = r-i` of
length `mu_i`, whose top index `b+m-1 = mu_i + r - 1 - i` **is** `beta_i` --
which is why `prod_i descFactF f beta_i` cancels against the hook side's.

**Brick 2 — the encoding bridge.** Corpus-grep again paid:
`HookLengthFormula.hookLengthProduct_eq_prodHooks` and
`ColLenRowLensBridge.colLen_rowLens` already existed over `N`, and again the
proof is reindexing with all content in the ARGUMENT. So
`prodHooksF_rowLens : prod_{c in mu.cells} f(h(c)) = prodHooksF f mu.rowLens`.

**A THIRD hook notion.** A route that stopped at `YoungDiagram.hookLength`
would still not reach `schurPrincipal`, which uses `QBeta.WenzlWeight.hook` --
`(rowLen i - j) + (colLen j - i) - 1`. On a cell that IS
`hookLength_eq_of_mem`'s closed form, so `wenzlHook_eq_hookLength` closes it
and `prodHooksF_rowLens_wenzl` states the bridge in the form `schurPrincipal`
needs.

**THE BETA TRAP — read before assembling.** `betaNum l i = l[i] + (|l|-1-i)`
measures against `|l|`, the number of NONZERO rows. The level-r principal
specialisation measures against **`r`**: pad with `r - |l|` empty rows first.
The two differ by the constant `r - |l|` on every row, AND the padded version
has extra rows `beta = r-1-|l|, ..., 0` that the unpadded one lacks entirely.
Differences between real rows survive, so the Vandermonde is unaffected up to
the new rows -- but nothing else transfers for free, and a proof that quietly
uses `|l|` where `r` belongs is wrong in a way **no type error catches**. I
nearly wrote one.

`prodHooksF_append_replicate_zero` closes the half that does transfer: empty
rows contribute no cells and are counted by no column, so the hook product is
unchanged. Pad first, then apply the beta machinery at `r`.

## Left — one assembly

Everything the assembly needs is now proved. Remaining:

1. Pad `mu.rowLens` to length `r`; apply `prodHooksF_one_sub_pow_pair` to get
   the hook side with a Vandermonde denominator at the `r`-row betas.
2. Apply `prod_block_mul_descFactF` per row for the numerator; watch the
   `prod_i descFactF beta_i` cancel.
3. Convert `prod_{i<j}(1 - Q^{beta_i - beta_j})` to `vandPairProd r x` with
   `x_i = Q^{beta_i}`, up to the monomial `prod_{i<j} x_i`.
4. Track the leftover monomials against `Q^{nPart mu}`, and discharge `hw` in
   `sum_eq_bracket_mul_of_qratio_scaling` -- or, since only the RATIO is
   needed, take the quotient of two instances of (1)-(3) and let the
   `mu`-independent constant cancel before any monomial bookkeeping.

(4)'s second option is likely much less work than the first and should be
tried first.


## Both sides now land on the SAME object

Commit `543f6a897`: `QOU/Mathlib/ContentProductRows.lean`.

    prodContentF_rows : prod_{c in mu} f(r - c1 + c2)
                          = prod_{i<r} prod_{j<rowLen i} f(r - i + j)

Outer range `r`, not `colLen 0`, so it is already in the zero-padded
convention. Row `i`'s inner product is a contiguous block, so
`prod_block_mul_descFactF` gives

    prodContentF_mul_descFactF :
      (prod_c f(r-c1+c2)) * prod_{i<r} descFactF f (r-1-i)
        = prod_{i<r} descFactF f (r - i + mu_i - 1)

**Checked, not assumed:** `r - i + mu_i - 1` is `beta_i` at `r` rows, and the
hook side's `l.getD i 0 + (l.drop (i+1)).length` on `l` padded to length `r`
is `mu_i + r - i - 1` -- the same number. So both sides produce
`prod_i descFactF f beta_i` and it cancels in a ratio, as does the
`mu`-independent `prod_{i<r} descFactF f (r-1-i)`.

`schurNumExponent` was needed and is easy to miss: `schurPrincipal`'s exponent
is `(r : Z) + content c`, a **zpow**. On a cell of an `<= r`-row diagram it is
the natural `r - c1 + c2`, but without that step the numerator cannot be
reindexed at all.

Also un-privated `cells_biUnion'` / `rows_disjoint` / `row_prodF` in
`HookProductMonoidBridge` -- the content side needs the identical reindexing.

## The assembly that remains

Small mismatches to bridge first (each ~10 lines):

* hook side indexes a **List** product over `range l.length`; content side a
  **Finset** product over `range r`. `list_range_map_prod'` bridges them.
* `mu.rowLens.getD i 0 = mu.rowLen i` for **all** `i`, not just `i < length`:
  beyond the length both are 0, by `rowLen_eq_zero_of_colLen_le`.

Then:

1. `schurPrincipal r Q mu = Q^{nPart mu} * N / D` -- split the single product
   into numerator and denominator. Needs `D != 0`, i.e. the genericity
   hypothesis `schurPrincipal_eq_zero_iff` already carries.
2. `N/D = prod_{i<j}(1 - Q^{beta_i - beta_j}) / prod_{i<r} descFactF (r-1-i)`
   by dividing the two identities.
3. Ratio for `nu = addCell mu s`: the `mu`-independent factor cancels; needs
   `rowLens (addCell mu s) = rowLens mu` with entry `a` incremented.
4. Monomials: `x_i - x_j = -Q^{beta_j}(1 - Q^{beta_i - beta_j})`, so
   `vandPairProd r x = (-1)^{C(r,2)} Q^{sum_j j*beta_j} prod_{i<j}(1-Q^{...})`.
   Under `beta -> beta + e_a` the monomial moves by `Q^a`, which **cancels the
   `Q^{nPart}` change** (`nPart nu - nPart mu = a`). Worth re-deriving in Lean
   rather than trusting this paper computation.
5. Discharge `hw` in `sum_eq_bracket_mul_of_qratio_scaling`.


## Step 4 de-risked: the full ratio identity checked symbolically

Commit `e7e20cc78` adds `rowLen_addCell` (the `beta -> beta + e_a` step) and
`getD_rowLens` (`mu.rowLens.getD i 0 = mu.rowLen i` for **every** `i`, which is
what lets the List-indexed hook side and the range-r-indexed content side be
compared with no side condition).

I flagged step 4 -- the monomial bookkeeping -- as "worth re-deriving rather
than trusting the paper computation". Checked it symbolically instead of
building Lean on it, and it holds:

    schurPrincipal r Q (mu + box at row a) / schurPrincipal r Q mu
      = prod_{j != a} (Q*x_a - x_j)/(x_a - x_j),   x_i = Q^{beta_i}

**10 / 10 legal cases**, exact sympy, `r = 3,4,5`, including `mu = []`,
one-row, and adding to an empty padded row:

    r=3 [2,1] a=0,1,2 | r=4 [3,1] a=0,1 | r=4 [2,2,1] a=0,2
    r=5 [3,2,1] a=1   | r=5 [1] a=0     | r=3 [] a=0

So every monomial -- `Q^{nPart}`, the `prod_{i<j} x_i` from converting
`prod(1-Q^{beta_i-beta_j})` to `vandPairProd`, the `(-1)^{C(r,2)}` -- cancels
exactly as the paper derivation said. Step 4 is bookkeeping, not a hidden
obstruction.

**The 11th case is a test artifact, not a failure.** `r=4, mu=[4,4], a=1` is an
ILLEGAL box (`mu_0 = mu_1`), and my harness evaluated `schur` on `[4,5]`, which
is not a partition, so its LHS is meaningless. Checked the RHS separately:
`beta = [7,6,1,0]`, so `Q*x_1 = Q^7 = x_0` and the q-ratio numerator is
**exactly 0** -- which is `vandPairProd_update_eq_zero`. In Lean `addCell`
requires `IsAddableCell`, so the case cannot arise at all.

Script: `ratio_check.py` / `illegal_check.py` in the session scratchpad
(throwaway, exact symbolic in `Q`, no floats).


## The closed form is proved — and the last step needs NO monomials

Commits `a7f697c5e` and `552c8397f`.

    schurPrincipal_mul_const :
      schurPrincipal r Q mu * prod_{i<r} descFactF (1-Q^n) (r-1-i)
        = Q^{nPart mu} * prod_{i<j<r} (1 - Q^{beta_i - beta_j})

Division-free apart from `hD` (hook product nonzero -- the same genericity
`schurPrincipal_eq_zero_iff` already carries). The left constant does not
depend on `mu`, so in a ratio it cancels outright.

Getting there needed both sides on one `beta`: the hook side indexes a **List**
product over `range |l|` and measures beta against `|l|`; the content side a
**Finset** product over `range r`, measured against `r`. `betaR r mu i =
mu_i + (r-1-i)` is the common form; `betaNum_paddedRowLens` identifies it with
the List-side `betaNum` on the zero-padded `rowLens`. Then `hookSide_betaR` and
`contentSide_betaR` both land on `prod_{i<r} descFactF f (betaR r mu i)` -- the
SAME product -- and `contentProd_mul_descFactF_eq` equates them.

Also landed: `betaR_lt` (beta strictly decreases) and `nPart_addCell`.

### CORRECTION to my own plan above

I recorded the final step as "monomial bookkeeping" -- the `(-1)^{C(r,2)}` and
`prod_{i<j} x_i` from converting `prod(1-Q^{beta_i-beta_j})` into
`vandPairProd` -- and verified it symbolically before trusting it. **That
verification stands, but the conversion is not needed.** Comparing
`P(beta')/P(beta)` against the q-ratio directly, per pair with
`x_i = Q^{beta_i}`:

* `j > a` (`beta_j < beta_a`): `(Q x_a - x_j)/(x_a - x_j)` becomes
  `(1 - Q^{beta_a+1-beta_j})/(1 - Q^{beta_a-beta_j})` after cancelling
  `Q^{beta_j}` -- an exact match, no leftover factor.
* `j < a` (`beta_j > beta_a`): the same cancellation of `Q^{beta_a}` leaves
  one `Q`.

So the q-ratio is `Q^{#{j<a}} = Q^a` times `P(beta')/P(beta)`, and `Q^a` is
exactly `nPart_addCell`. Since `sum_eq_bracket_mul_of_qratio_scaling` wants the
**q-ratio**, not `vandPairProd`, this route reaches it without ever building
the Vandermonde -- strictly less work than the plan recorded above.

### All that remains

1. The two per-pair identities above (`j > a`, `j < a`), each a `Q`-power
   cancellation under `betaR_lt`.
2. `P(beta')` vs `P(beta)`: only pairs involving `a` change; split
   `prod_{i<j}` at `a` as `VandermondeUpdateRatio.prod_erase_range_split`
   already does for the other product.
3. `betaR r (addCell mu s) i = betaR r mu i + [i = s.1]`, immediate from
   `rowLen_addCell`.
4. Divide two instances of `schurPrincipal_mul_const`, discharge `hw`.

`vandPairProd` / `sum_vandPairProd_scale` remain proved and correct; they are
simply not on the shortest path to `hw`.


## Every piece of the final assembly now exists

Commits `b632874ad` (per-pair q-ratio factors) and `f3796710f` (pair-product
split).

    qratio_factor_lower  (j > a)  exact match, no leftover factor
    qratio_factor_upper  (j < a)  same match, times one Q
    betaR_addCell                 beta_i(mu + box at a) = beta_i(mu) + [i=a]
    prod_pairs_split_ne           two families agreeing off the pairs
                                  involving a differ exactly by their row-a
                                  and column-a factors  (division-free)

Together with `schurPrincipal_mul_const`, `betaR_lt`, `nPart_addCell` and
`sum_eq_bracket_mul_of_qratio_scaling`, nothing conceptual is left.

**One reindexing stands between here and `hw`.** `SchurPrincipalBetaForm`
writes P as `prod_{i<r} prod_{k < r-(i+1)}` (offset form, inherited from
`SYTBetaGapVandermonde`), while `prod_pairs_split` uses
`prod_{i<r} prod_{j in Ico (i+1) r}` (interval form). `Finset.prod_Ico_eq_prod_range`
bridges them; do it once, in whichever direction keeps the split usable, and
prefer converting the beta-form file rather than weakening the split.

Then: apply `prod_pairs_split_ne` with `h i j = 1 - Q^{beta'_i - beta'_j}` and
`g i j = 1 - Q^{beta_i - beta_j}` (the off-pairs hypotheses discharge by
`betaR_addCell` + `if_neg`), rewrite the row-a and column-a factors by the two
`qratio_factor_*` lemmas, collect the `Q` per upper pair into `Q^a`, cancel it
against `nPart_addCell`, and divide two instances of `schurPrincipal_mul_const`.

### Trap for whoever finishes this

`ring` does NOT close associativity/commutativity goals over a `CommMonoid` --
it wants a semiring. Use `ac_rfl` (or `mul_right_comm`). Cost me two rounds
across two files.


## DONE — `hw` is proved; general-r branching reaches the corpus weight

Commits `494f41953`, `f4fb1b80e`, `78e220243`.

    schurPrincipal_addCell_eq :
      s_{mu + box at row a} = (prod_{j != a} (Q x_a - x_j)/(x_a - x_j)) * s_mu

with `x_i = Q^{beta_i}`. That is `hw` of
`QOU.Mathlib.sum_eq_bracket_mul_of_qratio_scaling`, so
`sum_a s_{mu + box at a} = [r]_Q * s_mu` for the CORPUS weight -- not a
lookalike, and no `sorry` anywhere in the chain.

Route, in three steps:

1. `schurPrincipal_addCell_mul` -- the ratio CROSS-MULTIPLIED:
   `s_nu * C * (row.col)_mu = Q^a * (row.col)_nu * (s_mu * C)`. Division-free
   on purpose: it needs no non-vanishing hypothesis beyond the two the closed
   form already carries, so it stays true at roots of unity where the quotient
   is 0/0.
2. `qratio_prod_eq_rowColProd` -- the q-ratio IS
   `Q^a * (row.col)_nu / (row.col)_mu`. Unconditional beyond `Q != 0`: a
   product of quotients is the quotient of the products, and the two
   `QRatioBetaFactors` lemmas give the factorwise identity.
3. `schurPrincipal_addCell_eq` -- divide, given `levelConst != 0` and
   `rowColProd_mu != 0`. Both are products of `(1 - Q^k)` at nonzero `k` (the
   betas are distinct by `betaR_lt`), so both hold under the genericity
   `schurPrincipal_eq_zero_iff` already assumes.

### Two Lean traps recorded, both cost a round

* `field_simp` clears only what appears in the GOAL. `levelConst` does not, so
  it must be cancelled from step 1 by `mul_right_cancel-0` FIRST; otherwise
  `linear_combination` mismatches by exactly that factor.
* `prod_pairs_split_ne`'s `hbelow` as first written (`forall i j, a < i -> ...`)
  was FALSE at `j = a, i > a`. The proof only ever applied it with `j > i > a`,
  so nothing depended on the wrong form -- but the statement claimed more than
  it should, and is now `a < i -> a < j`.

### What is genuinely left

Nothing on the branching front. Remaining, if anyone wants the full
general-`r` analogue of the merged convention-D chain:

* **normalisation** `sum_{|mu|=n} f^mu w_mu = 1` at general `r` -- the r=2
  proof is `MarkovNormalisation`; branching is the inductive step and is now
  available, so this should follow the same shape.
* **uniqueness / the Markov trace instance** at general `r` -- `markovTrace_unique`
  is already generic in the coefficient ring; what is r-specific is the weight
  system it is applied to.

`vandPairProd` / `sum_vandPairProd_scale` stay proved and correct; the final
route did not need them, and that is recorded in the file headers rather than
deleted.


## Toward the headline sum

Commits `45db7a60a`, `9209649a2`. Also retitled PR #5662 — its title still said
"branching reduced to one named classical fact", which was true when written
and is not now.

* `qratio_prod_eq_zero_of_not_addable` — a row that cannot take a box
  contributes 0, because `mu_{a-1} = mu_a` forces `beta_{a-1} = beta_a + 1`,
  hence `Q*x_a = x_{a-1}`. The `schurPrincipal`-level counterpart of
  `vandPairProd_update_eq_zero`, and why the r=2 chain's
  `rowLen_two_addCell_row2` needs no general-r analogue.
* `isAddableCell_rowEnd_iff` — row `a` takes a box iff `a = 0` or
  `mu_a < mu_{a-1}`. The other two `IsAddableCell` clauses are automatic at a
  row end. `not_isAddableCell_rowEnd` is the contrapositive in the form the
  vanishing lemma consumes.

### The headline statement, and what it still needs

    sum_{a<r} (if addable a then s_{mu + box at a} else 0)
      = [r]_Q * s_mu

is `sum_eq_bracket_mul_of_qratio_scaling` at `v i = Q^{beta_i}`, `W = s_mu`,
with `w` total via `addCellOrSelf` (already in the corpus, with a decidability
instance beside it). `hw` splits: addable rows by
`schurPrincipal_addCell_eq`, non-addable by
`qratio_prod_eq_zero_of_not_addable` making both sides 0.

Four hypotheses still have to be supplied, and none is deep — but they are
four, so budget a brick rather than a tail:

1. `Set.InjOn (fun i => Q^{beta_i}) (range r)` — from `betaR_lt` plus
   root-of-unity genericity.
2. `(addCell mu s).colLen 0 <= r` for each addable row — true because adding
   at row `a < r` either keeps `colLen 0` or raises it to `a+1 <= r`, but it
   needs a `colLen_zero_addCell` lemma.
3. `hD` at `nu` — the hook product of `mu + box` is nonzero. Same genericity;
   `hookLength_addCell_of_mem` (#5645) describes the new hooks.
4. `levelConst != 0` and `rowColProd != 0` — products of `1 - Q^k` at nonzero
   `k`, so again genericity plus `betaR_lt`.

All four are instances of "Q is not a root of unity", so the clean move is
probably to package that once as a hypothesis class or a single
`IsGeneric Q r` predicate rather than threading four separate non-vanishing
conditions through every statement. Worth deciding before writing them.


## HEADLINE LANDED — general-r branching is one theorem

Commits `b9556fafb`, `a260d2856`.

    sum_schurPrincipal_addCellOrSelf :
      sum_{a<r} s_{mu + box at row a}(1,Q,...,Q^{r-1})
        = (1 + Q + ... + Q^{r-1}) * s_mu(1,Q,...,Q^{r-1})

for `QBeta.WenzlWeight.schurPrincipal` itself, at every level, sorry-free and
axiom-clean. This is what #5575 proves at r=2 via `schurPrincipal_twoRow`'s
telescoping closed form.

**One hypothesis.** `hgen : forall k : Z, k != 0 -> Q^k != 1` — the same
genericity `schurPrincipal_eq_zero_iff` already carries. The bean's previous
note listed four separate non-vanishing conditions plus a row-count bound;
`BranchingGenericity.lean` derives all of them from `hgen`, so nothing extra
appears in the signature. Packaging first, as that note recommended, was the
right call — writing them inline would have put five conditions on every
downstream statement.

**The summand is total**, `addCellOrSelf` guarded by the decidable
`IsAddableCell`, rather than indexed by addability proofs. That is what
`qratio_prod_eq_zero_of_not_addable` buys: on a row that cannot take a box the
q-ratio is *already* zero, so the guarded sum and a sum over addable rows
agree. The r=2 chain needed `rowLen_two_addCell_row2` plus a three-term
expansion for the same fact.

### Recurring Lean trap, third occurrence

`dsimp only` before `rw` whenever the goal came from instantiating a
`forall`-quantified hypothesis with a lambda — the redex blocks the rewrite.
Hit in `betaPairProd_addCell`, `qratio_prod_eq_rowColProd` and again here.

### Still open (unchanged, and not blocking anything)

* **normalisation** `sum_{|mu|=n} f^mu w_mu = 1` at general r — branching is
  its inductive step and is now available; the r=2 proof is
  `MarkovNormalisation`.
* **the trace instance** at general r — `markovTrace_unique` is already
  generic in the coefficient ring; only the weight system is r-specific.


## Normalised branching + the omitted-cell fact

Commits `eb601851a`, `c23911f03`.

    sum_wenzlWeight_addCellOrSelf : sum_{a<r} w_{mu + box at a} = w_mu

The normalisation `w_mu = s_mu / [r]_Q^{|mu|}` is chosen so the `[r]_Q` the
unnormalised sum produces is absorbed by the one extra cell each summand
carries; `card_addCell` is the step that says so. This is
`MarkovNormalisation.ocneanuWeight_addable_sum` at r=2, now at every level.

    wenzlWeight_addCell_beyond_eq_zero :
      r <= a,  IsAddableCell mu (a, rowLen a)  ->  w_{mu + box} = 0

**Worked out before writing it, and worth recording because it is the one
non-obvious step in the bridge to come.** The guarded `range r` sum and a sum
over the ADDABLE CELLS of `mu` are not obviously the same finset:

* every addable cell is `(a, mu.rowLen a)` (`rowLen_of_isAddableCell`, #5645),
  so the addable set injects into row indices;
* if `colLen 0 < r` the addable rows are all `< r` and the two sums agree
  termwise;
* if `colLen 0 = r` there IS an addable cell at row `r` — start a new row,
  addable because row `r-1` is nonempty — which the `range r` sum omits.
  That term is zero, by the lemma above.

So they agree in both cases, but only because of the second bullet.

## Left for full normalisation

    sum_{|mu| = n} f^mu * w_mu = 1

Three steps, in order:

1. **The bridge**: `sum_{s : {s // IsAddableCell mu s}} w_{mu+s}
   = sum_{a<r} (guarded)`. The math is settled (above); the Lean is a
   `Finset.sum_nbij'` between the addable subtype and a subset of
   `range (colLen 0 + 1)`, plus the `colLen 0 = r` term. Budget a brick —
   dependent `f <s, proof>` under an `if` is the awkward part.
2. **`sum_dim_weight_succ`** at general r — reuse
   `YoungDiagramCornerReindex.sum_corner_eq_sum_addable` (#5575, stated for
   arbitrary diagrams) and `numStandardYoungTableaux_branching`, exactly as
   `MarkovNormalisation` does.
3. **Base case + induction**: only `bot` has size 0, `f = 1`
   (`numStandardYoungTableaux_bot`), and `wenzlWeight_bot = 1` is already
   proved in `WenzlWeightLevelR`.

Step 1 is the only one with any content left; 2 and 3 are transcription.


## NORMALISATION DONE — all three defining properties at every level

Commits `6f09a5edd`, `ce02eb408`, `7bc4b02e2`.

    sum_dim_wenzlWeight_eq_one :
      sum_{|mu| = n} f^mu * wenzlWeight r Q mu = 1

`MarkovNormalisation` proves this at r=2, over R, at convention D. Same
argument at every level, over any field. So the level-r weight system now has
all three defining properties proved, sorry-free:

* vanishes above r rows        `wenzlWeight_eq_zero_iff`
* consistent under restriction `sum_addable_wenzlWeight_all`
* sums to 1                    `sum_dim_wenzlWeight_eq_one`

### The step that would have stalled the induction

`sum_addable_wenzlWeight` carries `hrmu : colLen 0 <= r`. **The induction sums
over EVERY diagram of size n**, including those with more than r rows, where
that hypothesis fails. There the identity still holds, but for the opposite
reason — both sides are 0: the diagram's weight vanishes, and so does every
diagram obtained from it, because adding a box cannot lower the row count
(`colLen_zero_le_addCell`). `sum_addable_wenzlWeight_all` is the
hypothesis-free form. Missing this would have left the induction stuck on
exactly the diagrams the level-r cap is about.

### The indexing bridge, for the record

`sum_addable_eq_sum_range` goes through an explicit `addableRowSet` Finset and
`Finset.sum_subtype`, which **avoids forcing the noncomputable
`Set.Finite.fintype` instance** — the whnf timeout that cost a round in #5575
when `Equiv.sum_comp` was tried on the same subtype. Worth remembering: for
these addable/corner subtypes, build the Finset and use `sum_subtype`, do not
reach for an `Equiv`.

Also: `sum_corner_eq_sum_addable` is the double-sum reindexer;
`sum_cornerPair_eq_sum_addPair` is the flat sigma version, and substituting it
by mistake times out at whnf rather than failing to unify.

### Left

Only the **trace instance** at general r. `markovTrace_unique` is already
generic in the coefficient ring; what is r-specific is the weight system it is
applied to, and that system is now fully proved.


## CORRECTION: the trace instance is NOT assembly

I ended the last turn saying the trace instance at general r "should be
assembly rather than new mathematics, since `markovTrace_unique` is already
ring-generic". **That is wrong.** The Markov property does not rest on
branching; it rests on the CORNER IDENTITY, which is a different and harder
statement:

    sum_{s addable to nu} w_{nu+s} * seminormalParam q (c(s) - c(corner))
      = z * w_nu

Branching is the same sum WITHOUT the `seminormalParam` factor. At r=2 the
corpus proves it via `corner_identity_twoRow` and the telescoping closed form;
`markov_of_corner_identity` takes it as a hypothesis. So it is real remaining
content, not plumbing.

### But it does generalise, and I now have the constant — measured, not guessed

**11/11 exactly zero**, exact sympy, `r = 2,3,4,5`, every corner of
`[2,1] [1,1] [3,1] [2,2] [3,2,1]`, with

    z = Q^r (1-Q) / ((1-Q^r) * q)   =   z_W / q

The `1/q` is the Hecke normalisation shift (`sigma = g/q`), r-independent, and
the r=2 row reproduces convention D's `z_D = q^3/(q^2+1)`. **My first attempt
used `z_W` with no `/q` and every residual was nonzero** — worth recording,
because that is the version anyone would write down from Wenzl's parameter
relation directly.

### A route, with its open detail

In ratio form the target is

    sum_a (q-ratio_a) * a(c(s_a) - c(corner))  =  Q^r / q

With `x_i = Q^{beta_i}` at level r: `c(s_a) = beta_a - (r-1)`, and for a corner
in row b, `c(corner) = beta_b - r`, so `d = beta_a - beta_b + 1` and

    a(d) = (q - 1/q) * Q x_a / (Q x_a - x_b)

so the `(Q x_a - x_b)` **cancels the j = b factor** of the q-ratio numerator.
Each term is then `f(x_a) / prod_{j != a}(x_a - x_j)` with

    f(t) = (q - 1/q) * Q * t * prod_{j != b} (Q t - x_j)

— degree r, one above what `sum_eval_div_prod_eq_coeff` takes directly, but the
same `divX` subtraction that `sum_prod_qratio` uses handles that.

**Open detail:** `a = b` is possible (a row can carry a removable corner AND be
addable, when `nu_b < nu_{b-1}`). There the `j = b` factor is absent from the
product, no cancellation happens, and the term is `f(x_b)` over
`(Q-1) x_b * prod_{j != b}(x_b - x_j)` — off by `1/((Q-1) x_b)` from the
uniform shape. Resolve that before writing Lean.
