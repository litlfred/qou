import { remark } from "../../schema/builders";

export default remark({
  label: "rem:swampland-no-global-symmetry",
  title: "Swampland correspondence: observability and the absence of global symmetries",
  interprets: "def:quantum-observable-universe",
  uses: ["def:quantum-observable-universe"],
  tags: [
    "swampland",
    "global-symmetry",
    "observability",
    "adjoint-cohomology",
    "external-program",
  ],
  cites: ["banks-seiberg2011", "harlow-ooguri2021"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): imposed as a categorical axiom and discharged in Lean as $\\mathrm{Subsingleton}\\bigl((\\mathbf{1}_{\\mathbf{C}}) \\to \\mathrm{Ad}(A)\\bigr)$." },
  ],
});
