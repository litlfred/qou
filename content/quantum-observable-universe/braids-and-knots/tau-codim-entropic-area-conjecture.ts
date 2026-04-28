import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tau-codim-entropic-area",
  title:
    "Entropic--area identification of $\\tau(C_{\\dim_q})$ on the exceptional divisor",
  lean: {
    ref: "qou:QOU.BraidKnot.TauCodimEntropicArea",
    validation: "not_checked",
  },
  uses: [
    "thm:frobenius-codim-universal",
    "rem:frobenius-limits-substrate-cost",
  ],
  cites: ["kassel1995"],
  tags: [
    "frobenius",
    "entropic-gravity",
    "holographic",
    "area-law",
    "substrate",
    "conjecture",
    "open",
  ],
});
