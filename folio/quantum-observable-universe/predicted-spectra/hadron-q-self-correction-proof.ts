import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hadron-q-self-correction",
  title: "Net signed crossing and magnitude of the self-deformation",
  uses: ["prop:hadron-q-self-correction", "prop:qou-canonical-action"],
});
