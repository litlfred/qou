import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cmb-q-torsion",
  title: "CMB non-uniformity from $q$-torsion",
  uses: ["def:q-torsion-leaf", "def:q-reeb-flow"],
  tags: ["cmb", "torsion", "observation"],
});
