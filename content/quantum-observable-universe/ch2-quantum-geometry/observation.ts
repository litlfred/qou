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
    "def:quantum-observable-universe",
    "def:substrate-parameter",
    "def:categorical-point",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/observation-0.svg", blockIndex: 0, hash: "dc276429434c" },
    { mime: "image/svg+xml", url: "rendered/observation-1.svg", blockIndex: 1, hash: "98292928e613" },
  ],

});
