import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fivefold-crystallographic-obstruction",
  title:
    "Crystallographic restriction and the weak force as non-lattice 5-fold symmetry",
  tags: [
    "five-fold",
    "crystallographic-restriction",
    "penrose",
    "weak-force",
    "parity-violation",
  ],
  interprets: "def:quantum-universe",
  uses: [
    "rem:force-knot-identification",
    "prop:skein-finiteness-bound",
  ],
  cites: [
    "bourbaki1968",
    "humphreys1990",
    "shechtman1984",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-b4fe: sourced the algebraic crystallographic restriction (2 cos(2*pi/k) in Z => k in {1,2,3,4,6} for n = 2, 3) to `bourbaki1968` (Ch. VI, §1.3) and `humphreys1990` (§2.8), and anchored `shechtman1984` explicitly for non-periodic 5-fold quasicrystalline order instead of citing unread secondary leads.",
    },
  ],
});
