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
      body: "Lean (descent-lemma.lean) proves: descent is surjective and linear on End; a surjective algebra hom on the commutant of e_n; not multiplicative on all of End; no surjective algebra hom M_k(K) -> M_j(K) for 0<j<k; equivariance of r_n, l_n from their being Hopf morphisms, and the intertwining of the induced actions; the archimedean surjective *-homomorphism in a Hilbert-space model (l_n an isometry, r_n its adjoint). Not formalised: the jet object J1(A) and the claim that (C, A_{n-1}, tau) is again a QOU (proof Steps 1-3), and the identification of the section algebras Gamma(J1 S_n, SU_q(2)) with the operator algebras (the functor tau).",
      see: "docs/audits/2026-11-22-lean-audit-snapshot-gaps.md",
    },
  ],
});
