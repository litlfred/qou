import { proposition } from "../../schema/builders";

/**
 * LP dual for H2O: selects 2 shared pairs + 2 lone pairs on O,
 * with bent strand ordering (H1 and H2 on opposite sides of O).
 */
export default proposition({
  label: "prop:h2o-lp-dual-binding",
  title:
    "LP dual selects two single O–H bonds with two lone pairs on $O$ as optimal for $\\mathrm{H}_2\\mathrm{O}$",
  uses: [
    "def:h2o-molecular-braid",
    "prop:h2-lp-dual-binding",
    "prop:co-lp-dual-binding",
  ],
  tags: [
    "H2O",
    "water",
    "LP-dual",
    "single-bond",
    "lone-pair",
    "optimal",
  ],
});
