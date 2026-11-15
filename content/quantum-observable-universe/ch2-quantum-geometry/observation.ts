import { definition } from "../../schema/builders";

export default definition({
  label: "def:observation",
  title: "Observation",
  tags: ["observation", "quantum"],
  lean: {
    decl: "QOU.Observation",
    validation: "not_checked",
  },
  uses: [
    "def:substrate-parameter",
    "def:categorical-point",
    "def:quantum-observable-universe",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/observation-0.svg", blockIndex: 0, hash: "849f046a076b" },
    { mime: "image/svg+xml", url: "rendered/observation-1.svg", blockIndex: 1, hash: "8e5f48f1a2dd" },
  ],

});
