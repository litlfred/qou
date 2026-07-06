import { proof } from "../../schema/builders";

export default proof({
  label: "prf:local-substrate-q",
  title: "Proof of Local Value of the Substrate Parameter",
  uses: ["prop:local-substrate-q", "prf:knot-volumes-verification"],
  computation: {
    engine: "snappea",
    script: "computations/knot-volumes.py",
    witness: [
      "computations/substrate/knot-volumes.witness.json",
      "computations/q-pinning-50-digit.witness.json",
    ],
    status: "verified",
    requires: ["snappy>=3.3"],
  },
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
  ],
});
