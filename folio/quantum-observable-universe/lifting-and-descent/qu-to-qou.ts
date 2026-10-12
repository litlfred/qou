import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qu-to-qou",
  lean: { ref: "qou:QOU.Torsion.YekutieliTriple.qu_to_qou", validation: "not_checked" },
  title: "Quantum universe with observability and categorical lifting is a QOU",
  tags: ["main-theorem", "qou", "yekutieli", "descent"],
  examples: ["ex:qu-to-qou-su2"],
  uses: [
    "prop:yekutieli-lifting",
    "prop:fiber-adjoint-involution",
  ],
  proofs: ["prf:qu-to-qou"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-12",
      body: "Items 2 and 3 depend on the band B, which is not constructed anywhere in the corpus (six incompatible readings). For the archimedean band O^x on a closed surface, H^2(S, O^x) = 0: item 2 fails there (kappa_0 = 0 but e = -6 on Bring), and item 3 is vacuous (its non-torsion hypothesis is never met). Both are coherent only for a band whose H^2 contains the integral Euler class (e.g. Z). Items 1, 4 and 5 do not use the obstruction group. Scope note added to prf:qu-to-qou; open work in beans qou-lx8f, qou-2a2o, qou-n2aa.",
      see: "prf:qu-to-qou",
    },
  ],
});
