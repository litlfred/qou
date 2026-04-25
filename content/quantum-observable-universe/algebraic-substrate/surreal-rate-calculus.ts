import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:surreal-rate-calculus",
  title: "Surreal rate calculus for the classical-limit scaling laws",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.SurrealRateCalculus",
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
