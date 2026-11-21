import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-21", body: "Restated from the source, Leitner, arXiv:math/0602138 (library `arxiv-math-0602138v1`). The previous statement claimed a formal group $G$ over $\\mathbb{Z}_p$ reducing to $H$, and called the bialgebra compatibility the Frobenius relation. The paper works over a field of characteristic $p$, constructs no $\\mathbb{Z}_p$-lift, and its compatibility condition is strong multiplicativity (Def. 1.11 and Prop. 1.13), not the Frobenius relation. The old Lean `QOU.Archimedean.skew_poisson_integration` (an opaque context and a `sorry`, with no importers) is deleted; the ref now points at the proved defining relation of the quotient $U$. The statement is Theorem 3.7 as written, including both hypotheses on $\\pi$ (strongly filtered and strongly multiplicative)." },
    { kind: "status", date: "2026-11-21", body: "Lean proves the defining relation of $U$ only (sorry-free); that relation holds by construction for any bilinear bracket. Theorem 3.7 itself is cited from the paper, not formalised." },
  ],
  label: "prop:skew-poisson-integration",
  lean: { ref: "qou:QOU.FormalGroups.integrationMk_commutator", validation: "not_checked" },
  title: "Integration of skewed-Poisson structures",
  cites: ["leitner2006"],
  uses: [],
  proofs: ["prf:skew-poisson-integration"],
});
