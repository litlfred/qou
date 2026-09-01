import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wigner-coefficient-derivation",
  title: "Wigner coefficient $[5]_q! \\cdot m_e$ from Frobenius reciprocity",
  lean: { ref: "qou:QOU.BraidKnot.wigner_coefficient", validation: "not_checked" },
  uses: [
    // Declared by the .md banner and bound in the Lean (wigner_coefficient_conditional at :81 binds [inst : QIntegerMassFormula]),
    // but absent here and unreachable in the uses[] graph at any depth
    // until 2026-08-30 — the dependency was recorded in prose only
    // (bean `qou-s3zd`). Not transitively reachable, so not redundant.
    "conj:q-integer-mass-formula","prop:wedderburn-trace-identity"
  ],
  tags: ["wigner", "isospin", "casimir", "quantum-factorial", "frobenius-reciprocity"],
});
