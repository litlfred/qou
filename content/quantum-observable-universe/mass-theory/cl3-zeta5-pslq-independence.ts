import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cl3-zeta5-pslq-independence",
  title:
    "PSLQ certifies Cl$_3$(2$\\pi$/5) $-$ Cl$_3$(4$\\pi$/5) is independent of standard depth-3 periods up to coefficient norm 10$^8$",
  lean: {
    ref: "qou:QOU.BraidKnot.Cl3Zeta5PslqIndependence.pslq_independence",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/cl3_zeta5_pslq_search.py",
    witness:
      "computations/cl3-zeta5-pslq-search.witness.json",
    status: "verified",
  },
  uses: ["rem:b1-current-status"],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "pslq",
    "numerical-certification",
    "Cl3-zeta5",
    "depth-3",
    "antisymmetric-generator",
    "graded-mikusinski",
    "irreducibility-evidence",
  ],
});
