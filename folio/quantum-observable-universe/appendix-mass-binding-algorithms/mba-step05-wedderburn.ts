import { algorithm } from "../../schema/builders";

export default algorithm({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization reference moved out of published prose: the $q = 1$ Frame-Robinson-Thrall hook-length formula $d_\\lambda = n!/\\prod_c h_\\lambda(c)$ is verified in `QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct`; cross-checks against `prop:hoefsmit-ew-cell-content`.",
    },
  ],
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
