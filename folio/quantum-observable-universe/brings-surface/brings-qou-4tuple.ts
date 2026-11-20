import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:brings-surface",
  label: "rem:brings-qou-4tuple",
  title: "QOU 4-tuple for Bring's surface",
  uses: [
    "ex:c-quantum-observable-universe",
    "def:brings-surface",
    "def:so3-generators",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Lagrange resolvents](#rem:lagrange-resolvents)) (link retargeted to the earlier block that defines the transform)" },
  ],
});
