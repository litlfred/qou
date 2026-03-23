import { definition } from "../../schema/builders";

export default definition({
  label: "def:color-tube-fibers",
  lean: { decl: "QOU.ColorTubeFibers" },
  status: "stated",
  title: "Color tube fibers",
  tags: ["brings-surface", "color-tube"],
  uses: ["rem:color-tube-cubic", "rem:lagrange-resolvents", "prop:chiral-elliptic"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/color-tube-fibers-0.svg", blockIndex: 0, hash: "36bc7f6d5c91" },
  ],

});
