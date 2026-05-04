import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:denominator-zeros-as-sw-critical-points",
  title:
    "$q$-Pochhammer denominator zeros equal SW critical points of the color-tube cubic",
  lean: {
    ref: "qou:QOU.PicardLefschetz.denominator_zeros_eq_sw_critical_points",
    validation: "not_checked",
  },
  uses: [
    "def:q-pochhammer-partial-product",
    "conj:shared-denominator-cusp-holonomy",
    "def:picard-lefschetz-thimble",
    "rem:color-tube-cubic",
    "prop:sw-period-thimble-equivalence",
    "prop:jet-gb-pl-correspondence",
  ],
  cites: [
    "kashaev1997",
    "neumann-zagier1985",
    "thurston1978",
    "witten2011",
  ],
  tags: [
    "picard-lefschetz",
    "seiberg-witten",
    "q-pochhammer",
    "critical-points",
    "discriminant",
    "open-problem",
  ],
});
