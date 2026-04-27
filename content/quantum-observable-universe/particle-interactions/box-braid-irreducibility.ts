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
    "rem:virtual-particles-exceptional-divisor",
    "rem:electron-immortality",
    "ex:photon-wavefront",
  ],
});
