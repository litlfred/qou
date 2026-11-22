import { remark } from "../../schema/builders";

/**
 * Frobenius self-dual structure of the molecular bound-state
 * Wedderburn channel.
 *
 * The two force-carrier Wedderburn channels for the H_2 molecule —
 * λ^(T_{3,5}) = (3, 1) and λ^(T_{2,9}) = (2, 1, 1) — are TRANSPOSE
 * partitions of each other. Under the Hopf antipode S, V_λ ↔ V_λᵀ,
 * so the bound-state sub-sector V_(3,1) ⊕ V_(2,1,1) is closed under S.
 *
 * This Frobenius-self-dual structure is the categorical analogue of
 * parity-symmetry: H_2 is electrically neutral and has J^P = 0⁺
 * ground state, consistent with antiparticle-crossing-reversal
 * invariance.
 *
 * The (3,1) ↔ (2,1,1) transpose pair is special to the genus-4
 * Bring constraint at n=4. For other molecular strand counts the
 * force-carrier channels (p, 1^{n-p}) are not transpose pairs in
 * general — explaining why the simplest covalent bond (H_2) has
 * particularly clean categorical structure.
 */
export default remark({
  label: "rem:bound-state-frobenius-self-dual-channel",
  title:
    "Bound-state Wedderburn channels $(3,1) \\leftrightarrow (2,1,1)$ are Frobenius-self-dual transpose pair",
  interprets: "conj:force-carrier-intertwining-correspondence",
  tags: [
    "frobenius-self-dual",
    "transpose-partition",
    "hopf-antipode",
    "wedderburn-channel",
    "parity-symmetry",
    "h2-molecule",
    "bound-state",
  ],
});
