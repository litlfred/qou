import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:box-braid-irreducibility",
  label: "rem:box-braid-irreducibility-interpretation",
  title: "Box-braid vertex structure and suppression of neutrino decay",
  tags: [
    "neutrino",
    "stability",
    "box-diagram",
    "skein-relation",
    "weak-force",
    "photon",
  ],
  uses: [
    "prop:box-braid-irreducibility",
    "def:confined-particle",
    "ex:photon-wavefront",
    "rem:force-knot-identification",
    "rem:electron-immortality",
  ],
});
