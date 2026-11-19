import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cpt-d6-d7-d8-closure",
  title:
    "CPT closure: charge conjugation, parity and time reversal jointly preserve the Markov trace",
  lean: {
    ref: "qou:QOU.ParticleInteractions.CPTClosure",
    validation: "not_checked",
  },
  uses: [
    "conj:cpt-orbit-closure-density",
    "def:bar-involution",
  ],
  cites: [
    "wigner1937",
    "jones1987",
    "kassel1995",
  ],
  tags: [
    "cpt-closure",
    "discrete-symmetry",
    "compound-conjecture",
    "duality-d6-d7-d8",
    "markov-trace",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalisation note: downstream Lean declarations requiring CPT closure take `[CPTClosure R B tr cpt]` as an explicit typeclass hypothesis.",
    },
  ],
});
