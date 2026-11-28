import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-spectral-sunset-selection",
  title: "Selection rule for the typed spectral sunset on Bring's surface",
  lean: { ref: "qou:QOU.Transcendental.Brings.SpectralSunset.sunset_by_type" },
  uses: ["prop:bring-harmonic-types", "prop:bring-reflection-parity"],
  tags: ["brings-surface", "harmonics", "representation-theory", "maass", "two-loop", "selection-rule"],
  proofs: ["prf:bring-spectral-sunset-selection"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Bean `qou-u81q`. This is the hyperbolic counterpart of the flat-torus sunset in `docs/audits/2026-11-28-alpha-em-two-loop-measure-bring.md` (PR #9860), taken here at the coordinator's request after that thread closed. Lean, sorry-free, standard axioms only: `QOU/BringsSurface/BringTripleSelection.lean` (the table $N$) and `QOU/Transcendental/BringsSurface/BringSpectralSunset.lean` (the cut sunset over opaque labels, with ring-valued weights). The vanishing of $C_{abc}$ on forbidden triples (invariance of the integral and Schur's lemma) is cited and is a structure field, not proved. No closed form is claimed, and no eigenvalue is used.",
    },
  ],
});
