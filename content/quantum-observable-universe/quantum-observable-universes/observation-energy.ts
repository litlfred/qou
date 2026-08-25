import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:observation-energy",
  lean: { ref: "qou:QOU.QuantumObservableUniverse.observation_energy", validation: "not_checked" },
  title:
    "Observation increases quantum energy and deforms the action",
  tags: [
    "observation",
    "energy",
    "substrate-perturbation",
    "action",
    "intent",
  ],
  uses: [
    "def:observation",
    "def:quantum-planck-constant",
    "def:categorical-action",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/QuantumObservableUniverse/observation_energy.lean` " +
        "uses `deriv`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
