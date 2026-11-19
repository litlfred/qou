import { prose } from "../../schema/builders";

export default prose({
  label: "sec:cp-violation-evidence",
  uses: [
    "conj:complex-chirality-rotation",
    "prop:crossing-energy-decomposition",
    "def:crossing-energy",
    "prop:antiparticle-crossing-reversal",
  ],
  tags: [
    "cp-violation", "kaon", "b-meson", "CKM",
    "matter-antimatter", "experimental",
  ],
  cites: ["christenson1964", "aubert2001"],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "This block previously set θ_res ∼ tanh(ln r)·α_EM ≈ 7.5866e-4 and reported an asymmetry of order 1e-3 matching the kaon ε ≈ 2e-3 (ratio ≈ 0.38). With the phase removed the value is larger by exactly 1/α_EM, and the kaon agreement is lost. The correction was recorded because it is what the identity gives, not because it improves the comparison. Lean theorems: `QOU.Observations.crossingDisc_norm_theta_free` and `QOU.Observations.BarParityRankOne.isBarOdd_iff`.",
    },
  ],
});
