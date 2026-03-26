import { definition } from "../../schema/builders";

export default definition({
  label: "def:covalent-bond-types",
  title: "Covalent bond (shared Hopf links)",
  tags: [
    "covalent-bond",
    "hopf-link",
    "shared-sub-link",
    "single-bond",
    "double-bond",
    "triple-bond",
    "electron",
    "molecular",
  ],
  uses: [
    "prop:metallic-character-knot",
    "conj:electron-shells-hopf",
    "def:crossing-energy",
  ],
});
