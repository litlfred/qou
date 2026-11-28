import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-collatz",
  title: "The $q$-Collatz conjecture on domain-stable Laurent polynomials",
  lean: {
    ref: "qou:QOU.AppendixSurreals.CollatzSyracuseLift.QCollatzConvergence",
    validation: "stub",
  },
  uses: [
    "sec:collatz-intro",
    "quantum-observable-universe:rem:aether-gm-torsion",
    "quantum-observable-universe:def:reeb-bundle",
    "quantum-observable-universe:prop:q-syracuse-lift",
    "quantum-observable-universe:prop:balanced-holonomy-exclusion",
    "quantum-observable-universe:thm:qou-obstruction-reduction",
  ],
  cites: [
    "collatz1937",
    "lagarias2010",
    "aaronsonwigderson2009",
    "grochow2017",
    "razborovrudich1997",
  ],
  tags: ["collatz", "laurent-polynomial", "syracuse", "conjecture"],
});
