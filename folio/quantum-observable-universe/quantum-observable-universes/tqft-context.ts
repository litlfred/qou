import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-universe",
  label: "rem:tqft-context",
  cites: ["atiyah1988", "baez1995", "freed2010", "kock2004", "li2026-two-sphere", "lurie2009", "turaev2010", "witten1988"],
  title: "TQFT context",
  tags: ["tqft", "cobordism"],
  uses: ["ex:c-quantum-observable-universe"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-ffkf: anchored Daniel S. Freed, Michael J. Hopkins, Jacob Lurie, and Constantin Teleman (`freed2010`) in prose on the compact-Lie-group extended TQFT side; the earlier `-- Ref: [freed2010]` miscitation on `QOU.Glossary.FIsocrystal` was already retired when `QOU/Glossary.lean` replaced `FIsocrystal` with Mathlib's `WittVector.Isocrystal`.",
    },
  ],
});
