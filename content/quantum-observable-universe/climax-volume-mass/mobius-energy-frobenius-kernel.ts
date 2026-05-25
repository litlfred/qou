import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:mobius-energy-frobenius-kernel",
  lean: { ref: "qou:QOU.BraidsKnots.mobius_frobenius_kernel",
    validation: "not_checked",
  },
  title: "Classical limit of the Frobenius--Hopf kernel is the repulsive $1/r^2$",
  tags: ["frobenius-pairing", "mobius-energy", "classical-limit", "killing-form"],
  uses: ["def:frobenius-pairing"],
  proofs: ["prf:mobius-energy-frobenius-kernel"],
});
