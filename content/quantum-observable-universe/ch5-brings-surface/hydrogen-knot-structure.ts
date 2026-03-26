import { example } from "../../schema/builders";

export default example({
  label: "ex:hydrogen-knot-structure",
  title: "Hydrogen: the simplest atom in knot form",
  tags: [
    "hydrogen",
    "knot",
    "trefoil",
    "borromean",
    "ionization",
    "rydberg",
  ],
  uses: [
    "conj:borromean-quark",
    "def:up-quark",
    "def:down-quark",
    "def:electron-knot",
    "def:categorical-proton",
    "conj:electron-shells-hopf",
    "def:crossing-energy",
  ],
});
