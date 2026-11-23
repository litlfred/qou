import { proof } from "../../schema/builders";

export default proof({
  label: "prf:topological-mass",
  title: "Proof of Topological Decomposition of Mass",
  uses: [
    "prop:topological-mass-upper-bound",
    "conj:topological-mass-dilogarithm",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/topological-mass-proof-0.svg", blockIndex: 0, hash: "c1937dc2947f" },
  ],

});
