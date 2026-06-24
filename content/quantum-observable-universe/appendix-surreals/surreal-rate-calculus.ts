import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:surreal-rate-calculus",
  proofs: ["prf:surreal-rate-calculus"],
  title: "Surreal rate calculus for the classical-limit scaling laws",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.SurrealRateCalculus",
    validation: "not_checked",
  },
  uses: ["lem:surreal-squeeze"],
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
