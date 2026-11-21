import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:magic-numbers-bring",
  title:
    "Magic numbers $\\mathfrak{M} = \\{2, 8, 20, 28, 50, 82, 126\\}$ as ranks of $S_5$-stable Bring period sub-lattices",
  lean: {
    ref: "qou:QOU.Conjectures.MagicNumbersBring",
    validation: "not_checked",
  },
  uses: [
    "def:brings-coordinate-ring",
    "conj:homological-shell-condensation",
  ],
  cites: [
    "klein1888",
    "kassel1995",
    "geckpfeiffer2000",
  ],
  tags: [
    "tier:E",
    "magic-numbers",
    "brings-surface",
    "period-lattice",
    "S5-symmetry",
    "shell-closure",
    "open-problem",
  ],
});
