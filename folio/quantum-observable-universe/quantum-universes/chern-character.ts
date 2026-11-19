import { definition } from "../../schema/builders";

export default definition({
  label: "def:chern-character",
  title: "The Chern character of a quantum universe",
  lean: { ref: "qou:QOU.GrothendieckChern.chernCharacter", validation: "not_checked" },
  uses: ["def:quantum-universe", "def:grothendieck-group-of-a-qou", "def:hochschild-homology", "def:rigid-monoidal-category"],
  defines: ["chern-character"],
  foreshadows: ["ex:su2-characters-and-quantum-dimension"],
  cites: ["bghl-2017", "loday-1998"],
  tags: ["chern-character", "hochschild-homology", "grothendieck-group", "quantum-dimension", "trace"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Introduced by the 2026-09-15 explicit-layer selection (owner option B): this is the `K_0 → HH_0 → R` layer through which `dim_q` factors, so that a quantum dimension is one evaluation of a character rather than a primitive. Lean: `QOU.GrothendieckChern.chernCharacter`, `evDimQ`, and the factorisation theorem `dimQK0_eq_evDimQ_chernCharacter` (bean `qou-mjt3`, item 3), sorry-free, in `lean/QOU/GrothendieckChern.lean`. The identification of `HH_0` of the semisimple category with the free module on the central idempotents is the presentation used, not an additional axiom.",
    },
  ],
});
