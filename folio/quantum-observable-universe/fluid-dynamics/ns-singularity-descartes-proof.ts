import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ns-singularity-descartes",
  title: "Proof of ns singularity descartes",
  uses: ["thm:ns-singularity-descartes"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The arithmetic is checked in Lean as `QOU.FluidDynamics.descartes_kummer_root_levels`. The full analysis is in the audit `docs/audits/2026-10-12-ns-chain-after-item3-retraction.md`." },
  ],
});
