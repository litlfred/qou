import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:jones-markov-trace",
  lean: { ref: "qou:QOU.Braiding.jonesMarkov_H3_conventionD",
    validation: "external",
  },
  title: "Existence and non-degeneracy of the Markov trace (Jones, 1987)",
  tags: ["hecke-algebra", "markov-trace", "jones-polynomial", "external-proof"],
  cites: [
    "jones1987",
    "kimlee2018",
    "wenzl1988",
    "orellana1998",
    "geck-lambropoulou-2004",
    "jimbo1986",
    "temperley-lieb1971",
  ],
  uses: ["prop:braid-action-tensor", "prop:braiding-eigenvalue-extraction"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` constructs `rankOneMarkov` (`q = 1` over `ℚ`) inhabiting `QOU.Hecke.MarkovTrace` and `QOU.Shared.MarkovTraceContext`.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Repointed `lean.ref` from the `JonesMarkovTrace` carrier structure to the sorry-free three-strand theorem `QOU.Braiding.jonesMarkov_H3_conventionD` (paired with `trM_tlE0_conventionD` and `trM_mulNF_c3Anti_eq_zero` for the canonical Temperley–Lieb loop weight $z = q^3/(q^2+1)$). General-$n$ existence and uniqueness of the Markov trace remain external to Jones (1987).",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Loop-reciprocal identity tr_M(e_i) = 1/δ: (`loop_reciprocal`, [`TemperleyLiebTower.lean`](../lean/QOU/QBeta/TemperleyLiebTower.lean)).\n\nCatalan count of the Temperley–Lieb quotient: ([`TemperleyLiebTower.lean`](../lean/QOU/QBeta/TemperleyLiebTower.lean))." },
  ],
});
