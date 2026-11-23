import { proof } from "../../schema/builders";

export default proof({
  label: "prf:generator-volume-decomposition",
  title: "Proof of generator volume decomposition",
  uses: ["prop:generator-volume-decomposition"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This formalizes `energy_additive`. | This formalizes `beta_decay_locality`. | The Lean formalization proves `energy_additive` and `beta_decay_locality` directly. It states the assembly `generator_volume_decomposition_prop` as the decomposition identity itself. By construction, the categorically-defined energy `generator_volume_decomposition` equals the generator-volume sum $\\sum_i V_i$ (proved by `rfl`). The sublemmas above carry the substantive transfer-matrix, additivity, and locality content." },
  ],
});
