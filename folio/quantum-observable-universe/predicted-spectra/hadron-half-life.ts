import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "status", date: "2026-09-04", body: "Rate formula formalised (bean `qou-jk6k`). `lean.ref` names `hadron_half_life d r = ln 2 / betaRate d r` with `betaRate = |\\mathcal{W}|^2 \\mu_0/(2\\pi^3) \\cdot [2]_q \\cdot |\\mathcal{M}_q|^2 \\cdot f(Q)` over `BetaRateData` (the four non-$q$-integer factors as positive data: none has a closed form in the corpus yet — $|\\mathcal{W}(q)|^2$ is only a crossing budget in `def:beta-decay-skein`, $|\\mathcal{M}_q|^2$ is the `prop:trace-ratio-observable` product, $f(Q)$ the Sargent integral). `betaRate_eq_qPrefactor_iff` identifies the earlier carrier `ln 2 / ((q+q^{-1})(q-q^{-1})^5)` as this formula with those factors collapsed onto $(q-q^{-1})^5$; `qSensitivity_eq_logDeriv` proves the block's $\\partial \\ln\\Gamma/\\partial \\ln q$ is the logarithmic derivative of that shape, and `qSensitivity_near_48` checks the quoted $\\approx 48$ at $q = 1.1097$. Earlier the same day this note read \"partially formalised\": the ref named an alias for the $q$-shape and no declaration stated the rate." },
  ],
  label: "prop:hadron-half-life",
  title:
    "Hadron half-life from the $q$-deformed transition amplitude",
  tags: [
    "half-life",
    "beta-decay",
    "hadron",
    "transition-amplitude",
    "substrate-parameter",
    "valley-of-stability",
  ],
  lean: { ref: "qou:QOU.Archimedean.hadron_half_life",
    validation: "not_checked",
  },
  uses: ["prop:integer-stability"],
  computation: {
    engine: "mpmath",
    script: "computations/chebyshev_pairing_engine_witness.py",
    witness: "computations/chebyshev-pairing-engine.witness.json",
    status: "verified",
  },
});
