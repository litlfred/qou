import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-heat-equation-unique",
  title: "Proof of uniqueness of $q$-heat equation solutions",
  uses: ["prop:q-heat-equation-unique"],
});
