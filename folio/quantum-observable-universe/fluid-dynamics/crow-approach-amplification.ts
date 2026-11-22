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
      kind: "caveat",
      date: "2026-10-13",
      body:
        "**Re-scoped (owner decision 2026-10-13, Q1: $\\varTheta = f\\,\\xi^\\flat$).** " +
        "The closing paragraph previously drew \"three consequences for the branch " +
        "question of the Levi degeneracy conjecture\", where the branches were " +
        "stated on a Levi condition number that is undefined in dimension 3. The " +
        "three consequences are unchanged in content (reworded without ordinal " +
        "cadence) and now attach to the two-dimensional " +
        "reduction of the collision model, which is what they are about. A new " +
        "paragraph ties the Crow mode to the re-scoped conjecture: the Crow " +
        "instability bends the filaments, and the standard necessary condition for " +
        "blow-up (contrapositive of Beirão da Veiga–Berselli, recorded in " +
        "`conj:levi-degeneracy`) is a loss of ½-Hölder control of the line field. " +
        "The linear stage, with bounded amplification, does not supply it. Scope " +
        "(a): Crow linear theory alone. The quantitative content and its witness " +
        "are unchanged.",
      see: "../../../docs/audits/2026-10-12-ns-v1-geometric-depletion.md",
    },
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
