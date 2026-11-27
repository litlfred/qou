import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-brane",
  title: "Brane",
  tags: ["glossary", "brane", "terminology"],
  uses: [
    "def:recursive-brane-tower",
    "def:brane-boundary",
    "def:reeb-bundle",
    "rem:glossary-aether",
  ],
  defines: ["brane"],
  authorNotes: [
    { kind: "note", date: "2026-11-27", body: "Terminology ruling (owner, 2026-11-27): *brane* always means a base object (a level of the recursive tower, or the base manifold). It is never a synonym for the aether." },
  ],
});
