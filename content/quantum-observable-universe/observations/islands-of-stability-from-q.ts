import { remark } from "../../schema/builders";

export default remark({
  label: "rem:islands-of-stability-from-q",
  title:
    "Islands of stability from the $N = 7$ Borromean intruder",
  interprets: "prop:nuclear-shell-intruder",
  lean: {
    decl: "QOU.Observations.IslandsOfStabilityFromQ",
    validation: "not_checked",
  },
  uses: [
    "prop:nuclear-shell-intruder",
    "prop:integer-stability",
    "rem:skein-mass-relation",
    "rem:q-stability-ranges",
    "conj:shell-threading-energy",
  ],
  tags: [
    "magic-numbers",
    "island-of-stability",
    "superheavy",
    "flerovium",
    "n-184",
    "intruder",
    "substrate-parameter",
  ],
  cites: ["ding2026"],
});
