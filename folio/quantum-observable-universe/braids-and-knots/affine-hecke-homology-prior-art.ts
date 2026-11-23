import { remark } from "../../schema/builders";

export default remark({
  label: "rem:affine-hecke-homology-prior-art",
  title: "Prior art: Hochschild homology of affine Hecke algebras is independent of $q$",
  interprets: "rem:markov-trace-inductive-limit",
  cites: ["solleveld2022"],
  tags: ["affine-hecke-algebra", "hochschild-homology", "trace", "inductive-limit", "prior-art"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Relocated from block prose (Milnor Voice A; Lean talk out of prose): The note in the Lean scaffold that names the open construction as an inductive limit on the affine Hecke algebra should be read with this distinction in mind.",
    },
  ],
});
