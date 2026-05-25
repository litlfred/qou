import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:lepton-tower-h-n-plus-1-branching",
  lean: {
    ref: "qou:QOU.BraidKnot.LeptonTowerHnPlus1.lepton_xi_branching",
    validation: "not_checked",
  },
  title:
    "Canonical lepton-mass-tower ξ_m factor is d_q(std_rep S_{n+1}) · [2]_q / [n+1]_q where n = 2m+1 is the lepton-knot torus index; this couples lepton σ_1^{2m+1} braid at H_3 substrate level with H_{n+1} standard-rep branching, matching the T6 closure factor [3]_q·[2]_q/[4]_q at m=2 (muon) numerically to 0.034% of CODATA.",
  uses: [
    "prop:lepton-bring-surface-h3-3channel",
    "prop:three-parameters-wedderburn",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**Open conjecture (PR #1127 T6 rest-of-work).** Identifies the categorical " +
        "origin of the structural factor [3]_q·[2]_q/[4]_q in the canonical lepton " +
        "mass-tower closure as d_q(std irrep of S_{n+1}) · [2]_q / [n+1]_q, where " +
        "n = 2m+1 is the torus index of the lepton's canonical knot σ_1^n. At q=1: " +
        "d((3,1)) = 3 (dim std rep of S_4), [2]=2, [4]=4 → factor = 3/2. " +
        "Derivation from the per-braid mass tower categorically OPEN. Tau case " +
        "(m=3) requires H_5 with std irrep (4,1) — would predict ξ_3 = " +
        "d_q((4,1))·[2]_q/[5]_q · (1/ℏ_q²) but T(2,7) at H_3 3-channel diverges; " +
        "needs H_5 embedding for tau which is multi-day analytical work.",
    },
    {
      kind: "refined-framing",
      date: "2026-05-25",
      body:
        "**Categorical interpretation candidate.** The factor [3]_q·[2]_q/[4]_q " +
        "matches d_q((3,1)) · [2]_q / [4]_q at q_0 ≈ 1.110 to 0.034%. " +
        "d_q((3,1)) = [3]_q via hook-length formula (S_4 standard rep). The [4]_q " +
        "denominator suggests an H_4 normalisation (4-strand level above the " +
        "3-strand lepton substrate). Conjectural reading: each lepton-tower step " +
        "m → m+1 adds one strand to the H_n substrate, with the canonical mass " +
        "correction picking up the q-dimension of the next std irrep d_q((n,1)) " +
        "weighted by [2]_q/[n+1]_q. Open derivation: the per-braid mass tower's " +
        "operator-valued A^λ_{μν}(I) branching coefficient (per prop:hecke-" +
        "branching-trace-decomposition) should reduce to this factor when " +
        "specialised to lepton inputs.",
    },
    {
      kind: "caveat",
      date: "2026-05-25",
      body:
        "**Tau case requires separate work.** The conjecture's prediction for " +
        "tau (m=3) is ξ_3 = d_q((4,1)) · [2]_q / [5]_q · (1/ℏ_q²) ≈ ? at q_0. " +
        "But T(2,7) under H_3 3-channel gives V̂ = 1.119 > q_0 = 1.110 — outside " +
        "Li_2^q convergence radius. Need to apply the formula at H_5 substrate " +
        "(5-strand) instead of H_3, with V̂_τ recomputed via per_generator_V_hat_general " +
        "at n=5. Multi-day analytical follow-up.",
    },
  ],
  tags: [
    "lepton",
    "mass-tower",
    "ksi-factor",
    "h-n-branching",
    "categorical-interpretation",
    "phase-3",
    "open-conjecture",
  ],
});
