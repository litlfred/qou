import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-trilog-depth-3-witness",
  title:
    "Bring trilog at $\\zeta_5$ as depth-3 grouplike value (50-digit functional-equation cross-validated witness)",
  lean: { ref: "qou:QOU.BraidKnot.BringTrilogDepth3Witness", validation: "stub" },
  computation: {
    engine: "mpmath",
    script:
      "folio-assistant/computations/bring_trilog_zeta5_depth_3.py",
    witness:
      "folio-assistant/computations/bring-trilog-zeta5-depth-3.witness.json",
    status: "verified",
  },
  uses: ["conj:two-filtration-bridge"],
  cites: [
    "bloch2000",
    "kontsevich1995",
    "zagier1986",
  ],
  tags: [
    "depth-3",
    "trilogarithm",
    "zeta-5",
    "bring",
    "S5-symmetry",
    "graded-mikusinski",
    "functional-equation-cross-validation",
    "50-digit-precision",
    "numerical-witness",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Numerically discharged at 50 digits via functional-equation\ncross-validation.** Depth correspondence verified by construction\n(single $\\mathrm{Li}_3$ factor $\\Rightarrow$ depth 3 on both sides).\nGeometric realisation as a hyperbolic-4-manifold or Chern–Simons\ninvariant is **open**.",
    },
  ],
});
