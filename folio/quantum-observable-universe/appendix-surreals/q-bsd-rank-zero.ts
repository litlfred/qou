import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-bsd-rank-zero",
  title:
    "$r_q = 0$ is forced by the QOU observability axioms",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "def:categorical-mordell-weil",
    "prop:color-elliptic",
  ],
  tags: [
    "birch-swinnerton-dyer",
    "mordell-weil",
    "observability",
    "su2",
    "categorical",
  ],
});
