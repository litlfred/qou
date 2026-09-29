import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-genfun-qdifference",
  lean: {
    ref: "qou:QOU.Mass.binding_qdifference_recurrence",
    validation: "validated",
  },
  title: "The binding generating function's q-difference equation gives a depth-d recurrence",
  uses: [
    "conj:binding-manybody-eq-jet-filtration",
    "prop:sw-period-residue-sum",
  ],
  proofs: ["prf:binding-genfun-qdifference"],
});
