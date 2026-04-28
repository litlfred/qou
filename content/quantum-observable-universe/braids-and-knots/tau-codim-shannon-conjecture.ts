import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tau-codim-shannon",
  title:
    "$\\tau(C_{\\dim_q})$ as a Plancherel--Shannon channel sum",
  lean: {
    ref: "qou:QOU.BraidKnot.TauCodimShannon",
    validation: "not_checked",
  },
  uses: [
    "thm:frobenius-codim-universal",
    "rem:frobenius-limits-substrate-cost",
  ],
  cites: ["kassel1995"],
  tags: [
    "frobenius",
    "shannon",
    "plancherel",
    "information",
    "substrate",
    "conjecture",
    "open",
  ],
});
