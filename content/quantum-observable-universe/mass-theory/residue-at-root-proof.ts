import { proof } from "../../schema/builders";

export default proof({
  label: "prf:residue-at-root",
  title: "Proof of residue at root",
  uses: ["prop:residue-at-root"],
});
