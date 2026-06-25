import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:sl2-period-conserved-quantity",
  lean: {
    ref: "qou:QOU.Mass.sl2Invariant_eq_zeroth",
    validation: "validated",
  },
  title: "The depth-2 prolongation recurrence has a conserved first integral",
  uses: [
    "prop:sl2-prolongation-recurrence",
    "prop:sw-period-residue-sum",
    "prop:binding-genfun-qdifference",
  ],
  proofs: ["prf:sl2-period-conserved-quantity"],
});
