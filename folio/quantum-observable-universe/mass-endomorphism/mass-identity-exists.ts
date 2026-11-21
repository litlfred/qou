import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-identity-exists",
  title: "Existence of the inertial mass identity",
  lean: { ref: "qou:QOU.MassIdentity.exists",
    validation: "not_checked",
  },
  uses: ["def:mass-identity"],
  proofs: ["prf:mass-identity-exists"],
  tags: ["existence", "mass-identity", "inertial-mass"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): One proves uniqueness in [uniqueness of the mass identity](#prop:mass-identity-unique)." },
  ],
});
