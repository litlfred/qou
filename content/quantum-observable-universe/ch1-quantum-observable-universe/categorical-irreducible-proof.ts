import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-irreducible",
  title: "Proof of Irreducibility from observability",
  uses: ["lem:categorical-irreducible"],
});
