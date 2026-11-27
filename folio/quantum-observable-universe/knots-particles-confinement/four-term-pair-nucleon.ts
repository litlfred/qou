import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:four-term-pair-nucleon",
  renamedFrom: ["prop:four-term-pair-nucleon"],
  lean: { ref: "qou:QOU.Confinement.four_term_pair_nucleon", validation: "not_checked" },
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
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` inhabits unparameterised `FourTermPairNucleonContext` via a 1-bit flavour lookup.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "**Demoted from prop: to conj: (owner card, 2026-11-21, \"Demote both\").** " +
        "The Lean theorem `four_term_pair_nucleon` returns the two nets from fields of `FourTermPairNucleonContext`; nothing in Lean computes them. " +
        "A proof needs the Gröbner–Shirshov reduction and the Markov trace in Lean, which are not there. Issue #8911, PR #8912.",
    },
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
    {
      kind: "caveat",
      date: "2026-11-21",
      body:
        "**Construction predates the 2026-11-21 γγ selection ruling.** The owner now rules that the γγ word is selected by whole-word U(1) neutrality, which picks V³ = (σ₀σ₁⁻¹)³ = β_Bor uniquely up to 10 crossings (`docs/coordination/owner-rulings.md`; `QOU/PhotonU1NeutralCut.lean`). " +
        "This block instead builds each nucleon as 𝓑₃ times three pair words whose flavours (u,u,d) / (u,d,d) are supplied by hand, so the p/n difference is an input, not a selection. " +
        "Its Lean theorem `four_term_pair_nucleon` returns the two net values from fields of `FourTermPairNucleonContext` (a self-assuming carrier); nothing in Lean computes 0.999 or 0.811.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([photon](#def:photon))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict):  ([confinement universality](#prop:confinement-universality))" },
  ],

});
