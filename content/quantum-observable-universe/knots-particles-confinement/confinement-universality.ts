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
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/Interactions/confinementUniversality.lean` " +
        "quantifies over photon polarisation coefficients `(φ₀, φ₁, φ₀₁)`, which are continuous physical parameters. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
