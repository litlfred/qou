import { proof } from "../../schema/builders";

export default proof({
  label: "prf:feynman-trace-collapse",
  title: "Proof that the path integral collapses on the eigenbasis",
  uses: ["lem:feynman-trace-collapse"],
});
