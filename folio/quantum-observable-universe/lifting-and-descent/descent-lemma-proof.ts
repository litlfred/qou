import { proof } from "../../schema/builders";

export default proof({
  label: "prf:descent",
  title: "Proof of Descent along the brane tower",
  uses: ["lem:descent", "prop:jet-prolongation"],
});
