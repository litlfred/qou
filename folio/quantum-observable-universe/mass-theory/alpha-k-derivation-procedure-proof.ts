import { proof } from "../../schema/builders";

export default proof({
  label: "prf:alpha-k-derivation-procedure",
  title: "Proof of alpha k derivation procedure",
  uses: ["prop:alpha-k-derivation-procedure"],
  computation: {
    engine: "mpmath",
    script: "computations/cross_check_trM_1ppb.py",
    witness: "computations/cross-check-trM-1ppb.witness.json",
    status: "verified",
  },
});
