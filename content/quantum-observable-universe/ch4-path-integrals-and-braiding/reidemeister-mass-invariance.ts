import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reidemeister-mass-invariance",
  title:
    "Reidemeister invariance of mass and binding energy",
  tags: [
    "reidemeister",
    "mass",
    "binding-energy",
    "knot-invariant",
    "embedding",
    "shell-transition",
    "writhe",
  ],
  lean: {
    decl: "QOU.Braiding.reidemeister_mass_invariance",
    validation: "not_checked",
  },
  uses: [
    "def:crossing-energy",
    "def:hadron",
    "conj:electron-shells-hopf",
    "rem:hydrogen-orbitals",
    "def:electron-knot",
  ],
});
