import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-08-29",
      body: "**Correction (2026-08-29, bean `qou-toul`).** This block previously assigned $\\tfrac{1}{2}(n_+ + n_-)$ to the symmetric channel and $Q = \\tfrac{1}{2}(n_+ - n_-)$ to the antisymmetric one — the two multiplicities exchanged. That decomposition does not reconstruct $\\mathfrak{E}_{\\mathrm{cross}}$: it exceeds it by $2 n_- q^{-1}$, agreeing only on positive braids. It also stated the $\\tanh(\\ln q)$ ratio unconditionally, where it holds only at $n_- = 0$, and read the trichotomy $Q \\lessgtr 0$ as attractive-versus-repulsive Coulomb, which the corrected assignment does not support. [The channel decomposition](#prop:crossing-energy-decomposition) carried the correct multiplicities throughout; this block and its Lean sibling were the outliers.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): By [the channel decomposition](#prop:crossing-energy-decomposition), the crossing energy" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): [an open problem](#conj:sm-hypercharge-invariant)" },
    {
      kind: "note",
      date: "2026-11-22",
      body: "Sources for the 2026-11-22 additions (issue #9102, PR #9103; audit `docs/audits/2026-11-21-neutron-heavier-sign.md` §26–§29). Quarks: `QOU/StandardModel/QuarkBraidChargeObstruction.lean` (`linear_charge_map_refuted`, `charge_not_factoring_through_writhe`). Hypercharge: `QOU/StandardModel/WritheChargeLeavesNoHypercharge.lean` (`hypercharge_factors_of_charge_and_isospin_factor`, `isospin_not_writhe_of_charge_writhe`). Item 1: `QOU/QBeta/HeckeSeriesCollapse.lean` (`pow_eq_affine`, `sum_pow_eq_affine`, `coulomb_of_affine`) and `QOU/QBeta/TwoBlockExchangeNotCoulomb.lean` (`not_coulomb_*`). Item 2: `computations/probes/np_splitting/np_charge_vertex_search_probe.py` (audit §27A; exact over Q(q) in the second round below). Item 3: `QOU/QBeta/WeightShiftZeroTrace.lean` (`sectorTrace_eq_zero_of_shift`, `gaudin_readout`) and `QOU/QBeta/WeylSymmetricPairNotCoulomb.lean` (`invCartan_pp_eq_nn`, `coulomb_kappa_zero_of_pp_eq_nn`, `coulombPair_pp_ne_nn`, `blockCharge_eq`); q-Casimir and monodromy from `np_gaudin_pair_charge_probe.py` (exact over Q(q) in the second round below). Item 4: audit §27C. Requirement: `QOU/QBeta/NeutralExchangeSplit.lean` (`neutralExchange_split`) and `QOU/QBeta/CoulombNeedsZRemoval.lean` (`coulombShape_iff_Z_removed`, `photon_coupling_eq_zero_iff`). All Lean cited is sorry-free. Tower status: items 2–4 are n = 6 (n ≤ 9 for item 4); the tower in n is open.",
    },
    {
      kind: "note",
      date: "2026-11-22",
      body: "Second round (owner ruling 2026-11-22, \"Do all\" on #9103; audit `docs/audits/2026-11-22-coulomb-all-q-and-nucleon-writhe.md`). Nucleons: the ruled word β_Bor has writhe 0 (`QOU/Mass/GammaGammaWordSelection.lean`, `borromean_writhe`); `QOU/StandardModel/NucleonWritheCharge.lean` (`charge_not_writhe_on_nucleons`, `halved_writhe_proton_charge_zero`) and `WritheChargeLeavesNoHypercharge.lean` (`charge_not_writhe_of_equal_writhe`), sorry-free. The framing writhes ±2 recorded in `WritheIndependenceCriterion.lean` are the Hopf-link pair framings of the 2026-06-01/02 audits, and ±1 is the inter-nucleon arc; neither is the writhe of β_Bor. Items 2 and 3 are now exact over Q(q) at n = 6 (`computations/probes/np_splitting/np_all_q_symbolic_probe.py`, pre-registered; computer algebra, not Lean). The excluded q are the zeros of the denominator of α and of the elimination pivots, none of them q₀.",
    },
  ],
  label: "def:coulomb-charge",
  title: "Coulomb charge of a knot composite",
  tags: ["coulomb", "charge", "crossing", "asymmetry", "skein"],
  lean: { ref: "qou:QOU.Braiding.CoulombCharge",
    validation: "not_checked",
  },
  uses: [
    "def:crossing-energy",
  ],
});
