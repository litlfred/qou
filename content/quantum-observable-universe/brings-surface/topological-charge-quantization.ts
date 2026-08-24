import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:topological-charge-quantization",
  title: "Quantization of topological charge",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.topological_charge_quantization",
    validation: "stub",
  },
  uses: [
    "def:unit-particle-state",
    "def:rigid-dualizing-complex",
  ],
  tags: [
    "topological-charge",
    "residue",
    "quantization",
    "algebraic-residue",
  ],
  cites: ["yekutieli2015"],
});
