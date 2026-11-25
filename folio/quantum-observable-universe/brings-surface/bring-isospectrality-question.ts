import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-isospectrality-question",
  title: "Open question: is Bring's surface spectrally rigid?",
  uses: ["prop:photon-response-determines-q", "def:photon", "def:categorical-dirac-operator"],
  cites: ["kac1966", "sunada1985", "cook2021"],
  tags: ["bring-surface", "isospectral", "spectral-geometry", "open-problem", "conjectural-framing"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-25",
      body: "Recorded as an open question on owner instruction 2026-11-25 (\"Bring isospectrality --> leave is as an open question in the paper instead\"), superseding the same day's \"Bring isospectrality now\". No direction is conjectured. The Gassmann counts (S₅: 156 subgroups in 19 classes; S₅ × C₂: 535 subgroups in 57 classes; no almost-conjugate non-conjugate pair in either) are exact finite computations in `computations/probes/photon_jet_spectral/`, not Lean. Audit: `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` §3, §8.3.",
    },
  ],
});
