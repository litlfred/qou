import { proof } from "../../schema/builders";

export default proof({
  label: "prf:collatz-no-cycles",
  title: "Proof of collatz no cycles",
  uses: ["prop:collatz-no-cycles"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Affine (A!=1) case added and the open direction removed: end-coefficient proof of the cycle classification in Z[q^±1], formalised sorry-free as cycle_classification / laurent_cycle_classification in QOU/AppendixSurreals/collatz_cycle_classification.lean. The census sentence is now corroboration, not the only evidence. Supersedes the 2026-07-18 'nontrivial-cycle exclusion is open' framing for the formal ring; nothing is claimed about classical Collatz. Owner-approved (project thread, 2026-11-21).",
    },
    {
      kind: "refined-framing",
      date: "2026-07-18",
      body:
        "Re-scoped from 'settles half the conjecture' to the balanced-holonomy (A=1) sub-case. The Skein-Collatz odd branch is affine, so a cycle gives (1-A)P=B; coprimality only forces A!=1, making P0=B/(1-A) a solvable candidate, not an excluded one. Nontrivial-cycle exclusion (A!=1) is open. Analysis: docs/audits/2026-07-18-collatz-no-cycles-multiplicative-shadow-gap.md.",
    },
    {
      kind: "note",
      date: "2026-07-18",
      body:
        "Computational backing for the census sentence: computations/qcollatz_cycle_census.py + qcollatz_cycle_census.witness.json (exact Laurent arithmetic, primitive words through period 18; only cycles are {q^-1, 1+q^-1} and -q^-2).",
    },
  ],
});
