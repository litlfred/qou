import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-momentum",
  title: "$q$-Momentum from the braid writhe",
  tags: [
    "momentum",
    "q-deformed",
    "writhe",
    "braid",
    "hecke",
    "crossing",
    "kinematic",
  ],
  lean: {
    decl: "QOU.Descartes.QMomentum",
    validation: "not_checked",
  },
  uses: [
    "def:substrate-parameter",
    "prop:local-substrate-q",
    "def:crossing-energy",
    "rem:building-block-knots",
  ],
});
