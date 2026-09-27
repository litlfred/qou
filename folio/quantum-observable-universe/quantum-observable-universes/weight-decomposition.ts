import { definition } from "../../schema/builders";

export default definition({
  label: "def:weight-decomposition",
  title: "Weight decomposition",
  lean: { ref: "qou:QOU.WeightDecomposition",
    validation: "not_checked",
  },
  uses: [
    "def:maximal-torus",
    "def:higher-forms",
  ],
  tags: ["weight", "decomposition"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/weight-decomposition-0.svg", blockIndex: 0, hash: "4118388b90dd" },
  ],

});
