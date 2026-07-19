import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:binding-closure",
  lean: {
    ref: "qou:QOU.Mass.binding_closure_conditional",
    validation: "validated",
  },
  title: "Binding closure, conditional on the per-term mass identity",
  uses: [
    "thm:binding-manybody-eq-jet-filtration",
    "lem:bond-order-eq-jet-degree",
    "prop:sw-period-residue-sum",
    "prop:binding-genfun-qdifference",
  ],
  proofs: ["prf:binding-closure"],
});
