import { example } from "../../schema/builders";

export default example({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "status", date: "2026-09-04", body: "§$T_{3,5}$ weak vertex corrected. It read $\\mathcal{W}(q_0) \\approx 0.7036$ (\"computed exactly\") and \"the vertex ratio yields an 11 % reduction in transition amplitude\". Neither Markov-trace convention reproduces 0.7036 (convention D 1.1875, excised convention C 0.9063); the figure descends from the deprecated convention-C `hecke_division` pipeline (`computations/_deprecated/t35-full-calculation.py`) and was not reproduced. Replaced by the derived closed form (Lean `QOU.Braiding.WeakVertexT35.weakVertexTrace_eq`, witness `weak-vertex-t35-trace`, bean `qou-egvf`); the amplitude-reduction sentence is withdrawn, as nothing in the corpus derives an amplitude ratio from $\\mathcal{W}$. The tables in this block use the single-crossing approximation and were not affected. Bean `qou-4x7c`." },
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
});
