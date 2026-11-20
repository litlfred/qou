import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor",
  title: "Proof of qbeta delta tau canonical conditional q2 minus 1 factor",
  uses: ["prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3):  The Lean proof uses direct substitution and a ring identity. $\\square$\n\n- **Concrete instance of `CanonicalMarkovWeightsH3`.** The class is inhabited by `CanonicalMarkovWeightsH3.canonicalInstance`, the convention-D weights $y_{(3)} = (q^4+1)/(q^2+1)^2$, $y_{(2,1)} = q^2/(q^2+1)^2$, $y_{(1^3)} = 0$. These are rational in $q$, and the normalisation is discharged by `field_simp; ring`. The hypothesis of the theorem is therefore met by the canonical instance." },
  ],
});
