import { remark } from "../../schema/builders";

export default remark({
  label: "rem:trace-ledger",
  title: "The trace ledger: four traces, one Markov trace, and where the Euler characteristic is not",
  interprets: "prop:markov-trace-frobenius-selection",
  uses: [
    "def:chern-character",
    "def:grothendieck-group-of-a-qou",
    "def:hochschild-homology",
    "prop:markov-trace-frobenius-selection",
    "rem:three-euler-characteristics",
  ],
  cites: ["bghl-2017", "caldararu-willerton-2010", "trinh-2021", "nest-tsygan-1995"],
  tags: ["markov-trace", "categorical-trace", "quantum-dimension", "hochschild-homology", "chern-character", "wedderburn"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): that this Markov trace is convention D ... is proved in Lean at $n = 3$" },
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Written for the 2026-09-15 arc. The one proved bridge is the `n = 3` statement `QOU.BraidsAndKnots.markovWeights_eq_jones_of_fibre_categorical` (categorical trace of the fibre action forces convention D); its general-`n` extension and the antecedent that the mass-channel trace IS the categorical trace of the fibre action are open (bean `qou-n1dj`). Nothing in this ledger produces an Euler characteristic; the `-6` enters the paper only through the base curve.",
    },
  ],
});
