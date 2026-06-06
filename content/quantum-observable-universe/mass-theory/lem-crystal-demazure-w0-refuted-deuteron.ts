import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:crystal-demazure-w0-refuted-deuteron",
  title:
    "Crystal/Demazure-$w_0$ principal-specialisation $\\Delta_\\lambda$ refuted at the deuteron",
  lean: {
    ref: "qou:QOU.WedderburnMass.crystal_demazure_refuted_deuteron",
    validation: "not_checked",
  },
  uses: ["prop:deuteron-binding-frobenius-codim"],
  tags: [
    "delta-lambda",
    "refutation",
    "crystal",
    "demazure",
    "gap-a",
    "audit",
  ],
});
