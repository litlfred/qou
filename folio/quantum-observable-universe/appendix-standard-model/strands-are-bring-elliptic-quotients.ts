import { proposition } from "../../schema/builders";

/**
 * Strand i matches the A4 point stabiliser of Aut(Bring) and spans the A4-invariant line
 * of H0(K): each strand is the differential of an elliptic quotient B/A4.
 */
export default proposition({
  label: "prop:strands-are-bring-elliptic-quotients",
  title: "Each strand is an elliptic quotient of Bring's surface",
  uses: ["prop:strand-charges-are-holomorphic-differentials", "prop:bring-harmonic-types"],
  lean: {
    ref: "qou:QOU.StandardModel.StrandQuotients.alt0_invariants",
  },
  tags: ["appendix", "standard-model", "brings-surface"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`StrandsAreBringEllipticQuotients.lean`). Proves the equivariant " +
        "matching of strands with the five A4 subgroups and of invariant lines in H0(K). " +
        "Chevalley-Weil is cited; uniqueness of the 5-point S5-set is proved in " +
        "prop:index-five-subgroups-are-point-stabilisers. That " +
        "the physical strands are these quotients remains the modelling identification. " +
        "Bean qou-h0zz.",
    },
  ],
});
