import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-21", body: "Restated from the source, Leitner, arXiv:math/0602138 (library `arxiv-math-0602138v1`). The previous statement claimed a formal group $G$ over $\\mathbb{Z}_p$ reducing to $H$, and called the bialgebra compatibility the Frobenius relation. The paper works over a field of characteristic $p$, constructs no $\\mathbb{Z}_p$-lift, and its compatibility condition is strong multiplicativity (Def. 1.11 and Prop. 1.13), not the Frobenius relation. The old Lean `QOU.Archimedean.skew_poisson_integration` (an opaque context and a `sorry`, with no importers) is deleted; the ref now points at the proved defining relation of the quotient $U$. The statement is Theorem 3.7 as written, including both hypotheses on $\\pi$ (strongly filtered and strongly multiplicative)." },
    { kind: "status", date: "2026-11-21", body: "Both halves of the proof are now formalised, sorry-free, but not yet joined. (1) PBW (Thm. 1.9 in the form Thm. 3.7 uses): `ugb:UGB.GrobnerShirshov.BlockSplay.Model.normalFormBasis` proves that the ordered monomials are a basis of the presented algebra, for block data that is strongly filtered (by a weight-then-deglex order) and carries a Poisson bracket on the splay with internal symmetry. The proof is the Gröbner–Shirshov route of the paper (associativity, the two derivation conditions, Jacobi), not an analytic one. (2) Given that basis, `QOU.FormalGroups.formalGroupLaw_of_pbw` builds the formal group law. Still open: the identification of UGB's presented algebra with `IntegrationQuotient` over Mathlib's free product, which is what lets (1) feed (2). The Lean ref stays on the defining relation of $U$ until that bridge lands." },
  ],
  label: "prop:skew-poisson-integration",
  lean: { ref: "qou:QOU.FormalGroups.integrationMk_commutator", validation: "not_checked" },
  title: "Integration of skewed-Poisson structures",
  cites: ["leitner2006"],
  uses: [],
  proofs: ["prf:skew-poisson-integration"],
});
