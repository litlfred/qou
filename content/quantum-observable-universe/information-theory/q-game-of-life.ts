import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-game-of-life",
  proofs: ["prf:q-game-of-life"],
  title:
    "The quantum Game of Life (q-GoL) as a Toffoli-defined substrate automaton",
  tags: [
    "q-GoL",
    "toffoli",
    "cellular-automaton",
    "reversible-computation",
    "quantum-circuit",
    "q-AND",
    "conway",
    "hadamard",
    "planck-time",
  ],
  lean: { ref: "qou:QOU.Information.qGameOfLife",
    validation: "not_checked",
  },
  uses: [
    "rem:toffoli-q-and",
    "prop:toffoli-lp-stability",
    "def:information-speed-of-light",
  ],
  cites: [
    "bennett1973",
    "fredkin1982",
    "pena2022",
    "thooft2016",
    "toffoli1980",
  ],
});
