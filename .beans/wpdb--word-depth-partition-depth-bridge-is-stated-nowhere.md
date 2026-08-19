---
# wpdb
title: The curvature-rank chain assumes a word-depth -> partition-depth bridge that is stated nowhere
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T02:30:00Z
updated_at: 2026-08-16T12:55:34Z
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
