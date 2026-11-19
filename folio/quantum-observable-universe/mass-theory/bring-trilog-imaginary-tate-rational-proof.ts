import { proof } from "../../schema/builders";

export default proof({
  label: "prf:bring-trilog-imaginary-tate-rational",
  title: "Proof of bring trilog imaginary tate rational",
  uses: ["prop:bring-trilog-imaginary-tate-rational"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/kummer-reflection-zeta5.witness.json.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/kummer_reflection_zeta5.py",
    witness: "computations/kummer-reflection-zeta5.witness.json",
    status: "verified",
  },
});
