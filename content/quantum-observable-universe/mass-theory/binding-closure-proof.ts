import { proof } from "../../schema/builders";

export default proof({
  label: "prf:binding-closure",
  title: "Proof of binding closure conditional on the per-term mass identity",
  uses: [
    "thm:binding-closure",
    "lem:bond-order-eq-jet-degree",
  ],
});
