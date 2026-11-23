import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:topological-mass-eigenspace-decomp",
  lean: { ref: "qou:QOU.LiftingDescent.tm_eigenspace_decomp_norm_le",
    validation: "not_checked",
  },
  title: "Eigenspace decomposition of the mass integrand (descent involution)",
  tags: ["descent-involution", "killing-form", "multiplicative-integral", "mass"],
  uses: [
    "def:mass-identity",
    "prop:descent-eigenspaces",
  ],
  proofs: ["prf:topological-mass-eigenspace-decomp"],
  cites: ["yekutieli2015"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "Restated from `=` to `≤` (owner-approved D3, 2026-11-20, consistent with the #8555 split of the topological mass). The statement claimed norm additivity from Killing-form orthogonality. But orthogonality gives additivity of squared norms, and for two non-zero orthogonal vectors the triangle inequality is strict (`QOU.Torsion.norm_add_lt_of_inner_eq_zero`, PR #8581). The Lean is now `QOU.LiftingDescent.tm_eigenspace_decomp_norm_le` in the content sibling: given the factorisation of the multiplicative integral, the norm is at most the sum of the two norms. It is sorry-free. The equality is open and tracked in bean qou-tmeq. Both the factorisation and the equality would need further input. The library conditional `QOU.LiftingDescent.tm_eigenspace_decomp` assumes a class field (`mi_additive`) that no inner-product norm satisfies on non-zero orthogonal pairs.",
    },
  ],
});
