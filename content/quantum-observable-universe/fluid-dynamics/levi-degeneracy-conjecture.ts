import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:levi-degeneracy",
  lean: { ref: "qou:QOU.FluidDynamics.LeviDegeneracy" },
  title:
    "Levi degeneracy conjecture: contact non-degeneracy at vortex collision determines NS regularity",
  uses: [
    "prop:core-levi-form",
    "prop:root-of-unity-truncation",
  ],
  tags: [
    "tier:famous",
    "conjecture",
    "levi-form",
    "contact-degeneracy",
    "millennium-problem",
    "root-of-unity",
    "navier-stokes",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-30",
      body:
        "**The trichotomy carrier now ties $\\beta$ to $\\mathcal{C}_L$.** The " +
        "2026-07-18 note below records that `levi_growth_trichotomy.lean` was " +
        "added to hold the growth-rate structure the `LeviDegeneracy` class " +
        "does not. That structure carried `condNumber : ℕ → ℝ` and `beta : ℝ` " +
        "with **no field relating them**, and `leviNonDegenerate : Prop` as a " +
        "free field the instance chose for itself. Measured against the old " +
        "definition, two instances type-check: `condNumber ≡ 0` with " +
        "`beta = 1/2` (both branch fields vacuous), and `condNumber ≡ 1` — so " +
        "$\\mathcal{C}_L = O(1)$, true exponent $0$ — with `beta = 1`, the " +
        "*opposite* branch. `beta` is now pinned by a two-sided `limsup` " +
        "characterisation written without `Filter`, `leviNonDegenerate` is a " +
        "parameter, and the elementary trichotomy facts are restated on a bare " +
        "real where their unconditional character is visible (they used only " +
        "`beta_mem`, so they were facts about $[0,1]$ dressed as facts about a " +
        "Levi trichotomy). The tie earns a new theorem: " +
        "`bounded_condNumber_forces_beta_zero` **derives** the `.md`'s " +
        "branch-(A) identification of $\\beta = 0$ with $\\mathcal{C}_L = O(1)$, " +
        "which the second measurement above is a counterexample to under the old " +
        "definition. Sorry-free, `lean`-direct exit 0; the value of $\\beta$ " +
        "remains the open content of the conjecture and is untouched.",
    },
    {
      kind: "note",
      date: "2026-08-14",
      body:
        "**Two lock-side facts landed since the per-channel reading.** (1) The " +
        "second-order stretching correction vanishes on approach: " +
        "$V_2/V_1 \\to 0$ as $\\tau \\to 0^+$, owner-proved sorry-free " +
        "(`kappa_squared_tends_to_zero`, `townsend-biot-savart-strain.lean`, " +
        "2026-08-10) — the two-regime model's phase-1 leading order is now on " +
        "Lean footing. (2) The \"$\\Gamma$ growth during collision\" caveat on " +
        "the lock's uniformity is **closed in-model**: reparametrizing by " +
        "consumed circulation eliminates $\\Gamma(t)$ from the phase-plane " +
        "race, so the overlap cutoff engages at $d^2 = (V_{1,0} d_0)^{2/3} > 0$ " +
        "for every positive circulation history " +
        "(`overlap_at_small_separation`, `pair_phase1_riccati.lean`, PR #5019). " +
        "The surviving lock-uniformity caveat is model-to-PDE fidelity (bean " +
        "`qou-ohaz`). Phase-1 self-amplification is also theorem-grade: the " +
        "pair channel satisfies the GP5 Riccati-lower-bound hypothesis with " +
        "uniform $c' = \\Gamma/(\\pi d_0^2 \\Omega_0)$ " +
        "(`discrete_riccati_lower`).",
      see: "../../../../docs/audits/2026-07-25-qns-surreal-bridge-campaign-ledger.md",
    },
    {
      kind: "caveat",
      date: "2026-07-25",
      body:
        "**Per-channel reading + lock tension.** The corpus's own collision mechanism (`rem:hyperbolic-overlap-saturation`: Levi lock $\\kappa^2 = \\pi\\nu/\\Gamma > 0$) supports **both** branches at different scopes: at every fixed $q \\neq 1$ the lock is strictly positive (non-degenerate — the branch-A reading, and the in-QOU example realising the internal singularity), but its $\\nu$-scaling on the ladder gives $\\mathcal{C}_L = \\Gamma/(\\pi\\nu_q) \\sim \\kappa$, i.e. fitted $\\beta \\approx 0.996 \\approx 1$ = **branch B** for the anti-parallel-pair channel in the classical limit (witness `qns-levi-lock-scaling-probe.witness.json`; conditional on the lock asymptotic being uniform, $\\Gamma$ fixed). Suggested resolution: a **per-channel** branch assignment — pair-collision channel branch-B-conditional-on-lock; the blow-up claim then rides on channels the lock does not cover (sustained forcing, cf. the enstrophy-grade probe). Not a resolution of the conjecture. Campaign ledger: `docs/audits/2026-07-25-qns-surreal-bridge-campaign-ledger.md`; bean `qou-js2u`.",
      see: "../../../../docs/audits/2026-07-25-qns-surreal-bridge-campaign-ledger.md",
    },
    {
      kind: "refined-framing",
      date: "2026-07-18",
      body:
        "Restated from a two-way dichotomy to an exhaustive **trichotomy** on the growth exponent $\\beta = \\limsup_\\kappa \\log \\mathcal{C}_L / \\log \\kappa \\in [0,1]$: $\\beta = 0$ (blow-up, branch A), $\\beta = 1$ (regular via sheet-flattening, branch B), $0 < \\beta < 1$ (marginal, undetermined). The original \"exactly one of (A)/(B)\" was not a valid partition — it dropped the marginal window. Growth-rate formalisation added in `QOU/FluidDynamics/levi_growth_trichotomy.lean` (`levi_trichotomy_exhaustive`, `levi_marginal_undetermined`, `levi_branches_exclusive`, lean-direct exit 0); the existing `LeviDegeneracy` class encodes only the degeneracy set. Rationale: audit 2026-07-18 Finding 3; bean `qou-3g5m`.",
      see: "../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md",
    },
  ],
});
