import { remark } from "../../schema/builders";

export default remark({
  label: "rem:mathlib-upstreaming-laurent-pl-links",
  title:
    "Tier-A Mathlib4 upstreaming additions: Laurent units and piecewise-linear polygonal links",
  interprets: "prop:upstream-mathlib-additions",
  uses: ["prop:upstream-mathlib-additions"],
  cites: ["lickorish1997", "rolfsen"],
  tags: [
    "lean-infrastructure",
    "mathlib-upstreaming",
    "laurent-polynomials",
    "pl-links",
    "appendix",
  ],
});
