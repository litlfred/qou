import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-cyclic-braid-energy",
  title:
    "Cyclic Hecke-braid energy difference for the benzene chain $\\to$ ring transition",
  tags: [
    "benzene",
    "resonance",
    "hecke-algebra",
    "cyclic-braid",
    "open-vs-closed",
    "alternative-route",
  ],
  lean: { ref: "qou:QOU.Organic.hecke_cyclic_braid_energy",
    validation: "not_checked",
  },
  uses: ["ex:benzene-ring"],
  cites: [],
});
