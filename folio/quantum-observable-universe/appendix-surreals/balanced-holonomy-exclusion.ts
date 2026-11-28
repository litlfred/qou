import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:balanced-holonomy-exclusion",
  renamedFrom: ["prop:collatz-no-cycles"],
  lean: {
    ref: "qou:QOU.Core.AlgebraicSubstrate.balanced_holonomy_excluded",
    validation: "leanok",
  },
  title:
    "Balanced-holonomy exclusion and periodic-orbit classification for $\\mathcal{C}_q$ on $\\mathbb{Z}[q^{\\pm 1}]$",
  uses: [
    "def:two-q-adic-valuation",
  ],
  tags: [
    "laurent-polynomial",
    "periodic-cycle",
    "coprimality",
    "q-integer",
  ],
});
