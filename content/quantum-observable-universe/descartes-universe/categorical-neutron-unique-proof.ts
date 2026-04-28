import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-neutron-unique",
  title: "Proof of uniqueness of the categorical neutron",
  uses: ["prop:categorical-neutron-unique"],
});
