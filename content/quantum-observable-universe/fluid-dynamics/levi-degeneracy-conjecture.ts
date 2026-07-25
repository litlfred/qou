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
