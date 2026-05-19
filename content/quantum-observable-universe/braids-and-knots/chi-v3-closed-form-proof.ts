import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chi-v3-closed-form-proof",
  interprets: "rem:post-pr665-open-rd-inventory",
  title:
    "Formal proof of the V_(3) per-irrep character difference closed form: $\\chi_{(3)}(\\beta_n) - \\chi_{(3)}(\\beta_p) = -(q^2 + 1)^2 (q^2 - 1)/(4q) = -(q^5 + q^3 - q - q^{-1})/4$, with explicit $\\varepsilon^k$ pattern via polynomial + geometric decomposition",
  uses: [
    "rem:post-pr665-open-rd-inventory",
    "rem:typed-b3-sub-braid-extraction",
    "prop:hoefsmit-V21-cos-symmetrization",
  ],
  cites: [
    "jones1985",
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "lean-infrastructure",
    "v3-symmetric-irrep",
    "per-wedderburn-block",
    "closed-form",
    "epsilon-expansion",
    "geometric-series",
  ],
  computation: {
    engine: "sympy",
    script: "folio-assistant/computations/probe_per_wedderburn_block_ck.py",
    witness: [
      "folio-assistant/computations/per-wedderburn-block-ck.witness.json",
    ],
    status: "experimental",
  },
});
