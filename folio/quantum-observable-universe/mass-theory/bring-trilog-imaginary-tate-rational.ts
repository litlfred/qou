import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-trilog-imaginary-tate-rational",
  title:
    "Trilogarithm imaginary part at $\\zeta_5$: Tate-rational closed form $4\\pi^3/125$ via Kummer reflection (50-dps verified)",
  lean: {
    ref: "qou:QOU.BraidKnot.BringTrilogImaginaryTateRational.im_li3_zeta5_closed_form",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/kummer_reflection_zeta5.py",
    witness:
      "computations/kummer-reflection-zeta5.witness.json",
    status: "verified",
  },
  // conj:qou-infra-discharges-goncharov-zeta5 removed from uses[] (2026-06-08
  // §3b sweep): the closed form Im Li_3(ζ_5) = 4π³/125 is proved unconditionally
  // (Kummer reflection, 50-dps witness); the Goncharov program is context, not a
  // logical hypothesis. The conceptual link remains in the .md prose cross-ref.
  uses: [],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "kummer-reflection",
    "trilogarithm",
    "tate-rational",
    "depth-3",
    "zeta-5",
    "S5-symmetry",
    "graded-mikusinski",
    "theorem-level",
    "50-dps-numerical",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/BraidKnot/BringTrilogImaginaryTateRational.lean` uses " +
        "`Real.pi`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
