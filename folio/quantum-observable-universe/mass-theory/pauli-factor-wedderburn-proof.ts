import { proof } from "../../schema/builders";

export default proof({
  label: "prf:pauli-factor-wedderburn",
  title: "Proof of pauli factor wedderburn",
  uses: ["prop:pauli-factor-wedderburn"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): recovers the working definition of $F_{\\mathrm{Pauli}}$ in the\ncertificate engine\n([mass-formula validation](#rem:mass-formula-validation)) and\nidentifies it" },
  ],
});
