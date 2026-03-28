import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:box-braid-irreducibility",
  title:
    "The $\\gamma\\gamma \\to \\nu\\bar{\\nu}$ box braid is irreducible",
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
  lean: {
    decl: "QOU.Descartes.BoxBraidIrreducibility",
    validation: "not_checked",
  },
  uses: [
    "def:neutrino-knot",
    "def:antineutrino-knot",
    "def:beta-decay-skein",
    "rem:force-knot-identification",
    "rem:virtual-particles-exceptional-divisor",
    "prop:nuclear-groebner-reduction",
    "prop:groebner-shirshov-energy",
    "rem:electron-immortality",
    "def:mass-identity",
    "ex:photon-wavefront-example",
    "prop:reidemeister-action-table",
  ],
});
