import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mobius-energy",
  title: "Categorical recovery of Möbius energy",
  hasProof: true,
  tags: ["mobius-energy", "categorical-mass", "knot-energy", "q-deformation"],
  uses: [
    "def:quantum-observable-universe",
    "def:categorical-action",
    "def:substrate-parameter",
    "def:q-hodge-star",
    "thm:topological-mass",
    "rem:frobenius-simplification",
  ],
  lean: {
    decl: "QOU.MobiusEnergy",
    validation: "not_checked",
  },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/mobius-energy-0.svg", blockIndex: 0, hash: "1582a4fa10bb" },
  ],
});
