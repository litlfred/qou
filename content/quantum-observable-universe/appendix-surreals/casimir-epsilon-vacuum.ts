import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:casimir-epsilon-vacuum",
  title:
    "Casimir force as $\\mathrm{st}$-image of $\\varepsilon$-vacuum density gradient",
  lean: {
    ref: "qou:QOU.AppendixSurreals.CasimirEpsilonVacuum",
    validation: "stub",
  },
  uses: [
    "conj:vacuum-epsilon",
    "conj:archimedean-stpart",
    "def:standard-part-functor",
  ],
  cites: [
    "casimir1948",
    "mohideen1998",
    "lamoreaux1997",
    "robinson1966",
  ],
  tags: [
    "surreal-numbers",
    "vacuum",
    "casimir-effect",
    "unknot",
    "regularisation",
    "infinitesimal",
    "boundary-condition",
    "conditional-on-class",
    "open-problem",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/casimir_hoefsmit_additivity_probe.py",
    witness: [
      "folio-assistant/computations/casimir-epsilon-vacuum-probe.witness.json",
      "folio-assistant/computations/casimir-hoefsmit-additivity-probe.witness.json",
      "folio-assistant/computations/casimir-q-zeta-probe.witness.json",
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-05-31",
      body:
        "**ε-scaling refinement RESOLVED.** Earlier draft asserted " +
        "`N_⊙(A,d) ~ -π²·A/(720·d³·ε)·ℏc` (no `ℏ²_q` factor). The " +
        "Hoefsmit-additivity probe (`casimir_hoefsmit_additivity_" +
        "probe.py`) found that under disjoint-union additivity, " +
        "`Geom_ε(N · ⊙) = N · ε / ℏ²_q`. For this to give the " +
        "textbook `-π²·A·ℏc/(720·d³)` after taking the standard-" +
        "part, the `N_⊙` formula must carry an extra `ℏ²_q` " +
        "factor so the `ℏ²_q` numerator and denominator cancel. " +
        "The narrative + conditional implication are now updated " +
        "with the corrected formula `N_⊙ ~ -π²·A·ℏ²_q·ℏc/(720·d³·ε)`. " +
        "Interpretation (a) of the original caveat is correct; " +
        "interpretation (b) (`ε⁻²` birthday rank) is wrong " +
        "because it would give a surreal-infinite Casimir energy, " +
        "incompatible with archimedean experimental scale. See " +
        "[`docs/audits/2026-05-30-casimir-epsilon-vacuum-" +
        "investigation.md`](../../../docs/audits/2026-05-30-" +
        "casimir-epsilon-vacuum-investigation.md) Route B " +
        "(resolved 2026-05-31).",
    },
    {
      kind: "refined-framing",
      date: "2026-05-31",
      body:
        "**Prefactor sub-problem RESOLVED (with substrate " +
        "deviation prediction).** After six independent probe " +
        "sweeps (substrate q-rationals, Carlitz q-Bernoulli, " +
        "Φ_q/Markov, Macdonald, brute-force grid, q-factorial " +
        "with classical-limit constraint), the natural " +
        "q-deformation of `ζ(−3) = −1/5!` is " +
        "`ζ_q(−3) = −1/[5]_q!_sym` where " +
        "`[n]_q!_sym = ∏_{k=1}^n [k]_q`. " +
        "This gives **`c_q = π²/(2·[5]_q!_sym)`** as the " +
        "QOU Casimir force-per-area prefactor — correct " +
        "classical limit (`→ π²/240` as `q → 1`) and a " +
        "specific 8.6% deviation at substrate " +
        "(`c_q(q_0) ≈ 0.0376` vs textbook `π²/240 ≈ 0.0411`). " +
        "Falsifiable by ~1% Casimir experiment. See " +
        "[`docs/audits/2026-05-30-casimir-epsilon-vacuum-" +
        "investigation.md`](../../../docs/audits/2026-05-30-" +
        "casimir-epsilon-vacuum-investigation.md) §6th sweep " +
        "for derivation chain.",
    },
  ],
});
