import { proof } from "../../schema/builders";

export default proof({
  label: "prf:quantum-characteristic-classes-exists",
  title: "Proof of existence for quantum characteristic classes",
  uses: ["prop:quantum-characteristic-classes-exists"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The cocycle-level statement is proved in Lean as `QOU.CentralExtension.CechGerbe.CentralGerbeExtension.exists_lift_iff`, for gerbes modelled by their Čech cocycle data on a fixed cover." },
  ],
});
