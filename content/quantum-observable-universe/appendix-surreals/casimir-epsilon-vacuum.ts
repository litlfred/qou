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
    "prop:vacuum-epsilon",
    "prop:archimedean-stpart",
    "def:standard-part-functor",
  ],
  cites: [
    "casimir1948",
    "mohideen-roy1998",
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
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-05-30",
      body:
        "**ε-scaling under review.** The narrative states " +
        "`N_⊙(A,d) ~ ε⁻¹ · A/d³`, but the empirical Hoefsmit-" +
        "additivity probe " +
        "(`folio-assistant/computations/casimir_hoefsmit_" +
        "additivity_probe.py`) found that composing with the " +
        "`Geom_full = Vol/ℏ_q²` normalisation forces either " +
        "(a) `N_⊙ ~ ε⁻²` (birthday rank 2), or (b) a different " +
        "`linking_weight` for disjoint unknots than the " +
        "Borromean case. The dimensional consistency is not " +
        "yet pinned down. See " +
        "[`docs/audits/2026-05-30-casimir-epsilon-vacuum-" +
        "investigation.md`](../../../../docs/audits/2026-05-30-" +
        "casimir-epsilon-vacuum-investigation.md) Route B for " +
        "the full analysis. Resolution requires a paper-side " +
        "judgement before the conjecture is finalised.",
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
        "witness.json`](../../../../folio-assistant/" +
        "computations/casimir-q-zeta-probe.witness.json) for " +
        "the candidate table.",
    },
  ],
});
