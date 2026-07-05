import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ew-triplet-charge-spin-from-involution",
  title:
    "Charge and spin of the electroweak triplet are forced by the spin-involution sector selection",
  lean: {
    ref: "qou:QOU.ParticleInteractions.ew_charge_spin_forced",
    validation: "not_checked",
  },
  // NB: does NOT `use` conj:electroweak-higgs-torus-link-triplet, to avoid a
  // dependency cycle (that conjecture `uses` this theorem) and a false-positive
  // conjectural-propagation flag. This theorem is honestly conditional on its
  // *own* in-type postulate class `EWSectorSelection` (the §3b-cond pattern);
  // the conceptual link to the C1 selection is a prose cross-reference in the .md.
  uses: [
    "def:spin-involution",
    "thm:hoefsmit-ew-cell-content",
    "prop:self-dual-higgs-real-volume",
    "prop:vdw-pskew-isolation",
    "def:coulomb-charge",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "Conditional-class theorem (§3b-cond): the Lean sibling axiomatises " +
        "the EW sector selection as the class `EWSectorSelection` (the single " +
        "physics postulate) and carries it as an explicit `[instance]` " +
        "hypothesis; charge and spin are then *derived* (sorry-free). This " +
        "collapses the former C3 (charge) and C4 (spin) — previously two " +
        "independent open primary conjectures — into proved consequences.",
    },
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "σ₅⁸ bar-grading is now DERIVED-FROM-SPIN, not merely stated (Task 2, " +
        "2026-07-05). The former owner ruling (σ₅⁸ carries both H = A₊ and " +
        "B = A₋) is upgraded to a sorry-free theorem `ew_sigma5_bargrade_forced`: " +
        "the sector→spin map is injective and inverts (`barSectorOfSpin`, proved " +
        "a genuine two-sided inverse by `barSectorOfSpin_inverts`), so given the " +
        "Higgs is a scalar (spin 0) and B a vector (spin 1) — independent " +
        "physical inputs — H ∈ A₊ and B ∈ A₋ of σ₅⁸ are FORCED, not chosen. The " +
        "only residual postulate is that both inhabit the one σ₅⁸ slot. " +
        "`conj:weinberg-angle-categorical` (reads A₋ = B) and " +
        "`conj:electroweak-higgs-torus-link-triplet` (reads A₊ = H) agree by " +
        "derivation. 4₁ in `prop:self-dual-higgs-real-volume` is the Higgs mass " +
        "MECHANISM (muon scale m_μ/m_e = Vol(4₁)/ℏ_q²), distinct from the " +
        "125-GeV Higgs boson H = T(2,8) = A₊ of σ₅⁸.",
    },
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "Task 1 (which-slot-is-W) HONEST assessment: W = σ₁⁴ is NOT forced — it " +
        "is a FREE LABEL. Corpus-grep found def:coulomb-charge (Q = ½·writhe) as " +
        "the only crossing→charge map, but on σ₁^{2k} it gives Q = k > 0 for all " +
        "three carriers (2,3,4) — makes W,Z,H all charged, cannot pick the " +
        "neutral slot; writhe→Y is falsified (2026-06-02-u1-hypercharge-" +
        "assignment.md, only writhe→I₃ survives). Forced part proved: charge ⇒ " +
        "A₋ doublet, A₊ singlet ⇒ neutral (`charged_are_doublets_singlet_" +
        "neutral`). Non-forcing proved: `which_slot_is_W_free` exhibits two " +
        "distinct labelings (W=σ₁⁴ and mirror W=σ₃⁶) both satisfying every " +
        "proved constraint. The paper's W=σ₁⁴ rests only on mass ordering " +
        "4<6<8 (necessary, not sufficient). What would force it: a genuine " +
        "crossing/linking→T₃ map — carried as the free-label field t3Label of " +
        "conj:electroweak-higgs-torus-link-triplet.",
    },
  ],
  tags: [
    "electroweak",
    "spin-involution",
    "isospin",
    "charge",
    "spin",
    "conditional-on-class",
    "weak-sector",
  ],
});
