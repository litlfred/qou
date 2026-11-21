import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "The Lean link previously pointed at `QCasimir.exists`, a wrapper around an axiom that was false: `QuantumSu2` " +
        "allows q = 0, where `QCasimirData` (which needs q⁻¹) cannot exist. The axiom and wrapper were removed; the link " +
        "now points at the refutation. The prose claim (C_q is central in a genuine U_q(su(2)) at generic q) is open in Lean, bean qou-n2un.",
    },
  ],
  label: "prop:q-casimir-exists",
  title: "Existence of the $q$-Casimir element",
  lean: { ref: "qou:QOU.QCasimir.not_exists_unconstrained",
    validation: "not_checked",
  },
  uses: ["def:q-casimir"],
  proofs: ["prf:q-casimir-exists"],
  tags: ["existence", "casimir", "quantum-group", "central-element"],
});
