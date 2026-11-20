import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-mass-formula",
  title: "Topological mass formula (Archimedean)",
  tags: ["mass", "archimedean", "knot-volume", "quantum-planck"],
  uses: [
    "conj:topological-mass",
    "def:quantum-planck-constant",
  ],
  lean: { ref: "qou:QOU.Torsion.ArchimedeanMassFormula",
    validation: "not_checked",
  },
});
