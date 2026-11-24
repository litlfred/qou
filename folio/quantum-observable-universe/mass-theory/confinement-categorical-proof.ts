import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confinement-categorical",
  title: "Proof of confinement categorical",
  uses: ["prop:confinement-categorical", "prop:unified-curvature-rank-mass-formula"],
  authorNotes: [
    { kind: "note", date: "2026-11-24", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh): The Lean `confinement_categorical` follows exactly this route (`trace_unique`, `eq_scalar_of_commute`, `centreProj_central`, `trace_eq_residue_sum`). Witness references removed from prose: q-Dirac cell scanner witness ($D_q^2 = 0$) and Q-beta path A extended witness." },
  ],
});
