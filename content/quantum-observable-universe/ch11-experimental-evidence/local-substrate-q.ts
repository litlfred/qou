import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:local-substrate-q",
  lean: {
    decl: "QOU.Experimental.local_substrate_q",
    validation: "not_checked",
  },
  title: "Local Value of the Substrate Parameter",
  uses: ["def:substrate-parameter", "rem:skein-mass-relation", "prop:terminal-resolution", "rem:photonic-hall"],
  proofs: ["prf:local-substrate-q"],
  tags: ["substrate", "mass", "observation"],
});
