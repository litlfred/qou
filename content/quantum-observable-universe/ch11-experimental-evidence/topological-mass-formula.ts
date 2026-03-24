import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:topological-mass-formula",
  title: "Topological mass formula (Archimedean)",
  tags: ["mass", "archimedean", "knot-volume", "quantum-planck"],
  uses: [
    "ex:c-quantum-observable-universe",
    "def:mass-identity",
    "thm:topological-mass",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
  ],
  lean: {
    decl: "QOU.Torsion.ArchimedeanMassFormula",
    file: "QOU/ArchimedeanMassFormula.lean",
  },
});
