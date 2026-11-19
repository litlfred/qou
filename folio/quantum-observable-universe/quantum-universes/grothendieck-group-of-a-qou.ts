import { definition } from "../../schema/builders";

export default definition({
  label: "def:grothendieck-group-of-a-qou",
  title: "The Grothendieck group of a quantum universe",
  lean: { ref: "qou:QOU.GrothendieckChern.K0", validation: "not_checked" },
  examples: ["ex:grothendieck-group-of-a-qou-example"],
  uses: ["def:quantum-universe", "rem:simple-objects-V", "def:rigid-monoidal-category"],
  defines: ["grothendieck-group"],
  foreshadows: ["def:chern-character", "ex:su2-characters-and-quantum-dimension"],
  cites: ["bghl-2017", "kassel1995"],
  tags: ["grothendieck-group", "k-theory", "wedderburn", "quantum-dimension"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Introduced by the 2026-09-15 explicit-layer selection (owner option B). The Lean carrier `QOU.GrothendieckChern.K0` in `lean/QOU/GrothendieckChern.lean` presents `K_0` on the block set of axiom 4 as `U.blocks →₀ ℤ`, with the rank and the additively extended quantum dimension, sorry-free. The factorisation `dim_q = ev ∘ ch` (bean `qou-mjt3`, item 3) is proved there as `dimQK0_eq_evDimQ_chernCharacter` and is the content of `def:chern-character`.",
    },
  ],
});
