import { example } from "../../schema/builders";

export default example({
  label: "ex:o16-derived-nf",
  title: "O-16: doubly magic at $Z = N = 8$",
  interprets: "prop:nuclear-operator-regimes",
  tags: [
    "oxygen",
    "normal-form",
    "derived",
    "doubly-magic",
    "magic-number",
    "shell-closure",
    "inductive-reduction",
  ],
  uses: [
    "prop:four-term-pair-nucleon",
    "prop:nuclear-operator-regimes",
    "prop:demand-stability",
    "prop:inductive-gb-reduction",
    "conj:periodic-table-demand",
  ],
});
