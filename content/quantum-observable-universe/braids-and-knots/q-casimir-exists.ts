import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "This is a standard quantum-group Casimir existence result (Kassel/Lusztig). The formalization axiomatizes this standard mathematical fact pending a complete formalization of $U_q(\\mathfrak{su}_2)$, providing a rigorous structural interface without claiming a novel mathematical argument." },
  ],
  label: "prop:q-casimir-exists",
  title: "Existence of the $q$-Casimir element",
  lean: { ref: "qou:QOU.QCasimir.exists",
    validation: "not_checked",
  },
  uses: ["def:q-casimir"],
  proofs: ["prf:q-casimir-exists"],
  tags: ["existence", "casimir", "quantum-group", "central-element"],
});
