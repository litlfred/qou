import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:topological-mass",
  title: "Topological Decomposition of Mass",
  hasProof: true,
  tags: ["mass", "topological-decomposition", "dilogarithm", "yekutieli"],
  uses: [
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:mass-identity",
    "def:descent-involution",
    "def:brane-boundary",
    "def:briggs-klein-chart",
    "prop:descent-eigenspaces",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/topological-mass-0.svg", blockIndex: 0, hash: "a5fce34918a5" },
    { mime: "image/svg+xml", url: "rendered/topological-mass-1.svg", blockIndex: 1, hash: "64f5f3945579" },
  ],

});
