import { remark } from "../../schema/builders";

/**
 * Moved out of prop:gen3-meson-phi-hecke-seifert on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:gen3-meson-phi-hecke-seifert-identification",
  title: "Third-generation meson ratio: value at $q_0$ and identification with $\\phi(1020)$",
  interprets: "prop:gen3-meson-phi-hecke-seifert",
  uses: ["prop:gen3-meson-phi-hecke-seifert"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:gen3-meson-phi-hecke-seifert` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["meson", "phi-1020", "comparison-with-measurement"],
});
