import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:unified-iterative-correction",
  title:
    "Unified iterative LP-dual correction: per-step Wedderburn " +
    "projection over all partitions $\\lambda \\vdash k$ for " +
    "$k = 2, \\ldots, K$, starting at $A = 1$ (no special cases)",
  lean: { ref: "qou:QOU.Archimedean.ConfinedKnotBinding.Unified.unified_iterative_correction",
    validation: "not_checked",
  },
  uses: [
    "prop:wigner-np-pairing",
    "prop:mass-coefficient-shadow-price",
    "def:q-resolvent",
  ],
  cites: [
    "kerov1996",
    "feray-meliot2012",
    "satula1997",
  ],
  tags: [
    "wigner-energy",
    "iterative-correction",
    "partition-22",
    "q-hook-walk",
    "binding",
    "restartable-witness",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "Earlier formulations restricted the sum to blocks with tr ≤ 0. That restriction was asserted, not derived — it was what the accumulator computed — and was removed on that ground.",
    },
    { kind: "caveat", date: "2026-10-11", body: "Two inconsistent definitions of $C_\\lambda$ (bean `qou-wg3c`). `prf:unified-iterative-correction` states $C_\\lambda = m_e\\,H_q(\\lambda)$ (the $q$-hook product), while `prop:mass-coefficient-shadow-price` carries $C_\\lambda = w_\\lambda\\,h/2$ as the class field `C_eq`. " +
      /* <!-- literal-source: closed-form q-hook evaluation m_e * H_q((2,2)) = m_e * [3]_q * [2]_q^2 = 6.2893 MeV at q_0 --> */
      "At $(2,2)$ these give $6.2893$ MeV and $m_e w h/2 = 0.00887$ MeV; no stated map relates them. Neither is derived: the hook value is asserted universal and fails for six of the seven mass-formula coefficients (`qou-orjl`), and the factorisation $u^*_\\lambda = C_\\lambda S_\\lambda(Z,N,A)$ is a class field the stated LP cannot produce, since its dual constraints carry no $(Z,N)$." },
    {
      kind: "status",
      date: "2026-09-12",
      body:
        "**Statement re-aligned to the producer under the owner's ruling of " +
        "2026-09-12** — verbatim, *\"resolve functionals ... what lean provable\"*. " +
        "PR #7230 measured that this block and " +
        "`hecke_core_legacy.unified_iterative_correction` described different " +
        "functionals and deliberately left the choice open. Three divergences " +
        "were resolved against the block, each on a corpus artifact rather than " +
        "on a residual: (i) `u_λ` was called *\"its Frobenius positivity LP " +
        "shadow price\"* — refuted by `QOU.ParticleInteractions." +
        "y_0_eq_zero_of_radical` (sorry-free) and by " +
        "`prop:mass-coefficient-shadow-price`, corrected 2026-08-25 / 2026-09-05; " +
        "(ii) the q-Laplacian resolvent `ρ_λ(s_*)` the producer applies was " +
        "absent — deleting it moves the total by 4.12× at A=2 and 9.87× at A=4, " +
        "so it is not a rounding; (iii) *\"strictly over all λ\"* did not " +
        "describe the gated sum the producer computed at the time, a factor " +
        "1.93 / 1.95 apart at the production truncation k_exact = 11 (4.60 / " +
        "3.40 at k_exact = 4 — quote the tier). The criterion's discriminator is `QOU.MassTheory." +
        "UICFunctionalSelection.gate_not_a_function_of_displayed_data`: the " +
        "displayed summand is even in the trace, so the gate reads a sign the " +
        "formula has already discarded and the old text could not denote the " +
        "producer at all. **SUPERSEDED on divergence (iii) by PR #7253**, which " +
        "dropped the Pass-2 gate from the producer on the same day (owner " +
        "ruling, bean `qou-21oc`), after PR #7251 refuted its " +
        "complementary-slackness justification sorry-free. The producer now " +
        "sums over every enumerated λ, so this block's unrestricted reading " +
        "and the producer agree and (iii) is closed — not by re-aligning the " +
        "text to the gate, but by the gate going. Dropping it is NOT an " +
        "accuracy gain: both totals are wrong-signed against AME2020 and the " +
        "ungated one is further out. Beans `qou-sv7h`, `qou-brng`, `qou-21oc`.",
      see: "docs/audits/2026-09-12-uic-functional-resolution.md",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/casimir_q_zeta_probe.py",
    witness: [
      "computations/probes/casimir-q-zeta-probe.witness.json",
      "computations/sigma-f-electron-shell-chain.witness.json",
    ],
    status: "verified",
  },
});
