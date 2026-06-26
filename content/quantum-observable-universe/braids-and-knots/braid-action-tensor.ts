import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the braid-group action is a standard result (e.g., Kassel Thm XIII.1.3), its complete, sorry-free categorical Lean formalization in a generic braided monoidal category via an explicit hexagon and naturality chase represents a non-trivial engineering contribution to formal verification." },
  ],
  label: "prop:braid-action-tensor",
  lean: { ref: "qou:QOU.Braiding.braid_action_tensor",
    validation: "not_checked",
  },
  title: "Braid-group action on tensor powers",
  tags: ["braid-group", "braided-monoidal", "yang-baxter"],
  uses: ["def:quantum-observable-universe"],
  proofs: ["prf:braid-action-tensor"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/braid-action-tensor-0.svg", blockIndex: 0, hash: "0d1faa325318" },
  ],

});
