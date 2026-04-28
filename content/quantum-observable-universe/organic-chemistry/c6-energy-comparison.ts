import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:c6-energy-comparison",
  title:
    "Linear C${}_{6}$ chain vs. benzene ring energy difference",
  tags: [
    "carbon-chain",
    "benzene",
    "energy-comparison",
    "ring-favoured",
    "alexander-polynomial",
    "smoking-gun",
  ],
  lean: { ref: "qou:QOU.Organic.c6EnergyComparison",
    validation: "not_checked",
  },
  uses: [
    "lem:alexander-T2N-closed-form",
    "prop:molecular-crossing-quantum",
    "prop:threading-half-weight",
  ],
  cites: [],
});
