import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-mass-formula",
  title: "Topological mass formula (Archimedean)",
  tags: ["mass", "archimedean", "knot-volume", "quantum-planck"],
  uses: [
    "thm:topological-mass",
    "def:quantum-planck-constant",
  ],
  lean: {
    decl: "QOU.Torsion.ArchimedeanMassFormula",
    file: "QOU/ArchimedeanMassFormula.lean",
    validation: "not_checked",
  },
});
