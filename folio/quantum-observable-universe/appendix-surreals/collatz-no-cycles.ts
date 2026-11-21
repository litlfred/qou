import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:collatz-no-cycles",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.balanced_holonomy_excluded", validation: "leanok" },
  title:
    "Balanced-holonomy cycle exclusion: coprimality of $[2]_q$ and $[3]_q$",
  uses: [],
  tags: [
    "collatz",
    "periodic-cycle",
    "coprimality",
    "q-integer",
    "skein-divisibility",
  ],
  cites: ["collatz1937"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Last paragraph updated: the affine (A!=1) case is settled in Z[q^±1] by laurent_cycle_classification (QOU/AppendixSurreals/collatz_cycle_classification.lean, sorry-free). The only cycles are {0}, {-q^-2} and {q^-1, 1+q^-1}. Convergence (no divergent orbits) stays open in conj:q-collatz. Owner-approved content update (project thread, 2026-11-21).",
    },
    {
      kind: "refined-framing",
      date: "2026-07-18",
      body:
        "Re-scoped to the balanced-holonomy (A=1) sub-case and re-pointed lean.ref from the ℝ-based context theorem collatz_no_cycles to the proved generic-ring theorem balanced_holonomy_excluded. Base-ring rationale (§7c): the exclusion needs [2]_q=q+1 to be a NON-UNIT, which holds in the fibre ring ℤ[q^±1] but FAILS over ℝ; the fibre-level generic [CommRing] statement is the faithful one. Removed the spurious uses[conj:collatz-contact-boundary] dependency — the proved result is unconditional, not conditional on the conjecture.",
    },
  ],
});
