import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cs-gram-determinant-ratio-remark",
  title: "Basis independence of the Gram-determinant ratio",
  interprets: "def:cs-gram-determinant-ratio",
  uses: [
    "def:cs-gram-determinant-ratio",
    "rem:em-coupling-chern-simons",
  ],
});
