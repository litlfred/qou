import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:antiparticle-crossing-reversal",
  lean: { ref: "qou:QOU.Torsion.antiparticle_crossing_reversal" },
  title: "Antiparticles from crossing reversal",
  uses: ["def:knot-particle-generation"],
  tags: [
    "trefoil", "chirality", "electron", "positron",
    "antiparticle", "crossing-energy",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Electron ruling (owner, 2026-11-21): relabelled the electron from the trefoil T_{2,3} to the word sigma_0 sigma_1 sigma_0 in B_3 (closure: Hopf link). Wording only; no number moved." },
  ],
});
