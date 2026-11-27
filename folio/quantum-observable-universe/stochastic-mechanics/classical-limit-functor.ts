import { definition } from "../../schema/builders";

export default definition({
  label: "def:classical-limit-functor",
  title: "The classical limit functor $q \\to 1$",
  lean: { ref: "qou:QOU.Core.AlgebraicSubstrate.ClassicalLimitFunctor",
    validation: "not_checked",
  },
  uses: [
    "def:aether-parameter-planck",
    "def:adelic-base-ring",
  ],
  tags: [
    "classical-limit",
    "functor",
    "q-to-1",
    "deformation",
    "symmetric-monoidal",
    "adelic-assembly",
    "realization-tower",
  ],
});
