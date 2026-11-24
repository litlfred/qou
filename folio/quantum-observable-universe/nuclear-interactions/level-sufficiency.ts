import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:level-sufficiency",
  title:
    "Level sufficiency: Markov trace computable in the coarsest confinement algebra",
  lean: { ref: "qou:QOU.BraidKnot.LevelSufficiency",
    validation: "not_checked",
  },
  tags: [
    "confinement",
    "markov-trace",
    "filtration",
    "hecke-inclusion",
    "computational-minimality",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` proves `cover_always : kMax P q ≤ P.coarseStrands` by `le_refl` and inhabits `LevelSufficient` at zero trace.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
  ],
});
