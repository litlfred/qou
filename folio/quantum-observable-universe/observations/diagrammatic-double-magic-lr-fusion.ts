import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:diagrammatic-double-magic-lr-fusion",
  title:
    "Conjecture (diagrammatic double-magic): LR-fusion rigidity at $Z, N \\in \\mathfrak{M}$",
  lean: {
    ref: "qou:QOU.LRFusion.DoubleMagicConjecture",
    validation: "not_checked",
  },
  uses: [
    "conj:homological-shell-condensation",
    "conj:magic-numbers-from-q",
  ],
  computation: {
    engine: "python",
    script: "computations/lr_fusion_self_conj_test.py",
    witness:
      "computations/lr-fusion-self-conj-test.witness.json",
    status: "verified",
  },
  cites: [
    "ariki1996",
    "ram1991",
    "geckpfeiffer2000",
    "kassel1995",
  ],
  tags: [
    "magic-numbers",
    "double-magic",
    "LR-fusion",
    "shell-closure",
    "self-conjugate-partitions",
    "littlewood-richardson",
    "open-problem",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh; Lean talk out of prose): The Lean carrier proves this (`not_doubleMagicConjecture`), with the conjugation symmetry kept as a hypothesis of the class because it is not yet formalised there." },
  ],
});
