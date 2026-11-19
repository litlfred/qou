import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-s-classification",
  title: "Frobenius S-eigenvalue classification of the 3-term mass formula",
  lean: {
    ref: "qou:QOU.WedderburnMass.frobenius_s_classification",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula", "prop:confined-knot-binding"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-10-10",
      body:
        "**Restated (owner ruling 2026-10-10, bean `qou-fd2u`).** The statement previously " +
        "said that exactly one of the three terms is `S`-anti-invariant (the chirality term) " +
        "and that `S`-symmetric blends cannot capture chirality. Under convention D the raw " +
        "`Φ₁` is not an `S`-eigenvector, so `m(Sβ) − m(β) = −2α(Φ₁⁻ + h²Φ₃)` has two " +
        /* <!-- literal-source: closed-form evaluation of h^2 * Phi_3 from frobenius_s_parity_convention_d_probe.py (identity probe, no witness file) --> */
        "`S`-odd channels; at the proton pin `Φ₁⁻ ≈ 0.0526` against `h²Φ₃ ≈ 0.00912` " +
        "(`computations/probes/frobenius_s_parity_convention_d_probe.py`). The formula keeps " +
        "the raw `Φ₁`; the claim is restated. Lean: `mass_S_difference`, " +
        "`chirality_sole_S_odd_channel_iff`, `s_invariant_ansatz_captures_S_odd_iff`; the " +
        "former `chirality_is_unique_S_odd` was removed.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/h2_gg_electron/h2_gg_electron_probe.py",
    witness: "computations/probes/h2_gg_electron/h2-gg-electron.witness.json",
    status: "verified",
  },
});
