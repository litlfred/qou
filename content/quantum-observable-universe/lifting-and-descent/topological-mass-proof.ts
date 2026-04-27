import { proof } from "../../schema/builders";

export default proof({
  label: "prf:topological-mass",
  title: "Proof of Topological Decomposition of Mass",
  uses: [
    "thm:topological-mass",
    "lem:topological-mass-eigenspace-decomp",
    "lem:topological-mass-holonomy",
    "lem:topological-mass-transient-localisation",
    "lem:topological-mass-dilogarithm",
  ],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/topological-mass-proof-0.svg", blockIndex: 0, hash: "c1937dc2947f" },
  ],

});
