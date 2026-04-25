import { definition } from "../../schema/builders";

export default definition({
  label: "def:torsion-knot-flow",
  title: "Torsion-driven knot flow",
  tags: ["torsion", "flow", "knot", "geodesic", "categorical"],
  lean: { ref: "qou:QOU.ParticleState",
    validation: "not_checked",
  },
  uses: [
    "def:bundle-initial-conditions",
    "def:categorical-q-reeb-flow",
  ],
});
