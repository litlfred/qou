import { proof } from "../../schema/builders";

export default proof({
  label: "prf:categorical-mass-markov",
  title: "Proof of categorical mass markov",
  uses: ["prop:categorical-mass-markov"],
  computation: {
    engine: "sympy",
    script: "computations/markov/markov_trace_canonical.py",
    // The body already told the reader to reproduce with this script. It just
    // could not be DECLARED, because the script emitted no witness -- so the
    // nine values in its convention C-vs-D table were traceable only by
    // coincidence, matching decimals in `alpha-k-jones-markov-h3` and
    // `gram-matrix-dual`, neither of which is what the block cites (qou-ft3p).
    witness: [
      "computations/markov/markov-trace-canonical.witness.json",
    ],
    status: "verified",
    requires: ["mpmath", "sympy"],
  },
});
