import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-q-connection",
  label: "rem:q-torsion-leaf-minimum",
  title: "q-Torsion leaves as energy minima",
  tags: ["q-deformation", "torsion", "curvature"],
  uses: [
    "def:categorical-q-connection",
    "ex:q-torsion-leaf",
  ],
});
