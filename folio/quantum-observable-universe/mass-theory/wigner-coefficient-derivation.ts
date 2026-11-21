import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wigner-coefficient-derivation",
  authorNotes: [
    { kind: "caveat", date: "2026-10-11", body: "**Not derived, and in tension with a proved result.** The theorem `wigner_coefficient` is discharged by `wigner_coefficient_axiom`, an axiom asserting $|[5]_q!\\,m_e - 68.896|/68.896 < 0.03$ at the superseded muon-era $q_0$: an empirical comparison inside a formal proof. The level $k = 5$ is asserted. Under convention D no self-conjugate shape of $5$ has at most two rows (`no_selfConj_two_row_of_five_le`, sorry-free), so a level-5 self-conjugate shadow price vanishes (`qou-a5jk`, `qou-w06d`). Bean `qou-wg3c`." },
    { kind: "caveat", date: "2026-11-21", body: "**Axiom removed.** `wigner_coefficient_axiom` (the 3 % bound against the fitted 68.896 MeV at the retired CODATA-2018 muon pin $q_0 = 1.109978595554181$) is deleted. `wigner_coefficient` now proves only the product expansion $[5]_q!\\,m_e = [1]_q[2]_q[3]_q[4]_q[5]_q\\,m_e$, sorry-free. The identification with the Bethe--Weizsäcker Wigner term stays conjectural, and the proof's step from the Casimir trace to $[5]_q!$ is asserted, not derived. Round-trip audit pass 2, C12." },
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
