import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-turbulence-spectrum",
  lean: { ref: "qou:QOU.FluidDynamics.q_turbulence_spectrum", validation: "not_checked" },
  title: "$q$-deformed energy cascade and modified Kolmogorov spectrum",
  tags: ["turbulence", "kolmogorov", "energy-cascade", "fluid-dynamics", "prediction"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/FluidDynamics/q_turbulence_spectrum.lean` uses " +
        "`Real.log`, `Real.rpow`. These are real-analytic constructs with " +
        "no generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
