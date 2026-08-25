import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:main-commutative-diagram",
  lean: { ref: "qou:QOU.diagram_commutes",
    validation: "not_checked",
  },
  title: "Main Commutative Diagram",
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "**`lean.ref` retargeted to the declaration this block's own sibling " +
        "proves** (bean `qou-lo1t`). It read `qou:QOU.main_commutative_diagram`, " +
        "but per §0a the sibling `main-commutative-diagram.lean` resolves first " +
        "and that file declares `diagram_commutes`, not " +
        "`main_commutative_diagram` — so the ref named a declaration the " +
        "resolved file does not contain. The name it used belongs to a " +
        "*different* carrier in `QOU/QuantumObservableUniverse/Propositions.lean`, " +
        "which is what `prf:main-commutative-diagram` refs.\n\n" +
        "The two are genuinely different objects, which is why both should " +
        "exist. This block's `diagram_commutes` is over `R_q = ℤ[q, q⁻¹]` and " +
        "is now **derived** from the three arrow equations: " +
        "`(1 − q⁻¹)·einstein = (1 − q⁻¹)·jet = section = schrodinger`. Its " +
        "`commutativity` field was redundant and was dropped (PR #5533). The " +
        "`Propositions.lean` carrier is over opaque types and carries " +
        "commutativity as an axiom; nothing there constrains its four maps, so " +
        "that one cannot be derived — only restated in composition form.",
    },
  ],
  uses: ["def:q-yang-mills-levi"],
  proofs: ["prf:main-commutative-diagram"],
  tags: ["commutative-diagram", "main-result"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/main-commutative-diagram-0.svg", blockIndex: 0, hash: "ac46a8d6ede5" },
  ],

});
