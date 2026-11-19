import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:levi-degeneracy",
  lean: { ref: "qou:QOU.FluidDynamics.LeviDegeneracyQ1.LeviDegeneracy" },
  title:
    "Levi degeneracy conjecture: a vanishing Levi scalar $\\xi\\cdot\\mathrm{curl}\\,\\xi$ on the high-vorticity set prevents blow-up",
  uses: [
    "prop:core-levi-form",
  ],
  cites: ["constantin1993", "beiraodaveiga2002"],
  tags: [
    "tier:famous",
    "conjecture",
    "levi-form",
    "contact-degeneracy",
    "vorticity-direction",
    "millennium-problem",
    "navier-stokes",
  ],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "note",
      date: "2026-10-13",
      body:
        "**Consumers re-scoped (owner option 2, follow-up to Q1).** The consumers " +
        "named in the caveat below as \"not edited here\" have since been " +
        "re-scoped: `rem:core-levi-interpretation`, " +
        "`rem:hyperbolic-overlap-saturation`, `rem:observability-fluid-context`, " +
        "`rem:q-metric-contact-deformation`, " +
        "`rem:observability-independent-motivation` (+ its table), " +
        "`prop:ns-obstruction-tower` (proof step (d) withdrawn) and " +
        "`rem:ns-obstruction-tower-summary`. In Lean, " +
        "`levi_growth_trichotomy.lean` now carries `GrowthExponent` (no Levi " +
        "reading, no branch fields) and `levi_pair_channel_branch_b.lean` keeps " +
        "`linear_seq_forces_beta_one` as an aspect-ratio statement; the old " +
        "theorem names survive as deprecated aliases. Still carrying the " +
        "withdrawn statements and NOT edited: `yekutieli_levi_unification.lean` " +
        "(step (d) as a class field), `qou_ns_in_qou.lean` " +
        "(`QOUFluidUniverseLevi`, branch A), `ns-singularity-descartes-proof` " +
        "(lists the core-Levi equivalence as an input) and " +
        "`ns-singularity-descartes-interpretation`. Bean `qou-fm7s`." +
        " Update 2026-11-15 (owner option 1, PR #7747): all of these are now re-scoped; see bean qou-fm7s.",
    },
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped onto the vorticity plane field (owner decision 2026-10-13, " +
        "Q1: $\\varTheta = f\\,\\xi^\\flat$).** The block previously stated a " +
        "trichotomy on $\\beta = \\limsup_\\kappa \\log\\mathcal{C}_L(\\kappa)/" +
        "\\log\\kappa$ along the root-of-unity ladder: (A) $\\beta = 0$, Levi " +
        "non-degenerate, NS blows up (the branch the framework argued for); (B) " +
        "$\\beta = 1$, Levi degenerates, NS regular; (C) $0<\\beta<1$ undetermined. " +
        "Changes: **(A) is withdrawn**, refuted under this reading by the smooth " +
        "Beltrami solution $u = e^{-\\nu t}(\\sin z, \\cos z, 0)$ on " +
        "$\\mathbb{T}^3$ ($\\xi\\cdot\\mathrm{curl}\\,\\xi = 1$ everywhere, " +
        "$|\\omega| \\le 1$) — scope (b) for the implication under " +
        "$\\varTheta = f\\,\\xi^\\flat$, the counterexample being the invariant; " +
        "Lean `beltrami_refutes_branchA`. **$\\mathcal{C}_L$, $\\beta$ and regime " +
        "(C) are withdrawn as undefined**: in dimension 3 the Levi form of a plane " +
        "field is $1\\times1$ (`prop:core-levi-form`). **(B) is kept as the open " +
        "conjecture**, restated on the Levi scalar; Constantin–Fefferman / " +
        "Beirão da Veiga–Berselli bound $\\nabla\\xi$ only from above, and " +
        "neither degeneracy nor non-degeneracy of $\\xi\\cdot\\mathrm{curl}\\,\\xi$ " +
        "implies their hypothesis, so nothing in the standard literature supports " +
        "(B). **Added** the standard-cited contrapositive of Beirão da " +
        "Veiga–Berselli as the chapter's true conditional statement (Lean " +
        "`blowup_forces_direction_incoherence`, derived from the cited theorem " +
        "carried as the one field of `BeiraoDaVeigaBerselliCriterion`; primary " +
        "texts not held). The old `LeviDegeneracy` class (degeneracy set of an " +
        "abstract `leviForm` equal to $\\{1/\\kappa\\}$) is removed: under this " +
        "reading the Levi datum lives on the flow domain, not on the $q$-ladder. " +
        "`prop:root-of-unity-truncation` is dropped from `uses` for the same reason. " +
        "**The five notes below are kept as records**: the pair-channel " +
        "$\\beta = 1$ result, the lock formula $\\mathcal{C}_L = \\Gamma/(\\pi\\nu_q)$ " +
        "and $\\kappa^2 = V_2/V_1 \\to 0$ are statements about the Townsend core " +
        "aspect ratio, which stays well-defined, not about Levi data. " +
        "`QOU/FluidDynamics/levi_growth_trichotomy.lean` and " +
        "`levi_pair_channel_branch_b.lean` still carry the $\\beta$ / condition-number " +
        "encoding and are not edited here. Consumers still written against the " +
        "old statement (not edited here): `rem:core-levi-interpretation` and " +
        "`rem:hyperbolic-overlap-saturation` (both assert branch (A)), " +
        "`rem:observability-fluid-context`, `rem:q-metric-contact-deformation`, " +
        "`rem:observability-independent-motivation`, `prop:ns-obstruction-tower` " +
        "and `rem:ns-obstruction-tower-summary` (Levi eigenvalues / condition " +
        "number). " +
        "The conjecture is NOT resolved. Audits: " +
        "`docs/audits/2026-10-12-ns-v1-geometric-depletion.md` §3.4–3.5, " +
        "`docs/audits/2026-10-12-ns-attack-vectors-unforced.md` §3 V1, §4 Q1.",
      see: "../../../docs/audits/2026-10-12-ns-v1-geometric-depletion.md",
    },
    {
      kind: "note",
      date: "2026-09-03",
      body:
        "**The pair channel's $\\beta$ is exactly 1, not the fitted 0.99628 — so " +
        "window C is excluded for it.** The 2026-07-25 caveat below records " +
        "$\\beta_{\\mathrm{fit}} = 0.99628$ for the anti-parallel-pair channel. That " +
        "value is near 1 but formally sits inside the *marginal window* " +
        "$0 < \\beta < 1$, where the trichotomy's verdict is undetermined — so read " +
        "literally it leaves this channel undecided. It does not. Under the lock, " +
        "with $\\nu_q = (q-1)/(2q)$ and $\\varepsilon := q-1$, the condition number " +
        "has the **exact** closed form $\\mathcal{C}_L = (2\\Gamma/\\pi)\\," +
        "(1+\\varepsilon)/\\varepsilon$ — not an asymptotic — so " +
        "$\\log \\mathcal{C}_L = \\log(2\\Gamma/\\pi) + \\log(1+\\varepsilon) " +
        "- \\log\\varepsilon$ and $\\beta = 1$ on the nose. The 0.99628 is a " +
        "least-squares slope over a finite $\\varepsilon$ window dominated by its " +
        /* <!-- literal-source: closed-form secant exponent 1 - log10(1.1/1.01) = 0.962932 on [1e-1, 1e-2] from qns_levi_lock_beta_exact_probe.py --> */
        "coarse end: measured at 50 dps, the secant exponent is 0.9629 over " +
        "$[10^{-1},10^{-2}]$ and 1.0 to $10^{-15}$ by $\\varepsilon = 10^{-15}$, and " +
        "the *same* fit moved to $[10^{-13},10^{-20}]$ returns 0.999999999999996 " +
        "(`qns_levi_lock_beta_exact_probe.py`, 4/4). The Lean side does not use any " +
        "of these numbers: `linear_condNumber_forces_beta_one` " +
        "(`levi_pair_channel_branch_b.lean`, sorry-free) **derives** $\\beta = 1$ " +
        "from linear growth, the dual of `bounded_condNumber_forces_beta_zero`, so " +
        "no fit precision enters the argument. **Scope unchanged:** conditional on " +
        "the lock formula, which is a model input and is not derived; per-channel, " +
        "scope (a). The conjecture is NOT resolved — branch B for one channel is not " +
        "branch B for the flow.",
      see: "../../../../computations/qns_levi_lock_beta_exact_probe.py",
    },
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
  computation: {
    engine: "python",
    script: "computations/qns_levi_lock_scaling_probe.py",
    witness: [
      "computations/qns-levi-lock-scaling-probe.witness.json",
      "computations/close-321-weinberg-gap.witness.json",
    ],
    status: "verified",
  },
});
