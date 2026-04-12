import { proposition, remark } from "../../schema/builders";

/**
 * Each atom's construction produces a verified NF element.
 */
export const atomicNfWitness = proposition({
  label: "prop:atomic-nf-witness",
  title: "Atomic braid normal form witness",
  uses: ["def:atomic-braid", "nuclear-groebner-reduction"],
});

/**
 * Step-by-step LP stability verification for each atom.
 */
export const stepLpVerification = remark({
  label: "rem:step-lp-verification",
  title: "Step-by-step LP stability verification",
  interprets: "prop:atomic-lp-stability",
});
