import { definition } from "../../schema/builders";

export default definition({
  label: "def:surreal-blowup-calculus",
  lean: {
    ref: "qou:QOU.AppendixSurreals.BlowupCalculus",
    validation: "not_checked",
  },
  title:
    "Surreal blow-up calculus: named infinite surreals for renormalisation",
  tags: [
    "surreal-numbers",
    "renormalisation",
    "blow-up",
    "infinite-surreal",
    "regularisation",
    "named-infinity",
  ],
  uses: ["def:standard-part-functor"],
  cites: ["conway1976", "ehrlich2012"],
});
