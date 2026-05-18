import { remark } from "../../schema/builders";

export default remark({
  label: "rem:dressed-quark-numerology-at-q0",
  title: "Dressed-quark numerology at $q_0$",
  tags: [
    "flavor",
    "dressing",
    "quark-mass",
    "numerology",
    "q0",
  ],
  interprets: "prop:flavor-dressed-mass-from-substrate-split",
  uses: [
    "prop:flavor-dressed-mass-from-substrate-split",
    "thm:flavor-mass-splitting-bound",
  ],
});
