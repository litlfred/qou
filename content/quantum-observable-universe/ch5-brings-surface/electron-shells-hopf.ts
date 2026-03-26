import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:electron-shells-hopf",
  title:
    "Electron shells as closed sub-Hopf links of the trefoil chain",
  tags: [
    "electron",
    "shell",
    "hopf-link",
    "sub-link",
    "photon",
    "orbital",
    "trefoil",
    "absorption",
  ],
  uses: [
    "def:hadron",
    "def:stable-nucleus",
    "def:crossing-energy",
    "def:coulomb-charge",
    "conj:skein-shell-correction",
    "prop:torus-hopf-stability",
    "rem:knot-notation-convention",
  ],
});
