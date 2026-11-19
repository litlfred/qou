import { remark } from "../../schema/builders";

export default remark({
  label: "rem:isospin-mass-split-em-localisation",
  title: "Mirror-isobar mass split lives outside the spin-/sign-invariant sector",
  interprets: "prop:crystal-isospin-degeneracy",
  uses: ["prop:crystal-isospin-degeneracy"],
  tags: [
    "isospin",
    "tritium",
    "helium-3",
    "mass-split",
    "coulomb",
    "electromagnetic",
    "localisation",
    "structural-impossibility",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/m_p_substrate_identity_50dps.py",
    witness: "computations/m-p-substrate-identity-50dps.witness.json",
    status: "verified",
  },
});
