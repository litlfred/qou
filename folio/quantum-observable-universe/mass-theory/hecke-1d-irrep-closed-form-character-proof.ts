import { proof } from "../../schema/builders";

export default proof({
  label: "prf:hecke-1d-irrep-closed-form-character",
  title: "Proof of hecke 1d irrep closed form character",
  uses: ["prop:hecke-1d-irrep-closed-form-character"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): plus, for $\\dim = 2$ irreps, the cos-resummation from\n[$\\mathfrak{Q}_\\beta$ cos-resummation in convention D](#prop:q-beta-cos-resummation)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ($n \\in \\{3, 5, 8\\}$):\n[`q-beta-1d-irrep-universal-closed-form.witness.json`](../../computations/q-beta-1d-irrep-universal-closed-form.witness.json)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): characters (per `prop:hecke-branching-trace-decomposition`)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (per\n`prop:hecke-branching-trace-decomposition`)." },
  ],
});
