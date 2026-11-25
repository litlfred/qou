import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:photon-response-determines-q",
  title: "The one-photon Markov-trace response determines $q$ under convention D",
  lean: { ref: "qou:QOU.StandardModel.PhotonJet.audible_q" },
  uses: ["def:photon"],
  cites: ["kassel2008"],
  tags: ["photon", "markov-trace", "convention-d", "spectral-rigidity", "isospectral"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-25",
      body: "Promoted on owner ruling 2026-11-25 (\"1y\"). Lean: `QOU.PhotonJet.audible_q` (sorry-free) proves the inversion step. The trace formula itself is computed from the Markov rules in the proof paragraph and checked exactly over $\\mathbb{Q}(q)$ (`computations/probes/photon_jet_spectral/photon_jet_probe.py`); it is not in Lean. Context (the 'can you hear the shape of a QOU' question, and why states are not audible): `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` §3.",
    },
  ],
});
