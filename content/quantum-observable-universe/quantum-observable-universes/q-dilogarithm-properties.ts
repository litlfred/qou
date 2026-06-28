import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-dilogarithm-properties",
  interprets: "def:q-dilogarithm",
  title: "Realisations of $\\mathrm{Li}_2^q$: R-matrix, Habiro ring, three contexts, and the $q$-heat partition function",
  tags: ["hopf-algebra", "dilogarithm", "pentagon-identity", "associator", "q-series"],
  uses: [
    "def:q-dilogarithm",
    "def:habiro-ring",
    "def:categorical-laplace",
    "prop:q-heat-kernel-peter-weyl",
  ],
});
