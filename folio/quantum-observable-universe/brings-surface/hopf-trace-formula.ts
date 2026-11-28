import { proposition } from "../../schema/builders";

/**
 * Hopf trace formula for a two-step chain complex over a field, with trace additivity over an
 * invariant subspace and the fixed-cell count for a permuted cell basis.
 */
export default proposition({
  label: "prop:hopf-trace-formula",
  title: "Hopf trace formula for a two-step complex",
  uses: ["prop:bring-harmonic-types"],
  lean: {
    ref: "qou:QOU.Core.HopfTrace.ChainEnd.hopf_trace",
  },
  tags: ["brings-surface", "homology", "linear-algebra"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`QOU/Core/HopfTraceFormula.lean`). Replaces the cited Hopf trace formula " +
        "behind `hopf_trace_h1`. Still cited there: cellular homology of Bring's map equals " +
        "that of the surface with H0, H2 trivial and orientation; and Hodge. Bean qou-h0zz.",
    },
  ],
});
