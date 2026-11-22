import { proof } from "../../schema/builders";

export default proof({
  label: "prf:chi-lambda-w0-sign-weighting",
  title: "Proof of chi lambda w0 sign weighting",
  uses: ["prop:chi-lambda-w0-sign-weighting"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): proved as `chi_V111_eq_V3_div_q4`\n([All three $V_\\lambda$ per-irrep character difference closed forms with **cyclotomic factor pattern**](#rem:chi-per-irrep-cyclotomic-closed-forms)\n\"Lean theorems exported\") implies," },
  ],
});
