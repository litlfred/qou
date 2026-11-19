import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:motivic-substrate",
  label: "rem:motivic-substrate-remark",
  title: "The motivic substrate as the common source of the two substrates",
  uses: ["def:motivic-substrate", "def:frobenius-hopf-substrate", "def:adelic-substrate", "prop:full-pole-structure-mass-trace"],
});
