import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-gaussian-solves-q-heat",
  title: "Reeb-invariant $q$-Gaussian solves the $q$-heat equation (archimedean)",
  tags: ["q-heat-equation", "q-gaussian", "heat-kernel", "archimedean"],
  lean: {
    decl: "QOU.qGaussianSolvesQHeat",
    validation: "not_checked",
  },
  uses: [
    "def:q-heat-equation",
    "rem:q-laplacian-expansion",
    "prop:q-exponential-taylor",
    "rem:archimedean-realisations",
  ],
});
