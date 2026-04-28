import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wenzl-qmn-synergy",
  title:
    "Wenzl-bridge + q-Murnaghan-Nakayama synergy: $\\mathrm{tr}_M$ on canonical braids in $O(p(n)(\\max\\text{hooks} + n^2))$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.wenzl_qmn_synergy",
    validation: "not_checked",
  },
  uses: [
    "prop:y-lambda-closed-form-wenzl-bridge",
    "prop:y-lambda-recipe-from-partition",
    "prop:y-lambda-cyclotomic-factorization",
    "thm:jones-markov-trace",
  ],
  cites: ["wenzl1988", "halverson-ram-1995", "ram1991"],
  tags: [
    "wenzl-bridge",
    "q-murnaghan-nakayama",
    "markov-trace",
    "compute-speedup",
    "atom-knot-id",
    "synergy",
  ],
});
