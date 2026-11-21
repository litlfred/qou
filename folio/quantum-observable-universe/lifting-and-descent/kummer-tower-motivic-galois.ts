import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-characteristic-classes",
  label: "rem:kummer-tower-motivic-galois",
  title: "Motivic-Galois reading of the Kummer filtration",
  tags: ["kummer", "motivic-galois", "frobenius", "perpetual-obstruction"],
  uses: [
    "def:adelic-substrate",
    "thm:motivic-perpetual-obstruction",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([adelic substrate](#def:adelic-substrate))" },
  ],
  foreshadows: ["thm:motivic-perpetual-obstruction"],
});
