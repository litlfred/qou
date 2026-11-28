import { remark } from "../../schema/builders";

export default remark({
  label: "rem:skein-filtration-trichotomy",
  title: "Length-filtration trichotomy on abstract observation systems, and why sharing a type does not couple problems",
  interprets: "conj:qou-p-neq-np",
  uses: [
    "conj:q-collatz",
    "conj:qou-p-neq-np",
    "conj:p-vs-np-boundary",
    "quantum-observable-universe:def:computational-horizon",
  ],
  tags: ["skein", "filtration", "collatz", "P-vs-NP", "navier-stokes"],
});
