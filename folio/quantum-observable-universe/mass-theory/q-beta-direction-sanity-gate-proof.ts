import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-beta-direction-sanity-gate-argument",
  interprets: "rem:q-beta-direction-sanity-gate",
  title: "Argument for q beta direction sanity gate (not a proof)",
  uses: ["rem:q-beta-direction-sanity-gate"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): $c_2, \\ldots, c_{10}$ (witness\n`computations/qbeta/qbeta-radius-of-convergence-gate-probe.witness.json`)." },
  ],
});
