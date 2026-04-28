import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mobius-energy-frobenius-kernel",
  title: "Proof of the classical limit of the Frobenius--Hopf kernel",
  uses: ["lem:mobius-energy-frobenius-kernel"],
});
