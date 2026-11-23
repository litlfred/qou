import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "The closing sentence named $E_2$-collapse of the GB spectral sequence as a proof route. That route is closed: the length-filtered Hochschild sequence of $H_3$ has $d_2, d_4 \\neq 0$ and stabilises at $E_5$ (`computations/probes/gb_spectral_sequence_h3_probe.py`, bean `qou-6qbv`). The Yekutieli route is unaffected." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "conj:jet-tower-uniform-delta-max",
  title:
    "Uniform per-level binding bound $|\\Delta^{(n)}(\\varrho)| \\le \\Delta_{\\max}(\\varrho)$ for the brane tower",
  lean: {
    ref: "qou:QOU.BraidKnot.JetTowerUniformDeltaMax",
    validation: "not_checked",
  },
  uses: [
    "prop:jet-tower-convergence",
    "prop:gb-spectral-sequence",
    "lem:tower-pair-equality-fixed-level",
  ],
  cites: [
    "kassel1995",
    "yekutieli2010",
  ],
  computation: {
    engine: "python",
    script: "computations/jet_tower_delta_max.py",
    witness: "computations/jet-tower-delta-max.witness.json",
    status: "verified",
  },
  tags: [
    "tier:S",
    "jet-tower",
    "uniform-bound",
    "convergence",
    "open-problem",
    "empirically-supported",
  ],
});
