import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lepton-meson-torus-knot-dictionary",
  proofs: ["prf:lepton-meson-torus-knot-dictionary"],
  lean: { ref: "qou:QOU.ParticleInteractions.lepton_meson_crossing_match" },
  title:
    "Torus-knot dictionary: leptons at $H_2$ vs mesons at $H_3$",
  uses: ["def:categorical-meson"],
  cites: [
    "jones1987",
    "kashaev1997",
  ],
  tags: [
    "lepton",
    "meson",
    "torus-knot",
    "hecke-algebra",
    "dictionary",
  ],
});
