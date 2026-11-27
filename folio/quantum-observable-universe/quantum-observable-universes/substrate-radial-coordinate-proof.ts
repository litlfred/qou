import { proof } from "../../schema/builders";

export default proof({
  label: "prf:aether-radial-coordinate",
  renamedFrom: ["prf:substrate-radial-coordinate"],
  title: "Proof of aether radial coordinate",
  uses: ["prop:aether-radial-coordinate"],
});
