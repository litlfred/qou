import { definition } from "../../schema/builders";

export default definition({
  label: "def:cs-gram-determinant-ratio",
  title: "Chern--Simons Gram-determinant ratio $\\kappa$",
  tags: ["gram-matrix", "chern-simons", "kappa", "determinant"],
  uses: ["rem:em-coupling-chern-simons"],
  lean: {
    ref: "qou:QOU.Archimedean.csGramDetRatio",
    validation: "not_checked",
  },
});
