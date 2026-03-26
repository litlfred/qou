import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hadron-half-life-regimes",
  title: "Half-life regimes and the $q$-landscape",
  tags: [
    "half-life",
    "beta-decay",
    "substrate-parameter",
    "limiting-behaviour",
    "drip-line",
  ],
  uses: [
    "prop:hadron-half-life",
    "prop:beta-stability",
    "def:substrate-parameter",
  ],
});
