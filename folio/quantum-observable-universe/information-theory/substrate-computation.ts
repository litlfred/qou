import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:toffoli-transfer-matrix",
  label: "rem:aether-computation",
  renamedFrom: ["rem:substrate-computation"],
  title: "Aether-independence of computation",
  tags: [
    "computation",
    "universality",
    "planck-time",
    "combinatorics",
    "substrate-parameter",
    "classical-limit",
  ],
  uses: ["rem:toffoli-q-and"],
  cites: ["thooft2016"],
});
