import { remark } from "../../schema/builders";

export default remark({
  label: "rem:double-slit-q-phase-remark",
  title: "Geometric and Reeb parts of the double-slit phase",
  interprets: "def:double-slit-q-phase",
  tags: ["definition-commentary"],
  uses: [
    "def:double-slit-q-phase",
    "def:categorical-q-ext-deriv",
  ],
});
