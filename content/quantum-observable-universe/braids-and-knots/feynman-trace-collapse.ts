import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:feynman-trace-collapse",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.trace_collapse",
    validation: "not_checked",
  },
  title: "Path integral collapses to a finite sum on the eigenbasis",
  tags: ["feynman", "path-integral", "trace-collapse", "semisimplicity"],
  uses: ["lem:feynman-eigenbasis-decomposition"],
  proofs: ["prf:feynman-trace-collapse"],
});
