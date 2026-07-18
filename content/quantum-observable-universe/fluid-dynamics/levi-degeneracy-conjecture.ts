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
      date: "2026-07-18",
      body:
        "**Dichotomy may not be exhaustive.** The stated \"exactly one of (A) $\\mathcal{C}_L = O(1)$ / (B) $\\mathcal{C}_L \\sim \\kappa$\" is not complementary: an intermediate marginal rate $\\mathcal{C}_L \\sim \\kappa^\\beta$ with $0 < \\beta < 1$ satisfies neither branch, so as written the conjecture could be vacuously false rather than a genuine dichotomy. Recommended restatement as a **trichotomy** keyed on $\\beta = \\limsup_{\\kappa} \\log \\mathcal{C}_L / \\log \\kappa$: $\\beta = 0$ (blow-up), $\\beta = 1$ (regular via sheet-flattening), $0 < \\beta < 1$ (marginal, undetermined) — or a proof that the marginal window is empty. Note the Lean `LeviDegeneracy` class currently encodes only the degeneracy *set*, not the growth rate, so it does not yet capture the dichotomy. Tracked under bean `qou-3g5m`.",
      see: "../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md",
    },
  ],
});
