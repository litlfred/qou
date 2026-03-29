import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:cmb-q-torsion",
  title: "CMB non-uniformity from $q$-torsion",
  uses: ["ex:q-torsion-leaf"],
  tags: ["cmb", "torsion", "observation"],
});
