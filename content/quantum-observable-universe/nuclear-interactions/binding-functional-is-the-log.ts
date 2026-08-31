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
  tags: ["binding-functional", "extensivity", "markov-trace", "deuteron"],
});
