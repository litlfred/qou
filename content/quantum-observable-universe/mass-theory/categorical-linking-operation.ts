import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:categorical-linking-operation",
  title:
    "Categorical linking operation $\\mathrm{Lk}_R$: ribbon-category dual of topological linking number",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.CategoricalLinkingOperation",
    validation: "not_checked",
  },
  uses: ["conj:categorical-higgs-mechanism"],
  tags: [
    "ribbon-category",
    "linking-number",
    "categorical-physics",
    "braided-monoidal",
    "trace-cut",
    "knot-vs-link",
    "open-problem",
    "tier-a",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** The categorical content above is internally\nconsistent with the ribbon-category framework, but each of the\nfive properties (linearity, reduction at $k=0$, multiplicativity,\ntrace-cut symmetry, bar-involution compatibility) requires a\nformal proof in the QOU substrate-category. To promote to a\n`proposition`:\n\n1. **Construct $\\mathrm{Lk}_R^{(k)}$** as a concrete morphism in\n   $\\mathbf{C}$ using the trace-cut formula above.\n2. **Prove the five properties** above from the rigid-monoidal-\n   category axioms + the Frobenius-trace structure on $A$.\n3. **Verify the disjoint-strand-pair reduction** matches the\n   Hoefsmit identification at $n = 6$.\n4. **Discharge the bar-involution compatibility** by direct\n   computation in $H_n(q)$ (path-α-Bring eigenvalue analysis).",
    },
  ],
});
