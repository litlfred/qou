import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:crystal-graph-realization",
  title:
    "Hecke normal forms realise crystal highest-weight vectors",
  lean: { ref: "qou:QOU.BraidKnot.CrystalGraphRealization", validation: "stub" },
  uses: [
    "def:hecke-normal-form",
  ],
  cites: [
    "brundankleshchev2009",
    "kashiwara1991",
    "lecouvey2007",
  ],
  tags: [
    "tier:S",
    "crystal-graph",
    "kashiwara-operator",
    "highest-weight",
    "klr",
    "computational-shortcut",
    "audit-flag-13a",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-09-04-conjecture-carriers-round-two.lean` (`C1`) inhabits `QOU.BraidKnot.CrystalGraphRealization` on `PUnit` with `raising := fun _ _ => none`.",
      see: "docs/audits/2026-09-04-conjecture-carriers-round-two.lean",
    },
  ],
});
