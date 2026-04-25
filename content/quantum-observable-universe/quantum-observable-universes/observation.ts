import { definition } from "../../schema/builders";

export default definition({
  label: "def:observation",
  title: "Observation",
  tags: ["observation", "quantum"],
  lean: { ref: "qou:QOU.Intent",
    validation: "not_checked",
  },
  uses: [
    "def:substrate-parameter",
    "def:categorical-point",
    "prop:fibre-functor-atlas",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/observation-0.svg", blockIndex: 0, hash: "dc276429434c" },
    { mime: "image/svg+xml", url: "rendered/observation-1.svg", blockIndex: 1, hash: "98292928e613" },
  ],

});
