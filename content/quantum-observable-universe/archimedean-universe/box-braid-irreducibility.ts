import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:box-braid-irreducibility",
  title:
    "The $\\gamma\\gamma \\to \\nu\\nu^{\\sigma}$ box braid is irreducible",
  tags: [
    "neutrino",
    "stability",
    "box-diagram",
    "groebner-basis",
    "irreducibility",
    "skein-relation",
    "weak-force",
    "photon",
    "virtual-particles",
  ],
  lean: { ref: "qou:QOU.Descartes.BoxBraidIrreducibility",
    validation: "not_checked",
  },
  uses: [
    "def:neutrino-knot",
    "def:antineutrino-knot",
    "def:beta-decay-skein",
    "rem:force-knot-identification",
    "rem:unmapped-torus-knots",
    "rem:virtual-particles-exceptional-divisor",
    "prop:nuclear-groebner-reduction",
    "thm:groebner-shirshov-energy",
    "rem:electron-immortality",
    "def:mass-identity",
    "ex:photon-wavefront",
    "prop:reidemeister-action-table",
  ],
});
