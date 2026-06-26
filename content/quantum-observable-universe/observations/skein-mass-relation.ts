import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:topological-mass-formula",
  label: "rem:skein-mass-relation",
  title: "$q$-Deformed Skein Relation (Observation)",
  uses: [
    "rem:skein-decomposition",
    "thm:weight-decomposition-exists",
    "thm:categorical-reeb-exists",
    "thm:substrate-parameter-exists",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "deprecated",
      body: "**Substrate-density ($\\rho_q$) ansatz — leading-order only.** The relation $m_\\mu/m_e = \\mathrm{Vol}(4_1)/\\hbar_q^2$ uses the superseded substrate density $\\rho_q = 1/\\hbar_q^2$ as the dimensional factor. Per [`prop:mass-endomorphism-tower`](../mass-theory/mass-endomorphism-tower.md) and [`prop:rho-k-graded-expansion`](../mass-endomorphism/rho-k-graded-expansion.md), the scalar $\\rho_q$ is braid-class-independent, whereas the categorical density $\\rho_K$ varies $\\sim 30\\times$ across atoms. The Skein formula here is the leading-order substrate-truncation of the operator-valued $\\rho_K^{\\text{LO}} + \\rho_K^{\\text{single-gen}} + \\rho_K^{\\text{pair-gen}} + \\cdots$ graded expansion. The numerical match to $m_\\mu/m_e \\approx 206.77$ holds at lepton level because operator-valued corrections are small for leptons; the $+0.17\\%$ $\\mathfrak{Q}_\\beta$ residual is consistent with those corrections becoming non-negligible for hadronic observables. Re-derivation of $m_\\mu/m_e$ in canonical (graded-expansion) form is open work.",
      see: "../mass-endomorphism/rho-k-graded-expansion.md",
    },
  ],
  tags: ["mass", "skein"],
});
