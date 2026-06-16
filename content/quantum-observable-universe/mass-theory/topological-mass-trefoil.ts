import { example } from "../../schema/builders";

export default example({
  label: "ex:topological-mass-trefoil",
  title: "Topological mass of the trefoil knot (electron)",
  interprets: "prop:topological-mass-formula",
  uses: ["prop:topological-mass-formula"],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: ["mass", "trefoil", "electron", "example"],
});
