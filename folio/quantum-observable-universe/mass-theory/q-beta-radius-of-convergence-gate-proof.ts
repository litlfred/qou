import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-radius-of-convergence-gate-evidence",
  title:
    "Evidence for the $\\mathfrak{Q}_\\beta$ radius-of-convergence conjecture from the $c_2, \\ldots, c_{10}$ window",
  interprets: "conj:q-beta-radius-of-convergence-gate",
  uses: [
    "conj:q-beta-radius-of-convergence-gate",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (canonical SDP extraction,\n`qbeta-decay-sdp-extended-ck.witness.json`)," },
  ],
});
