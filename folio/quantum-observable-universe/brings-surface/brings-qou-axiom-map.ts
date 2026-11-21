import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-observable-universe",
  label: "rem:brings-qou-axiom-map",
  title: "QOU axioms instantiated on Bring's surface",
  uses: [
    "prop:positive-definite-dagger",
    "rem:brings-qou-4tuple",
    "rem:lagrange-resolvents",
    "rem:archimedean-realisations",
    "lem:volume-from-rigidity",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Lagrange resolvents](#rem:lagrange-resolvents)) (link retargeted to the earlier block that defines the transform)" },
  ],
});
