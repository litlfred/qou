import { proposition } from "../../schema/builders";

/**
 * LP dual binding for CO: optimal triple bond.
 */
export default proposition({
  label: "prop:co-lp-dual-binding",
  lean: { ref: "qou:QOU.Molecular.co_lp_dual_binding", validation: "not_started" },
  title: "LP dual selects the triple bond as optimal for $CO$",
  uses: [
    "def:co-molecular-braid",
    "prop:h2-lp-dual-binding",
  ],
  tags: ["CO", "LP-dual", "triple-bond", "optimal"],
});
