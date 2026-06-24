import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-lichnerowicz",
  proofs: ["prf:categorical-lichnerowicz"],
  title:
    "Categorical Lichnerowicz: $\\Delta_\\nabla^q = \\mathfrak{D}_\\nabla^2 + \\tfrac{1}{4}\\,\\mathrm{Sc}_q$",
  tags: [
    "lichnerowicz",
    "weitzenbock",
    "q-laplacian",
    "categorical-dirac",
    "spin-geometry",
    "self-duality",
    "clifford",
  ],
  uses: [
    "def:categorical-dirac-operator",
    "rem:hodge-laplacian-relation",
    "rem:q-laplacian-expansion",
    "def:q-hodge-star",
    "def:categorical-instanton",
    "thm:categorical-reeb-exists",
    "ex:categorical-reeb-brings",
    "prop:reeb-u1-chart-swap",
  ],
  cites: [
    "lichnerowicz1963",
    "woronowicz1989",
  ],
  lean: {
    ref: "qou:QOU.Lichnerowicz.qDirac",
    validation: "not_checked",
  },
});
