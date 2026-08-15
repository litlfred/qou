import { remark } from "../../schema/builders";

export default remark({
  label: "rem:archimedean-stpart-strategy",
  interprets: "conj:archimedean-stpart",
  title:
    "Proof strategy for archimedean = $\\mathrm{St}$ of surreal QOU",
  // The strategy step "St recovers Rep_R(SU(2)) BY classical-limit-stpart".
  // conj:archimedean-stpart itself is NOT listed here: `interprets` above
  // already records that edge, and the editorial graph reads it.
  uses: ["conj:classical-limit-stpart"],
  tags: [
    "surreal-numbers",
    "archimedean",
    "standard-part",
    "proof-strategy",
    "open-problem",
  ],
});
