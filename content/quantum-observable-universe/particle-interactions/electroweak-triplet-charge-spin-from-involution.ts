import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:ew-triplet-charge-spin-from-involution",
  title:
    "Charge and spin of the electroweak triplet are forced by the spin-involution sector selection",
  lean: {
    ref: "qou:QOU.ParticleInteractions.ew_charge_spin_forced",
    validation: "not_checked",
  },
  uses: [
    "conj:electroweak-higgs-torus-link-triplet",
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
      kind: "caveat",
      date: "2026-07-05",
      body:
        "TENSION FLAGGED FOR OWNER (σ₅⁸ = B vs H). `conj:weinberg-angle-" +
        "categorical` reads the Hoefsmit slot σ₅⁸ as the U(1)_Y singlet `B` " +
        "(pre-mixing), whereas `conj:electroweak-higgs-torus-link-triplet` " +
        "reads σ₅⁸ (= T(2,8), strands 5–6) as the Higgs `H`. Both are " +
        "singlet-like (bar-even / A₊), but B (a gauge singlet that mixes into " +
        "Z, γ) and H (the scalar) are distinct particles. The Z-neutral-via-" +
        "mixing field `z_t3 = 0` of `EWSectorSelection` is where this bites. " +
        "Not silently resolved — needs an owner ruling on the σ₅⁸ assignment.",
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
