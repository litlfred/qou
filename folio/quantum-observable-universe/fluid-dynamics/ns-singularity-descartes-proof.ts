import { proof } from "../../schema/builders";

export default proof({
  label: "prf:ns-singularity-descartes",
  title: "Proof of ns singularity descartes",
  uses: ["thm:ns-singularity-descartes"],
  authorNotes: [
    {
      kind: "status",
      body: "Divisor arithmetic checked in Lean as `QOU.FluidDynamics.descartes_kummer_root_levels`. For the retraction of the earlier 4-step curve-restriction blowup argument, see `docs/audits/2026-10-12-ns-chain-after-item3-retraction.md`.",
    },
  ],
});
