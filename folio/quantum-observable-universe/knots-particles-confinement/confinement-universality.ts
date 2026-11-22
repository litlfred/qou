import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-universality",
  title: "Confinement universality: the confinement stage depends only on the flavours",
  tags: [
    "confinement",
    "universality",
    "photon",
    "polarization",
    "independence",
    "strong-force",
  ],
  lean: { ref: "qou:QOU.Interactions.confinementUniversality",
    validation: "not_checked",
  },
  uses: ["def:quark-antiquark-production", "def:photon"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body:
        "**Edge re-pointed.** This block used `prop:four-term-pair-nucleon`, now the conjecture conj:four-term-pair-nucleon (owner card 2026-11-21). " +
        "The statement here is true by construction: it needs only the definition of the γγ → qq̄ → 𝓑₃ chain and the photon, not that chain's net values, " +
        "and its Lean (`confinementUniversality`) imports Mathlib only. So it now uses the two definitions and stays a proposition.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "**Definitional reading adopted (owner E1 = (a), bean `qou-qs2u`).** The statement now takes the quark " +
        "flavours as an input and is true by construction: the confinement word contains no photon coefficient. " +
        "The previous framing, a derived decoupling and the categorical expression of asymptotic freedom, is " +
        "withdrawn. The substantive reading (universality over the photon states that produce the nucleon " +
        "flavours) is tracked as a bean, conditional on the flavour map.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (superseded 2026-11-15).** " +
        "This note said the `ℝ` was forced by the statement. It is not: the statement " +
        "and proof use no structure of the coefficient type. The Lean context is now " +
        "parametrised by the coefficient type `K` and the NF type `M`, and `K = ℂ` " +
        "covers circular polarisations (bean `qou-qs2u`, PR #7825).",
    },
  ],

});
