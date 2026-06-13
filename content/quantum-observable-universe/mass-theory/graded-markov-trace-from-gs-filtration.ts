import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:graded-markov-trace-from-gs-filtration",
  title:
    "Graded Markov trace as the induced trace on $J^\\ell / J^{\\ell+1}$",
  lean: {
    ref: "qou:QOU.BraidKnot.GradedMarkovTraceFromGSFiltration",
    validation: "not_checked",
  },
  cites: [
    "kassel1995",
    "geckpfeiffer2000",
    "ariki1996",
    "mathas1999",
  ],
  tags: [
    "graded-trace",
    "gb-filtration",
    "markov-trace",
    "associated-graded",
    "spectral-sequence",
    "narrative-replacement",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Status: provable** in pure Hecke combinatorics, conditional on the\nGS filtration's two-sidedness\n([`prop:gb-spectral-sequence`](#prop\\:gb-spectral-sequence)) and\nthe Markov-trace uniqueness theorem\n\\cite{kassel1995, geckpfeiffer2000}.  The downstream effect is\nthat the Lean `noncomputable opaque gradedMarkovTrace` can be\n**replaced** by a `def` plus a `theorem` body; this refactor is\nthe Lean-side action item for P2.6, deferred to Phase 2 of the\nalgebraic-refactor branch.",
    },
  ],
});
