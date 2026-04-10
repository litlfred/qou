import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:feynman-categorical-trace",
  label: "rem:feynman-qou-dictionary",
  title: "Dictionary: Feynman path integral $\\leftrightarrow$ QOU categorical trace",
  tags: ["path-integral", "feynman", "dictionary", "categorical-trace"],
  uses: [
    "prop:feynman-categorical-trace",
    "def:categorical-transfer-matrix",
    "def:q-energy",
    "rem:r-matrix-braiding",
  ],
});
