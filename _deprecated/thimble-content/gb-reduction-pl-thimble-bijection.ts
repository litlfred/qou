import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gb-reduction-pl-thimble-bijection",
  title:
    "GB normal-form reduction maps bijectively to PL steepest-descent thimble flow",
  lean: {
    ref: "qou:QOU.PicardLefschetz.gb_reduction_pl_thimble_bijection",
    validation: "not_checked",
  },
  uses: [
    "prop:jet-gb-pl-correspondence",
    "rem:picard-lefschetz-thimble",
    "prop:sw-period-thimble-equivalence",
    "def:q-pochhammer-partial-product",
    "conj:denominator-zeros-as-sw-critical-points",
  ],
  cites: [
    "kashaev1997",
    "neumann-zagier1985",
    "thurston1978",
    "witten2011",
    "yekutieli2015",
  ],
  tags: [
    "picard-lefschetz",
    "groebner-shirshov",
    "thimble",
    "steepest-descent",
    "filtration",
    "open-problem",
  ],
});
