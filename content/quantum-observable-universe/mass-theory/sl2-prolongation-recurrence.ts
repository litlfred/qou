import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sl2-prolongation-recurrence",
  lean: {
    ref: "qou:QOU.Mass.sl2_prolongation_recurrence",
    validation: "validated",
  },
  title: "Symplectic prolongation (det B = 1) gives a one-parameter recurrence",
  uses: [
    "prop:prolonged-periods-fixed-depth",
  ],
  proofs: ["prf:sl2-prolongation-recurrence"],
});
