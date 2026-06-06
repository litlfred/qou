import { proof } from "../../schema/builders";

export default proof({
  label: "prf:sl2-prolongation-recurrence",
  title: "Proof of the symplectic one-parameter recurrence",
  uses: [
    "prop:sl2-prolongation-recurrence",
    "prop:prolonged-periods-fixed-depth",
  ],
});
