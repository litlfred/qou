import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-stabilisation-needs-a-fresh-generator",
  title:
    "Markov stabilisation at the interface requires a generator the word does not already use",
  lean: {
    ref: "qou:QOU.QBeta.InterfaceScalar.markov_stabilisation_fails_on_repeat",
    validation: "not_checked",
  },
  uses: ["prop:content-keyed-interface-refuted"],
  tags: ["interface-scalar", "markov-trace", "convention-d", "deuteron"],
});
