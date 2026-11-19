import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:surreal-limit-transfer",
  title:
    "Surreal limit transfer: limits as standard-part equalities via an $\\omega$-evaluation",
  lean: {
    ref: "qou:QOU.AppendixSurreals.SurrealLimitTransfer",
    validation: "not_checked",
  },
  tags: [
    "surreal-numbers",
    "standard-part",
    "nonstandard-analysis",
    "limits",
    "inequality-to-equality",
    "archimedean",
  ],
  uses: [
    "def:standard-part-functor",
    "rem:st-is-median-resummation",
  ],
  cites: ["robinson1966", "berarducci-mantova2018"],
  authorNotes: [
    {
      kind: "note",
      body:
        "Formalised in QOU.AppendixSurreals.SurrealLimitTransfer as a Lean class with no instance over the abstract SurrealField interface; standardPart_evalOmega_of_tendstoReal and tendstoReal_le_of_eventuallyLE are proved from the class fields.",
    },
  ],
});
