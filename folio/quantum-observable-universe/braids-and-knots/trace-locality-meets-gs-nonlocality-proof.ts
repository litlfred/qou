import { proof } from "../../schema/builders";

export default proof({
  label: "prf:trace-locality-meets-gs-non-locality",
  title:
    "Proof of the locality / non-locality reconciliation",
  uses: ["prop:trace-locality-meets-gs-non-locality"],
});
