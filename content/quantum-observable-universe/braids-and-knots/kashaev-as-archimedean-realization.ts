import { remark } from "../../schema/builders";

export default remark({
  label: "rem:kashaev-as-archimedean-realization",
  interprets: "def:archimedean-realization-functor",
  title: "Kashaev limit as the archimedean realization functor",
  tags: ["kashaev", "volume-conjecture", "realization-functor", "knot-volume", "archimedean"],
  uses: [
    "def:archimedean-realization-functor",
    "rem:kashaev-volume-density",
  ],
  cites: ["kashaev1997", "murakami-murakami2001"],
});
