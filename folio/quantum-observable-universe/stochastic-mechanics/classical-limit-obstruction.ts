import { definition } from "../../schema/builders";

export default definition({
  label: "def:classical-limit-obstruction",
  title:
    "The classical limit obstruction of a quantum universe",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.ClassicalLimitObstruction",
    validation: "not_checked",
  },
  uses: [
    "def:hochschild-homology",
    "def:classical-limit-functor",
    "def:quantum-characteristic-classes",
  ],
  tags: [
    "obstruction",
    "classical-limit",
    "hochschild-cohomology",
    "deformation-theory",
    "q-to-1",
  ],
  cites: ["yekutieli2010"],
});
