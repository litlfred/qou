import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:quantum-dilogarithm-stratified",
  title: "Quantum dilogarithm stratifies by partition GB-depth",
  lean: {
    ref: "qou:QOU.WedderburnMass.phi_q_frobenius_truncation",
    validation: "not_checked",
  },
  proofs: ["prf:quantum-dilogarithm-stratified"],
  tags: [
    "quantum-dilogarithm",
    "brane-tower",
    "centre-stratification",
    "spectral-sequence",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "The proposition is asserted, not yet fully proved at the level of the\ncurvature-rank stratification. The proof\n([proof block](#prf:quantum-dilogarithm-stratified)) derives existence\nof $\\phi_q^{(k)}(z_i)$ by applying the Frobenius dual to the depth-\ngraded centre decomposition; the truncation identity follows from\n$T_w$-orthogonality at depths $> k_\\star(T_w)$. The remaining gap is a **uniform bound on the\n$\\phi_q^{(k)}(z_i)$ at $|z_i| \\to q$**: the proposition asserts the\ntruncation identity as a Frobenius-paired equality, but to conclude\nthat *replacing* $\\Phi_q$ with $\\Phi_q^{[\\leq k_\\star(T_w)]}$ in the\nmass formula gives the same numerical answer one needs the\n$\\phi_q^{(k)}$'s to be uniformly bounded as $|z_i| \\to q$. That bound\nis the open part — the conjectural target of\n[$z$-Habiro completion](#conj:brane-tower-z-habiro).",
    },
  ],
});
