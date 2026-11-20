import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qbeta-z-recursion-to-ck-recursion-bridge",
  title: "Proof of qbeta z recursion to ck recursion bridge",
  uses: ["prop:qbeta-z-recursion-to-ck-recursion-bridge"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The `QOU.QBeta.CKRecursion.CKRecursion ℝ` structure defined in ...; table row: | **Linear in history** | Yes (proven, `applyRecursion_linear`) |" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean proof is `field_simp` + `linarith` on the recursion equation." },
  ],
});
