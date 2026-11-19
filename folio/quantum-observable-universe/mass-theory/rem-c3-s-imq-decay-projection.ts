import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:im-q-physical-role",
  label: "rem:c3-s-imq-decay-projection",
  title:
    "The $\\beta$-decay $S = \\mathfrak{Q}_\\beta/E_0$ realizes candidate (iii): a small sign-flipped $\\mathrm{Im}(q)$",
  uses: ["conj:im-q-physical-role"],
  tags: [
    "im-q",
    "decay-width",
    "non-hermitian",
    "q-beta",
    "c3-bar-odd",
    "candidate-iii",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/qbeta/qbeta_c3_imq_decay_projection_probe.py.",
    },
  ],
});
