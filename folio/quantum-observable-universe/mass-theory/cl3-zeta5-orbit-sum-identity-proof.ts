import { proof } from "../../schema/builders";

export default proof({
  label: "prf:cl3-zeta5-orbit-sum-identity",
  title: "Proof of cl3 zeta5 orbit sum identity",
  uses: ["prop:cl3-zeta5-orbit-sum-identity"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/cl3-zeta5-orbit-sum.witness.json.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/cl3_zeta5_orbit_sum.py",
    witness: "computations/cl3-zeta5-orbit-sum.witness.json",
    status: "verified",
  },
});
