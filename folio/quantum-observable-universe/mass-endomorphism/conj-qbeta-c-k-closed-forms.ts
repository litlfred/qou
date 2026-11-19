import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qbeta-c-k-closed-forms",
  lean: {
    ref: "qou:QOU.BraidKnot.QBetaCKClosedForms",
    validation: "not_checked",
  },
  title:
    "Higher-order $\\mathfrak{Q}_\\beta$ ladder coefficients $c_k$ ($k \\ge 4$): retired Convention-C pattern guesses vs Convention-D generating-function structure",
  uses: ["rem:per-block-hopf-jones-absorption-pattern"],
  cites: [
    "khovanov2000",
    "khovanov-rozansky2008",
    "khovanovlauda2009",
    "wenzl1988",
    "hoefsmit1974",
    "jones1985",
  ],
  tags: [
    "lean-infrastructure",
    "open-rd",
    "precision-ladder",
    "empirical-conjecture",
    "khovanov-rozansky",
    "klr-canonical-basis",
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/qbeta_convention_d_all_order_ck_generating_probe.py",
    witness: [
      "computations/qbeta/qbeta-convention-d-all-order-ck-generating.witness.json",
      "computations/qbeta/qbeta-convention-d-c4-quartic-derivation.witness.json",
    ],
    status: "verified",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-19",
      body: "Updated to reflect the proved Wave-2 Convention-D formalizations while keeping genuinely open higher-order questions explicit:\n(1) `QOU.QBeta.ConventionDAllOrderCkGeneratingFunction` proves the bar-even `H = (q - q⁻¹)^2` operator generating function `Π_op(u) = ∏_{k≥2} (1 + c_k u^k) = 1 + ∑_{n≥2} p_n u^n`, strict monotonicity of `uBarSq(H)` on `H ≥ 0`, the Lagrange–Bürmann critical branch point `H_* = (-15 + √33)/4 ∈ (-3, -2)` (`R_u ≈ 0.36900873`), the division-free distinct-partition polynomial bijection between `(c_2, ..., c_{10})` and `(p_2, ..., p_{10})`, and the `< 10⁻¹⁶` (`< 1 ppQ`) geometric Cauchy tail bound at `N = 9`.\n(2) `QOU.QBeta.ConventionDC3AndTailSelectionDerivation` proves the five-letter valence/gluon tail characterization (`qou-j1e5`) and the operator-level Habiro–Kashiwara `N = 3` expansion in `y = (q + q⁻¹) - 2 = q ℏ_q^2` (`c_2 = -1`, `c_3 = -2`).\n(3) `QOU.QBeta.ConventionDC4QuarticCumulantDerivation` proves rationality of all even Habiro rungs `u(q)^{2m} ∈ ℚ(q)`, the `m = 2` Kashiwara divided-power cosine coefficient `[2]_q / ([3]_q [4]_q) → +1/6` (matching the Convention-D Jucys–Murphy excess-kurtosis rung `1/2 + γ_2^D(1)/6 = +1/6`, vs GPMT+ 3-block kurtosis `+101/288`), and `u(q_0)^4 < 6 × 10⁻⁹` (`< 10⁻⁴ σ_exp(m_n)`).\n(4) Uniquely selecting a single canonical operator projection for individual `c_k` (`k ≥ 4`) and closed-form categorical expressions for `k ≥ 5` remain open; the historical Convention-C pattern guesses (`c_4 = -2 b^4`, `c_5 = -(b^2 + 1/2)`, `c_6 = 4 b^2`, `c_7 = -8`) remain retired calibration records in the uninhabited `QBetaCKClosedForms` class.",
    },
  ],
});
