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
      kind: "status",
      body: "Convention D (z_D = q^3/(q^2+1)) is canonical per owner ruling 2026-09-08; full-tower energy scale E_0 = m_e / (q_0(q_0 - 1)(1 - hbar_q^2)) is canonical under the full-tower ruling.",
    },
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
        "ansatz** $\\mathfrak{Q}_\\beta = |\\Delta(\\mathrm{net})| \\cdot \\mathfrak{E}_0$. " +
        "**Update 2026-11-15 (owner: replace convention-C values with convention-D values even where worse).** " +
        "The block now states the ruled base, the Markov trace at $z_D$, giving 0.4447 MeV (-43.16 %). " +
        "The unweighted `net` sum above is the trace at $z = 1$ and is kept only as retired Form A.",
    },
    {
      kind: "caveat",
      date: "2026-11-16",
      body:
        "Owner card 2026-11-16 (prose + canonical E0). The element Delta is unchanged. E0 is now the tower-summed form of `computations/qbeta/qbeta_e0.py::canonical`, so the base moves 0.4447 -> 0.4491 MeV (-43.16% -> -42.59%). Added: the typed-crossing rule is labelled as the only u/d-breaking input (a definition; see #8111), a note that Delta has a sign-block part invisible to the convention-D trace, and the Form B paragraph no longer calls Form A an equivalent basis. Other blocks that still print 0.4447 MeV are not changed here.",
    },
    {
      kind: "status",
      date: "2026-11-16",
      body:
        "Owner ruling 2026-11-16: L+ and L- join the gamma-gamma word rule. The element Delta is therefore no longer guaranteed canonical, and 0.4491 MeV is provisional until the element is reselected over {V, V^-1, L+, L-} (bean qou-99qc).",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalisation note: the commutant exclusion on weight-preserving operators commuting with $F_3$ is proved as `commutant_trace_eq` in `QOU/BraidsAndKnots/NucleonIsospinExclusions.lean`. The all-order Convention-D generating function $\\mathcal{G}_D(u; q)$ and cumulants $c_2^{(D)} = -1$, $c_3^{(D)}(q) = -(3q^2-1)/(2q(q^2+1))$, $c_4^{(D)}(q)$ are formalized in `QOU/QBeta/ConventionDCumulantClosedForms.lean` and `QOU/QBeta/AllOrderConventionDGeneratingFunction.lean`, the GPMT-screened axial coupling $g_A(q_0) \\approx 1.2690$ in `QOU/QBeta/WeakCoevaluationAndNeutronLifetimeBridge.lean`, and the unbraided $(2,1)$ trace cancellation ($\\mathrm{tr}_{(2,1)}(\\Delta) = 0$) together with the 11-crossing Borromean GPMT $(1,1,1)$ sign-block closure ($|d_{\\mathrm{mod}}(1,1,1)| = 1/([2]_q[3]_q)$) in `QOU/QBeta/GPMTSignBlockAndTwoTermNucleonSplitting.lean` (80-dps witness `computations/probes/gpmt-sign-block-qbeta-and-np-splitting.witness.json`).",
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
    witness: [
      "computations/codata-masses.witness.json",
      "computations/probes/gpmt-sign-block-qbeta-and-np-splitting.witness.json",
      "computations/c-k-beta-decay-bound.witness.json",
      "computations/qbeta/weak-coevaluation-ga-and-neutron-lifetime.witness.json",
    ],
    status: "verified",
  },
});
