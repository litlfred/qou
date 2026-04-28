import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:tau-codim-landauer",
  title:
    "Landauer-type lower bound: vortex creation costs $\\geq m_e \\cdot \\tau(C_{\\dim_q})$",
  lean: {
    ref: "qou:QOU.BraidKnot.TauCodimLandauer",
    validation: "not_checked",
  },
  uses: [
    "thm:frobenius-codim-universal",
    "rem:frobenius-limits-substrate-cost",
  ],
  cites: ["kassel1995"],
  tags: [
    "frobenius",
    "landauer",
    "thermodynamic",
    "substrate",
    "information",
    "conjecture",
    "open",
  ],
});
