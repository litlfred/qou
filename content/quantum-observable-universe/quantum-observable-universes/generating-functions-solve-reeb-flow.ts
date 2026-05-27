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
    "prop:q-exponential-unique",
    "prop:q-dilogarithm-unique",
    "prop:categorical-fourier-exists",
    "prop:vertex-is-exceptional-divisor",
    "prop:thurston-volume-additivity",
  ],
});
