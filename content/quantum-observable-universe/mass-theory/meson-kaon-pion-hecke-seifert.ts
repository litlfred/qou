import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:meson-kaon-pion-hecke-seifert",
  title:
    "Kaon-to-pion mass ratio from Hecke characters and Seifert volumes",
  uses: [
    "def:categorical-meson",
    "prop:hoefsmit-binding-amplitude",
  ],
  cites: [
    "jones1987",
    "kassel1995",
  ],
  lean: {
    ref: "qou:QOU.Mass.seifert_ratio_T25_T23",
  },
  tags: [
    "meson",
    "kaon",
    "pion",
    "hecke-character",
    "seifert-volume",
    "torus-knot",
    "mass-ratio",
  ],
});
