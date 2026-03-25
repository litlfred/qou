import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-mass-formula",
  title: "Topological mass formula (Archimedean)",
  tags: ["mass", "archimedean", "knot-volume", "quantum-planck"],
  uses: [
    "ex:c-quantum-observable-universe",
    "def:mass-identity",
    "thm:topological-mass",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
    "prop:descent-eigenspaces",
    "def:descent-involution",
  ],
  lean: {
    decl: "QOU.Torsion.ArchimedeanMassFormula",
    file: "QOU/ArchimedeanMassFormula.lean",
  },
});
