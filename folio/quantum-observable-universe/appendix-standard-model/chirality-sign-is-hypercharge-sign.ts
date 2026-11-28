import { proposition } from "../../schema/builders";

/**
 * Merges the two open signs (even vs odd matter part, alpha = +1/6 vs -1/6) into
 * one, and shows colour and electric charge cannot see it while hypercharge can.
 */
export default proposition({
  label: "prop:chirality-sign-is-hypercharge-sign",
  title: "The chirality sign is the hypercharge sign",
  uses: ["prop:even-strand-generation", "prop:neutral-lepton-fixes-charges"],
  lean: {
    ref: "qou:QOU.EightfoldWay.ChiralitySignIsHyperchargeSign.even_neg_alpha_eq_odd",
  },
  tags: ["appendix", "standard-model", "chirality", "hypercharge"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`ChiralitySignIsHyperchargeSign.lean`). Consolidates two " +
        "signs into one; the remaining sign is not derived. Bean qou-h0zz.",
    },
  ],
});
