import { prose } from "../../schema/builders";

export default prose({
  label: "prose:sm-intro",
  title: "Scope and epistemic status",
  tags: ["appendix", "standard-model", "gauge-theory", "epistemic-status"],
  authorNotes: [
    {
      kind: "note",
      body: "Epistemic tier mapping in the formalization: *proved* corresponds to machine-checked Lean theorems, *conjectural* to content-bearing Lean classes with no instance.",
    },
  ],
});
