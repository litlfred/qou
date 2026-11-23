import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:braid-group",
  label: "rem:braid-group-action",
  title: "Braid-group action on the resolvents",
  uses: [
    "rem:brings-curve",
    "rem:lagrange-resolvents",
    "def:braid-group",
    "def:so3-generators",
    "def:braid-twist-flip",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Lagrange resolvents](#rem:lagrange-resolvents)) (link retargeted to the earlier block that defines the transform)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Bring's curve](#rem:brings-curve))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): These three families—spectral, coordinate, and geometric—correspond to the three copies of $S_3$ inside $S_5$ identified in [chirality and trefoil](#rem:chirality-trefoil)." },
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/braid-group-action-0.svg", blockIndex: 0, hash: "f44799e1a010" },
    { mime: "image/svg+xml", url: "rendered/braid-group-action-1.svg", blockIndex: 1, hash: "1c761b8c5b7c" },
  ],

});
