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
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): ([$q$-Collatz](#conj:q-collatz))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Two consequences of the shared filtration are machine-checked in [`SkeinCounterfactual`](../lean/QOU/Information/SkeinCounterfactual.lean). The two legs: — `qCollatzSystem`, whose complexity measure is a caller-supplied parameter, and `vortexReductionSystem`, on which … The hitting-time descent measure ([`SkeinCounterfactual`](../lean/QOU/Information/SkeinCounterfactual.lean)). The $v_{[2]}$ refutation ([`collatz_vtwo_obstruction`](../lean/QOU/AppendixSurreals/collatz_vtwo_obstruction.lean))." },
  ],
});
