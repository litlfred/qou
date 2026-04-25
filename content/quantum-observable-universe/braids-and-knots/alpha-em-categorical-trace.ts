import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:alpha-em-categorical-trace",
  title: "$1/\\alpha_{EM} = 45 \\cdot [3]_q \\cdot (1 + \\delta_{CS} + 8q \\cdot \\delta_{CS}^2)$ as the unique categorical trace pairing (Yekutieli rigidity)",
  lean: {
    ref: "qou:QOU.WedderburnMass.alpha_em_categorical_trace",
    validation: "not_checked",
  },
  uses: [
    "prop:exterior-square-borromean",
    "prop:curvature-rank-delta-cs",
    "prop:gluon-octet-substrate-coupling",
    "prop:vol-through-tau",
    "prop:confinement-categorical",
    "prop:categorical-mass-markov",
    "prop:curvature-rank-gb-stratification",
    "prop:gb-residue-spectral-sum",
    "prop:three-parameters-wedderburn",
  ],
});
