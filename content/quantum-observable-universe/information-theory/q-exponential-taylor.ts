import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-exponential-taylor",
  title: "Taylor series of $\\exp_q$ (archimedean)",
  tags: ["q-exponential", "taylor-series", "archimedean"],
  lean: {
    decl: "QOU.qExponentialTaylor",
    validation: "not_checked",
  },
  uses: [
    "def:q-exponential",
    "rem:archimedean-realisations",
  ],
});
