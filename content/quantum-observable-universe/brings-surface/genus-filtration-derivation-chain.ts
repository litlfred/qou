import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:genus-filtration-ideal",
  label: "rem:genus-filtration-derivation-chain",
  title:
    "The non-circular derivation chain: Hecke completeness forces $g = 4$ and identifies the Bring surface",
  tags: [
    "derivation-chain",
    "genus",
    "hecke-completeness",
    "brings-surface",
    "non-circular",
  ],
  uses: ["prop:genus-filtration-ideal"],
  cites: ["yekutieli2010"],
});
