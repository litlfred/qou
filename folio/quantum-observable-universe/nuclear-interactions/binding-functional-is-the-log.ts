import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-functional-is-the-log",
  title:
    "Only the logarithmic binding functional is extensive; the linear rival fails by $-\\alpha(1-x)(1-y)$ and carries a ceiling",
  lean: {
    ref: "qou:QOU.QBeta.InterfaceScalar.linearForm_extensivity_defect",
    validation: "not_checked",
  },
  uses: ["prop:markov-stabilisation-needs-a-fresh-generator"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalisation note: the classical uniqueness step for Cauchy's functional equation (no continuous solutions beyond $c \\ln x$) is not formalised in Lean; `QOU.QBeta.InterfaceScalar.linearForm_extensivity_defect` proves the algebraic extensivity comparison.",
    },
  ],
  tags: ["binding-functional", "extensivity", "markov-trace", "deuteron"],
});
