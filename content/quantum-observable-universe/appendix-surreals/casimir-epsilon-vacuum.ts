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
      kind: "note",
      date: "2026-05-30",
      body:
        "**Prefactor π²/720 is not a low-degree substrate q-" +
        "rational.** Empirical search across ~150 candidate " +
        "forms (q-integers, ℏ_q², h_q², α_em products) found " +
        "no sub-1% match at substrate `q_0` other than the " +
        "trivial `q → 1` continuity match `2·π²/(720·[2]_q)`. " +
        "Closure of sub-problem 3 needs Cherednik-style " +
        "Macdonald-operator machinery. See " +
        "[`folio-assistant/computations/casimir-q-zeta-probe." +
        "witness.json`](../../../folio-assistant/" +
        "computations/casimir-q-zeta-probe.witness.json) for " +
        "the candidate table.",
    },
  ],
});
