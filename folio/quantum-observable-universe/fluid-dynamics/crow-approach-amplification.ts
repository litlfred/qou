import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:levi-degeneracy",
  label: "rem:crow-approach-amplification",
  title:
    "Crow amplification during the pair approach is a bounded power law $(d_0^2/V_{1,0})^{s^*/3}$",
  uses: [
    "rem:townsend-biot-savart-strain",
    "rem:hyperbolic-overlap-saturation",
  ],
  cites: ["crow1970", "saffman1992"],
  tags: [
    "crow-instability",
    "vortex-pair",
    "three-dimensional",
    "fluid-dynamics",
    "navier-stokes",
    "millennium-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-14",
      body:
        "Bean `qou-7fi2` (U3 of the model-to-PDE decomposition). Quantitative " +
        "content verified by `computations/qns_crow_efolds_probe.py` (witness " +
        "2/2: closed form vs Simpson to 1e-14; power-law exponent $s^*/3$ " +
        "exact). Scope (a): Crow linear theory with constant $s^*$ + the " +
        "phase-1 approach law, alone. The nonlinear regime and seed-amplitude " +
        "question remain the open content of bean `qou-ohaz`.",
    },
  ],
});
