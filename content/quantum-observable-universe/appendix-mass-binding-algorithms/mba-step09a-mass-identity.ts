import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:mass-identity",
  title: "Mass identity $m(K) = m_e \\cdot \\mathrm{Geom}_{\\mathrm{full}}(K, q_0)$",
  uses: [
    "prop:mass-identity-exists",
    "prop:mass-identity-unique",
    "thm:knot-mass-formula-unified",
    "conj:geom-yekutieli-alignment",
  ],
  computation: {
    engine: "python+mpmath",
    script: "qou-mass/src/qou_mass/api.py",
    witness: "computations/per-observable-100x-status.witness.json",
    status: "verified",
  },
  tags: [
    "mba",
    "step-9a",
    "mass-identity",
    "vol-density",
    "canonical-chain",
  ],
});
