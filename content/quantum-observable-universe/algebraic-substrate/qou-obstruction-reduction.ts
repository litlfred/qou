import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qou-obstruction-reduction",
  title:
    "In a QOU the classical limit obstruction is one-dimensional",
  lean: {
    decl: "QOU.AlgebraicSubstrate.qou_obstruction_reduction",
    file: "QOU/AlgebraicSubstrate.lean",
    validation: "not_checked",
  },
  uses: [
    "def:classical-limit-obstruction",
    "def:quantum-observable-universe",
    "thm:qu-to-qou",
    "def:quantum-characteristic-classes",
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
