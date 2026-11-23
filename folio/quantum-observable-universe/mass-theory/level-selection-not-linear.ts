import { proposition } from "../../schema/builders";

/**
 * Exclusion of linear / bond-count level-selection (no longer conditional —
 * the tower-bound class is inhabited at k₀ = 3 by QOU.Mass.WStd):
 * given the geometric tower lower bound (prop:tower-geometric-lower-bound) and
 * extensive binding for A ≥ 1, a geometric c·r^A eventually beats any linear
 * M·A, so no linear selection rule is consistent — the level is at most
 * logarithmic. Lean sorry-free (QOU.Mass.LevelSelection.no_linear_selection),
 * via Mathlib isLittleO_coe_const_pow_of_one_lt. The A ≥ 1 restriction (avoiding
 * the A=0 boundary artifact) is stated in the narrative.
 */
export default proposition({
  label: "prop:level-selection-not-linear",
  title: "Linear level-selection is excluded (exponential beats linear)",
  lean: {
    ref: "qou:QOU.Mass.LevelSelection.no_linear_selection",
    validation: "not_checked",
  },
  uses: ["prop:tower-geometric-lower-bound"],
  tags: ["binding", "level-selection", "logarithmic", "gap-a-3", "brane-tower"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\n[`QOU.Mass.LevelSelection.no_linear_selection`](../lean/QOU/Mass/LevelSelectionLogarithmic.lean) proves the contradiction outright, taking the tower bound as the class hypothesis `[TowerGeometricLowerBound w r c k₀]`. The exponential-beats-linear step is Mathlib's `isLittleO_coe_const_pow_of_one_lt` ($(A:\\mathbb{R}) = o[\\mathrm{atTop}]\\, r^{A}$); `#print axioms` reports only `propext / Classical.choice / Quot.sound`. The companion inequality `linear_selection_bound` ($c\\,r^{A} \\leq M\\cdot A$) is the un-contradicted form; this proposition is the exclusion it entails.\n\n**The hypothesis is discharged, so the exclusion is not conditional.** `QOU.Mass.WStd.towerGeometricLowerBound_wStd` inhabits the class at $k_{0} = 3$, and [`QOU.Mass.WStd.no_linear_selection_wStd`](../lean/QOU/Mass/WStdSuperExponential.lean) is this theorem at the actual $w_{\\mathrm{std}}$ with no class argument to supply; `no_superlinear_selection_wStd` is its bond-count companion. Until that instance existed the class had none, so neither exclusion could be applied to any concrete weight. The threshold costs the argument nothing, because both proofs already select their $A$ from an `atTop` filter." },
    {
      kind: "refined-framing",
      body: "This paragraph previously justified the A ≥ 1 restriction by saying the tower bound forces w(0) ≥ c > 0 while M·0 = 0. That reading was backwards: w_std(0) = 0, and the A = 0 case exhibited a false antecedent.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). Here the $\\mathbb{R}$ is not a convenience — the " +
        "**Archimedean axiom is logically necessary**, and " +
        "de-specialising to `[CommRing R] [LinearOrder R] " +
        "[IsStrictOrderedRing R]` would make the theorem *false*. " +
        "`no_linear_selection` is exactly *\"geometric beats linear\"*: " +
        "from $1 < r$ and $0 < c$ it derives a contradiction with " +
        "$c\\,r^A \\le M A$ for all $A \\ge 1$, via Mathlib's " +
        "`isLittleO_coe_const_pow_of_one_lt` on `Filter.atTop`. Over a " +
        "**non-Archimedean** ordered field the conclusion fails: in " +
        "$\\mathbb{R}(t)$ with $t$ a positive infinitesimal, take " +
        "$r = 1+t$, $c = 1$, $w(k) = (1+t)^k$, $M = 2$ — the lower bound " +
        "holds with equality, yet $(1+t)^A - 1$ is infinitesimal for every " +
        "natural $A$, so $(1+t)^A \\le 2A$ holds for all $A \\ge 1$ and no " +
        "contradiction arises. The theorem does hold over $\\mathbb{Q}$, so " +
        "what is required is Archimedean-ness specifically, not " +
        "completeness; $\\mathbb{R}$ is simply where Mathlib's little-o " +
        "growth lemma lives. Nothing generic is being hidden: the " +
        "combinatorial level indexing is $\\mathbb{N}$-valued and the " +
        "conjectural growth hypothesis is carried separately by " +
        "[`prop:tower-geometric-lower-bound`](tower-geometric-lower-bound.md).",
    },
  ],
});
