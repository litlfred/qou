import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The dictionary's Lean side is the " +
        "`FeynmanQOUDictionary`-style data at the end of " +
        "`lean/QOU/FeynmanPathIntegrals.lean`, whose fields are physical: " +
        "`q : ℝ`, `planckConstant : ℝ := 1 - q⁻¹`, `singleLevelMass : ℝ`. A " +
        "Planck constant and a mass are `ℝ` by meaning (§7c), and the file's " +
        "governing claims about them are ε–δ limits. The correspondence this " +
        "remark tabulates therefore runs *from* the generic Hecke/Markov side " +
        "*to* the archimedean observables — the `ℝ` marks the target of the " +
        "dictionary, not a leak in its source.",
    },
  ],
  interprets: "prop:feynman-categorical-trace",
  label: "rem:feynman-qou-dictionary",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.FeynmanQOUDictionary",
    validation: "not_checked",
  },
  title: "Dictionary: Feynman path integral $\\leftrightarrow$ QOU categorical trace",
  tags: ["path-integral", "feynman", "dictionary", "categorical-trace"],
  uses: [
    "def:categorical-transfer-matrix",
    "prop:feynman-classical-limit",
    "prop:photon-threading-mass",
  ],
  cites: [
    "yekutieli2015",
  ],
});
