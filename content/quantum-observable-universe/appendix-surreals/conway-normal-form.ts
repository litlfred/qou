import { definition } from "../../schema/builders";

export default definition({
  label: "def:conway-normal-form",
  lean: {
    decl: "QOU.AppendixSurreals.ConwayNormalForm",
    validation: "not_checked",
  },
  title:
    "Conway normal form: $x = \\sum \\omega^{y_i} r_i$",
  tags: [
    "surreal-numbers",
    "conway-normal-form",
    "hahn-series",
    "growth-rates",
    "asymptotic",
    "leading-exponent",
  ],
  uses: [
    "def:birthday-grading",
    "def:surreal-blowup-calculus",
  ],
  cites: ["conway1976", "gonshor1986", "ehrlich2012"],
});
