import { remark } from "../../schema/builders";

/**
 * Numerical phase-boundary analysis of the quantum ideal gas law
 * PV_q = N T_q (1 + ℏ_q²⟨S_q⟩/[2]_q) at the substrate value q = q₀.
 *
 * Evaluates the q-anomaly correction, the gas–liquid and
 * liquid–solid critical-temperature ratios, and compares the
 * predicted phase boundaries to the classical PV = nRT regime
 * and to the water phase diagram as a concrete worked example.
 */
export default remark({
  interprets: "prop:quantum-ideal-gas-law",
  label: "rem:pv-nrt-at-q0",
  title:
    "Phase-boundary analysis of $PV = nRT$ at the substrate value $q_0$",
  tags: [
    "ideal-gas",
    "equation-of-state",
    "phase-boundary",
    "phase-transition",
    "q-anomaly",
    "q0",
    "falsifiability",
    "water-phase-diagram",
  ],
  uses: [
    "prop:quantum-ideal-gas-law",
    "prop:phase-transition-boundary",
    "rem:phase-transition-interpretation",
    "def:quantum-temperature",
    "def:quantum-pressure",
    "def:quantum-volume",
    "def:h2o-molecular-braid",
  ],
});
