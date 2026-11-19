import { example } from "../../schema/builders";

export default example({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data. Axial-coupling epistemic status recorded in QOU/Archimedean/AxialCoupling.lean." },
    { kind: "status", date: "2026-09-04", body: "§$T_{3,5}$ weak vertex corrected. It read $\\mathcal{W}(q_0) \\approx 0.7036$ (\"computed exactly\") and \"the vertex ratio yields an 11 % reduction in transition amplitude\". Neither Markov-trace convention reproduces 0.7036 (convention D 1.1875, excised convention C 0.9063); the figure is reproduced (0.70355) by the live `hecke_division` engine's former trace rule — the Markov rotation applied without the Hecke relation, i.e. $\\sum_w c_w z^{|w|}$ over the reduced word — evaluated at the excised convention-C parameter $z_C$; the same rule at $z_D$ gave the 0.9684 that `t35-weak-vertex.witness.json` carried from 2026-08-29. Engine fixed and provenance identified 2026-09-05, bean `qou-ix74` (an earlier note here attributed the figure to the deprecated `t35-full-calculation.py`; that was wrong). Replaced by the derived closed form (Lean `QOU.Braiding.WeakVertexT35.weakVertexTrace_eq`, witness `weak-vertex-t35-trace`, bean `qou-egvf`); the amplitude-reduction sentence is withdrawn, as nothing in the corpus derives an amplitude ratio from $\\mathcal{W}$. The tables in this block use the single-crossing approximation and were not affected. Bean `qou-4x7c`." },
  ],
  label: "ex:hadron-half-life-verification",
  title: "Half-life predictions for selected beta emitters",
  tags: [
    "half-life",
    "beta-decay",
    "verification",
    "numerical",
    "tritium",
    "cobalt-60",
    "carbon-14",
  ],
  lean: { ref: "qou:QOU.Archimedean.HalfLifeVerification.all_six_agree",
    validation: "not_checked",
  },
  uses: ["rem:hadron-half-life-regimes"],
  computation: {
    engine: "python",
    script: "computations/t35-weak-vertex.py",
    witness: [
      "computations/t35-weak-vertex.witness.json",
      "computations/qbeta/qbeta-fmap-phi-b-root-of-unity-reference.witness.json",
      "computations/probes/h2_gg_electron/h2-gg-electron.witness.json",
      "computations/weak-vertex-t35-trace.witness.json",
    ],
    status: "verified",
  },
});
