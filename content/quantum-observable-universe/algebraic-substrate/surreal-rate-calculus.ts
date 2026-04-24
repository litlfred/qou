import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:surreal-rate-calculus",
  title: "Surreal rate calculus for the classical-limit scaling laws",
  lean: {
    decl: "QOU.AlgebraicSubstrate.surreal_rate_calculus",
    validation: "not_checked",
  },
  uses: [
    "def:reeb-epsilon",
    "def:q-from-epsilon",
    "def:classical-limit-functor",
    "thm:quantum-gap-collapse",
    "def:categorical-reeb-derivation",
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
