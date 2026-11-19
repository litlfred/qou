import { proof } from "../../schema/builders";

export default proof({
  label: "prf:generator-volume-decomposition",
  title: "Proof of generator volume decomposition",
  uses: ["prop:generator-volume-decomposition"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalisation note: Lean proves `energy_additive` and `beta_decay_locality` directly and states the assembly `generator_volume_decomposition_prop` as the decomposition identity itself (`generator_volume_decomposition = \\sum_i V_i` by `rfl`).",
    },
  ],
});
