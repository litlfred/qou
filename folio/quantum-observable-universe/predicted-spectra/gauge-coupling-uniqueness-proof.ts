import { proof } from "../../schema/builders";

export default proof({
  label: "prf:gauge-coupling-uniqueness",
  title: "Proof of gauge coupling uniqueness",
  uses: ["cor:gauge-coupling-uniqueness"],
});
