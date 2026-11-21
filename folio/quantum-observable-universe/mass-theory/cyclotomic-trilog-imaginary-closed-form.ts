import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body: "Lean proof added (owner card, 2026-11-21): `imLi3_zeta_hasSum` proves the closed form for every n >= 1, with Im Li3(zeta_n) read as the series sum over m of sin(2 pi m/n)/m^3. The Lean route is the Fourier series of the Bernoulli polynomial B_3 at x = 1/n, not the Kummer reflection used in the prose proof; both give the same identity.",
    },
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
    ref: "qou:QOU.BraidKnot.CyclotomicTrilogImaginary.imLi3_zeta_hasSum",
    validation: "not_checked",
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
