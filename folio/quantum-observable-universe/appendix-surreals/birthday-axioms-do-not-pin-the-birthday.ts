import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:birthday-axioms-do-not-pin-the-birthday",
  title:
    "The six birthday axioms admit a two-valued model, so they bound birthday only from above",
  tags: [
    "surreals",
    "birthday",
    "axiom-audit",
    "independence",
    "hyperreals",
    "mixin",
  ],
  lean: {
    ref: "qou:QOU.AppendixSurreals.birthdayFaithful_independent_witnessed",
    validation: "leanok",
  },
  uses: ["thm:hyperreal-limit-transfer"],
  cites: ["conway1976", "gonshor1986"],
  authorNotes: [
    {
      kind: "note",
      body: "Historical note migrated from prose: an earlier phrasing asserted without explicit verification that adding the matching >= inequality kills the flat model outright; this is now proved explicitly at n = 2.",
    },
    {
      kind: "note",
      body:
        "Discovered while instantiating the six SurrealField birthday axioms on Mathlib's hyperreals (Real*) in QOU.AppendixSurreals.birthdayFaithful_independent_witnessed.",
    },
  ],
});
