import { remark } from "../../schema/builders";

export default remark({
  label: "rem:connes-distance-not-reeb-step-count",
  title:
    "$d_{\\mathrm{Connes}}$ is a minimal Reeb step count only in the $q \\to \\infty$ limit",
  interprets: "prop:reeb-coefficient-is-hbar-q",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.dirac_coefficients_convex",
    validation: "not_checked",
  },
  uses: [
    "prop:reeb-coefficient-is-hbar-q",
    "prop:reeb-operations-per-planck",
  ],
  tags: ["connes-distance", "reeb-flow", "limit", "dirac-operator"],
});
