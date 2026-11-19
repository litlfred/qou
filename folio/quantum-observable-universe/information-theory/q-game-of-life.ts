import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-game-of-life",
  title:
    "The quantum Game of Life (q-GoL) as a Toffoli-defined aether automaton",
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
    "aharonov2003",
    "bennett1973",
    "fredkin1982",
    "pena2022",
    "shi2002",
    "toffoli1980",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "This block once named the regime q > 1 via the golden-ratio threshold q_⋆ = 1/φ²; both were artifacts of the excised convention C.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/toffoli-lp-stability.witness.json",
    status: "verified",
  },
});
