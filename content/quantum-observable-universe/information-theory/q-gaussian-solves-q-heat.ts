import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-gaussian-solves-q-heat",
  proofs: ["prf:q-gaussian-solves-q-heat"],
  title: "Reeb-invariant $q$-Gaussian solves the $q$-heat equation (archimedean)",
  tags: ["q-heat-equation", "q-gaussian", "heat-kernel", "archimedean"],
  lean: { ref: "qou:QOU.qGaussianSolvesQHeat",
    validation: "not_checked",
  },
  uses: ["prop:q-exponential-taylor"],
});
