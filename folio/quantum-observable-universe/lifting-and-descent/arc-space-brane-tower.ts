import { remark } from "../../schema/builders";

export default remark({
  label: "rem:arc-space-brane-tower",
  title: "The brane tower as a jet-scheme tower carrying motivic integration",
  interprets: "def:arc-space",
  tags: ["arc-space", "jet-scheme", "brane-tower", "motivic"],
  uses: [
    "def:arc-space",
    "def:recursive-brane-tower",
    "def:motivic-mass-measure",
    "def:algebraic-quantum-volume",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This algebraic evaluation grounds the [motivic mass measure](#def:motivic-mass-measure), predictably assigning a finite volume to subsets of $\\mathcal{L}(X)$ even when $X$ inherently lacks a smooth volume form." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The [algebraic quantum volume](#def:algebraic-quantum-volume) formally makes this measure explicit." },
  ],
});
