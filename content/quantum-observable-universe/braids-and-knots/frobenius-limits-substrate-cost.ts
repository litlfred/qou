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
    "thm:frobenius-codim-universal",
    "thm:knot-mass-formula-unified",
    "prop:mass-endomorphism-tower",
    "prop:categorical-mass-markov",
    "rem:deuteron-first-principles",
  ],
});
