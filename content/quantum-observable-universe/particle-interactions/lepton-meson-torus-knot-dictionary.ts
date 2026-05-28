import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lepton-meson-torus-knot-dictionary",
  title:
    "Torus-knot dictionary: leptons at $H_2$ vs mesons at $H_3$",
  uses: ["conj:meson-volume-conjecture"],
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
