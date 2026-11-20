import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-spectral-sum-finite",
  title:
    "Finiteness of the GS residue spectral sum",
  lean: {
    ref: "qou:QOU.BraidKnot.spectral_sum_finite",
    validation: "not_checked",
  },
  uses: ["conj:gs-residue-at-root-existence"],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "finiteness",
    "confinement-level",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean encoding.** Cast as a tautology over the compact domain `Fin levelBound` in `spectral_sum_finite`. The substantive claim is that `levelBound` correctly represents the confinement level.\n\nProving the bound requires formalising $\\mathrm{ConfinementLevel}$ and establishing" },
  ],
});
