import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qou-obstruction-reduction",
  title:
    "In a QOU the classical limit obstruction is one-dimensional",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.qou_obstruction_reduction",
    validation: "not_checked",
  },
  uses: [
    "def:classical-limit-obstruction",
    "thm:qu-to-qou",
  ],
  tags: [
    "obstruction",
    "classical-limit",
    "hochschild-cohomology",
    "observability",
    "frobenius-duality",
    "euler-characteristic",
    "kummer",
  ],
  cites: ["yekutieli2010"],
});
