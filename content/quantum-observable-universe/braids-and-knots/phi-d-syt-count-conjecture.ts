import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-d-syt-count-conjecture",
  interprets: "rem:chi-per-irrep-cyclotomic-closed-forms",
  title:
    "Conjecture: per-irrep character differences factor via $\\Phi_{4 f_\\lambda}(q)$, where $f_\\lambda$ is the SYT count — verified at $n=3$ for $V_{(3)}, V_{(2,1)}, V_{(1,1,1)}$; predicts cyclotomic structure at all $n$",
  uses: [
    "rem:chi-per-irrep-cyclotomic-closed-forms",
    "rem:chi-v3-closed-form-proof",
    "rem:post-pr665-open-rd-inventory",
  ],
  cites: [
    "jones1985",
    "wenzl1988",
    "hoefsmit1974",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "conjecture",
    "cyclotomic",
    "syt-count",
    "per-wedderburn-block",
    "generalization",
  ],
});
