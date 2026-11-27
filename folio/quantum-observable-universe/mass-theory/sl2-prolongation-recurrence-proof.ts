import { proof } from "../../schema/builders";

export default proof({
  label: "prf:sl2-prolongation-recurrence",
  title: "Proof of the symplectic one-parameter recurrence",
  uses: [
    "prop:sl2-prolongation-recurrence",
    "prop:prolonged-periods-fixed-depth",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): which is the Lean theorem [`QOU.Mass.sl2_prolongation_recurrence`](#prop:sl2-prolongation-recurrence) (`rw [pow_add, hCH, mul_sub, mul_one, mul_smul_comm, ← pow_succ]`)." },
  ],
});
