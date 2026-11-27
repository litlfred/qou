import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-isospectrality-question",
  title: "Open question: is Bring's surface spectrally rigid?",
  uses: ["prop:photon-response-determines-q", "def:photon", "def:categorical-dirac-operator", "prop:photon-filtration-depth-bounds"],
  cites: ["kac1966", "sunada1985", "cook2021"],
  tags: ["bring-surface", "isospectral", "spectral-geometry", "open-problem", "conjectural-framing"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-25",
      body: "Item 3 corrected the same day. It first said every photon response factors through the cocenter, so braid states are not determined. That is true of the zero-photon response only. The $k$-photon responses determine a state modulo the radical of the trace form (Lean: `QOU.PhotonAudibility.responses_determine_mod_radical`; under convention D on $H_3$ the radical is the sign line, `sign_inaudible_D`, with the determinant of the trace form computed exactly in `computations/probes/photon_jet_spectral/audibility_and_depth_exact_probe.py`). Audit §14.",
    },
    {
      kind: "status",
      date: "2026-11-25",
      body: "Recorded as an open question on owner instruction 2026-11-25 (\"Bring isospectrality --> leave is as an open question in the paper instead\"), superseding the same day's \"Bring isospectrality now\". No direction is conjectured. The Gassmann counts (S₅: 156 subgroups in 19 classes; S₅ × C₂: 535 subgroups in 57 classes; no almost-conjugate non-conjugate pair in either) are exact finite computations in `computations/probes/photon_jet_spectral/`, not Lean. Audit: `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` §3, §8.3.",
    },
  ],
});
