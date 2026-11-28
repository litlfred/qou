import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-bsd-rank-zero",
  title: "Why categorical rank $r_q = 0$ comes from observability rather than arithmetic on $E(\\mathbb{Q})$",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "conj:q-birch-swinnerton-dyer",
    "quantum-observable-universe:def:categorical-mordell-weil",
    "quantum-observable-universe:prop:color-elliptic",
  ],
  tags: ["birch-swinnerton-dyer", "mordell-weil", "observability"],
});
