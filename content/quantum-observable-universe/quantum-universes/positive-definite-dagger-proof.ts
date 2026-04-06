import { proof } from "../../schema/builders";

export default proof({
  label: "prf:positive-definite-dagger",
  title: "Proof that the Frobenius dagger is positive-definite",
  uses: ["prop:positive-definite-dagger"],
});
