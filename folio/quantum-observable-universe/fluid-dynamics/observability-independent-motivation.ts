import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-observable-universe",
  label: "rem:observability-independent-motivation",
  title:
    "Independent motivation for observability: why $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) = 0$ is not an NS assumption",
  uses: ["thm:ns-singularity-descartes"],
  // prop:core-levi-form sits later in this section; item 2 points forward to it.
  foreshadows: ["prop:core-levi-form"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped after owner ruling Q1 ($\\varTheta = f\\,\\xi^\\flat$, " +
        "2026-10-13).** Withdrawn, verbatim: item 2, \"Observability matches " +
        "exactly the non-degeneracy of the Levi form $\\mathcal{L}_\\varTheta$ " +
        "(core-Levi equivalence), the cardinal property of a contact manifold. " +
        "Contact manifolds enforce maximal non-integrability. Bring's surface " +
        "possesses a strictly pseudoconvex CR structure (its Levi form is positive " +
        "definite). This describes the intrinsic manifold, not an ad-hoc NS " +
        "assumption.\"; in item 4 the gloss \"(meaning the Levi form resists " +
        "degeneracy)\" on $L \\neq 0$; and the QPU clause \"because the weakened " +
        "contact structure can degenerate smoothly at collision zones, allowing " +
        "vortices to flatten safely\". Reason: `prop:core-levi-form` no longer " +
        "states a core-Levi equivalence; in dimension 3 the Levi datum is the " +
        "scalar $\\xi\\cdot\\mathrm{curl}\\,\\xi$, which carries no core-shape " +
        "information and is linked by no result to observability. The Bring's-" +
        "surface CR sentence goes with item 2 because it was offered as support " +
        "for that identification; it is not separately assessed here. The " +
        "remaining items, the table row \"Contact structure: non-degenerate / may " +
        "degenerate\" (in `observability-independent-motivation-table-data`, not " +
        "edited) and the dependence on `thm:ns-singularity-descartes` are " +
        "untouched; note that `ns-singularity-descartes-proof` lists the " +
        "withdrawn core-Levi equivalence as one of its inputs. Bean `qou-fm7s`.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Updated opening and closing sentences per owner decision (Q-VO9T-2 = 1, beans qou-nzyr, qou-507c, qou-hjl0): " +
        "observability $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) = 0$ deduces the internal global surface obstruction " +
        "$\\mathrm{NS}(A) = e(\\xi) \\neq 0 \\in H^2(\\mathcal{S}, \\mathbb{Z})$ (`QOU.FluidDynamics.qou_internal_ns_singular`), " +
        "while connecting that internal categorical class to classical 3D PDE blowup is scoped as the framework model correspondence (`def:ns-regular-qou`).",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The [Descartes Reeb-bundle theorem](#thm:ns-singularity-descartes) and the in-QOU obstruction reduction deduce the internal categorical singularity $\\mathrm{NS}(A) = e(\\xi) \\neq 0 \\in H^2(\\mathcal{S}, \\mathbb{Z})$ from the QOU observability axiom $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) = 0$ (which the framework model correspondence associates with Navier--Stokes blowup). This mandates the question: does this axiom stand independently, or does it merely smuggle in the NS conclusion?" },
  ],
  tags: [
    "observability",
    "motivation",
    "independence",
    "gauge-theory",
    "contact",
    "measurement",
  ],
});
