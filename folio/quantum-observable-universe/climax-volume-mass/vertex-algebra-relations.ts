import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "QUO-3a withdrawn (owner decision, PR #8005, bean qou-078y). It read $\\sum_{i=1}^{n-1} \\mathrm{tr}_M(\\sigma_i - \\sigma_i^{-1}) = 0$, glossed as $c_1(\\mathrm{Ad}(A)) = 0$, with Lean sibling `axiom first_chern_vanishes`. The Hecke relation gives $\\sigma_i^{-1} = \\sigma_i - (q - q^{-1})$, so the left side is $(n-1)(q - q^{-1})\\mathrm{tr}_M(1)$, nonzero for $q^2 \\neq 1$. The axiom is replaced by the proved `trace_sub_trace_inv` / `trace_ne_trace_inv`. The relation count goes from 26 to 25. The line defining $\\mathrm{wr}(a)$ as a trace sum is replaced by the abelianisation writhe. A $c_1$ functional on $\\mathrm{Ad}(A)$ is an open research item.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"**Perpetual obstruction** (C-5a): When $\\chi(A) = -6$,\n\n$$\n  \\kappa_n  \\neq  0\n  \\qquad \\forall n \\geq 0.\n$$\n\nIn Hecke generators: at every brane level, there exist braid words $\\beta_{n+1} \\in H_{n+1}(q)$ that cannot be expressed as $L_{-1}(\\mathcal{B}_n)$ for any $\\mathcal{B}_n \\in H_n(R, q)$. The jet corrections and the base obstruction occupy complementary subgroups; cancellation is impossible.\"",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data. Gram matrix degeneracy on $H_3$ (`det G = 0`, radical = $(1^3)$ block) is formalised in `QOU/QBeta/MarkovGramDegenerate.lean`." },
  ],
  label: "prop:vertex-algebra-relations",
  lean: { ref: "qou:QOU.VertexAlgebra.descartes_genus",
    validation: "not_checked",
  },
  title: "QU and QUO axioms as relations on Hecke generators",
  tags: [
    "vertex-operator", "hecke-algebra", "knot-coordinates",
    "quantum-universe", "relations", "generators",
  ],
  uses: [
    "prop:frobenius-relation",
    "prop:categorical-dq-squared",
    "rem:hodge-laplacian-relation",
    "prop:cohomological-embedding",
    "rem:instanton-on-shell",
  ],
  cites: ["kassel1995", "jones1987", "yekutieli2010"],
});
