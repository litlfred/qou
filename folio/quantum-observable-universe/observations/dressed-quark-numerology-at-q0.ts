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
  interprets: "prop:flavor-dressed-mass-from-aether-split",
  uses: ["thm:flavor-mass-splitting-bound", "lem:pair-skein-mass-formula", "conj:flavor-split-aether-mass"],
});
