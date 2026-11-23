import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:core-levi-form",
  lean: { ref: "qou:QOU.FluidDynamics.CoreLevi.core_levi_form", validation: "not_checked" },
  title:
    "The Levi datum of the vorticity plane field is the single scalar $\\xi\\cdot\\mathrm{curl}\\,\\xi$",
  uses: [
    "def:levi-form-defect",
  ],
  cites: ["constantin1993", "beiraodaveiga2002"],
  tags: [
    "levi-form",
    "contact-structure",
    "vorticity-direction",
    "integrability",
    "millennium-problem",
  ],
  authorNotes: [
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
        "**Re-scoped onto the vorticity line field (owner decision 2026-10-13, " +
        "Q1: $\\varTheta = f\\,\\xi^\\flat$).** The block previously placed a " +
        "vortex filament on the state bundle $(\\mathcal{S}, \\varTheta)$, took " +
        "two Levi eigenvalues $\\lambda_\\parallel, \\lambda_\\perp$ on the " +
        "normal plane $N_p\\varrho \\subset \\ker\\varTheta$, and asserted " +
        "(a) $a_\\perp/a_\\parallel = \\sqrt{\\lambda_\\parallel/\\lambda_\\perp}" +
        "\\,(1+O(\\hbar_q^2))$, (b) $\\mathrm{cond}(\\mathcal{L}_\\varTheta|_{N_p}) " +
        "= \\max(a_\\perp/a_\\parallel, a_\\parallel/a_\\perp)^2(1+O(\\hbar_q^2))$, " +
        "(c) a five-way equivalence of bounded aspect ratio, bounded condition " +
        "number, contact non-degeneracy on the collision locus, the local " +
        "observability axiom and failure of Frobenius integrability, (d) the " +
        "quantum-pressure bound $\\mathrm{cond} \\le 1 + C_0\\hbar_q^2$ for " +
        "$q > 1$, and (e) a $q = 1$ degeneration clause. It carried a " +
        "conditional banner on `conj:q-aubin-lions`, `conj:ns-counterexample`, " +
        "`conj:critical-exponent`, `prop:blowup-yekutieli` and " +
        "`conj:regularity-breakdown`, and `uses` " +
        "`conj:vorticity-lower-bound`, `rem:c-substrate-via-levi`. **All of " +
        "(a)–(e) are removed.** In dimension $3$ a plane field has complex rank " +
        "$1$, so its Levi form is $1\\times 1$: the eigenvalue pair and its " +
        "condition number are undefined (`levi_restriction_rank_one` in the " +
        "`.lean` sibling is the algebraic form of this). The core aspect ratio " +
        "is still a well-defined fluid quantity (the Townsend covariance of " +
        "`rem:townsend-biot-savart-strain`), but it is no longer a Levi " +
        "quantity: for a straight anti-parallel pair the Levi scalar is $0$ for " +
        "every core shape. No numerical finding was attached to (a)–(e); the " +
        "only derived content was the real-algebra identity " +
        "$\\max\\lambda/\\min\\lambda = \\max(a_\\perp/a_\\parallel, " +
        "a_\\parallel/a_\\perp)^2$ under the exact leading-order relation " +
        "(theorem `core_levi_ratio_eq_aspect_sq`), which has no remaining " +
        "referent and is kept in git history (parent of this commit). The new " +
        "statement is unconditional differential geometry, so the conditional " +
        "banner and the two `uses` are dropped. Consumers still written against " +
        "the old statement: `rem:core-levi-interpretation` (asserts " +
        "\"NS blows up iff Levi non-degenerate\", the withdrawn branch (A)), " +
        "`rem:hyperbolic-overlap-saturation` (branch (A), \"both eigenvalues stay " +
        "bounded away from zero\"), `rem:observability-fluid-context`, " +
        "`rem:q-metric-contact-deformation`, " +
        "`rem:observability-independent-motivation`, `prop:ns-obstruction-tower`, " +
        "`rem:ns-obstruction-tower-summary`, and the trichotomy library files " +
        "`levi_growth_trichotomy.lean` / `levi_pair_channel_branch_b.lean`. " +
        "None is edited here. " +
        "Audits: `docs/audits/2026-10-12-ns-v1-geometric-depletion.md` §3.3–3.4, " +
        "`docs/audits/2026-10-12-ns-attack-vectors-unforced.md` §2 (D1, D2). " +
        "Beans `qou-fm7s`, `qou-0ueg`.",
      see: "../../../docs/audits/2026-10-12-ns-v1-geometric-depletion.md",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): What the criteria do give is stated in [Levi degeneracy conjecture](#conj:levi-degeneracy)." },
  ],
});
