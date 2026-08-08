import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:four-term-pair-nucleon",
  lean: { ref: "qou:QOU.ParticleInteractions.four_term_pair_nucleon", validation: "not_checked" },
  title: "Nucleon derivation from 4-term photon pair production",
  tags: [
    "pair-production",
    "nucleon",
    "proton",
    "neutron",
    "4-term-photon",
    "color-content",
    "borromean",
    "derivation",
  ],
  uses: [
    "def:quark-antiquark-production",
    "prop:confinement-operator-selection",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean` " +
        "declares measured nucleon net targets as decimal literals (`protonNetTarget : ℝ := 0.999`, `neutronNetTarget := 0.811`). " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
