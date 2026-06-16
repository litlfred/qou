import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wigner-np-pairing",
  title:
    "Wigner energy from $T{=}0$ np pairing: $(2,2)$ partition at $k{=}4$",
  lean: { ref: "qou:QOU.Archimedean.ConfinedKnotBinding.wigner_energy_from_22",
    validation: "not_checked",
  },
  uses: [],
  computation: {
    engine: "python",
    script: "computations/b_over_a_evaluator.py",
    witness: "computations/b-over-a.witness.json",
    status: "verified",
    requires: ["mpmath"],
  },
  cites: [
    "kerov1996",
    "feray-meliot2012",
    "satula1997",
  ],
  tags: [
    "wigner-energy",
    "np-pairing",
    "partition-22",
    "binding",
    "q-hook-product",
  ],
});
