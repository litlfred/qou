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
    { kind: "note", body: "Discharged in Lean as `Subsingleton ((1_C) -> Ad(A))`." },
  ],
});
