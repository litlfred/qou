import { proof } from "../../schema/builders";

export default proof({
  label: "prf:brings-euler-characteristic",
  title: "Proof of the Euler-characteristic computation",
  uses: ["lem:brings-euler-characteristic"],
});
