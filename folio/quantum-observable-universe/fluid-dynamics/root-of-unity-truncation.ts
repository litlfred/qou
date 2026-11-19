import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:root-of-unity-truncation",
  lean: { ref: "qou:QOU.FluidDynamics.root_of_unity_truncation_conditional", validation: "not_checked" },
  title:
    "Representation-theoretic truncation at roots of unity and the $q = 1$ accumulation",
  uses: ["conj:vorticity-lower-bound", "prop:q-laplacian-spectral-tower"],
  cites: ["verlinde1988"],
  tags: [
    "root-of-unity",
    "truncation",
    "verlinde",
    "modular-tensor-category",
    "regularity",
    "accumulation-point",
    "millennium-problem",
  ],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Levi reading withdrawn by owner decision (PR #7747, bean qou-fm7s, option 1: re-scope " +
        "files still stating the withdrawn Levi branch (A); this block was missed by the earlier " +
        "scan). The boxed equivalence read \"NS blows up ⟺ Levi form stays non-degenerate at " +
        "collision ⟺ κ(t) = O(1)\"; the middle term is removed. The paragraph identifying κ(t)² " +
        "with the Levi condition number λ_max/λ_min is replaced by a withdrawal note. Old text, " +
        "verbatim: \"The explicit [Levi form condition number](#def:levi-form-defect) governing the vortex core rigidly evaluates to $\\lambda_{\\max}/\\lambda_{\\min}$, perfectly equating to $\\kappa(t)^2$. The underlying contact structure mathematically degenerates (flipping completely integrable) exactly if and only if $\\lambda_{\\min} \\to 0$, driving $\\kappa(t) \\to \\infty$. This establishes the boxed equivalence stated above.\" Reason: in dimension 3 the Levi datum is the single scalar ξ·curl ξ " +
        "(prop:core-levi-form) and branch (A) is refuted by a Beltrami solution " +
        "(conj:levi-degeneracy). The remaining equivalence NS blows up ⟺ κ(t) = O(1) is unchanged " +
        "and stays conditional on the listed conjectures. Lean: the field leviNonDegenerate is " +
        "replaced by coreBounded in both encodings.",
      see: "conj:levi-degeneracy",
    },
  ],
});
