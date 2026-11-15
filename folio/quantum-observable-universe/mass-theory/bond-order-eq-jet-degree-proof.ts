import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bond-order-eq-jet-degree",
  title: "Proof that body order equals jet degree",
  uses: [
    "lem:bond-order-eq-jet-degree",
    "prop:gb-spectral-sequence",
  ],
});
