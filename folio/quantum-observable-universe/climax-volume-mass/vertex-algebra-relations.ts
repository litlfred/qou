import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"**Perpetual obstruction** (C-5a): When $\\chi(A) = -6$,\n\n$$\n  \\kappa_n  \\neq  0\n  \\qquad \\forall n \\geq 0.\n$$\n\nIn Hecke generators: at every brane level, there exist braid words $\\beta_{n+1} \\in H_{n+1}(q)$ that cannot be expressed as $L_{-1}(\\mathcal{B}_n)$ for any $\\mathcal{B}_n \\in H_n(R, q)$. The jet corrections and the base obstruction occupy complementary subgroups; cancellation is impossible.\"",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
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
