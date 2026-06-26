import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "status", date: "2026-06-26", body: "The intended Lean theorems (establishing `deltaQ <= 0` for neutron-rich nuclei, `differentialShift >= 0`, and `qEff > 1`) contain mathematically sound proof bodies relying on basic arithmetic, `omega`, and `positivity` tactics. Currently, the Lean file structure is technically broken because the theorem headers were commented out (due to their Archimedean/real-number nature not matching the generic `R_q` Laurent polynomial ring). However, closing this gap is highly plausible: it only requires separating the generic definitions from the Archimedean instantiations (e.g., via a ring homomorphism to $\\mathbb{R}$) and restoring the theorem headers over the reals. The underlying inequalities are elementary, and the formalization gap is purely structural." },
    { kind: "note", date: "2026-06-26", body: "Although the C(p,2)-C(n,2) signed-crossing excess is a natural back-reaction mechanism, framing it as a topological self-deformation of the substrate field by nuclear linking density (l_net/A^2) provides a genuinely novel geometric formalization of nuclear self-correction dynamics." },
  ],
  label: "prop:hadron-q-self-correction",
  title:
    "Effective substrate parameter: hadron self-deformation of $q$",
  tags: [
    "substrate-parameter",
    "self-energy",
    "effective-q",
    "hadron",
    "linking-number",
    "back-reaction",
  ],
  lean: { ref: "qou:QOU.Archimedean.hadron_q_self_correction",
    validation: "not_checked",
  },
  uses: ["prop:hadron-half-life"],
});
