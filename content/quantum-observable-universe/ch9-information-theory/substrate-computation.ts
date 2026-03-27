import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:toffoli-transfer-matrix",
  label: "rem:substrate-computation",
  title: "Why computers can be built from anything",
  tags: [
    "computation",
    "universality",
    "planck-time",
    "combinatorics",
    "substrate-parameter",
    "classical-limit",
  ],
  uses: [
    "prop:toffoli-transfer-matrix",
    "rem:toffoli-q-and",
    "rem:discrete-planck-step",
    "def:substrate-parameter",
  ],
});
