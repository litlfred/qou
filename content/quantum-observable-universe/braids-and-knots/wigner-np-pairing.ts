import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wigner-np-pairing",
  title:
    "Wigner energy from $T{=}0$ np pairing: $(2,2)$ partition at $k{=}4$",
  lean: { ref: "qou:QOU.Descartes.ConfinedKnotBinding.wigner_energy_from_22",
    validation: "not_checked",
  },
  uses: [],
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
