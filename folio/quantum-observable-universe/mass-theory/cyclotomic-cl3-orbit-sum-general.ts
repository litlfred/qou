import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body: "Lean proof added (owner card, 2026-11-21): `cl3_orbit_sum` proves the identity for every N >= 1, with Cl_3(theta) the series sum over m of cos(m theta)/m^3 and zeta(3) the series sum of 1/m^3. The Lean route is the roots-of-unity character sum (sum over k of cos(2 pi k m/N) is N or 0) plus summing over multiples of N, the same content as the multiplication formula in the prose proof.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's only `ℝ` is the argument " +
        "`zeta3 : ℝ` of `orbit_sum_general`, fed to " +
        "`cl3OrbitSumPredicted N zeta3`. That argument is **ζ(3)** — Apéry's " +
        "constant, a transcendental period with no generic-ring counterpart — " +
        "and the closed form `-(N²-1)/N² · ζ(3)` is a statement about a real " +
        "number. `ℝ` is correct by meaning, not gratuitous.",
    },
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Flagged for the vacuity queue, not fixed here.** The declaration " +
        "concludes `cl3OrbitSumPredicted N zeta3 = cl3OrbitSumPredicted N " +
        "zeta3`, closed by `rfl` — a tautology under §\"Strict Lean " +
        "Discipline\" item 5. The substantive identification with the actual " +
        "orbit sum is the `TheoremB` class. Recorded while triaging the " +
        "base-ring queue; deliberately left for the vacuity drain rather " +
        "than silently patched.",
    },
  ],
  label: "prop:cyclotomic-cl3-orbit-sum-general",
  title:
    "General orbit-sum identity: $\\sum_k \\mathrm{Cl}_3(2\\pi k/N) = -(N^2-1)/N^2 \\cdot \\zeta(3)$ at every $N \\geq 2$",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicCl3OrbitSum.cl3_orbit_sum",
    validation: "not_checked",
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
