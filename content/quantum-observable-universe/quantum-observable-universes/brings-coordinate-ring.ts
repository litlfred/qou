import { definition } from "../../schema/builders";

export default definition({
  label: "def:brings-coordinate-ring",
  title: "Non-commutative coordinate ring of Bring's curve",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.BringsCoordinateRing",
    validation: "not_checked",
  },
  uses: ["def:frobenius-hopf-substrate"],
  defines: ["brings-coordinate-ring"],
  tags: ["brings-curve", "coordinate-ring", "genus-4", "S5-symmetry"],
});
