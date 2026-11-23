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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The extraction is recorded in [`qbeta_c3_imq_decay_projection_probe.py`](../../../computations/qbeta/qbeta_c3_imq_decay_projection_probe.py)." },
  ],
});
