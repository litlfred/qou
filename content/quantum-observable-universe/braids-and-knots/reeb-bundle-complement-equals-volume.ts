import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-bundle-complement-equals-volume",
  lean: {
    ref: "qou:QOU.BraidsKnots.ReebBundleComplementEqualsVolume",
    validation: "not_checked",
  },
  title:
    "Reeb-bundle complement is the JSJ-graded volume sum (Reeb-bundle face of mass-volume)",
  tags: [
    "knot-complement",
    "hyperbolic-volume",
    "jsj-decomposition",
    "reeb-bundle",
    "mass-volume",
    "markov-trace",
  ],
  uses: [
    "def:reeb-bundle",
    "prop:vertex-is-exceptional-divisor",
    "prop:six-canonical-knot-operators",
    "prop:thurston-volume-additivity",
    "conj:mass-volume-factorization",
  ],
});
