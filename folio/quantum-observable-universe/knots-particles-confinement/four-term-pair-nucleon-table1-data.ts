import { table } from "../../schema/builders";
export default table({
  label: "tbl:four-term-pair-nucleon-table1-data",
  title: "Data table 1 from prop:four-term-pair-nucleon",
  uses: ["prop:four-term-pair-nucleon"],
  tags: ["extracted-table"],
  computation: {
    engine: "python",
    script: "computations/four_term_pair_nucleon_table.py",
    witness: "computations/four-term-pair-nucleon-table.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-20",
      body:
        "**Restated with the ruled photon (owner, 2026-11-20: \"pair-nucleon table: restate it with the new photon\"; bean qou-99qc).** " +
        "The table was computed with the old fourth term σ₀σ₁ and had no producer or recorded weights. " +
        "Producer `computations/four_term_pair_nucleon_table.py` (exact over ℚ(q), proton q₀, 70 dps) first recomputes the OLD table " +
        "as γ_old(φ)² with φ = (0.0487, 0.0487, 0.02) and reproduces all six recorded entries at their 3-decimal rounding, " +
        "then restates it with γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹ at the same weights. " +
        "Before → after (3 dp): 1: 1.005 → 1.004; σ₀: 0.099 → 0.090; σ₁: 0.099 → 0.099; L₊: 0.043 → 0.043; L₋: 0.003 → 0.003; e⁻: 0.002 → 0.002. " +
        "At 70 dps σ₀ moves 0.0988698 → 0.0904259 (the only move above 4e-4), because γ(φ₀, φ₁, φ₀₁) = γ_old(φ₀ − hφ₀₁, φ₁, φ₀₁) exactly; σ₀ and σ₁ are no longer equal. " +
        "**The weights are reconstructed, not derived:** 0.0487 = fit to 2m_e (Breit–Wheeler); 0.02 = unsourced, reconstructed by matching the old rounded entries. " +
        "On a grid (a step 1e-4, b step 1e-3) the old entries are reproduced for a ∈ [0.0486, 0.0490], b = 0.020 only, so the reconstruction is not unique in a. " +
        "The table is a worked illustration of the γγ normal form, not a prediction. " +
        "Second column: the corpus-derived eigenvalue pair γ₊ = γ(0,0,qh), γ₋ = γ(0,0,−q⁻¹h) of prop:borromean-two-photon-factorisation, γ₊γ₋ = (σ₀σ₁⁻¹)³; it has no e⁻ term. " +
        "The nucleon nets 0.999 / 0.811 of prop:four-term-pair-nucleon do not depend on the photon (prop:confinement-universality: the confinement word contains no photon coefficient) and are not recomputed here.",
      see: "https://github.com/litlfred/qou/pull/8583",
    },
  ],
});
