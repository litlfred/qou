import { proposition } from "../../schema/builders";

/**
 * The traceless strand charges (S5 standard rep) twisted by sign equal Bring's
 * holomorphic differentials H0(K) = [2,1,1,1]; dimension 4 forces five strands.
 */
export default proposition({
  label: "prop:strand-charges-are-holomorphic-differentials",
  title: "Strand charges are Bring's holomorphic differentials up to sign",
  uses: ["prop:strand-count-from-bring", "prop:bring-harmonic-types"],
  lean: {
    ref: "qou:QOU.StandardModel.StrandDifferentials.h0K_is_signed_strand_charges",
  },
  tags: ["appendix", "standard-model", "brings-surface"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`StrandChargesAreHolomorphicDifferentials.lean`), reusing " +
        "`hopf_trace_h1` and `h0K_character_forced` from main (PR #9855). Shows the two " +
        "S5 modules agree up to the sign character; does not prove that strand " +
        "relabellings are Bring's automorphisms, nor that the sign twist is the open " +
        "hypercharge sign. Bean qou-h0zz.",
    },
  ],
});
