import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jet-prolongation-categorical-jet",
  title: "Proof that $J^1(A)$ inherits the Frobenius--Hopf structure",
  uses: ["lem:jet-prolongation-categorical-jet"],
  cites: ["leitner2006"],
});
