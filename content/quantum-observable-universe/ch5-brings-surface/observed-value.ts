import { definition } from "../../schema/builders";

export default definition({
  label: "def:observed-value",
  lean: { decl: "QOU.ObservedValue" },
  status: "stated",
  title: "Observed spacetime value",
  tags: ["brings-surface", "color-tube"],
  uses: ["def:color-tube-fibers", "rem:brings-smoothness"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/observed-value-0.svg", blockIndex: 0, hash: "768da6d6762e" },
  ],

});
