import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:surreal-rate-calculus",
  title: "Surreal rate calculus for the classical-limit scaling laws",
  lean: {
    decl: "QOU.AlgebraicSubstrate.SurrealRateCalculus",
    file: "lean/QOU/AlgebraicSubstrate/SurrealRateCalculus.lean",
    validation: "not_checked",
  },
  uses: [
    "def:q-from-epsilon",
    "thm:quantum-gap-collapse",
    "rem:body-asymptotics-catalog",
  ],
  tags: [
    "surreal",
    "error-bounds",
    "rate-calculus",
    "mass-gap",
    "reeb-period",
    "enstrophy",
    "classical-limit",
    "millennium-problem",
  ],
});
