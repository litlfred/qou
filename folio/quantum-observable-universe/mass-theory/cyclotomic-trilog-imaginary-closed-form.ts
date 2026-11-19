import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's `ℝ` is the coercion " +
        "`imLi3ZetaPredicted (n : ℝ)`. The value predicted is " +
        "`Im Li₃(ζ_n) = (n-1)(n-2) π³ / (3 n³)` — it contains **π³**, a " +
        "transcendental, and it is the imaginary part of an analytic " +
        "polylogarithm at a root of unity. Both facts make `ℝ` the correct " +
        "base ring; the substrate-side content is the cyclotomic " +
        "combinatorics, which is carried separately.",
    },
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**Flagged for the vacuity queue, not fixed here.** " +
        "`closed_form_holds` concludes " +
        "`imLi3ZetaPredicted (n : ℝ) = imLi3ZetaPredicted (n : ℝ)` by `rfl`, " +
        "with `2 ≤ n` introduced and discarded — a tautology under " +
        "§\"Strict Lean Discipline\" item 5. The real identification lives in " +
        "`QOU.Infra.Polylogarithm.TheoremA`. Recorded during base-ring " +
        "triage, deliberately not patched here.",
    },
  ],
  label: "prop:cyclotomic-trilog-imaginary-closed-form",
  title:
    "Trilogarithm imaginary part at $\\zeta_n$: closed form $(n - 1)(n - 2)\\pi^3 / (3 n^3)$ for every root of unity",
  lean: {
    ref: "qou:QOU.Infra.Polylogarithm.TheoremA",
    validation: "leanok",
  },
  computation: {
    engine: "mpmath",
    script: "computations/cyclotomic_trilog_imaginary.py",
    witness:
      "computations/cyclotomic-trilog-imaginary.witness.json",
    status: "verified",
  },
  uses: ["prop:bring-trilog-imaginary-tate-rational"],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "kummer-reflection",
    "trilogarithm",
    "cyclotomic",
    "tate-rational",
    "closed-form",
    "depth-3",
    "graded-mikusinski",
    "theorem-level",
  ],
});
