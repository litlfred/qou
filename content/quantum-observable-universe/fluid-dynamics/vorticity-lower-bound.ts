import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vorticity-lower-bound",
  lean: { ref: "qou:QOU.FluidDynamics.vorticity_lower_bound_conditional", validation: "not_checked" },
  title:
    "Vorticity lower bound for anti-parallel filament collision as $q \\to 1$",
  uses: [
    "thm:q-bkm",
    "conj:q-aubin-lions",
  ],
  tags: [
    "vorticity",
    "lower-bound",
    "biot-savart",
    "anti-parallel",
    "blowup",
    "last-gap",
  ],
  authorNotes: [
    {
      kind: "note",
      body:
        "Lean sibling is archimedean by construction (AGENTS.md §7c): the collision time, separation $d(t)$, vorticity sup-norm and the Biot–Savart law $c_1\\sqrt{T^*-t}$ are real-analytic quantities over $\\mathbb{R}$ (uses `Real.sqrt`). This is the observable/archimedean side of the substrate→archimedean wall, on which the blow-up estimate is genuinely meaningful — not a gratuitous specialisation of otherwise-generic combinatorial content.",
    },
  ],
});
