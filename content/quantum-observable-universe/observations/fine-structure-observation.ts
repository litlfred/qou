import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fine-structure-observation",
  title: "Fine structure constant: CODATA comparison",
  interprets: "prop:em-coupling-projection",
  tags: [
    "fine-structure-constant",
    "electromagnetic",
    "CODATA",
    "observation",
    "coupling",
    "q-integer",
  ],
  uses: [
    "prop:em-coupling-projection",
    "sec:mass-predictions-data",
    "rem:half-life-as-q-probe",
    "rem:mass-comparison-table",
  ],
});
