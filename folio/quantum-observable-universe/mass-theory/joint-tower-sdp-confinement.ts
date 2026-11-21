import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:joint-tower-sdp-confinement",
  title:
    "Joint mass-tower confinement SDP at $q_0$ with GB-filtration + jet-order tracking",
  lean: {
    ref: "qou:QOU.BraidKnot.JointTowerSdp",
    validation: "not_checked",
  },
  uses: ["conj:atom-knot-mass-derivation"],
  tags: [
    "sdp",
    "confinement",
    "joint-tower",
    "gb-filtration",
    "jet-order",
    "design-spec",
    "wedderburn",
    "cross-level-consistency",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/d_from_scratch.py",
    witness: "computations/d-from-scratch.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-20",
      body: "The Lean sibling encodes the SDP's input data and its well-formedness only. The predicates formerly named `WedderburnBlockPositivity`, `GbFiltrationGrading`, `JetOrderOrdering` and `CrossLevelConsistency` checked `n_0 ≥ 1`, a cutoff bound, a non-empty list and `m ≤ n`; they are renamed to say so, and `joint_tower_sdp_feasible`, which returned its hypothesis, is removed. `lean.ref` now names `JointTowerSdp`, which exists; the old ref named no declaration. Block positivity, the filtration and jet-order conditions, cross-level consistency and joint feasibility are not formalised (bean `qou-w8cg`).",
    },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
    {
      kind: "status",
      body: "See [Table 2](#tbl:joint-tower-sdp-confinement-table2-data).\n\nThe certificate format (Wedderburn block $\\times$ filtration grade $\\times$ jet\nposition $\\to$ coefficient) is identical at every scale; only the variable\ncount grows.",
    },
  ],
});
