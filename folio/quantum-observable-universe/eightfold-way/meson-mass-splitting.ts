import { remark } from "../../schema/builders";

/**
 * Meson mass splitting via q-deformation.
 *
 * Explains how the crossing energy E_×(q) and quantum dimensions
 * split the mass degeneracy of the meson octet. The hexagonal
 * weight pattern is q-independent; the dynamics (mass, transitions)
 * are q-dependent.
 *
 * ANTI-FITTING: The Gell-Mann-Okubo relation is stated as an
 * open cross-check, not claimed as derived. Conditional on N=3 and Y.
 */
export default remark({
  label: "rem:meson-mass-splitting",
  title: "Meson mass splitting from q-deformed dynamics",
  interprets: "prop:meson-octet-decomposition",
  // Lean backs the NEGATIVE result: GMO is an identity of the first-order
  // octet ansatz and therefore cannot discriminate between mechanisms. It does
  // NOT back any derivation of the splitting — see bean qou-8pl2.
  // The ref now names a DECLARATION, not the module. `gmo_cannot_discriminate`
  // is the negative result stated above: two different breaking parameter sets
  // (a,b,c) and (a',b',c') both satisfy GMO, so the relation cannot select
  // between mechanisms.
  lean: {
    ref: "qou:QOU.Eightfold.GellMannOkuboIdentity.gmo_cannot_discriminate",
  },
  uses: [
    "prop:a2-from-three-strands",
    "rem:q-deformation-weight-lattice",
    "prop:meson-octet-decomposition",
  ],
  cites: ["gellmann1962", "okubo1962", "kleinkreisler1996"],
  computation: {
    engine: "mpmath",
    script:
      "computations/probes/sm8w_eightfold_clasp_diquark_gmo/sm8w_eightfold_clasp_diquark_gmo_probe.py",
    witness:
      "computations/probes/sm8w_eightfold_clasp_diquark_gmo/sm8w-eightfold-clasp-diquark-gmo.witness.json",
    status: "verified",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is proved over any commutative ring in\n`QOU/Eightfold/GellMannOkuboIdentity.lean`\n, together with the sharper consequence\n`gmo_cannot_discriminate`: two arbitrarily" },
    {
      kind: "note",
      date: "2026-11-23",
      body: "Second-order GMO and 3-strand hyperbolic meson clasp (`qou-8fw2`, `qou-3ttt`, `qou-qpj9`, `qou-c9uj`): `QOU/Eightfold/GellMannOkuboIdentity.lean` and `QOU/Eightfold/GellMannOkuboSecondOrder.lean` (surjectivity of generic 2nd-order `(I,Y)` polynomial onto every GMO residual) are wired into `QOU.lean`, and `QOU/Eightfold/HyperbolicMesonClaspAndDiquarkSplit.lean` proves (1) the parameter-free rational quantum Casimir law `(4 M_K - 3 M_η - M_π)/(M_π - M_η) = -((q - 1)/(q + 1))² = -(q - q⁻¹)² / ([2]_q + 2)²` (`qCasimir_gmo_second_order_and_universal_ratio`), matching both meson (`+`) and baryon (`-`) PDG-2024 residual signs at `q₀` (`-0.0027168155`, explaining `1.21%` of the `6.43%` isospin-averaged meson deviation and `0.82%` of the `-0.57%` baryon deviation), and (2) the 3-strand gluon-clasp map `β_clasp(n₁, n₂) = σ₁^{n₁} σ₂^{-n₂} σ₁ σ₂⁻¹` (`claspSL2_det_and_trace`, `claspSL2_hyperbolic_all_generations`, `claspMarkovTrace_separates_Dbar0_K0`), separating `D̄⁰ = (5,3)` from `K⁰ = (3,5)` by `0.21247128` (`z₂`) and `0.14415739` (`z₃`).",
    },
  ],
});
