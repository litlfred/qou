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
  lean: { ref: "qou:QOU.Descartes.shell_structure_eigenvalues",
    validation: "not_checked",
  },
  uses: [
    "def:transfer-matrix-operator",
    "rem:hydrogen-orbitals",
  ],
});
