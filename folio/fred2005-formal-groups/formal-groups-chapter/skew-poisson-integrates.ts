import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:skew-poisson-integrates",
  title: "Integration theorem",
  lean: { ref: "fred2005:Fred2005.integration_commutator",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body: "Rewritten to the source, arXiv:math/0602138 Thm. 3.7. The earlier statement (a structure on $H/\\mathbb{F}_p$ integrating to $G/\\mathbb{Z}_p$ reducing to $H$ mod $p$) is not in the paper, which works over a field of characteristic $p$ throughout. Lean proves only the construction step: in $U = T/J$ the bracket becomes the commutator (`Fred2005.integration_commutator`, sorry-free, axioms `propext`, `Classical.choice`, `Quot.sound`). That $U$ is $\\mathrm{Dist}(G)$ of a formal group is cited, not formalised.",
    },
  ],
  tags: ["integration", "formal-group", "main-theorem"],
  uses: [
    "def:commutative-formal-group",
    "def:skewed-poisson-structure",
    "def:strong-multiplicativity",
    "def:non-commutative-formal-group",
  ],
  cites: ["leitner2006", "fred2005"],
});
