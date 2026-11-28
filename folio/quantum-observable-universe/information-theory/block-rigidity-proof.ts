import { proof } from "../../schema/builders";

export default proof({
  label: "prf:block-rigidity",
  title: "Proof that derivations and automorphisms respect the blocks",
  uses: ["prop:block-rigidity"],
});
