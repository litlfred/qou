import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-21", body: "Restated from the source, Leitner, arXiv:math/0602138 (library `arxiv-math-0602138v1`). The previous statement claimed a formal group $G$ over $\\mathbb{Z}_p$ reducing to $H$, and called the bialgebra compatibility the Frobenius relation. The paper works over a field of characteristic $p$, constructs no $\\mathbb{Z}_p$-lift, and its compatibility condition is strong multiplicativity (Def. 1.11 and Prop. 1.13), not the Frobenius relation. The old Lean `QOU.Archimedean.skew_poisson_integration` (an opaque context and a `sorry`, with no importers) is deleted; the ref now points at the proved defining relation of the quotient $U$. The statement is Theorem 3.7 as written, including both hypotheses on $\\pi$ (strongly filtered and strongly multiplicative)." },
    { kind: "status", date: "2026-11-21", body: "Formalised, sorry-free (axioms: propext, Classical.choice, Quot.sound): `QOU.FormalGroups.PBW.formalGroup_of_splay`. Scope of the Lean statement. It is over any commutative ring $R$ (the paper uses a field). Each $H_i$ is one-dimensional, so $A_i$ has a divided-power basis $b_i(n)$ with $\\Delta b_i(n) = \\sum_{p+q=n} b_i(p) \\otimes b_i(q)$ and $b_i(0) = 1$, and products of basis elements do not raise weight. The hypotheses on $\\pi$ are the paper's: internal symmetry, strong filtration (a preimage of each cross-block bracket lighter than the product), and strong multiplicativity for the splay coproduct. One hypothesis is added: the splay counit kills $\\pi$. It is assumed, not derived. Conclusion: $U$ has the PBW basis $\\prod_{i\\text{ increasing}} [b_i(J_i)]$ indexed by multi-indices $J$, it carries the bialgebra structure descended from $T$, and there is a formal group law $G$ with $G.F$ the Cartier series of that basis and the product of $U$ the convolution of $G$. Not formalised: that $\\{H_i, G\\}$ is a geometric formal group, and the case of $H_i$ of dimension above one. Files: `PBWFilteredData.lean`, `PBWMultiIndex.lean`, `SplayBialgebra.lean`, `PBWFormalGroup.lean` under `QOU/FormalGroups/`." },
  ],
  label: "prop:skew-poisson-integration",
  lean: { ref: "qou:QOU.FormalGroups.PBW.formalGroup_of_splay", validation: "not_checked" },
  title: "Integration of skewed-Poisson structures",
  cites: ["leitner2006"],
  uses: [],
  proofs: ["prf:skew-poisson-integration"],
});
