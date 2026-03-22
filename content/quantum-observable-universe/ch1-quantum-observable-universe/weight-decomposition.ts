import { definition } from "../../schema/builders";

export default definition({
  label: "def:weight-decomposition",
  title: "Weight decomposition",
  lean: {
    decl: "QOU.WeightDecomposition",
    validation: "not_checked",
  },
  status: "stated",
  uses: ["def:quantum-observable-universe", "def:maximal-torus", "def:higher-forms"],
  tags: ["weight", "decomposition"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/weight-decomposition-0.svg", blockIndex: 0, hash: "4118388b90dd" },
  ],

});
