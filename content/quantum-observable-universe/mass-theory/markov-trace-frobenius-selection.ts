import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-trace-frobenius-selection",
  proofs: ["prf:markov-trace-frobenius-selection"],
  title: "Markov trace uniqueness on H_n(R, q) — the Jones–Markov form τ_M",
  chapter: "mass-theory",
  cites: ["jones1987", "wenzl1988", "yekutieli2015"],
  uses: [],
  defines: [],
  tags: ["normalization", "frobenius", "no-fitting", "uniqueness"],
  lean: { ref: "qou:QOU.BraidKnot.qou_markov_trace_is_jones_markov" },
  authorNotes: [
    {
      kind: "note",
      date: "2026-05-29",
      body: "The degenerate Schur–Weyl candidate τ_SW was purged per owner decision A' (PR #1422). An earlier 2026-05-11 escalation framed the from-scratch result as a τ_M / τ_SW conflation; it is read instead as a different braid's τ_M.",
    },
  ],
});
