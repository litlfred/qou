import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gen3-meson-phi-hecke-seifert",
  title:
    "Third-generation meson ($\\phi$) mass ratio from Hecke characters and Seifert volumes",
  uses: [
    "def:categorical-meson",
    "prop:hoefsmit-binding-amplitude",
    "prop:meson-kaon-pion-hecke-seifert",
  ],
  cites: [
    "jones1987",
    "kassel1995",
  ],
  lean: {
    ref: "qou:QOU.Mass.Gen3.phiMassRatio",
  },
  tags: [
    "meson",
    "phi",
    "pion",
    "hecke-character",
    "seifert-volume",
    "torus-knot",
    "mass-ratio",
    "third-generation",
  ],
});
