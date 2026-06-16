import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:wedderburn-decomposition",
  title: "Wedderburn decomposition $H_n(q) \\cong \\bigoplus_\\lambda M_{d_\\lambda}(R)$",
  uses: [
    "prop:wedderburn-trace-identity",
    "prop:wenzl-bridge-applicability-qou",
    "prop:wedderburn-as-noncomm-fourier",
  ],
  computation: {
    engine: "python",
    script: "tools/pyhecke/python/pyhecke/wedderburn.py",
    witness: "computations/wedderburn-lp-ew-wiring.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-5",
    "wedderburn",
    "wenzl",
    "partitions",
    "canonical-chain",
  ],
});
