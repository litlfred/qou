import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:witness-completeness",
  title: "Witness completeness: the exterior degree-$\\geq 1$ record determines the trapped degree-$0$ data",
  lean: { ref: "qou:QOU.Information.WitnessCompleteness", validation: "stub" },
  tags: [
    "jet-horizon",
    "information-paradox",
    "black-hole-complementarity",
    "unitarity",
    "godel-incompleteness",
    "hawking-radiation",
  ],
  uses: [
    "def:jet-horizon",
    "rem:hawking-radiation",
    "rem:information-paradox-incompleteness",
  ],
  cites: ["susskind1993", "harlowhayden2013", "marolf2017"],
});
