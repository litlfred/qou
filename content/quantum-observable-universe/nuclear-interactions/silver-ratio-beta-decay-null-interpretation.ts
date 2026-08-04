import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:silver-ratio-beta-decay-null",
  label: "rem:silver-ratio-beta-decay-null-interpretation",
  title: "Silver-ratio bar-symmetry, SU(2)_L connection, and the $c_5$ outlier",
  tags: [
    "silver-ratio",
    "beta-decay-null",
    "pell-lucas",
    "bar-involution",
    "c-k-closed-forms",
    "su2-weak",
  ],
  cites: ["wenzl1988", "hoefsmit1974"],
  uses: ["prop:silver-ratio-beta-decay-null", "def:bar-involution"],
});
