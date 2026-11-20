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
      kind: "note",
      date: "2026-11-20",
      body:
        "**Photon last term changed by owner ruling (qou-99qc, 2026-11-18, confirmed 2026-11-20); data table 1 restated.** " +
        "`def:photon` has fourth term σ₀σ₁⁻¹ instead of σ₀σ₁; the narrative above follows it. " +
        "`tbl:four-term-pair-nucleon-table1-data` now has a producer (`computations/four_term_pair_nucleon_table.py`), which reproduces the old entries " +
        "with the old form and restates them with the ruled photon at the same reconstructed weights (σ₀: 0.099 → 0.090, the other entries move by at most 4e-4). " +
        "Those weights are labelled in the table: 0.0487 is a fit to 2m_e (Breit–Wheeler) and 0.02 is unsourced, so the table is a worked illustration, not a prediction. " +
        "The proton/neutron nets 0.999 / 0.811 do not depend on the photon (confinement universality: flavours supplied as input) and are unaffected; they are not recomputed by that producer. " +
        "Symbolic γγ NF for the ruled photon: `tbl:trivial-knot-photon-interpretation-table5-data`, Lean `QOU.QuarkState.pairNFChiral_eq`.",
      see: "https://github.com/litlfred/qou/pull/8583",
    },
  ],

});
