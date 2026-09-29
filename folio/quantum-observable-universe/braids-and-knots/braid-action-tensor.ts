import { proposition } from "../../schema/builders";

export default proposition({
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
