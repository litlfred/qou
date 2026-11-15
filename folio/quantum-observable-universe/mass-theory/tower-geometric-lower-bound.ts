import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tower-geometric-lower-bound",
  title: "Brane-tower growth above the containment threshold (GAP-A-3)",
  lean: {
    ref: "qou:QOU.Mass.WStd.wStd_geometric_from_three",
    validation: "not_checked",
  },
  tags: ["binding", "brane-tower", "level-selection", "gap-a-3", "plancherel"],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "This block previously asserted the lower bound for every k; it is false below k = 3, so the statement now carries the threshold.",
    },
    {
      kind: "status",
      date: "2026-09-02",
      body:
        "Promoted from `conj:tower-geometric-lower-bound` to a proposition. The bound is " +
        "proved sorry-free; the earlier status note said a faithful proof \"needs SYT / " +
        "skew-tableau / Plancherel-measure Mathlib infrastructure\", and it needed none of " +
        "it. The route is the skew branching rule plus the up-operator identity.",
    },
    {
      kind: "refined-framing",
      date: "2026-09-02",
      body:
        "The previous statement asserted the bound *for every* jet level $k$, which is " +
        "**false**, not merely unproved: $w_{\\mathrm{std}}(k) = 0$ for $k < 3$ because " +
        "the skew count vanishes off containment. The threshold is therefore part of the " +
        "claim rather than a weakening of it, and its necessity is itself machine-checked " +
        "(`not_towerGeometricLowerBound_wStd_of_lt_three`, which refutes every $k_0 < 3$ " +
        "for all $r$ and $c$).",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). Recorded honestly, because this block's " +
        "specialisation is **weaker than its file's**: the class fields — " +
        "$1 < r$, $0 < c$, $\\forall k \\geq k_0,\\; c\\,r^k \\le w(k)$ — are " +
        "order-only, use no `Real.*` and no completeness, and would type " +
        "over any linearly ordered commutative ring (the values they " +
        "abstract, the Plancherel expectations " +
        "$w_{\\mathrm{std}}(k) = \\mathbb{E}_{\\mathrm{Planch}}" +
        "[f^{\\lambda/(2,1)}]$, are in fact rational). The $\\mathbb{R}$ is " +
        "inherited from the file the class lives in, " +
        "`QOU/Mass/LevelSelectionLogarithmic.lean`, whose exclusion " +
        "theorems are its only consumers and *provably require the " +
        "Archimedean axiom* (see " +
        "[`prop:level-selection-not-linear`](level-selection-not-linear.md) " +
        "for the $\\mathbb{R}(t)$ counterexample). Stating " +
        "an antecedent in the same ordered field as the conclusion it " +
        "feeds is the ordinary reading, and this note is the record that " +
        "the class itself carries no archimedean content. " +
        "(Amended 2026-09-02: the displayed bound now uses $\\sqrt{2}$, which *is* a " +
        "`Real.*` construct, so the block's own statement is archimedean where the class " +
        "is not — the square bound it descends from, $k!/(81\\cdot 2^k) \\le w^2$, is " +
        "rational and order-only.)",
    },
  ],
});
