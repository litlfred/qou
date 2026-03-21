import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-torsion-leaf-minimum",
  title: "q-Torsion leaves as energy minima",
  tags: ["q-deformation", "torsion", "curvature"],
  uses: [
    "def:q-connection",
    "def:q-lie-bracket",
    "def:q-torsion-leaf",
  ],
});
