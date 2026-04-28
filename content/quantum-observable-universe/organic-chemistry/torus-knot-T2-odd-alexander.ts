import { definition } from "../../schema/builders";

export default definition({
  label: "def:torus-knot-T2-odd-alexander",
  title:
    "Symmetric Alexander polynomial of $T(2, 2m+1)$",
  tags: [
    "torus-knot",
    "T2N",
    "odd-N",
    "alexander-polynomial",
    "symmetric",
    "definition",
  ],
  lean: { ref: "qou:QOU.Organic.torusKnotT2OddAlexander",
    validation: "not_checked",
  },
  uses: ["lem:alexander-T2N-closed-form"],
  cites: [],
});
