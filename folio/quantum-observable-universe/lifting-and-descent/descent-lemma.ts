import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:descent",
  examples: ["ex:descent-lemma-su2"],
  lean: { ref: "qou:QOU.descentHom_surjective", validation: "not_checked" },
  title: "Descent preserves the quantum observable universe",
  tags: ["descent", "frobenius-hopf", "star-homomorphism"],
  uses: ["def:recursive-brane-tower"],
  proofs: ["prf:descent"],
  defines: ["descent"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-22",
      body: "The Lean file proves the compression is surjective and linear on all of End, a surjective algebra homomorphism on the centralizer of e_n, not multiplicative on all of End (Z^2 counterexample), and that no surjective algebra homomorphism M_k(K) -> M_j(K) exists for 0 < j < k. The G_q intertwining is proved given equivariant r_n and l_n (descentCompression_intertwines, descentCompression_conj, descentHom_sandwich); the equivariance itself (Step 5, r_n a Hopf morphism) and the archimedean *-homomorphism are not formalised.",
      see: "docs/audits/2026-11-22-lean-audit-snapshot-gaps.md",
    },
  ],
});
