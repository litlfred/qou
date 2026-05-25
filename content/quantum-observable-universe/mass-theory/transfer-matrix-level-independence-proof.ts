import { proof } from "../../schema/builders";

export default proof({
  label: "prf:transfer-matrix-level-independence",
  of: "prop:transfer-matrix-level-independence",
  uses: ["lem:tmli-constituent-composite-agreement"],
});
