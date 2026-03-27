import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:quantum-computational-universality",
  label: "rem:skein-turing-machine",
  title: "A Turing machine is a braid; its Skein decomposition is the path integral",
  tags: [
    "turing-machine",
    "braid",
    "skein-decomposition",
    "path-integral",
    "descent",
    "information-theory",
    "planck-computation",
  ],
  uses: [
    "conj:quantum-computational-universality",
    "prop:toffoli-transfer-matrix",
    "rem:discrete-planck-step",
    "rem:jet-planck-steps",
    "prop:skein-polynomial-transfer-matrix",
    "thm:markov-trace-factorization",
    "def:descent-involution",
    "def:bundle-initial-conditions",
  ],
});
