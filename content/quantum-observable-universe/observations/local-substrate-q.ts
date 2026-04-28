import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:local-substrate-q",
  lean: { ref: "qou:QOU.Experimental.local_substrate_q",
    validation: "not_checked",
  },
  title: "Local Value of the Substrate Parameter",
  uses: [
    "prop:terminal-resolution",
    "rem:photonic-hall",
  ],
  examples: [
    "rem:mass-from-generators",
    "rem:knot-formula-table",
    "rem:mass-comparison-table",
    "rem:w-boson-mass-discrepancy",
  ],
  proofs: ["prf:local-substrate-q"],
  tags: ["substrate", "mass", "observation"],
});
