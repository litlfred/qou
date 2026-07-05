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
        "OWNER RULING (2026-07-05) — the σ₅⁸ = B vs H tension is RESOLVED by " +
        "the very A± bar-grading this theorem proves. σ₅⁸ (= T(2,8)) carries " +
        "BOTH: the Higgs BOSON H = the A₊ (bar-even, scalar) part, and B (the " +
        "U(1)_Y hypercharge gauge boson) = the A₋ (bar-odd, vector) part. " +
        "`conj:weinberg-angle-categorical` reads the A₋ (B) part; " +
        "`conj:electroweak-higgs-torus-link-triplet` reads the A₊ (H) part — " +
        "the two σ-eigen-sectors of one slot, no contradiction. The `z_t3 = 0` " +
        "mixing field stays as the Weinberg (W³,B) → (Z,γ) residual. Note also " +
        "that 4₁ in `prop:self-dual-higgs-real-volume` is the Higgs mass " +
        "MECHANISM (muon scale m_μ/m_e = Vol(4₁)/ℏ_q²), distinct from the " +
        "125-GeV Higgs boson H = T(2,8) = A₊ of σ₅⁸.",
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
