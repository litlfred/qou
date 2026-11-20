import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ew-triplet-charge-spin-from-involution",
  title:
    "Sector label and charge of the electroweak triplet computed through the spin involution",
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
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "T₃ and mixing tested against the skew charge (sorry-free, same Lean " +
        "sibling). `ewT3Double_not_affine_in_charge`: the table is not λ·Q + μ. " +
        "`t3OfSkew_values`: Q/Q(W⁺) gives 1, −1, 0 on W⁺, W⁻, H and ≠ 0 on Z. " +
        "`sgnT3Double_values` / `_vs_table`: the def:spin-involution rule with " +
        "the sign read off Q (ordered field, a > 1) gives Z ↦ 1, disagreeing " +
        "with the table only at Z; H ↦ 0 follows from H ∈ A₊. " +
        "`mixing_neutral_both_iff` / `mixing_cannot_neutralise_model`: a " +
        "rotation with c² + s² = 1 preserves x² + y², so linear mixing cannot " +
        "make Z and γ both neutral when Q(W³) ≠ 0; the previous sentence " +
        "attributing Z neutrality to mixing is withdrawn. The ewT3Double values " +
        "±1 read as 2·T₃ are doublet values, not the triplet T₃ = ±1 of the .md.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body:
        "Self-assuming projection removed (owner-authorised QA fix). The old " +
        "`ew_charge_spin_forced` returned the class fields `wPlus_t3` … " +
        "`higgs_t3` as its T₃ conjuncts, and defined spin directly from " +
        "`isSinglet`, so σ was never used. `EWSectorSelection` now carries " +
        "inputs only (sectors, carrier eigenvalues, W⁻ = σ-image of W⁺, " +
        "a² ≠ 1); `spinDouble` is computed from whether `swap₂` fixes the " +
        "sector vector and `ewCharge` is its skew. T₃ is no longer in the " +
        "class or the theorem: it is the recorded table `ewT3Double`. " +
        "`z_not_neutral_by_parity` records that σ-parity makes Z charged. " +
        "`def:coulomb-charge` and `rem:chirality-trefoil-electron-positron` " +
        "were dropped from uses[]: only the Task 1/1′ side lemmas use them, " +
        "not the theorem. The earlier notes below describe the pre-fix " +
        "statement where they say charge is 'derived'.",
    },
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
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "Task 1′ (signed σ↔σ⁻¹ / C-invariance test, 2026-07-05): tried to FORCE " +
        "the W-slot label with the two ingredients the prior result named — a " +
        "signed crossing asymmetry and a second baryon/color-trace charge. " +
        "NEITHER forces it; proved the SHARPER NEGATIVE. Charge conjugation " +
        "C = crossing reversal negates writhe (rem:chirality-trefoil-electron-" +
        "positron), so neutral ⟺ C-invariant ⟺ amphichiral (w=0), proved " +
        "`cInvariant_iff_writhe_zero` (−w=w ↔ w=0, by omega). (i) Signed test " +
        "does NOT force: `signed_which_slot_is_W_free` exhibits two distinct " +
        "C-consistent labelings. (ii) But it EXCLUDES every pure even-twist slot " +
        "from neutrality: `evenTwist_not_cInvariant` (writhe 2k≠0 for σ₁⁴,σ₃⁶," +
        "σ₅⁸), so the neutral Z is NECESSARILY the mixed (W³,B)→(Z,γ) Weinberg " +
        "state, not a single slot — upgrading which_slot_is_W_free with the " +
        "reason. (iii) The second charge is a MISSING corpus object (audit " +
        "2026-06-02); `second_charge_would_force_neutral_slot` is the proved " +
        "conditional pinpointing exactly what is absent. Capstone: " +
        "`signed_C_does_not_force_W_slot_but_forces_neutral_mixed`, all sorry-" +
        "free, base ring ℤ. lean-direct exit 0 on lake-cache/qou-v4-24-0.",
    },
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "Task 1′ sharpening (2026-07-05, two more theorems). (A) NEGATIVE — the " +
        "NAMED second-charge candidates provably don't force the label: " +
        "`named_second_charge_candidates_do_not_force_label` shows the Milnor " +
        "triple linking μ̄(123) ≡ 0 on every even-twist carrier (2-component ⇒ no " +
        "triple) AND the pairwise linking Lk(T(2,2k)) = k ≠ 0 on all carriers " +
        "(k=2,3,4) — so neither satisfies `second_charge_would_force_neutral_" +
        "slot`'s hypothesis (nonzero on exactly one slot). Non-vacuous (real " +
        "rfl/decide, two distinct ways of missing the datum). (B) CONDITIONAL-" +
        "POSITIVE — the group-structure data DOES force it: open §3b-cond class " +
        "`EWGroupAssignment` carries WHICH vector slot is the su(2)_L Cartan (W³) " +
        "vs charged root (W±) member (a group datum, NOT the T₃ conclusion); " +
        "`label_forced_given_group_assignment` DERIVES 2T₃ = 0 for the Cartan " +
        "slot, 2 for the charged slot, and neutral ⟺ Cartan slot, via the adjoint " +
        "zero-weight rule (weights {+1,0,−1}). No instance supplied — stays the " +
        "open (W³,B)→(Z,γ) Weinberg mixing input (conj:weinberg-angle-" +
        "categorical). Net: label unforced by any single-slot topological " +
        "invariant, forced only by the conjectural SU(2)_L×U(1)_Y assignment — " +
        "RELOCATES the postulate, does not close it. Whole file lean-direct " +
        "exit 0 (no warnings) on lake-cache/qou-v4-24-0.",
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
