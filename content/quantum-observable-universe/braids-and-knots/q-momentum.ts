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
  lean: { ref: "qou:QOU.Descartes.QMomentum",
    validation: "not_checked",
  },
  uses: ["rem:building-block-knots"],
});
