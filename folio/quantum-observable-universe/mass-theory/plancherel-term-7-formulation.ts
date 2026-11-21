import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:plancherel-term-7-formulation",
  title:
    "Universal residue at curvature-rank $k \\geq 4$ (Molien-weighted log functional)",
  lean: {
    ref: "qou:QOU.WedderburnMass.plancherel_term_7",
    validation: "not_checked",
  },
  uses: [
    "prop:spectral-sequence-collapse",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **One caution on citing the identity.** `molienSum_eq_qFactorial` is $" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): it remains valid within a single $n$, by `QOU.BraidKnot.WLambdaNormalizationInvariance.ratio_invariant`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Measurements: [`2026-09-04-plancherel-convention-gap.md`](../../../docs/audits/2026-09-04-plancherel-convention-gap.md); producers [`probes/molien_feray_meliot_bridge_probe.py`](../../../computations/probes/molien_feray_meliot_bridge_probe.py), [`probes/plancherel_deformation_uniqueness_probe.py`](../../../computations/probes/plancherel_deformation_uniqueness_probe.py), [`audits/w_lambda_family_consumer_audit.py`](../../../computations/audits/w_lambda_family_consumer_audit.py); registry [§B-norm](../../../docs/coordination/trace-convention-registry.md)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): So [`fr_pullback_k3_test.py`](../../../computations/fr_pullback_k3_test.py) computes and reports **both arms**, Molien primary." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): All six candidates in [`beta_ew_delta_I_321_and_wedderburn.py`](../../../computations/beta_ew_delta_I_321_and_wedderburn.py) are ratios" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Measured instances: [`probes/deuteron_fpn_wlambda_wiring.py`](../../../computations/probes/deuteron_fpn_wlambda_wiring.py) and [`yekutieli_volume_join.py`](../../../computations/yekutieli_volume_join.py)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): $\\tau(T_w) = \\delta_{w,1}$: `QOU.SchurWeyl.ocneanuWeight_zero_eq_molienWeight` identifies the Ocneanu weight at $z = 0$ with the Molien weight, and `QOU.SchurWeyl.sum_dim_molienWeight_eq_one` is the normalisation $\\tau(1) = 1$." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (at $n = 4$, `QOU.QBeta.MolienJonesMarkovN4.n4_markov_normalisation`)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): of `QOU.QBeta.MolienJonesMarkovN3` and `QOU.QBeta.MolienJonesMarkovN4`, a generating function" },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body: "Restated on owner approval from the Molien critical analysis: normalisation is shared by every Markov trace, so the distinguishing property is the z = 0 symmetrising trace; the κ-forcing scan over c ∈ [−3,3] replaced by the n = 2 argument; the n ≤ 9 Féray–Méliot check replaced by the hook-sum identity; the unreproduced \"≈ 0.457 at n = 6\" replaced by measured values (0.922 at q₀, 0.061 at q = 2, balanced convention); \"Molien\" disambiguated; Wenzl-family remark added. Steinberg's coinvariant theorem is named in prose; no bibliography key exists for it yet.",
    },
    {
      kind: "note",
      body: "An earlier version of the citation-caution paragraph wrote the Molien weight without the q^{-κ_λ} factor.",
    },
    {
      kind: "status",
      date: "2026-09-05",
      body:
        "**Weight family fixed to Molien.** The functional was defined " +
        "against `dim_q^2/[n]_q!` until this date; the replacement to " +
        "`f^lambda q^{-kappa} dim_q/[n]_q!` follows an owner ruling on " +
        "bean `qou-oots`. The two are not one normalisation apart — they " +
        "differ by up to 1831x per partition at n = 9 (= A = 3). The " +
        "requirement set R1/R2/R3 does NOT separate Molien from " +
        "`dim_q^2/D^2` (R2 asks only that the normaliser be " +
        "n-independent, and both satisfy it), so the second is retained " +
        "as a labelled comparison arm rather than dropped, and " +
        "`fr_pullback_k3_test.py` reports both. The two arms DISAGREE on " +
        "the best k=3 knot: Molien ranks 5_2 (+21.4%, with 6_1 worse " +
        "than baseline), `dim_q^2/D^2` ranks 6_1 (+1.7%).",
      see: "computations/fr_pullback_k3_test.py",
    },
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `mass-theory/plancherel-term-7-formulation.lean` " +
        "uses `Real.exp`, `Real.log`. These are real-analytic constructs " +
        "with no generic-`CommRing` counterpart, so the `ℝ` " +
        "specialisation is forced by the statement itself rather than " +
        "chosen. The block therefore sits on the archimedean side of the " +
        "§7c wall by construction.",
    },
  ],
});
