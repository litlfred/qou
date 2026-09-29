import { proof } from "../../schema/builders";

export default proof({
  label: "prf:feynman-eigenbasis-decomposition",
  title: "Proof of eigenbasis decomposition for the Feynman amplitude",
  uses: ["lem:feynman-eigenbasis-decomposition"],
});
