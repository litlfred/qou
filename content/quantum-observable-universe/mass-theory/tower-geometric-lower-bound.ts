import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tower-geometric-lower-bound",
  title: "Super-exponential brane-tower growth (GAP-A-3)",
  lean: {
    ref: "qou:QOU.Mass.LevelSelection.TowerGeometricLowerBound",
    validation: "not_checked",
  },
  tags: ["binding", "brane-tower", "level-selection", "gap-a-3", "plancherel"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-13",
      body: "Open combinatorial core: verified exact for `k ≤ 10` (`computations/deltalambda/wlambda_wstd_growth_bound_probe.py`); a faithful proof needs SYT / skew-tableau / Plancherel-measure Mathlib infrastructure. Carried in Lean as the §3b class `TowerGeometricLowerBound` with **no** fabricated instance (the honest open state). Per the anti-laundering rule, axiomatizing the class is not a proof of the bound.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). Recorded honestly, because this block's " +
        "specialisation is **weaker than its file's**: the three class " +
        "fields — $1 < r$, $0 < c$, $\\forall k,\\; c\\,r^k \\le w(k)$ — are " +
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
        "for the $\\mathbb{R}(t)$ counterexample). Two alternatives were " +
        "considered and rejected: generalising the class in place leaves " +
        "the file's theorems on $\\mathbb{R}$ regardless and merely adds a " +
        "mixed generic/archimedean signal to the same file; hoisting it to " +
        "a separate generic file is a no-gain indirection, since the sole " +
        "use site re-specialises at $R := \\mathbb{R}$ immediately. Stating " +
        "an antecedent in the same ordered field as the conclusion it " +
        "feeds is the ordinary reading, and this note is the record that " +
        "the class itself carries no archimedean content.",
    },
  ],
});
