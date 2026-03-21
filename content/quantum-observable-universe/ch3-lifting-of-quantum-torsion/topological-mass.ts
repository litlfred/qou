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
});
