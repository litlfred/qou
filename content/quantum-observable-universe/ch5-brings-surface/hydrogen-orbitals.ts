import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:electron-knot",
  label: "rem:hydrogen-orbitals",
  title:
    "Hydrogen orbitals: the spinning trefoil around the Borromean anchor",
  tags: [
    "hydrogen",
    "orbital",
    "shell",
    "subshell",
    "trefoil",
    "writhe",
    "borromean",
    "electron-cloud",
  ],
  uses: [
    "ex:hydrogen-knot-structure",
    "conj:borromean-quark",
    "conj:electron-shells-hopf",
    "def:electron-knot",
    "def:categorical-proton",
    "def:crossing-energy",
  ],
});
