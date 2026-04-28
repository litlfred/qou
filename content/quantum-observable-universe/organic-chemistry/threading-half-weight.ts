import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:threading-half-weight",
  title:
    "Threading half-weight: $\\Delta_{T(2,2m)}(q)/N \\to \\tfrac{1}{2}$",
  tags: [
    "threading",
    "alexander-polynomial",
    "half-weight",
    "limit",
    "T2N",
    "topological",
  ],
  lean: { ref: "qou:QOU.Organic.threadingHalfWeight",
    validation: "not_checked",
  },
  uses: ["lem:alexander-T2N-closed-form", "def:threading-link"],
  cites: [],
});
