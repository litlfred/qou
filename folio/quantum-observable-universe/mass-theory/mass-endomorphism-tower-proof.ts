import { proof } from "../../schema/builders";

export default proof({
  label: "prf:mass-endomorphism-tower",
  title: "Proof of mass endomorphism tower",
  uses: ["prop:mass-endomorphism-tower"],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "Earlier versions of this proof identified the integral with the compact quantum dilogarithm Φ_q; the symmetric Li_2^q identification replaced it.",
    },
  ],
});
