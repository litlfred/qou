import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "This is a standard quantum-group result regarding the Joseph-Letzter centre (Kassel VI.4.9). It is axiomatized here to support the framework's broader structural proofs; no novel mathematical argument is claimed for the uniqueness itself." },
  ],
  label: "prop:q-casimir-unique",
  title: "Uniqueness of the $q$-Casimir element up to scalar",
  lean: { ref: "qou:QOU.QCasimir.unique_up_to_scalar",
    validation: "not_checked",
  },
  uses: ["prop:q-casimir-exists"],
  proofs: ["prf:q-casimir-unique"],
  tags: ["uniqueness", "casimir", "central-element"],
});
