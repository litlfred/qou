import { proposition } from "../../schema/builders";

/**
 * Scope-limited negative: the linking number of a particle's braid closure does
 * not fix the hypercharge sign (charge is not a function of linking; linking is
 * P-type, the open sign is C-type).
 */
export default proposition({
  label: "prop:linking-does-not-fix-charge",
  title: "The linking number does not fix the charge sign",
  uses: ["prop:chirality-sign-is-hypercharge-sign"],
  lean: {
    ref: "qou:QOU.EightfoldWay.LinkingDoesNotFixCharge.charge_not_function_of_linkSum",
  },
  tags: ["appendix", "standard-model", "chirality", "linking-number"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`LinkingDoesNotFixCharge.lean`). Scope (a): linking alone " +
        "does not fix the sign; a closure combining linking with the strand " +
        "picture is not excluded. Bean qou-h0zz.",
    },
  ],
});
