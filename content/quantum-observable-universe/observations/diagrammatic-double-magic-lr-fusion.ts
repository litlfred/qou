import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:diagrammatic-double-magic-lr-fusion",
  title:
    "Proposition (diagrammatic double-magic): LR-fusion rigidity at $Z, N \\in \\mathfrak{M}$",
  lean: {
    ref: "qou:QOU.LRFusion.DoubleMagicConjecture",
    validation: "not_checked",
  },
  uses: [
    "conj:categorical-neutrality-saturated-shells",
    "conj:homological-shell-condensation",
    "prop:magic-numbers-from-q",
    "prop:hoefsmit-seminormal-form",
    "thm:wedderburn-mass-formula",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/lr_fusion_self_conj_test.py",
    witness:
      "folio-assistant/computations/lr-fusion-self-conj-test.witness.json",
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
});
