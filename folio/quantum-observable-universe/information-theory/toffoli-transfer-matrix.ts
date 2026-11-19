import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:toffoli-transfer-matrix",
  lean: { ref: "qou:QOU.Information.toffoli_transfer_matrix", validation: "not_checked" },
  title:
    "The massive Toffoli transfer matrix $M(q)$ and the q-AND polynomial $P_{7,6}(q)$",
  tags: [
    "toffoli",
    "transfer-matrix",
    "q-AND",
    "hecke-algebra",
    "destructive-interference",
    "planck-computation",
    "braiding",
  ],
  uses: [
    "prop:skein-polynomial-transfer-matrix",
    "rem:discrete-planck-step",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/Information/toffoli_transfer_matrix.lean` uses " +
        "`Real.sqrt`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/probes/toffoli_published_vs_construction_audit.py",
    witness: "computations/probes/toffoli-published-vs-construction.witness.json",
    status: "verified",
  },
});
