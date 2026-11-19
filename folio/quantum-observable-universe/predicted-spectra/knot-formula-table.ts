import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:knot-particle-generation",
  label: "rem:knot-formula-table",
  title: "Topological knot formulas for fundamental and composite particles",
  tags: [
    "knot",
    "formula",
    "notation",
    "particle",
    "hadron",
    "nucleus",
    "generation",
    "fermion",
    "boson",
    "torus-link",
  ],
  // Earlier `uses[]` listed `conj:higgs-t28`, which transitively
  // typed every block citing this remark as downstream of an open
  // conjecture (per `docs/audits/conjecture-cones.md` "Methodology"
  // — case (2) cleanup). The table is a forward narrative reference
  // ("Higgs as T(2,8)") that interprets the conjecture; the
  // conjecture's content does not feed the table. Citation moves
  // to prose only.
  uses: [
    "thm:embeddability-closure",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
