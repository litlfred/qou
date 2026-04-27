import { proposition } from "../../schema/builders";

/**
 * Each atom's construction produces a verified NF element.
 */
export default proposition({
  label: "prop:atomic-nf-witness",
  title: "Atomic braid normal form witness",
  uses: ["def:atomic-braid"],
});
