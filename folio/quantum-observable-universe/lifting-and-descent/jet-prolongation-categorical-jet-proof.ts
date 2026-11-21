import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jet-prolongation-categorical-jet",
  title: "Proof that $\\Omega^1(A)$ is a direct summand of $A \\otimes A$",
  uses: ["lem:jet-prolongation-categorical-jet"],
});
