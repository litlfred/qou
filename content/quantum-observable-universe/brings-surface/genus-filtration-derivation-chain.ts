import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:genus-filtration-ideal",
  label: "rem:genus-filtration-derivation-chain",
  title:
    "Non-circular derivation chain: Bring's surface as a consequence of $H_n(q)$",
  tags: [
    "derivation-chain",
    "brings-surface",
    "genus",
    "hecke",
  ],
  uses: ["prop:genus-filtration-ideal"],
});
