import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:q-hecke-seminormal-character-closure",
  label: "rem:recomputed-low-isotope-mass-table-path-a-shift-verification",
  title:
    "Path A categorical verification of the per-proton shift coefficient $18$",
  uses: [
    "prop:q-hecke-seminormal-character-closure",
    "prop:per-nucleon-shift-additive-linearity",
  ],
  cites: ["wenzl1988", "hoefsmit1974"],
  tags: [
    "shift-exponent",
    "pole-order",
    "hoefsmit",
    "per-nucleon-shift",
  ],
});
