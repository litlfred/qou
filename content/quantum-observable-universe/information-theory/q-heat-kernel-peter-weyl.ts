import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-heat-kernel-peter-weyl",
  title: "Peter--Weyl decomposition of the $q$-heat kernel (archimedean)",
  tags: ["q-heat-equation", "peter-weyl", "heat-kernel", "hecke", "wedderburn", "archimedean"],
  lean: {
    decl: "QOU.qHeatKernelPeterWeyl",
    validation: "not_checked",
  },
  uses: [
    "def:q-heat-equation",
    "def:categorical-fourier",
    "prop:q-gaussian-solves-q-heat",
    "rem:q-laplacian-expansion",
    "rem:archimedean-realisations",
  ],
});
