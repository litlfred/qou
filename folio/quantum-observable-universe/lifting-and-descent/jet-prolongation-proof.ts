import { proof } from "../../schema/builders";

export default proof({
  label: "prf:jet-prolongation",
  title: "Proof of Jet Prolongation",
  uses: [
    "prop:jet-prolongation",
    "lem:jet-prolongation-categorical-jet",
  ],
});
