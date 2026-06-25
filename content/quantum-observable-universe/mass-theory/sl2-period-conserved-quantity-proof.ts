import { proof } from "../../schema/builders";

export default proof({
  label: "prf:sl2-period-conserved-quantity",
  title: "Proof of the depth-2 conserved first integral",
  uses: [
    "prop:sl2-period-conserved-quantity",
    "prop:sl2-prolongation-recurrence",
  ],
});
