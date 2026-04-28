import { proposition } from "../../schema/builders";

/**
 * LP stability criterion for atoms.
 */
export default proposition({
  label: "prop:atomic-lp-stability",
  title: "LP stability of the atomic braid",
  uses: ["def:atomic-braid"],
});
