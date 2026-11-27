import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-aether",
  title: "Aether",
  tags: ["glossary", "aether", "terminology"],
  uses: [
    "def:frobenius-hopf-substrate",
    "def:substrate-parameter",
    "rem:einstein-ether-substrate",
    "rem:substrate-line-bundle-base-not-fibre",
    "rem:glossary-brane",
  ],
  defines: ["aether", "aether-parameter"],
  authorNotes: [
    { kind: "note", date: "2026-11-27", body: "Terminology ruling (owner, 2026-11-27): *aether* is the preferred term. It replaces *substrate* in the senses 'the medium A', 'the parameter q' and 'built from q alone' (substrate-derived/pure/only → aether-derived/pure/only). The generic-ring layer of AGENTS.md §7c is the *algebraic layer* (algebraic→archimedean wall), and adelic/motivic/Hahn 'substrates' are *base rings*. Labels and Lean identifiers still carry `substrate` until the phased rename lands; Lean renames keep `@[deprecated]` aliases." },
  ],
});
