import { definition } from "../../schema/builders";

export default definition({
  label: "def:color-tube-coordinates",
  lean: { ref: "qou:QOU.ColorTubeCoordinates", validation: "not_checked" },
  title: "Color tube coordinates",
  tags: ["brings-surface", "color-tube"],
  uses: ["rem:braid-group-action"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Lagrange resolvents](#rem:lagrange-resolvents)) (link retargeted to the earlier block that defines the transform)" },
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/color-tube-coordinates-0.svg", blockIndex: 0, hash: "8df1be36adf7" },
  ],

});
