import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-game-of-life",
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
  lean: {
    decl: "QOU.Information.qGameOfLife",
    validation: "not_checked",
  },
  uses: [
    "prop:toffoli-transfer-matrix",
    "rem:toffoli-q-and",
    "prop:toffoli-lp-stability",
    "prop:reeb-operations-per-planck",
    "rem:discrete-planck-step",
    "def:categorical-action",
    "def:information-speed-of-light",
  ],
});
