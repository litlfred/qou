import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-trilog-depth-3-witness",
  title:
    "Bring trilog at $\\zeta_5$ as depth-3 grouplike value (50-digit functional-equation cross-validated witness)",
  computation: {
    engine: "mpmath",
    script:
      "folio-assistant/computations/bring_trilog_zeta5_depth_3.py",
    witness:
      "folio-assistant/computations/bring-trilog-zeta5-depth-3.witness.json",
    status: "verified",
  },
  uses: [
    "conj:gb-depth-period-correspondence",
    "def:brings-coordinate-ring",
    "prop:q-dilogarithm-exists",
    "conj:bring-figure-eight-depth-2-witness",
    "conj:two-filtration-bridge",
    "rem:chirality-period-pairing",
  ],
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
});
