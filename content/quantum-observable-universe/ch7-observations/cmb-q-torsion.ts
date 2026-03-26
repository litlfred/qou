import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cmb-q-torsion",
  title: "CMB non-uniformity from $q$-torsion",
  uses: ["ex:q-torsion-leaf", "ex:q-reeb-flow"],
  tags: ["cmb", "torsion", "observation"],
});
