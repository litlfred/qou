import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:frobenius-codim-universal",
  label: "rem:frobenius-limits-substrate-cost",
  title:
    "Limits of $\\tau(C_{\\dim_q})$: substrate information cost vs vortex computation",
  tags: [
    "frobenius",
    "limits",
    "substrate",
    "information",
    "landauer",
    "interpretation",
    "brane-tower",
  ],
  uses: [
    "rem:deuteron-first-principles",
    "conj:tau-codim-shannon",
    "conj:tau-codim-landauer",
    "conj:tau-codim-entropic-area",
  ],
});
