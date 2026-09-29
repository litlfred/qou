import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "caveat", date: "2026-08-29", body: "Both axioms this file's Lean sibling once carried proved `False`. `explicit_formula_axiom` quantified over `ideals` and `spectrum` INDEPENDENTLY, so it asserted the identity for unrelated data; `qLog_tendsto_log_axiom` claimed `log x / log q` tends to `log x` as `q -> 1`, when it diverges. Both are now withdrawn and replaced by theorems: `not_qExplicitFormula_empty` and `not_qLog_tendsto_log` are the proved refutations, `qLog_mul_log` the true renormalisation identity, and the formula itself is the no-instance conjecture class `QExplicitFormula` over a bundled `QZetaDatum`. The file has zero live axioms and zero sorries. Bean `qou-qexf`." },
    { kind: "note", date: "2026-08-30", body: "DEMOTED. This block was kind `theorem` while its content is an unproved conjecture of the framework, and its Lean is a projection of a no-instance class (degenerate under 3b-cond item 5). It is now `conjecture` with label `conj:explicit-formula`. The rename was the reason for the earlier deferral: it touches the citations in `rem:yekutieli-quantum-li` and `rem:unitary-stability` and the generated definition index, all of which were updated with it. Both consumers are remarks, so no provable-kind block became downstream-of-conjecture — cascade zero." },
  ],
  label: "conj:explicit-formula",
  title: "Explicit formula as a spectral--geometric trace identity",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.explicit_formula",
    validation: "not_checked",
  },
  uses: [
    "def:q-chebyshev-function",
    "conj:tannaka-krein-isomorphism",
  ],
  tags: [
    "explicit-formula",
    "trace-formula",
    "fourier-transform",
    "spectral-geometric",
  ],
  // rosen2002/weil1948 are cited for the CLASSICAL explicit formula over a
  // finite field, which is theirs; the q-deformation stated here is not.
  cites: ["rosen2002", "weil1948", "reshetikhin1991"],
});
