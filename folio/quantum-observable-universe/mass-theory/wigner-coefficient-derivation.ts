import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wigner-coefficient-derivation",
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
    { kind: "caveat", date: "2026-10-11", body: "**Not derived, and in tension with a proved result.** The theorem `wigner_coefficient` is discharged by `wigner_coefficient_axiom`, an axiom asserting $|[5]_q!\\,m_e - 68.896|/68.896 < 0.03$ at the superseded muon-era $q_0$: an empirical comparison inside a formal proof. The level $k = 5$ is asserted. Under convention D no self-conjugate shape of $5$ has at most two rows (`no_selfConj_two_row_of_five_le`, sorry-free), so a level-5 self-conjugate shadow price vanishes (`qou-a5jk`, `qou-w06d`). Bean `qou-wg3c`." },
  ],
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
