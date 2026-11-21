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
    {
      kind: "caveat",
      date: "2026-11-20",
      body:
        "**Photon last term changed by owner ruling (qou-99qc, 2026-11-18, confirmed 2026-11-20).** " +
        "`def:photon` now has fourth term σ₀σ₁⁻¹ instead of σ₀σ₁; the narrative above follows it. " +
        "The numeric six-term γγ NF in `tbl:four-term-pair-nucleon-table1-data` was computed with the old σ₀σ₁ term, " +
        "and neither its producer nor its colour weights are recorded in the block, so it has NOT been recomputed. " +
        "The proton/neutron nets 0.999 / 0.811 do not depend on the photon (confinement universality: flavours supplied as input) and are unaffected. " +
        "Symbolic γγ NF for the ruled photon: `tbl:trivial-knot-photon-interpretation-table5-data`, Lean `QOU.QuarkState.pairNFChiral_eq`.",
      see: "https://github.com/litlfred/qou/pull/8583",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([photon](#def:photon))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([confinement universality](#prop:confinement-universality))" },
  ],

});
