import { definition } from "../../schema/builders";

export default definition({
  label: "def:observation",
  title: "Observation",
  tags: ["observation", "quantum"],
  lean: {
    decl: "QOU.Observation",
    validation: "not_checked",
  },
  status: "stated",
  uses: [
    "def:quantum-observable-universe",
    "def:substrate-parameter",
    "def:categorical-point",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/observation-0.svg", blockIndex: 0, hash: "f1af0d9a68b2" },
    { mime: "image/svg+xml", url: "rendered/observation-1.svg", blockIndex: 1, hash: "d1d06a9dd1ef" },
  ],

});
