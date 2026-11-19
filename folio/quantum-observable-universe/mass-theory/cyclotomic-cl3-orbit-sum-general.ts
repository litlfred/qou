import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean formalisation's `ℝ` carries " +
        "`zeta3 : ℝ` (`ζ(3)`, Apéry's constant, a transcendental period with " +
        "no generic-ring counterpart) and derives the primitive orbit sum " +
        "`-(N²-1)/N² · ζ(3)` and its strict negativity (`< 0` for `ζ(3) > 0` " +
        "and `N ≥ 2`) from the zero-mode value and weight-3 Kubert distribution sum.",
    },
  ],
  label: "prop:cyclotomic-cl3-orbit-sum-general",
  title:
    "General orbit-sum identity: $\\sum_k \\mathrm{Cl}_3(2\\pi k/N) = -(N^2-1)/N^2 \\cdot \\zeta(3)$ at every $N \\geq 2$",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicCl3OrbitSum.orbit_sum_general",
    validation: "leanok",
  },
  computation: {
    engine: "mpmath",
    script: "computations/cyclotomic_trilog_imaginary.py",
    witness:
      "computations/cyclotomic-trilog-imaginary.witness.json",
    status: "verified",
  },
  uses: [
    "prop:cyclotomic-trilog-imaginary-closed-form",
    "prop:cl3-zeta5-pslq-independence",
  ],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "multiplication-formula",
    "orbit-sum",
    "trilogarithm",
    "cyclotomic",
    "zeta-3",
    "closed-form",
    "depth-3",
    "graded-mikusinski",
    "theorem-level",
  ],
});
