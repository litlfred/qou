import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cl3-zeta5-orbit-sum-identity",
  title:
    "Cl$_3$(2$\\pi$/5) + Cl$_3$(4$\\pi$/5) = $-$(12/25)$\\zeta$(3) — depth-3 reduces to a 1-dim antisymmetric generator",
  lean: {
    ref: "qou:QOU.BraidKnot.Cl3Zeta5OrbitSum.orbit_sum_identity",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script: "computations/cl3_zeta5_orbit_sum.py",
    witness:
      "computations/cl3-zeta5-orbit-sum.witness.json",
    status: "verified",
  },
  uses: ["prop:bring-trilog-imaginary-tate-rational"],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "orbit-sum",
    "depth-3-reduction",
    "Cl3-zeta5",
    "antisymmetric-generator",
    "borel-rank-2",
    "graded-mikusinski",
    "theorem-level",
    "50-dps-numerical",
  ],
});
