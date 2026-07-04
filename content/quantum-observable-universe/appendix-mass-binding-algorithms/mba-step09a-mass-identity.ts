import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:mass-identity",
  title: "Mass identity $m_p = 2\\,(m_\\mu F_{\\mathrm{Bor}} - 6 m_e) \\cdot R_{\\mathrm{s5bb}}$ (muon-anchored Hecke energy)",
  uses: [
    "prop:mass-identity-exists",
    "prop:mass-identity-unique",
    "thm:knot-mass-formula-unified",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/canonical_mass.py",
    witness: "computations/m-p-substrate-identity-50dps.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-9a",
    "mass-identity",
    "muon-anchor",
    "canonical-chain",
  ],
});
