---
# wpdb
title: The curvature-rank chain assumes a word-depth -> partition-depth bridge that is stated nowhere
status: in-progress
pr: 8193
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T02:30:00Z
updated_at: 2026-11-16T20:41:00Z
parent: qou-n4nr
---

Surfaced in #5183 as an open question, investigated and confirmed. Full
evidence:
[`2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md`](../docs/audits/2026-08-16-word-depth-vs-partition-depth-bridge-is-unstated.md).

**The gap.** Five sites assume

    Z^(k)(A) = span{ e_lambda : depth_GB(lambda) = k }

and all five cite `prop:curvature-rank-gb-stratification` for it. That
proposition states `J^r/J^{r+1} = {T_w : r(T_w) = r}` — a statement about
**words**. Its Lean context class carries `rank_T_w : A -> N` and
`quotient_set : N -> Set A`; **no partition type appears in it at all**.

The partition side, `gbDepth lambda = max hook`, is a plain Lean `def`. Nothing
relates the two — verified by an exhaustive pass over `QOU/**/*.lean` for a
declaration mentioning both.

**Sites:** `prf:phi-q-categorical-truncation` Step 3;
`prf:quantum-dilogarithm-stratified` Step 3(b) (corrected in #5183);
`prf:unified-curvature-rank-mass-formula`; `conj:two-filtration-bridge` (which
*presupposes* the grading rather than supplying it); and
`computations/gb_depth_period_bring_fig8.py`, which flags the two filtrations as
"SEPARATE" with an open relationship *and* attributes the partition one to the
word proposition in the same sentence.

**Scope-(a).** Unstated, not false. It may be true and provable. Two reasons to
expect it is not trivial: the word filtration counts rewrites to normal form
while the partition depth is a hook statistic; and the `(2,2)` self-conjugate
cell of `H_4(q)` (max-hook 3) is exactly where the neighbouring
iterated-integral comparison found the two filtrations disagreeing.

**Why it matters.** It is load-bearing for the whole curvature-rank mass-formula
chain — the `m^(k)` functionals, the Terms 1-7 mapping, the Phi_q truncation
depth. All of it is conditional on a step nobody has written down.

**Next step.** Give the identification its own block, so downstream blocks cite
a statement that says what they use. If it is conjectural, the three `prf:`
blocks become downstream of a conjecture and §3b applies — which is precisely
why it should be named rather than left inside a citation.

## Attempted the proof — NOT closed, but the partition side is now measured (2026-08-16)

Tried to prove the bridge. Did not close it. What the attempt did establish,
sorry-free, is a sharp fact about the partition side that bears directly on the
downstream use — `QOU/BraidKnot/TwoFiltrationBridge.lean`:

| theorem | content |
|---|---|
| `gbDepth_eq_corner` | `gbDepth μ = rowLen 0 + colLen 0 - 1` — the max hook is always the **corner** hook |
| `gbDepth_eq_of_border_eq` | two diagrams sharing a first row and column have the same depth, however different their interiors |
| `four_le_card_of_mem_one_one` | a non-hook needs ≥ 4 cells, so every partition of `n ≤ 3` is a hook |
| `gbDepth_const_on_H3` | all three `H₃` blocks have depth `3` |

**The last one is the point.** `prop:phi-q-categorical-truncation` sets
`k⋆(T_w) := max{gbDepth λ : λ ∈ supp(T_w)}` and states the truncation depth is
*"structurally locked to the NF support of `T_w`"*. At `n = 3` that maximum is
`3` for **every** `T_w` with nonempty support — constant, so it locks onto
nothing. And `n = 3` is the single-nucleon case (`schur-weyl-mass-decomposition`:
the symmetric / standard / antisymmetric blocks), not a toy.

Scope-(a): the grading is degenerate at `n ≤ 3`, not the truncation false. It
becomes non-trivial from `n = 4`, where `(2,2)` has depth `3` against `4` for
the four hooks.

**Why the bridge itself did not yield.** Two obstructions, neither dissolved:

1. **Well-definedness.** `r(T_w)` is "the number of `R_H`/`R_YB` rewrites needed
   to reach normal form" — a property of a **word**, not of its image in
   `H_n(R,q)`. Different words for the same algebra element need different
   counts. The proof's own Step 2 says `J^ℓ` is *"the image of `I^ℓ` under the
   quotient map"*, and `H_n = ℂ⟨σ⟩/I`, so that image is **zero** for `ℓ ≥ 1`.
   As written the filtration is either trivial or not a function on the
   quotient. This needs resolving before there is a statement to prove.
2. **Coarseness mismatch.** `gbDepth` is determined by `(λ₁, λ'₁ )` alone
   (`gbDepth_eq_of_border_eq`), taking values in `[2√n − 1, n]`. Any candidate
   word-side rank would have to be equally blind to the interior of `λ`, which
   is a strong constraint on what `r(T_w)` could be.

**Next honest step:** fix the definition of the word filtration so it is
well-defined on `H_n(R,q)` — as a filtration by *ideals* of the algebra, not by
rewrite counts on representatives. Until then the bridge has no well-formed
statement, which is a sharper diagnosis than "unproved".


---

## 2026-08-16 — partition side closed to one named GAP; the free word-side route is dead (#5205)

**Partition side — done, and localised.**

* `content_image_eq_range` / `card_content_image` (unconditional, sorry-free):
  the contents of `λ` are an unbroken integer interval, so
  `gbDepth λ = #{distinct contents}` — an *equality*, not the `2·card − 1` bound
  I first wrote and discarded as useless.
* `SeminormalEigenvalue` (§3b-cond, no instance) carries the open seminormal
  eigenvalue theorem as *hypotheses*. `card_eigen_image` /
  `gbDepth_eq_card_eigen` **derive** `gbDepth λ = #{distinct JM eigenvalues on
  the λ-block}` from those fields alone — no diagram, no hook, no cell survives
  in the statement.

So the whole remaining partition-side debt is one named class, and it is an
*existing* corpus GAP, not a new one: bean `qou-ck0g` item 2, whose substrate
(the sorry-free `seminormalRep`) is landing in PR #5076.

**Word side — the free route is provably not it.**
`QOU/BraidKnot/WordFiltrationObstruction.lean`: since `H_n(R,q) = R⟨σ⟩/I`, the
tempting reading of `J^r` is the r-th power of the image of `I`. But that image
is `⊥`, so every positive power vanishes (`map_pow_eq_bot`) and the filtration
has **two strata** — everything in degree 0, nothing above. `gbDepth` already
takes two values on partitions of 4 (`gbDepth_ne_on_H4`: `[4] ↦ 4`,
`[2,2] ↦ 3`), so a one-stratum grading cannot be it.

**Scope-(b), of a READING.** Proved invariant ⇒ structural exclusion — but of
one candidate meaning of `J^r`, not of the proposition. The two live readings
are filtrations of *vector spaces* (word length in a GS normal form; rewrite
depth to normal form) and neither is touched. Not evidence the bridge is false;
evidence the cheap route to it does not exist.

## What is still open — the sharper question

**Is `r` even well defined on the quotient?** Both surviving readings are
defined on a *word*, and a word is not an element of `H_n(q)`. A grading needs
`r` constant on the fibres of `R⟨σ⟩ ↠ H_n(q)`, and the Hecke relation
`σ² = (q − q⁻¹)σ + 1` relates words of different lengths. On the face of it, it
is not — which would mean `prop:curvature-rank-gb-stratification` needs a
*chosen normal form* as part of its data, not just a rank function.

Next step is to state that as a Lean question against a GS normal-form
selector, rather than to keep asserting the filtration exists.

Also worth noting for whoever picks this up: `n = 4` is now the first testable
case from *both* directions — the partition grading is degenerate at `n = 3`
(`gbDepth_const_on_H3`) and separates at `n = 4`, and `(2,2)` is independently
the cell `computations/gb_depth_period_bring_fig8.py` flags as where the two
filtrations were observed to disagree.


---

## 2026-08-16 (later) — read the PROOF block, not just the statement. Three findings, two of them corrections to me.

Reading `curvature-rank-gb-stratification-proof.md` and
`mba-step07-gb-filtration.md` changes this bean's finding. `J^•` is **three
inequivalent objects under one symbol**, and two of the three are excluded.
Full write-up: `docs/audits/2026-08-16-three-gb-filtrations-one-name.md`.

| # | definition | where | status |
|---|---|---|---|
| 1 | "elements requiring at least ℓ applications of `R_H`, `R_YB`" | proof Step 2, 1st sentence | the survivor; well-definedness open |
| 2 | "**Equivalently**, the image of `I^ℓ` under the quotient map" | proof Step 2, same sentence | **provably `⊥` for ℓ ≥ 1** |
| 3 | `F_ℓ = span{T_w : ℓ(w) ≤ ℓ}` (Coxeter length) | `mba-step07` | well defined; **fails a dimension count at n ≤ 3** |

### 🔺 I UNDER-claimed the Lean I landed this morning

`WordFiltrationObstruction.lean` described the ideal-power reading as *"the
tempting reading"* — a hypothetical. **It is not hypothetical: Step 2 of the
proof asserts it as an "equivalently".** So that file does not exclude a
strawman I invented; it refutes a clause the corpus actually contains, inside
the proof of the very proposition four blocks cite. Docstring corrected in
place. Correcting an under-claim upward is the same duty as correcting an
over-claim downward, and this direction is the more consequential one — a reader
of the original file would have concluded the obstruction was academic.

### 🔻 I over-claimed the well-definedness objection

I wrote here that `r` is "on the face of it" not well defined on the quotient.
**Wrong for object 3**: `T_w` is indexed by `w ∈ S_n` and `ℓ(w)` is Coxeter
length, well defined by Matsumoto. Retracted. (It *does* still apply to object
1: "requiring at least ℓ applications" describes a *word*, and the minimum over
representing words is 0 for every element — so object 1 needs a **chosen**
normal form as data, not just a rank function.)

### New: object 3 fails a dimension count exactly at the single-nucleon case

With `r = ℓ` pinned the comparison is pure counting — the `e_λ` are independent,
the `T_w` are a basis, so `Z^{(k)} ⊆ gr_k` needs
`#{λ ⊢ n : gbDepth λ = k} ≤ #{w ∈ S_n : ℓ(w) = k}`.
Measured (`docs/audits/scripts/curvature_rank_vs_gbdepth_dimension_count.py`):

* **n = 2 — FAILS.** needs `dim gr_2 ≥ 2`; `gr_2` is empty.
* **n = 3 — FAILS.** gbDepth ≡ 3 on all three partitions, so needs
  `dim gr_3 ≥ 3`; only the longest element of `S_3` has length 3, so
  `dim gr_3 = 1`.
* **n = 4..7 — holds.**

`n = 3` is `H_3`, the single-nucleon case — where `m_p` / `m_n` live.

### The dilemma this leaves the four citing blocks in

Either the identification means compatibility with the length filtration (**and
is excluded at n ≤ 3, precisely where the physics is**), or `Z^{(k)}` is just a
labelling of the centre with no compatibility claim (**and the citation to
`prop:curvature-rank-gb-stratification` does no work**, which is this bean's
original finding). No third branch.

**Not claimed:** that any mass result is wrong; that the proposition's
*statement* is false; that `prop:gb-spectral-sequence` is affected. All three
untouched and unexamined.

### Next

Not "state the well-definedness question" any more — that is answered per
object. The live item is the repair: give `J^•` **one** definition and say
which. Deleting the false "equivalently" clause is necessary but repairs
nothing on its own; the three-way ambiguity is what let a provably-zero object
sit unnoticed inside a load-bearing proof.


---

## 2026-08-16 (owner fork answered: 1 + 4 + 3) — and option 3 is dead on arrival

Owner picked options **1**, **4**, **3**, and asked for the Coxeter-length
impact in more detail.

### Option 1 — DONE

The false "Equivalently, `J^ℓ` = image of `I^ℓ`" clause is removed from Step 2
of `curvature-rank-gb-stratification-proof.md`, with an explicit Gap note that
**Step 3 depends on it and is incomplete as written**. The refutation is Step 1
of the same proof: it states `I = ker π`, so `π(I^ℓ) = 0` for `ℓ ≥ 1`. The proof
contained its own refutation two steps apart.

**Sidecar staled and NOT refreshed** — `content/pipeline/qa-sweep.ts` moved to
folio-assistant in the miga migration with no standalone replacement, so no
honest refresh exists in this checkout. Declared, not hand-edited.

### Option 3 — REFUTED before starting, so not started

`def:hecke-normal-form` settles the `T_w` question **against** the rewrite
reading. It says normal form is *"of an element `h`"*, is **unique**, the
reduction is **confluent**, and *"the resulting basis elements correspond
bijectively to the symmetric group `S_n`"*.

So `T_w` is the normal-form basis indexed by `S_n` — and a normal-form element
requires **zero** rewrites. Therefore `r(T_w) = 0` identically, and
`{T_w : r(T_w) = r}` is the whole basis at `r = 0` and empty above. **The
rewrite-depth reading is degenerate on exactly the set the proposition applies
it to.**

This also resolves §2b of the audit: reading (a) is correct, so the two readings
are not merely "mutually exclusive" — (a) is *the* reading, and it is the one
that kills object 1.

**All three readings of `J^•` are now excluded**, each for a different reason:
`⊥` by proved invariant (object 2); dimension count at `n ≤ 3` (object 3);
identically zero given `def:hecke-normal-form` (object 1). I did not do option
3's work, because its premise is refuted — reporting the negative rather than
manufacturing progress on a dead branch.

### Option 4 — SCOPE CORRECTED, not yet executed

**The blast radius is 10 citing sites across 8 blocks, not the 5 I reported.**
My audit grepped for blocks *asserting the identification*; the full citation
count also reaches `confinement-categorical-proof`,
`gb-depth-period-correspondence`, `plancherel-term-7-formulation-proof` and
`spectral-sequence-collapse-proof`. Those cite the proposition for *different*
things, so option 4 needs per-site judgement, not a blanket edit — mechanical
editing across sites whose uses differ is how this class of defect got in.
Deliberately left for the next tranche rather than done badly under time.

### Coxeter-length impact, in detail (the owner's question)

`F_ℓ = span{T_w : ℓ(w) ≤ ℓ}` filters `H_n(q)` by **vector spaces**;
`dim gr_ℓ = #{w : ℓ(w) = ℓ}` (Mahonian). `Z(H_n(q))` has dim `p(n)`. For the
citation to do work, `Z^{(k)}` must be `(Z ∩ F_k)/(Z ∩ F_{k-1})`, which injects
into `gr_k` (kernel `= Z ∩ F_k ∩ F_{k-1} = Z ∩ F_{k-1}`). Hence the count.

**At n = 3, concretely.** `dim H_3 = 6`; lengths `0,1,1,2,2,3` so
`dim F_• = 1,3,5,6`. Centre dim 3. Each `e_λ` has generically nonzero
`T_{w_0}`-coefficient, so all three lie in `F_3 \ F_2`; `Z ∩ F_2` is cut by
**one** linear condition, dim ≥ 2, leaving
`dim((Z ∩ F_3)/(Z ∩ F_2)) ≤ 1`. The blocks need all three idempotents there.

**Does NOT reach:** Wedderburn, Markov trace, `tr_M`, `y_λ`, the idempotents
themselves, `gbDepth`, `prop:gb-spectral-sequence`, or the `E₂`-collapse claim.
No mass is evaluated anywhere in the argument.

**Confined to n ≤ 3, holds cleanly n = 4..7** — Mahonian numbers grow fast while
`p(n)` stays small, so the constraint is tight only for small `n`. **The
multi-nucleon binding work at H₄+ is unaffected.** It hits exactly `H_3`, the
single-nucleon case — which independently already had `gbDepth` constant there,
making `k⋆` vacuous. Two unrelated defects on the same `n` is the part worth
weighting highest.

### Observed, not claimed

`curvature-rank-gb-stratification-proof.qa.json` carries `da-false-claim`,
`da-circular`, `da-overclaim` and `da-vacuous`. All four ran. All four returned
**zero findings** on a proof containing a clause its own Step 1 refutes. One
miss is not evidence a checker is useless, but it is worth knowing before
relying on `da-*` as coverage.


## A SIXTH consumer, and it is on the BINDING side (2026-08-25)

The five sites listed above are all **mass-formula** sites. The binding chain
routes through the same unestablished bridge and is not in that list:

    prop:jet-filtration-binding-extensive        (extensive, sorry-free)
      -> conj:binding-manybody-eq-jet-filtration
           -> lem:bond-order-eq-jet-degree       ("body order n = jet degree n")
                -> prop:gb-spectral-sequence
                -> prop:jet-prefix-gb-filtration

`prop:jet-prefix-gb-filtration` DEFINES its jet prefix as a GB graded piece:
`beta_k^GS := sigma_{k-3}(T_w) in J^{k-3}(q) / J^{k-2}(q)`. So the step naming
WHICH body order an `a_D^{(n)}` belongs to is stated in the same `J^bullet` with
three excluded readings.

**This raises the stakes on wpdb.** The binding side is where the corpus's
extensive term lives — the object the 4He measurement demands (it exceeds the
complete-graph pairwise ceiling by 11.12 MeV,
`2026-08-25-low-isotope-binding-error-staleness-vs-gap.md`).

**Two consequences, deliberately separated — one is much weaker.**

*Consistency observation only, NOT a derivation:* under the ideal-power reading,
`J^{k-3}/J^{k-2}` is the zero quotient for every k > 3, so every prefix above the
first stratum vanishes and the body-order series would truncate at the pairwise
term — the same shape as the measured 4He failure. Since the ideal-power reading
is precisely the one already EXCLUDED, this is a consequence of a reading nobody
is committed to. It shows the two candidate explanations are not obviously
independent; it establishes nothing.

*Solid:* the magnitude gap is NOT downstream of `J^bullet`. `a_D^{(n)}` is a
Seiberg-Witten period; the GB filtration enters only the indexing. Fixing
`J^bullet` would say which term the MeV belong to, not supply them.

Also note `gbDepth_const_on_H3` lands directly on the light isotopes: the atom
word sits in `H_{3A}(q)`, so at A = 1 the grading this chain reads off is
constant, separating first at n = 4.

Analysis: `docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md` §4.

## 2026-08-26 — attempted the bridge. NOT closed. The obstruction is now sharper, and the last reading is dead.

Full write-up:
[`docs/audits/2026-08-26-no-shift-rescues-the-word-partition-bridge.md`](../docs/audits/2026-08-26-no-shift-rescues-the-word-partition-bridge.md).
**It is open. Nothing here closes it.** What changed is that the surviving
candidate is gone and the obstruction is now shift-invariant.

### The one thing in the inherited record that was too optimistic — and it was mine to catch

The second audit tested

    #{lambda |- n : gbDepth = k}  <=  #{w in S_n : l(w) = k}

and reported **fails at n <= 3, holds at n = 4..7**, concluding the Coxeter
reading "is not an exclusion of the identification in general". That verdict is
correct *about the test that was run* and I am not retracting it. But the test
compares the partition strata against `gr_k` of the **whole algebra**, and
`Z^(k)` is a graded piece of the filtration induced on the **centre**. The bound
is sound and very lossy: at n = 6 it compares against `{1, 5, 14, 29, 49, 71,
90, 101, ...}` when the true graded dimensions are
`{1,0,0,0,0,0,0,0,1,1,1,0,1,3,2,1}`.

Computing `dim(Z cap F_k)` instead turns a necessary condition into an
**equality test**. It fails at every n. So the reading was never viable at
n = 4..7 — the earlier pass could not see it through that bound, and that is why
this front looked open for ten days.

### Result 1 — degree 0, and it is filtration-AGNOSTIC (scope (b))

For ANY filtration with `F_{-1} = 0` and `1 in F_0` — true of every reading the
corpus names — `Z^(0) = Z cap F_0` contains the unit, so it is nonzero. The
partition side's degree-0 stratum is EMPTY, because `gbDepth = lambda_1 +
lambda'_1 - 1 >= 1`. So the identification **as written** is false for every n
and every candidate `J^bullet`. Invariant cited: the unit is central and sits in
filtration degree 0; `gbDepth > 0` (Lean `gbDepth_pos`, sorry-free).

This matters because the six sites write it unshifted, and
`phi-q-categorical-truncation-proof` writes the sum starting at `k = 0`
explicitly. It also says what the repair has to be: a shift.

### Result 2 — the sharp measurement (exact, three backends)

`docs/audits/scripts/centre_length_filtration_vs_gbdepth.py`. Builds `H_n(q)` in
the `T_w` basis, solves for the centre, intersects with each `F_k`. **No
floating point anywhere.** `Fraction` over QQ, `F_p` with p = 2^61-1, and
symbolic `QQ(q)` for n <= 4 — three exact backends agreeing. `dim Z = p(n)` at
every sample, certifying the specialisations generic. Specialising q can only
LOWER the rank, so every dimension reported is an upper bound on the generic
value — the direction every exclusion needs, so no genericity is assumed.

| n | p(n) | gbDepth strata | dim Z^(k) (Coxeter) |
|---|---|---|---|
| 2 | 2 | {2:2} | [1,1] |
| 3 | 3 | {3:3} | [1,0,1,1] |
| 4 | 5 | {3:1,4:4} | [1,0,0,0,1,2,1] |
| 5 | 7 | {4:2,5:5} | [1,0,0,0,0,0,1,1,1,2,1] |
| 6 | 11 | {4:2,5:3,6:6} | [1,0,0,0,0,0,0,0,1,1,1,0,1,3,2,1] |

No match at any n. At n = 6 the two dimension MULTISETS already differ
(`{1,1,1,1,1,1,2,3}` vs `{2,3,6}`), so not even an arbitrary permutation of the
index set works.

### Result 3 — no SHIFT repairs it, for all n >= 3 (scope (b))

The table is finite; this is not.

* **Lemma 1.** `Z cap F_0 = R.1`, so `dim Z^(0) = 1`. (`F_0 = R.T_e = R.1`.)
* **Lemma 2.** For n >= 3, `Z cap F_1 = R.1`, so `dim Z^(1) = 0`. Proof: in
  `[a_0 + sum_i a_i T_{s_i}, T_{s_j}]` the commuting pairs (|i-j| >= 2)
  contribute nothing, and for |i-j| = 1 the elements `s_i s_j` and `s_j s_i` are
  DISTINCT of length 2, so the coefficient of `T_{s_i s_j}` is exactly `a_i`.
  Centrality kills every `a_i` with an adjacent `j` — every i once n >= 3.
* **Lemma 3.** The gbDepth spectrum is the CONTIGUOUS interval `[m_n, n]`.
  Proof: depth d is attained iff some `r + s = d + 1` has `rs >= n` and
  `r + s - 1 <= n`; the max product `floor((d+1)^2/4)` is monotone in d.
  (Verified to n = 40.)
* **Theorem.** The word side is nonzero at 0, zero at 1, and nonzero above
  (total `p(n) >= 3`) — so its support has an INTERIOR GAP. The partition side
  has none. A shift is an order isomorphism of the index set, so it transports
  gap-freeness. No shift exists. n = 2 falls to the table.

Lean, sorry-free, `lean`-direct exit 0 against the real import cone,
`#print axioms` clean on all five declarations (propext / Quot.sound /
Classical.choice only):
`folio/quantum-observable-universe/lean/QOU/BraidKnot/CentreGradingObstruction.lean`
— `gbDepth_pos`, `gbDepth_ne_zero`, `shift_cannot_fill_a_gap`, `N4_gapfree`,
`coxeter_reading_excluded_at_four`. The algebra-side inputs are carried as
hypotheses (H_n(q) and its centre are not Lean objects here) and the theorem
DERIVES the exclusion from them, per §3b-cond.

### What I did NOT prove — read before citing any of the above

**The identification is NOT refuted in the abstract.** A filtration inducing the
gbDepth grading on the centre exists trivially: filter by the Wedderburn blocks,
`F_k := sum_{gbDepth lambda <= k} R.e_lambda`. What is excluded is that any of
the THREE things the corpus calls `J^bullet` is such a filtration. Saying it the
other way round is exactly the over-claim the scope-(a)/(b) rule exists to stop.

**No mass or binding number is touched.** `J^bullet` enters downstream as an
INDEXING — which body order an `a_D^(n)` belongs to, which stratum a projector
lands in — not as a magnitude. Wedderburn, Markov trace, `tr_M`, `y_lambda`, the
idempotents, `gbDepth`-as-a-definition and `prop:gb-spectral-sequence` are all
unaffected. **And `prop:curvature-rank-gb-stratification`'s own statement, about
words, is not refuted** — what fails is reading a partition grading off it.

### The six consumer sites — recommendation (judgement, not finding)

The second audit's dilemma collapses: branch (i) is now excluded at EVERY n, so
**the citation does no work, at all six sites.** The repair splits, and one half
needs no conditionality:

* **Class A — the site needs only the grading as a DEFINITION.** `Z = sum_lambda
  R.e_lambda` is Wedderburn; bucketing by `gbDepth` is free, and
  `k*(T_w) := max{gbDepth lambda : lambda in supp(T_w)}` is defined from the
  PARTITION support, not from any word rank. Such sites are sound mathematics
  and need only to stop citing the word proposition — no conjecture, no §3b
  propagation. `prf:phi-q-categorical-truncation` looks like this. (But its
  truncation claim is then carried by the partition support alone, and
  `gbDepth_const_on_H3` already showed that support is constant at n = 3 — so it
  is vacuous at the single-nucleon case either way.)
* **Class B — the site needs genuine word-filtration compatibility.**
  `prop:jet-prefix-gb-filtration` (`beta_k^GS in J^{k-3}/J^{k-2}`) and
  `prf:unified-curvature-rank-mass-formula` ("by curvature-rank stratification,
  `e_lambda` has GB-depth `depth(lambda)`"). These ARE the identification and
  should be re-scoped conditional on a named conjecture — which must record that
  all three candidate readings are excluded, so it is open AND currently without
  a candidate construction.

**Deliberately not executed here.** The sites cite the proposition for different
things and mechanical editing across them is how this defect got in. What I did
do is add forward-pointers at the top of both 2026-08-16 audits, since seven
blocks' banners point there — a reader following the existing chain now lands on
this finding without any content-block sidecar being staled.

### Still open, and now more precisely

**Is there a filtration of `H_n(q)`, definable from the Groebner-Shirshov
rewriting data, whose induced grading on the centre is the gbDepth grading?**
Nobody has tested a fourth object. Any candidate must satisfy: its degree-0
piece is the line spanned by the unit (Result 1), so it can match only after a
shift; and the shift must carry a GAP-FREE spectrum onto a sequence beginning
`1, 0` (Result 3). So a candidate has to either fail to be an algebra
filtration, or **put a second central element in `F_1`** — and Lemma 2 proves
the Coxeter one cannot. That is the next thing to test, and it is a much
narrower target than "find the bridge".

### Housekeeping

PR #5799 was CLOSED unmerged at 2026-08-26T03:19Z, mid-session — after this bean
was created. All four commits are pushed to
`claude/isotope-mass-binding-dashboard-kdvhz6` and are safe, but the tranche
currently has no open PR. Did not reopen or duplicate it: the close looks like a
deliberate act and re-opening someone else's closed thread is not mine to do.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under related carrier M12 of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.

## Round 53 Progress (PR #8193)
- [x] Added `partitionCornerHook`, `partitionCornerHook_bounds` (`1 ≤ h(0,0) ≤ n`), `n_three_corner_hook_degenerate`, `n_four_corner_hook_stratification`, `WordPartitionDepthBridge`, `partDepth_unique_of_wordPartitionDepthBridge`, and `no_unshifted_degree_zero_stratum` to `folio/quantum-observable-universe/mass-theory/curvature-rank-gb-stratification.lean` (`0 sorry`, `0` vacuity hits).
- [x] Verified corner-hook bounds and `n = 3, 4` stratification in `computations/probes/route89_staircase_wpdb_stargram_probe.py` (`computations/probes/route89-staircase-wpdb-stargram.witness.json`, Commit 1 `f3d7f0a51d31a6d9fa4e53d717fcd6d96c6ad0de`).
- [ ] Await CI verification and Merge Manager merge of PR #8193 (`9d88b10b75877699bcfe0134c2f9a3d95a32edf4`).
