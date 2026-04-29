import { proof } from "../../schema/builders";

export default proof({
  label: "prf:local-substrate-q",
  title: "Proof of Local Value of the Substrate Parameter",
  uses: ["prop:local-substrate-q", "prf:knot-volumes-verification"],
  computation: {
    engine: "snappea",
    script: "folio-assistant/computations/knot-volumes.py",
    witness: [
      "folio-assistant/computations/knot-volumes.witness.json",
      "folio-assistant/computations/q-pinning-50-digit.witness.json",
    ],
    status: "verified",
    requires: ["snappy>=3.3"],
  },
});
