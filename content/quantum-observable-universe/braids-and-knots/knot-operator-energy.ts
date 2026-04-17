import { definition } from "../../schema/builders";

export default definition({
  label: "def:knot-operator-energy",
  title: "Knot operator energy (LP-dual shadow price)",
  lean: {
    decl: "QOU.BraidKnot.KnotOperatorEnergy",
    validation: "not_checked",
  },
  uses: ["prop:bw-coefficient-shadow-price", "def:hecke-normal-form"],
  cites: [],
  tags: [
    "knot-operator",
    "shadow-price",
    "lp-dual",
    "energy-functional",
  ],
});
