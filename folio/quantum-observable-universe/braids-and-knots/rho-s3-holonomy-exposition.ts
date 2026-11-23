import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:braid-twist-flip",
  label: "rem:rho-s3-holonomy-exposition",
  title: "The $\\rho$ representation as $S_3$ holonomy",
  tags: ["exposition", "holonomy", "s3", "chiral-sheets", "lagrange-resolvents"],
  uses: [
    "rem:holonomy-trefoil",
    "prop:lagrange-resolvent-transform",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([the braid-group action](#rem:braid-group-action))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): of [the $\\mathrm{SU}(2)$ generators](#def:su2-generators)" },
  ],
});
