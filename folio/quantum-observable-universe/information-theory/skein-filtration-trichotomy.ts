import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:computational-horizon",
  label: "rem:skein-filtration-trichotomy",
  title:
    "One length filtration, three problems: $q$-Collatz halting, $P$ vs $NP$, $q$-NS regularity",
  uses: [
    "def:computational-horizon",
    "conj:q-collatz",
    "conj:qou-p-neq-np",
    "thm:q-bkm",
    "rem:skein-turing-machine",
  ],
  cites: ["cardona2021", "freedman2003"],
  authorNotes: [
    {
      kind: "note",
      body: "Lean companion modules: `QOU/Information/SkeinCounterfactual.lean` (`SkeinObservationSystem`, `qCollatzSystem`, `vortexReductionSystem`, `QCollatz`) and `QOU/AppendixSurreals/collatz_vtwo_obstruction.lean` (`collatz_vtwo_obstruction`).",
    },
  ],
  tags: [
    "skein-module",
    "markov-trace",
    "length-filtration",
    "q-collatz",
    "p-vs-np",
    "q-navier-stokes",
    "computational-horizon",
    "unification",
    "information-theory",
  ],
});
