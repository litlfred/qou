import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:local-substrate-q",
  title: "Local Value of the Substrate Parameter",
  uses: ["def:substrate-parameter", "prop:skein-mass-relation", "prop:terminal-resolution", "rem:photonic-hall"],
  hasProof: true,
  tags: ["substrate", "mass", "observation"],
});
