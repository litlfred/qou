import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bring-figure-eight-depth-2-witness",
  title:
    "Bring figure-8 volume as depth-2 grouplike value (50-digit numerical witness)",
  lean: { ref: "qou:QOU.BraidKnot.BringFigureEightDepth2Witness", validation: "stub" },
  computation: {
    engine: "mpmath",
    script: "folio-assistant/computations/gb_depth_period_bring_fig8.py",
    witness:
      "folio-assistant/computations/gb-depth-period-bring-fig8.witness.json",
    status: "verified",
  },
  uses: [
    "conj:gb-depth-period-correspondence",
    "def:brings-coordinate-ring",
  ],
  cites: [
    "thurston1978",
    "neumann-zagier1985",
    "bloch2000",
    "suslin1991",
    "kashaev1997",
  ],
  tags: [
    "depth-2",
    "figure-8-knot",
    "bring",
    "hyperbolic-volume",
    "bloch-wigner",
    "clausen",
    "graded-mikusinski",
    "numerical-witness",
    "50-digit-precision",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "**Numerically discharged at 50 digits via mpmath** (witness above).\n**Conjectural** as a structural identification of *the* depth-2\ngrouplike value with Vol(4_1), conditional on\n[`conj:gb-depth-period-correspondence`](#conj:gb-depth-period-correspondence).\nThe witness rules out coarse numerical drift to relative precision\n$\\sim 10^{-37}$.\n\nA future cross-validation at full 50-digit precision would compute\n$\\mathrm{Cl}_2(\\pi/3)$ via Lobachevsky integral\n$-\\int_0^{\\pi/3} \\log|2\\sin t|\\,dt$ using `mpmath.quad`, independent\nof the polylog series machinery — currently deferred.",
    },
  ],
});
