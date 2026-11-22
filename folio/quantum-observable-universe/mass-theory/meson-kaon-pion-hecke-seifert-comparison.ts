import { remark } from "../../schema/builders";

/**
 * Moved out of prop:meson-kaon-pion-hecke-seifert on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:meson-kaon-pion-hecke-seifert-comparison",
  title: "Kaon-to-pion ratio: inputs and comparison with experiment",
  interprets: "prop:meson-kaon-pion-hecke-seifert",
  uses: ["prop:meson-kaon-pion-hecke-seifert"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:meson-kaon-pion-hecke-seifert` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["meson", "kaon", "pion", "comparison-with-measurement"],
});
