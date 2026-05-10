import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cl3-zeta5-pslq-independence",
  title:
    "PSLQ certifies Cl$_3$(2$\\pi$/5) $-$ Cl$_3$(4$\\pi$/5) is independent of standard depth-3 periods up to coefficient norm 10$^8$",
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/cl3_zeta5_pslq_search.py",
    witness:
      "folio-assistant/computations/cl3-zeta5-pslq-search.witness.json",
    status: "verified",
  },
  uses: [
    "prop:cl3-zeta5-orbit-sum-identity",
    "prop:bring-trilog-imaginary-tate-rational",
    "rem:b1-current-status",
    "conj:bring-trilog-depth-3-witness",
    "conj:qou-infra-discharges-goncharov-zeta5",
    "conj:cl3-zeta5-geometric-realization",
  ],
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
