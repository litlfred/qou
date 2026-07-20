import { proof } from "../../schema/builders";

export default proof({
  label: "prf:binding-closure-conditional",
  title: "Proof of binding closure conditional on the per-term mass identity",
  uses: [
    "thm:binding-closure-conditional",
    "lem:bond-order-eq-jet-degree",
  ],
});
