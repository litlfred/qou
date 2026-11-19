import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    {
      kind: "note",
      date: "2026-08-22",
      body:
        "**Order of presentation.** The working variable (the isospin label " +
        "$T$) is introduced before the refuted one, so that the refutation " +
        "reads as a statement about what content cannot do rather than as a " +
        "gap the reader is left holding.",
    },
  ],
  label: "prop:content-keyed-interface-refuted",
  title:
    "No interface keyed on nucleon content can work: the two $pn$ channels share content and differ in boundness",
  lean: {
    ref: "qou:QOU.QBeta.InterfaceScalar.content_keyed_interface_refuted",
    validation: "not_checked",
  },
  uses: ["prop:isospin-singlet-binds-more"],
  tags: [
    "refutation",
    "isospin",
    "nn-channel",
    "crossing-multiplicity",
    "deuteron",
  ],
  computation: {
    engine: "python",
    script: "computations/two_term_qed_isotope_and_nucleon_compute.py",
    witness: "computations/two-term-qed-isotope-and-nucleon-compute.witness.json",
    status: "verified",
  },
});
