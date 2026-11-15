# The p-n interface convention: what R3 made canonical, and what the corpus proves about it (2026-10-11)

**Finding, in one line: the R3 ruling (2026-08-15, `bring_color_weighted`
canonical) selected the one p-n averaging convention that the corpus's own
uniqueness theorem does *not* cover — and a producer docstring describes it as
"the categorically-canonical convention … and IS derived".**

This is an instance of AGENTS.md §"Conditional-proved ≠ premise-established"
applied to *canonicity* rather than to a value. Nothing here is enacted: R3 and
AGENTS.md are **unchanged**, per §ASK THE OWNER.

## What was asked, and what this document is not

A sibling session relayed an owner pick to *"record the atom-word provenance
table as an audit entry"*, with a per-ingredient verdict table
(DERIVED-conditional / RULED / CHOSEN / POSTULATED / FIT / CONJECTURED) and
`file:line` cites, sourced from
`/mnt/project-files/mass-endomorphism/klambda/word-provenance.md`.

🛑 **That path is not readable from this container, so the table is not
transcribed here.** Reproducing it from memory of a summary would mean
publishing cites I never opened — which is the defect this corpus guards against
most carefully. What follows is only the part that was **verified at source in
this repository**, which is the relay's item (c).

## 🛑 Two claims in the relay do not survive checking

Both are recorded because they are the *interesting* kind of wrong — each
conflates two corpus objects that a prior agent has already conflated once.

### "δ is fitted" — NO. The leading term is derived, sorry-free

| | |
|---|---|
| closed form | `δ(q) = (q−1)²(1−q⁻⁴)/3 = ℏ_q²·h_q·[2]_q/3` — a function of `q` alone |
| carrier | `prop:flavor-split-substrate` (`folio/…/observations/flavor-split-substrate.md`), live |
| Lean | `theorem flavor_split_substrate`, `QOU/HadronicMass.lean:826` — **0 sorries in the file** |
| the block's own claim | *"The proton–neutron mass splitting requires **no calibration** to the u–d mass difference"* |
| residual | **−0.10 %** vs CODATA (`1.376e-3` against `1.377e-3`) |

A closed form in `q` with a sorry-free theorem and a published −0.10 % miss is a
**derivation with an honest residual**, not a fit. A fit would not have left the
0.10 %.

**What is posited is the SUBLEADING factor**, and the corpus is emphatic about
it. `_li_2_q_util.flavor_split_subleading`: *"⚠ POSITED — NOT DERIVED (audit
2026-06-29). The `(1+ℏ_q³)` multiplier has no derivation … It is also
INSUFFICIENT: … it supplies only 76 % of the gap … and must **NOT** be cited as
backed by `prop:flavor-split-substrate` (which proves ONLY the leading
`flavor_split_leading`)."* It was **de-wired** on 2026-06-29.

**This exact conflation has happened before, and the corpus records it.**
`tr_m_algebraic_q.flavor_split_leading_sym`: *"IT USED TO MULTIPLY BY THE
POSITED SUBLEADING (1 + ℏ³), while its docstring claimed it matched … at any q.
It did not … conflating them here silently gave every consumer the posited
quantity under the proven one's name."* Bean `qou-4e5k`. The repo's own witness
had carried `symbolic_delta_matches_li2q … passed=False` since 2026-08-09 **and
nothing read it**.

### "the `/4` is only a def" — NO. There is a sorry-free theorem

`prop:pn-averaging-uniqueness`
(`folio/…/mass-theory/pn-averaging-uniqueness.md`) with sibling
`pn-averaging-uniqueness.lean`, **0 sorries**: `pn_averaging_unique` at line
203, plus `pn_averaging_unique_via_weight` and `pn_averaging_subsingleton`.

> **A note on how that nearly went into this document as the opposite.** A grep
> for `pn_averaging_unique` under `folio/quantum-observable-universe/lean/`
> returns **no files**, and the obvious reading is that the block cites a
> declaration that does not exist. It does exist — in the **content-block
> sibling**, which is resolution candidate 1 of AGENTS.md §0a, not in the
> library tree. The scan universe was wrong, not the corpus. Same class as
> detector-blindness row 55.

## The actual finding: the theorem is CONDITIONAL, and the canonical convention fails its hypothesis

`pn_averaging_unique` is a conditional, and its proof shows how narrow:

```lean
theorem pn_averaging_unique
    (σ_pn σ_pn' : PnAveragingForm R) (z : R → R)
    [BarInvariant R σ_pn] [ColorFlavorCompatible R σ_pn] [hN : StandardNorm R σ_pn z]
    [BarInvariant R σ_pn'] [ColorFlavorCompatible R σ_pn'] [hN' : StandardNorm R σ_pn' z] :
    σ_pn = σ_pn' := by
  funext q
  rw [hN.norm q, hN'.norm q]
```

`BarInvariant` is an **instance hypothesis**, and the two production candidates
do not both satisfy it:

| candidate | form | bar-invariant? |
|---|---|---|
| uniform (strict-averaged) | `z − h/2` | **yes**, exactly — it is the bar-symmetriser `½(z + z̄)` of the p-p factor, since `z̄ = z − h` |
| **Bring colour-weighted (R3-canonical)** | `z − h(1/2 − δ/4)` | **NO** |

The colour weighting is **bar-mixed**: `δ̄ = −q²δ`, and the defect is exact,

```
  σ̄_weighted − σ_weighted  =  (q−1)⁵(q+1)³(q²+1) / (12 q⁵)  ≠ 0   (q ≠ 1)
```

≈ **1.67e-5** at the substrate anchor, verified in
`computations/probes/pn_interface_bar_structure_probe.py`.

**The content block already records this, as a correction to its own earlier
text**, and draws the right conclusion: *"the uniqueness statement covers the
bar-invariant class, and the colour-weighted convention **lies outside its
hypotheses** … This does not say the colour weighting is wrong, and it does not
by itself bear on which convention should be canonical."* Recorded there rather
than resolved.

### What that leaves for R3

`computations/closed_form_tau_M.py:76-80` says of `bring_color_weighted`:

> *"This **IS** the categorically-canonical convention (Bring's 3-color-tube
> structure on the modular Belyi cover) and **IS derived** (uses PR #690
> substrate split, no fitted quark masses)."*

Each half is separately checkable, and they come apart:

- **"no fitted quark masses"** — **true**. δ is the sorry-free closed form above.
- **"IS derived"**, of the *interface factor* — the `δ/4` placement is not
  derived by the uniqueness theorem, because that theorem's hypothesis is the
  one this convention fails. The substrate split being derived does not make the
  **weighting that consumes it** derived.
- **"the categorically-canonical convention"** — this is the load-bearing one.
  The corpus's uniqueness result proves canonicity **within the bar-invariant
  class**, and that class contains the *uniform* form, not this one.

So the docstring restates a conditional's antecedent as a settled fact — which
is exactly what the block's own correction note identifies in its earlier self:
*"What was wrong was restating the antecedent as established for both — a
conditional hypothesis reported as a settled fact."* The same slip, one file
over, still live.

**Not enacted, and deliberately.** Whether R3 should change, whether the
docstring should be reworded, and whether canonicity should rest on something
other than bar-invariance are all owner calls under §ASK THE OWNER. This
document records the state; it changes neither R3 nor AGENTS.md nor the
convention.

## Scope

**Scope (a)** throughout. Nothing here shows the colour weighting is wrong, and
nothing excludes it. Two negatives are stated and both are about *what is
proved*, not about what is true: the uniqueness theorem does not reach this
convention, and one docstring overstates what follows from `prop:flavor-split-substrate`.

## Cross-links

`qou-99qc` (nucleon letters / `nuc11_interleaved`), `qou-vls6` (δ), `qou-kj4v`
(pp/nn signs), `qou-brng` (chain topology), `qou-9f4h` (`k_λ`) — all open.
