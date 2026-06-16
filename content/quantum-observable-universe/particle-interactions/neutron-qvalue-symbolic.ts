import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:neutron-qvalue-symbolic",
  lean: { ref: "qou:QOU.ParticleInteractions.neutron_qvalue_symbolic", validation: "not_checked" },
  title: "Symbolic $Q$-value of free neutron decay",
  uses: [
    "def:typed-crossing-operator",
    "rem:energy-scale-planck",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-05-24",
      body:
        "**Ansatz dependency flagged (PR #1127).** The relation " +
        "$\\mathfrak{Q}_\\beta = |\\Delta(\\mathrm{net})| \\cdot \\mathfrak{E}_0$ used in " +
        "this proposition is stated **\"by construction\"** in " +
        "[`pre-archimedean-derivation-chain.md`](../braids-and-knots/pre-archimedean-derivation-chain.md):391 " +
        "and is **not derived** from the canonical per-braid mass " +
        "formula ([`prop:per-braid-mass-tower`](../braids-and-knots/per-braid-mass-tower.md)), which uses " +
        "Markov-trace **weighted** sums (`tr_M(γ)=z`, `tr_M(σ_i)=z²`, " +
        "`tr_M(L_+)=z³`, …) — different from the unweighted `net` " +
        "sum used here. The +0.17% match between this proposition's " +
        "prediction (0.7836 MeV) and CODATA (0.7823 MeV) is either " +
        "(a) genuine N=0 brane-tower truncation residual, or " +
        "(b) numerical coincidence at $q_0 \\approx 1.110$ from a " +
        "wrong leading-order operator. **Resolution open**; see " +
        "[`docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md`](../../../docs/audits/2026-05-24-q-beta-net-ansatz-fitting-finding.md). " +
        "Until resolved, this block's claim **\"genuine prediction " +
        "from two leptonic inputs only\"** is **conditional on the " +
        "ansatz** $\\mathfrak{Q}_\\beta = |\\Delta(\\mathrm{net})| \\cdot \\mathfrak{E}_0$.",
    },
  ],
  tags: [
    "beta-decay",
    "q-value",
    "symbolic",
    "neutron",
    "typed-crossing",
    "prediction",
    "ansatz-dependent",
  ],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
