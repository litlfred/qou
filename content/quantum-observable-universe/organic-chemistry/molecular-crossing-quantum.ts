import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:molecular-crossing-quantum",
  title:
    "Molecular crossing-energy quantum $\\lvert q + q^{-1}\\rvert_{\\mathrm{mol}}$",
  tags: [
    "crossing-energy",
    "molecular",
    "scale-separation",
    "alpha",
    "m_e_over_m_p",
    "nuclear",
    "trefoil",
  ],
  lean: { ref: "qou:QOU.Organic.molecularCrossingQuantum",
    validation: "not_checked",
  },
  uses: ["lem:alexander-T2N-closed-form"],
  cites: [],
});
