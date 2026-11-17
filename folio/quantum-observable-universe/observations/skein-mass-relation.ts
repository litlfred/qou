import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:topological-mass-formula",
  label: "rem:skein-mass-relation",
  title: "The Jones polynomial obeys the skein relation; the mass does not",
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
      kind: "refined-framing",
      date: "2026-11-16",
      body: "Corrected on owner ruling (decision card, 2026-11-16, \"say Jones obeys skein, mass not\"). The remark previously stated $q\\mathfrak{m}(L_+) - q^{-1}\\mathfrak{m}(L_-) = (q^{1/2}-q^{-1/2})\\mathfrak{m}(L_0)$ for the mass. That is false: on a crossing of $4_1$ the crossing change (unknot) and smoothing (Hopf link) have volume $0$, which would force $\\mathfrak{m}(4_1) = 0$. Lean: `no_skein_on_volume_triple`, `old_skein_mass_fails`. The $m_\\mu/m_e$ pin of $q$ is unchanged.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-06-30",
      body: "**Identification: the figure-eight $4_1$ is the Higgs, not the muon.** The $4_1$ in $m_\\mu/m_e = \\mathrm{Vol}(4_1)/\\hbar_q^2$ is the Higgs (mass mechanism), not the muon. The muon's own identity knot is the torus knot $T(2,5)$ ([`prop:s5-equivariant-torus-knots`](s5-equivariant-torus-knots.md), [`lepton-meson-torus-knot-dictionary`](../particle-interactions/lepton-meson-torus-knot-dictionary.md)); as a torus knot it has $\\mathrm{Vol}_q = 0$ and no intrinsic volume-mass. So $\\mathrm{Vol}(4_1)/\\hbar_q^2$ is the Higgs-coupling mass scale — the figure-eight volume that gives the muon its mass — not the muon's own knot volume. Reading this as $\\text{muon} = 4_1$ is a category error (it confuses the muon with the Higgs that gives it mass). What the formula derives is $q_0$, via the muon mass scale set by the Higgs volume, not a muon–$4_1$ identification.",
      see: "https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md",
    },
    {
      kind: "deprecated",
      body: "**Substrate-density ($\\rho_q$) ansatz — leading-order only.** The relation $m_\\mu/m_e = \\mathrm{Vol}(4_1)/\\hbar_q^2$ uses the superseded substrate density $\\rho_q = 1/\\hbar_q^2$ as the dimensional factor. Per [`prop:mass-endomorphism-tower`](../mass-theory/mass-endomorphism-tower.md) and [`prop:rho-k-graded-expansion`](../mass-endomorphism/rho-k-graded-expansion.md), the scalar $\\rho_q$ is braid-class-independent, whereas the categorical density $\\rho_K$ varies $\\sim 30\\times$ across atoms. The Skein formula here is the leading-order substrate-truncation of the operator-valued $\\rho_K^{\\text{LO}} + \\rho_K^{\\text{single-gen}} + \\rho_K^{\\text{pair-gen}} + \\cdots$ graded expansion. The numerical match to $m_\\mu/m_e \\approx 206.77$ holds at lepton level because operator-valued corrections are small for leptons; the $+0.17\\%$ $\\mathfrak{Q}_\\beta$ residual is consistent with those corrections becoming non-negligible for hadronic observables. Re-derivation of $m_\\mu/m_e$ in canonical (graded-expansion) form is open work.",
      see: "../mass-endomorphism/rho-k-graded-expansion.md",
    },
  ],
  tags: ["mass", "skein"],
});
