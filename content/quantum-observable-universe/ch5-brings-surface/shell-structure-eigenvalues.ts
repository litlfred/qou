import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:shell-structure-eigenvalues",
  title:
    "Orbital shells from eigenvalues of the photon-electron transfer matrix",
  tags: [
    "shell",
    "orbital",
    "eigenvalue",
    "transfer-matrix",
    "chebyshev",
    "rydberg",
    "hydrogen",
    "photon",
    "electron",
    "recurrence",
  ],
  lean: {
    decl: "QOU.Descartes.shell_structure_eigenvalues",
    validation: "not_checked",
  },
  uses: [
    "def:transfer-matrix-operator",
    "prop:beta-decay-transfer-matrix",
    "prop:skein-polynomial-transfer-matrix",
    "def:electron-knot",
    "def:neutrino-knot",
    "conj:electron-shells-hopf",
    "rem:hydrogen-orbitals",
    "prop:local-substrate-q",
  ],
});
