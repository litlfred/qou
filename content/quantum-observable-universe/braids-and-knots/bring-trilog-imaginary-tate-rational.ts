import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-trilog-imaginary-tate-rational",
  title:
    "Im Li$_3$($\\zeta_5$) = 4$\\pi^3$/125 — Tate-rational, via Kummer reflection (50-dps verified)",
  lean: {
    ref: "qou:QOU.BraidKnot.BringTrilogImaginaryTateRational.im_li3_zeta5_closed_form",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/kummer_reflection_zeta5.py",
    witness:
      "folio-assistant/computations/kummer-reflection-zeta5.witness.json",
    status: "verified",
  },
  uses: [
    "conj:bring-trilog-depth-3-witness",
    "rem:transcendental-accounting",
    "conj:cl3-zeta5-geometric-realization",
    "prop:borel-partial-resolution",
    "conj:qou-infra-discharges-goncharov-zeta5",
  ],
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
});
