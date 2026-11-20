import { definition } from "../../schema/builders";

export default definition({
  label: "def:h2o-molecular-braid",
  title: "Water $H_2O$ as a molecular braid",
  lean: { ref: "qou:QOU.Molecular.waterParts", validation: "not_checked" },
  uses: ["def:molecular-assembly-projector", "def:molecular-strand-partition"],
  tags: [
    "water",
    "H2O",
    "molecular-braid",
    "assembly-projector",
    "c2v",
    "lone-pair",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): *Lean sibling: combinatorial strand-partition datum, self-contained.*" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean sibling fixes the combinatorics: total $N = 28$, two bonding generators, and the hydrogen-exchange symmetry of the partition." },
  ],
});
