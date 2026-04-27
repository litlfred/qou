import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-q-connection",
  label: "rem:quantum-torsion-motivation",
  title: "$\\mathrm{SU}(2)$ action as quantum torsion",
  uses: [
    "rem:q-torsion-existence",
    "def:categorical-q-connection",
    "def:quantum-gauge-group",
  ],
  tags: ["torsion", "su2", "q-deformation", "spinor"],
});
