import { remark } from "../../schema/builders";

/**
 * The flavor charge assignments (I₃, Y) from the A₂ weight lattice.
 *
 * Connects the hexagonal weight lattice of §1 to the physical
 * quantum numbers. The isospin I₃ is the writhe-derived invariant
 * (proved). The hypercharge Y is the open problem: requires a second
 * crossing invariant (ribbon twist candidate identified but untested).
 *
 * ANTI-FITTING: States the open problem honestly. Does NOT import
 * Y from external sources. The Gell-Mann–Nishijima relation is
 * a consistency battery, not an axiom.
 */
export default remark({
  label: "rem:flavor-charge-assignments",
  title: "Flavor charge assignments and the hypercharge gap",
  interprets: "prop:a2-from-three-strands",
  uses: [
    "prop:a2-from-three-strands",
    "def:coulomb-charge",
    "conj:sm-hypercharge-invariant",
    "conj:electroweak-higgs-torus-link-triplet",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): is multiset counting. Proved in\n`QOU/StandardModel/TwistBatteryVacuity.lean`:\n\nIn\n   `strand_twist_y_battery.py` it is a function of the\n\nonly consistent with them. See\n`strand-twist-y-battery.witness.json`." },
    {
      kind: "note",
      date: "2026-11-22",
      body: "Sources for the 2026-11-22 edits (issue #9102, PR #9103; audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §28–§29). Injective-only falsification: `QOU/StandardModel/WritheIndependenceCriterion.lean` (`pn_test_admits_writhe_only_map`, `injective_writhe_map_is_falsified`). Quark charge not a writhe function: `QOU/StandardModel/QuarkBraidChargeObstruction.lean`. Y factors through w when Q and I₃ do: `QOU/StandardModel/WritheChargeLeavesNoHypercharge.lean`. Y = B on the nucleon doublet: `QOU/StandardModel/HyperchargeBatteryReduction.lean` (`nucleon_hypercharge_eq_baryon_number`; read from the Standard-Model table, not derived). Strand charge and block charge a − 1: `QOU/QBeta/WeylSymmetricPairNotCoulomb.lean` (`blockCharge_eq`). μ̄₁₂₃ = B candidate: `QOU/StandardModel/SecondCrossingInvariant.lean` (class, no instance). Exchange split and nucleon values: `QOU/QBeta/NeutralExchangeSplit.lean` (`neutralExchange_split`, `nucleon_unbroken_isospin`, `nucleon_photon_coulomb`). Coulomb iff the Z part is removed: `QOU/QBeta/CoulombNeedsZRemoval.lean`. All sorry-free. The Weinberg-angle conjecture (`conj:weinberg-angle-categorical`) is named without a link because it comes later in reading order. Lepton number: bean `qou-kl39`; Z / electroweak scale: bean `qou-z3x8`.",
    },
  ],
});
