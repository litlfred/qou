import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wedderburn-weight-canonical",
  title:
    "Canonical q-deformed Wedderburn-block weight $\\tilde w_\\lambda$ and named scalings (BW, LP for all $\\lambda$; Wenzl-bridge on the self-conjugate stratum)",
  tags: [
    "wedderburn",
    "weight",
    "canonical",
    "bw",
    "shadow-price",
    "wenzl-bridge",
    "self-conjugate",
    "consolidation",
  ],
  uses: [
    "prop:wedderburn-as-noncomm-fourier",
    "prop:plancherel-weight-boundedness",
  ],
  cites: ["jones1985", "wenzl1988", "kassel1995", "halverson-1998-markov-weights"],
  computation: {
    engine: "python",
    script:
      "computations/_deprecated/bw_wenzl_shadow_equivalence.py",
    witness: "docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json",
    status: "verified",
  },
  lean: { ref: "qou:QOU.BraidKnot.wedderburnWeightCanonical" },
});
