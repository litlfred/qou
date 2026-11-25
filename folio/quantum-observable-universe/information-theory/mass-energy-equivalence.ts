import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-energy",
  title:
    "Mass--energy equivalence from the causal-cone Legendre transform ($\\mathfrak{E} = \\mathfrak{m} \\cdot c_q^2$)",
  tags: [
    "mass-energy",
    "legendre-transform",
    "speed-of-light",
    "information-theory",
  ],
  lean: {
    ref: "qou:QOU.Information.energy",
    validation: "validated",
  },
  proofs: ["prf:mass-energy"],
  uses: [
    "def:categorical-hamiltonian",
    "def:information-speed-of-light",
    "def:mass-identity",
    "conj:braid-boost-inertial-equivalence",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-24",
      body:
        "Promoted from standalone definition (`def:mass-energy`) to derived proposition (`prop:mass-energy`) " +
        "under the unified Legendre Hamiltonian (`def:categorical-hamiltonian`, `QOU.Core.CategoricalHamiltonianLegendre`): " +
        "on the Dirac causal cone $|v| < c_q = 1/(q-1)$, the worldline Legendre transform yields " +
        "$E(v) = m_{\\mathrm{in}} c_q^2 / \\sqrt{1 - v^2/c_q^2}$, rest value $E(0) = m_{\\mathrm{in}} c_q^2$, " +
        "and mass-shell $E^2 - p^2 c_q^2 = (m_{\\mathrm{in}} c_q^2)^2$ unconditionally; equating boosted " +
        "kinematic inertia $m_{\\mathrm{in}}(\\beta)$ with static Frobenius--Hopf holonomy mass $\\mathfrak{m}(\\beta)$ " +
        "(`def:mass-identity`) is isolated explicitly in the §3b-cond class `BraidBoostInertialEquivalence`.",
    },
  ],
});
