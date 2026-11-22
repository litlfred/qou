import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-prolongation",
  lean: { ref: "qou:QOU.JetProlongation", validation: "not_checked" },
  title: "Jet Prolongation",
  tags: ["jet-bundle", "frobenius-hopf", "prolongation"],
  examples: ["ex:jet-prolongation-su2", "rem:prolongation-categorical", "ex:brane-tower-levels"],
  uses: ["def:quantum-observable-universe"],
  proofs: ["prf:jet-prolongation"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body:
        "The proof cites `lem:jet-prolongation-categorical-jet` for the claim that $J^1(A)$ inherits " +
        "$(\\Delta', \\varepsilon', S')$ from $A$. That claim was retracted on 2026-11-21: restricting " +
        "$\\Delta$ to $\\Omega^1(A)$ fails for every bialgebra with $m$ not injective " +
        "(`rem:jet-comul-does-not-restrict`). That step of the proof is open until a Frobenius–Hopf " +
        "structure on $J^1(A)$ is supplied some other way.",
    },
  ],
});
