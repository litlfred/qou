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
    "conj:hoefsmit-scattering-pipeline",
    "def:quantum-planck-constant",
  ],
  cites: [
    "casimir1948",
    "mohideen1998",
    "lamoreaux1997",
    "robinson1966",
  ],
  tags: [
    "tier:P",
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
    script: "computations/probes/casimir_hoefsmit_additivity_probe.py",
    witness: [
      "computations/probes/casimir-epsilon-vacuum-probe.witness.json",
      "computations/probes/casimir-hoefsmit-additivity-probe.witness.json",
      "computations/probes/casimir-q-zeta-probe.witness.json",
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
      kind: "note",
      date: "2026-05-31",
      body:
        "**Prefactor sub-problem remains open (probes ruled out " +
        "fitting routes, not derived).** Six probe sweeps " +
        "(substrate q-rationals, Carlitz q-Bernoulli, " +
        "Φ_q/Markov, Macdonald, brute-force grid, q-factorial " +
        "with classical-limit constraint) all amount to " +
        "*template fitting*: pick a 'natural' q-deformation of " +
        "the classical formula and substitute. The Carlitz " +
        "q-Bernoulli and `[5]_q!_sym` candidates DISAGREE by " +
        "~10% at substrate — both are 'natural q-deformations', " +
        "so neither is structurally forced. A genuine derivation " +
        "requires constructing the categorical N_⊙(A, d) count " +
        "(sub-problem 1) and a regularization scheme native to " +
        "QOU (sub-problem 3), not template substitution. The " +
        "audit doc records all six probe routes and their " +
        "candidate values for future agents — they are " +
        "*candidates*, not derivations. See " +
        "[`docs/audits/2026-05-30-casimir-epsilon-vacuum-" +
        "investigation.md`](../../../docs/audits/2026-05-30-" +
        "casimir-epsilon-vacuum-investigation.md).",
    },
  ],
});
