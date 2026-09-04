---
# qou-ah2l
title: trSummand from seminormalRepFin — the general-n rep is PROVED, so this is small
status: todo
type: task
priority: normal
created_at: 2026-09-04T10:41:57Z
updated_at: 2026-09-04T20:55:11Z
---

Split out of `qou-t5ve` once the corpus-grep established that the general-`n`
seminormal representation is **already proved** (see that bean's 2026-09-04
correction). Scoped accordingly — this is smaller than the "formalise the
seminormal construction" job I had described.

## What exists

* `QOU.SchurWeyl.hoefsmit_seminormal_rep` (`HoefsmitRepGeneral.lean`,
  sorry-free): for every `λ ⊢ N` at real `q ≠ 0` not a root of unity,
  `∃ ρ : Hecke ℝ q q⁻¹ (N-1) →ₐ[ℝ] Matrix (Fin dλ) (Fin dλ) ℝ`, non-scalar
  when `dλ ≥ 2`.
* `SeminormalRep.seminormalRepFin` — the underlying construction, a
  *function*, not an existential.
* `QOU.Archimedean.rhoMixedSigma2_conj_S1` (`qou-t5ve`) — the gauge relating
  the library's square-root-free basis to the orthogonal basis
  `pyhecke_native` returns. **Read this before wiring anything to the Rust
  numbers**: only trace, determinant, spectrum and the relations transfer
  entry-free.

## What is missing

`DescartesMarkovTrace.trSummand` is still free data constrained only by
`tr_eq_sum_summands`. To tie it to the mathematics:

1. Define `chiLambda λ (w : word) : ℝ := Matrix.trace (seminormalRepFin … w)`
   — the character as a function. `hoefsmit_seminormal_rep`'s existential form
   is not directly usable for this; `seminormalRepFin` is.
2. Instantiate `trSummand n i x` from it, with the summand index `i` ranging
   over the `≤ 2`-row partitions of `n` (the SU_q(2) constraint).
3. Discharge `tr_eq_sum_summands` — the Wedderburn decomposition of the trace,
   which is the real content and may already be reachable from
   `HeckeWedderburnGeneral` / `MarkovAssembly` in the same directory.

Step 3 is the one that could still be large. Steps 1–2 are plumbing.

## Do not repeat

Four times in this arc I asserted something was missing and the corpus-grep
found it present: the general-`n` characters (Rust, months old), `S0`
(duplicated outright), the "21 sorries" (zero), and the general-`n` rep
(proved). **Run the six paths against `QOU/SchurWeyl/` — 73 files — before
writing a line of Lean here.**


## 2026-09-04, second pass — the scope above is wrong too. Step 3 is largely DONE.

I opened this bean saying "steps 1–2 are plumbing, step 3 (`tr_eq_sum_summands`)
is the real content and could still be large." Ran the six paths against
`QOU/SchurWeyl/` before writing any Lean, as the section below instructs.
**Step 3 is essentially done for exactly the case that matters, and step 1 needs
no new definition at all.**

### Step 1 — the character as a function: it exists

`(seminormalRep q hq0 hq2 m ν.2 y).trace` **is** `χ^ν(y)`, a function, used
throughout `MarkovAssembly.lean`. No `chiLambda` definition is needed; at most a
convenience abbreviation. `hoefsmit_seminormal_rep`'s existential form is the
wrong handle, and `seminormalRepFin`/`seminormalRep` is the right one — that part
of my note was correct.

### Step 3 — the weighted λ-sum: proved at general `n`

`MarkovAssembly.markov_of_corner_identity` proves

    ∑_{|λ|=m+2} w_λ · tr(ρ_λ(ι y) · σ_{m+1}) = z · ∑_{|ν|=m+1} w_ν · tr(ρ_ν(y))

for **every** `y ∈ H_{m+1}(q)` and **any** weight `w`, conditional on a finite
corner identity — which is a hypothesis, not an axiom and not a `sorry`. Its
docstring is explicit that everything representation-theoretic (branching, the
block structure of `σ_{m+1}`, the Hoefsmit entry, the reindexing) is discharged.

And the hypothesis is **discharged for the two-row case** in
`OcneanuWeightMarkovCorner`: `markov_corner_row0`, `markov_corner_row1`,
`markov_corner_row1_diag`, stated over `twoRow m k` at convention D with weight
parameter `q ^ 3 / (q ^ 2 + 1)` — which is `z_D` exactly. Two-row partitions are
precisely the `SU_q(2)` summands the Descartes file is about.

### So what is actually missing

Not the mathematics. **`DescartesMarkovTrace` in
`content/.../brings-surface/descartes-knot-eigenbasis.lean` is a hand-rolled,
weaker duplicate of library machinery that is already proved.** Its `tr`,
`trSummand` and `tr_eq_sum_summands` are free data plus a definitional
constraint; `QOU/SchurWeyl/` has the genuine `seminormalRep … .trace` and a
proved λ-sum Markov property over it.

The remaining work is therefore **wiring, not derivation**: replace the free
fields with the library objects, or state the bridge. That is a real change —
it couples a content-block structure to a 73-file library and will move what
`descartes_knot_eigenbasis` can claim — and it is NOT started here, because
starting it blind is what produced the five corrections below.

### One observation, explicitly NOT a claim

`rhoMixedSigma2 q 1 1 = q³/(1+q²)`, which is the same expression as convention
D's `z_D` and as `OcneanuWeightMarkovCorner`'s weight parameter. Whether the
seminormal corner entry *is* the Markov parameter in general, or this is a
small-case coincidence at `λ = (2,1)`, is **not established here** and should
not be repeated as though it were.

### The count is now five

Five times in this arc I asserted something was missing and the corpus-grep
found it present: the general-`n` characters (Rust, months old); `S0`
(duplicated outright); "21 sorries" (zero); the general-`n` representation
(proved); and now the λ-sum (proved, two-row case discharged). The checklist
caught every one. The lesson is not that the checklist works — it is that
**I keep running it after forming the claim instead of before.**
