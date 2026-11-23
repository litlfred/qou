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
  lean: {
    ref: "qou:QOU.Eightfold.HyperbolicMesonClaspAndDiquarkSplit.antiUp_down_same_weakSign_yet_distinct_charge",
  },
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
    {
      kind: "note",
      date: "2026-11-23",
      body: "Split-bundle framing (`qou-8fw2`, `qou-8fl1`, `qou-3oi0`): `QOU/Eightfold/HyperbolicMesonClaspAndDiquarkSplit.lean` proves over any `[Field K]` (`2 ≠ 0`, `3 ≠ 0`) that tracelessness of `diag(y₂, y₂, y₃, y₃, y₃)` in `End(V₂ ⊕ W₃*)` forces `y₃ = -(2/3) y₂` (`splitBundle_traceless_iff`), pins the exterior-pair doublet hypercharge `y₂ + y₃ = +1/3` and Killing-trace Weinberg ratio `(1/2)/(1/2 + 5/6) = 3/8` (`splitBundle_killing_traces`), separates `ū` (`-2/3`) from `d` (`-1/3`) by `+1/3 ≠ 0` despite equal weak/crossing sign `-1` (`antiUp_down_same_weakSign_yet_distinct_charge`), and proves `z₂(q) - z₃(q) = q³ / ((q² + 1)(q⁴ + q² + 1)) ≠ 0` (`zRank2_sub_zRank3`). Numerics verified at 80 dps in `computations/probes/sm8w_eightfold_clasp_diquark_gmo/sm8w_eightfold_clasp_diquark_gmo_probe.py` (`sm8w-eightfold-clasp-diquark-gmo.witness.json`).",
    },
  ],
});
