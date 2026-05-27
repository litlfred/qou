import { remark } from "../../schema/builders";

export default remark({
  label: "rem:per-wedderburn-block-c5-c6",
  interprets: "rem:multi-link-jones-q1-extension",
  title:
    "Per-Wedderburn-block $c_5/c_6$ scaffolding: weighted-sum hypothesis that the empirical $c_5 \\approx -395$, $c_6 \\approx -45485$ arise from a $\\dim_q^2$-weighted sum over the three $H_3$ irreps $V_{(3)}, V_{(2,1)}, V_{(1^3)}$",
  uses: [
    "rem:multi-link-jones-q1-extension",
    "rem:h3-hecke-idempotents",
    "prop:q-beta-categorical-precision-ladder",
  ],
  cites: [
    "wenzl1988",
    "jones1985",
    "macdonald1995",
  ],
  tags: [
    "lean-infrastructure",
    "per-wedderburn-block",
    "c5-c6-investigation",
    "open-rd",
    "scaffolding",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_q_beta_c5_c6_multilink.py",
    witness: [
      "folio-assistant/computations/q-beta-c5-c6-multilink.witness.json",
    ],
    status: "experimental",
  },
});
