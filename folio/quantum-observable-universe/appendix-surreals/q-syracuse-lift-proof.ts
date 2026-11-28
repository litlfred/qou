import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-syracuse-lift",
  title: "Proof of Syracuse projection and parity-periodicity lifting",
  uses: ["prop:q-syracuse-lift", "prop:balanced-holonomy-exclusion"],
});
