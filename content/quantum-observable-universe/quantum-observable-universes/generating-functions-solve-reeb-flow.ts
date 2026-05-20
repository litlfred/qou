import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:vertex-is-exceptional-divisor",
  label: "rem:generating-functions-solve-reeb-flow",
  title:
    "Generating functions ($\\exp_q$, $\\mathrm{Li}_2^q$, categorical Fourier) are the Reeb-flow solutions",
  tags: [
    "q-exponential",
    "q-dilogarithm",
    "categorical-fourier",
    "habiro-ring",
    "reeb-flow",
    "pre-archimedean",
  ],
  uses: [
    "def:q-exponential",
    "prop:q-exponential-unique",
    "def:q-dilogarithm",
    "prop:q-dilogarithm-unique",
    "def:categorical-fourier",
    "prop:categorical-fourier-exists",
    "def:q-heat-equation",
    "def:habiro-ring",
    "def:archimedean-realization-functor",
    "prop:vertex-is-exceptional-divisor",
    "prop:thurston-volume-additivity",
  ],
});
