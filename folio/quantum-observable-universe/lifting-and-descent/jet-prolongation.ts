import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:jet-prolongation",
  lean: { ref: "qou:QOU.JetProlongation", validation: "not_checked" },
  title: "Jet Prolongation",
  tags: ["jet-bundle", "frobenius-hopf", "prolongation"],
  examples: ["ex:jet-prolongation-su2", "rem:prolongation-categorical", "ex:brane-tower-levels"],
  uses: ["def:quantum-observable-universe", "def:categorical-jet"],
  proofs: ["prf:jet-prolongation"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-22",
      body:
        "On the owner ruling of 2026-11-22 the jet object is $(A \\otimes A)/I^2$, $I = \\ker m$. That " +
        "object contains $A$ as a direct summand (`lem:jet-prolongation-categorical-jet`), which the old " +
        "$A \\otimes \\Omega^1(A)$ did not. The Frobenius–Hopf inheritance is still open for the new object: " +
        "for a commutative Hopf algebra $I$ is a Hopf ideal, but $I^2$ is not a coideal in general, so " +
        "$(A \\otimes A)/I^2$ is not obviously a quotient bialgebra.",
    },
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
