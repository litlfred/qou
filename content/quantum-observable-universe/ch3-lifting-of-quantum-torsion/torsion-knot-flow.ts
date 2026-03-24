import { definition } from "../../schema/builders";

export default definition({
  label: "def:torsion-knot-flow",
  title: "Torsion-driven knot flow",
  tags: ["torsion", "flow", "knot", "geodesic", "categorical"],
  lean: {
    decl: "QOU.ParticleState",
    validation: "not_checked",
  },
  uses: [
    "def:bundle-initial-conditions",
    "def:localized-knot",
    "def:projective-line-object",
    "def:categorical-q-reeb-flow",
  ],
});
