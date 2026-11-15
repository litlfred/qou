import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-universality",
  title: "Confinement universality: nucleon NF independent of photon polarization",
  tags: [
    "confinement",
    "universality",
    "photon",
    "polarization",
    "independence",
    "strong-force",
  ],
  lean: { ref: "qou:QOU.Interactions.confinementUniversality",
    validation: "not_checked",
  },
  uses: ["prop:four-term-pair-nucleon"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (superseded 2026-11-15).** " +
        "This note said the `ℝ` was forced by the statement. It is not: the statement " +
        "and proof use no structure of the coefficient type. The Lean context is now " +
        "parametrised by the coefficient type `K` and the NF type `M`, and `K = ℂ` " +
        "covers circular polarisations (bean `qou-qs2u`, PR #7825).",
    },
  ],

});
