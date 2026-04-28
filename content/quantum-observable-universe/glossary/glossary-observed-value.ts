import { remark } from "../../schema/builders";

export default remark({
  label: "rem:glossary-observed-value",
  lean: { ref: "qou:QOU.ObservedValue", validation: "not_checked" },
  title: "Observed spacetime value",
  tags: ["glossary", "brings-surface", "color-tube"],
  uses: ["def:color-tube-fibers", "rem:brings-smoothness"],
  defines: ["observed-value"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/observed-value-0.svg", blockIndex: 0, hash: "768da6d6762e" },
  ],
});
