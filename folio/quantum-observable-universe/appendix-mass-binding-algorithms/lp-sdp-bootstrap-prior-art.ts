import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lp-sdp-bootstrap-prior-art",
  title:
    "Prior art for symmetry-reduced bootstrap programs and machine-checked dual certificates",
  interprets: "alg:rationalized-dual-slack-certificate",
  uses: ["alg:rationalized-dual-slack-certificate"],
  cites: [
    "farkas1902",
    "kantorovich1939",
    "rattazzi-rychkov-tonni-vichi2008",
    "elshowk2012",
    "simmons-duffin2015",
    "goulart-chen2024",
    "cohn-elkies2003",
    "viazovska2017",
    "delsarte1973",
    "schrijver2005",
    "gijswijt-schrijver-tanaka2006",
    "gatermann-parrilo2004",
    "verstichel-vanaggelen2009",
    "navascues-pironio-acin2007",
    "kazakov-zheng2022",
    "kazakov-zheng2023",
    "hales2017",
    "boldo-lelay-melquiond2015",
    "roux2016",
    "mahboubi-sibut-pinote2021",
    "dvorak-kolmogorov2024",
  ],
  tags: [
    "mba",
    "lp-dual",
    "sdp-dual",
    "bootstrap",
    "prior-art",
    "extremal-functional",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Reusable generic-ordered-ring Lean 4 backing lives in `folio/quantum-observable-universe/lean/QOU/MathlibInfra/SymmetryReducedDualCertificate.lean` (`lp_primal_lower_bound_of_dual`, `lp_optimal_of_zero_gap`, `unique_support_of_strict_dual_slack`, `unique_primal_of_strict_dual_slack`, `central_cone_iff_character_weights_nonneg`) and `QOU/MathlibInfra/NuclearChamberGS.lean`, with 80-dps witnesses `computations/probes/lp_bootstrap_dual_gaps/lp-bootstrap-dual-gaps.witness.json` and `chamber-gs-model-a-b.witness.json`.",
    },
  ],
});
