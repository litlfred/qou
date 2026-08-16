import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:lepton-tower-h-n-plus-1-branching",
  lean: {
    ref: "qou:QOU.BraidKnot.LeptonTowerHnPlus1.lepton_xi",
    validation: "not_checked",
  },
  title:
    "Canonical lepton-mass-tower factor ξ_m = [2m-1]_q · [m]_q / [2m]_q: matches muon (m=2 → [3]_q·[2]_q/[4]_q, 0.001%) and tau (m=3 → [5]_q·[3]_q/[6]_q, +0.79%) of CODATA. Supersedes the earlier muon-only d_q(std_rep S_{n+1})·[2]_q/[n+1]_q reading (whose tau prediction was falsified); categorical derivation of the q-bracket form remains open.",
  uses: [
    "prop:three-parameters-wedderburn",
    "prop:three-halves-structural-factor",
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
        "But T(2,7) under H_3 3-channel gives $\hat{V}$ = 1.119 > q_0 = 1.110 — outside " +
        "Li_2^q convergence radius. Need to apply the formula at H_5 substrate " +
        "(5-strand) instead of H_3, with $\hat{V}_\tau$ recomputed via per_generator_V_hat_general " +
        "at n=5. Multi-day analytical follow-up.",
    },
    {
      kind: "refined-framing",
      date: "2026-05-25",
      body:
        "**PR #1253 tau finding — amphichiral closure via [5]_q · [3]_q / [6]_q.** " +
        "Owner directive ('tau is not torus knot; same symmetries as 1st gen → " +
        "verify via SDP') reinterpreted: muon = 4_1 amphichiral; tau also " +
        "amphichiral hyperbolic (not torus). Census filter (12 candidates) under " +
        "q-bracket closure found **10_43 × [5]_q·[3]_q/[6]_q → +0.79 %** of " +
        "CODATA m_τ/m_e. The closure form is [5]_q · [3]_q / [6]_q (NOT the " +
        "originally-conjectured [4]_q · [2]_q / [5]_q). The unifying pattern " +
        "is ξ_m = [2m-1]_q · [m]_q / [2m]_q — matches muon (m=2 → [3]·[2]/[4]) " +
        "AND tau (m=3 → [5]·[3]/[6]) under one formula. Numerical verification " +
        "at q_0 ≈ 1.110: m=2 → 1.489307 vs required 1.48929 (0.001 %); " +
        "m=3 → 2.487363 vs required 2.46776 (0.79 %); m=4 prediction " +
        "→ [7]·[4]/[8] = 3.503110 (no Standard Model lepton at m=4). " +
        "Algebraic cores Lean-proved in `three-halves-structural-factor.lean`: " +
        "muon [4]_q = (2+h²) · [2]_q AND tau [6]_q = [2]_q · [3]_q · (1+h²). " +
        "Empirical foundation at +0.79 %; categorical derivation (why this " +
        "specific q-bracket form arises, and how 10_43's amphichirality + " +
        "hook-length (3,2,1) pattern selects it) remains open work for " +
        "Option E (Kashiwara crystal, PR #1252). See " +
        "`docs/audits/2026-05-25-t6-f-ell-derivation-attempt.md` followup section.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-09",
      body:
        "**Base ring minimised (AGENTS.md §7c).** The q-bracket algebra in the " +
        "Lean sibling moved from `[Field R]` + `field_simp` to a generic " +
        "`[CommRing R]` with the modulus carried as a unit `q : Units R`, so " +
        "`↑q⁻¹` is a `Units` coercion rather than a ring inverse. The two ξ_m " +
        "closed forms are now division-free identities " +
        "(`muon_xi_cross_mul`, `tau_xi_cross_mul`) that hold in every " +
        "commutative ring with **no** non-vanishing hypotheses. Because ξ_m is " +
        "itself a quotient of brackets, `lepton_xi` and the two theorems about " +
        "it keep their field and their `≠ 0` hypotheses, now confined to a " +
        "`RatioForm` section and derived from the generic identities by " +
        "`div_eq_div_iff`. The conjecture's content is untouched: what is open " +
        "is still the categorical derivation of the q-bracket form, not the " +
        "algebra.",
    },
  ],
  tags: [
    "tier:E",
    "lepton",
    "mass-tower",
    "ksi-factor",
    "h-n-branching",
    "categorical-interpretation",
    "phase-3",
    "open-conjecture",
  ],
});
