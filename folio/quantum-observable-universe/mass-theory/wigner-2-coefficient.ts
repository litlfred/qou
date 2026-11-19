import { proposition } from "../../schema/builders";

/**
 * The Wigner-2 coefficient at k=6 derived from the LP dual:
 * C_{321} = w_{321} · h/2 = [2][4][6]h/(2[3]²[5]).
 *
 * The h/2 is a THEOREM about self-conjugate partitions:
 * conjugation pairs SYT T↔T' with opposite axial distances,
 * and the seminormal paired sum identity gives h per pair.
 */
export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-10-11", body: "Scope: this block's $C_\\lambda = w_\\lambda\\,h/2$ is not the coefficient of $-\\Delta_W T(T+1)/A$. Its headline shape $[3,2,1]$ scales as $(Z-N)(A-1)$ (interpretation block) and has three rows, so its Markov weight is zero under convention D. The $h/2$ trace theorem stands. Two inconsistent definitions of $C_\\lambda$ (bean `qou-wg3c`). `prf:unified-iterative-correction` states $C_\\lambda = m_e\\,H_q(\\lambda)$ (the $q$-hook product), while `prop:mass-coefficient-shadow-price` carries $C_\\lambda = w_\\lambda\\,h/2$ as the class field `C_eq`. At $(2,2)$ these give $6.2893$ MeV and $m_e w h/2 = 0.00887$ MeV; no stated map relates them. Neither is derived: the hook value is asserted universal and fails for six of the seven mass-formula coefficients (`qou-orjl`), and the factorisation $u^*_\\lambda = C_\\lambda S_\\lambda(Z,N,A)$ is a class field the stated LP cannot produce, since its dual constraints carry no $(Z,N)$." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:wigner-2-coefficient",
  title:
    "Wigner-2 coefficient $C_{[3,2,1]} = w_{[3,2,1]} \\cdot h/2$ from self-conjugate trace pairing",
  lean: { ref: "qou:QOU.BraidKnot.wigner2_coefficient",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-coefficient-shadow-price",
    "prop:hoefsmit-seminormal-form",
  ],
  tags: [
    "wigner",
    "self-conjugate",
    "seminormal",
    "shadow-price",
    "isospin",
    "cyclotomic",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/casimir_q_zeta_probe.py",
    witness: [
      "computations/probes/casimir-q-zeta-probe.witness.json",
      "computations/qbeta/qbeta-isospin-class-singleton.witness.json",
    ],
    status: "verified",
  },
});
