import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:photon-augmentation-jet",
  title: "The augmentation jet of $H_n(q)$ vanishes, and a photon is not augmentation-normalised",
  lean: { ref: "qou:QOU.StandardModel.PhotonJet.hecke_sub_mul_self" },
  uses: ["def:photon"],
  cites: ["iwahori1964", "kassel2008"],
  tags: ["photon", "hecke-algebra", "augmentation", "jet", "tangent-space"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-25",
      body: "Promoted on owner ruling 2026-11-25 (\"1y\"). Lean: `QOU.PhotonJet.hecke_sub_mul_self`, `sub_eq_smul_sq`, `augmentation_photon` (sorry-free, lean-direct exit 0). The passage from the generator identity to $I = I^2$ for the whole ideal is the two-line argument in the proof paragraph and is not itself in Lean. Measured independently over $\\mathbb{Q}(q)$: rank $I$ = rank $I^2$ = 5 in $H_3$ (`computations/probes/photon_jet_spectral/photon_jet_probe.py`).",
    },
  ],
});
