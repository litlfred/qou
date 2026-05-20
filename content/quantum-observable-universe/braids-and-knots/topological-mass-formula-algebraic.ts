import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:topological-mass-formula-algebraic",
  title:
    "Topological mass formula (algebraic, $\\mathbb{Q}(q)$-side)",
  lean: {
    ref: "qou:QOU.Torsion.AlgebraicMassFormula",
    validation: "not_checked",
  },
  uses: [
    "thm:topological-mass",
    "def:algebraic-quantum-volume",
    "def:quantum-planck-constant",
    "thm:markov-trace-factorization",
    "lem:tower-pair-equality-fixed-level",
  ],
  cites: [
    "kassel1995",
    "habiro2002",
    "kashaev1997",
    "murakami-murakami2001",
  ],
  tags: [
    "mass",
    "algebraic",
    "quantum-volume",
    "tau-wall",
    "narrative-replacement",
  ],
});
