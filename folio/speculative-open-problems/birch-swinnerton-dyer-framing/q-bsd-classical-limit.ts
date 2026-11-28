import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-bsd-classical-limit",
  title: "Parameter regimes of the formal $q$-BSD dictionary and classical Kolyvagin rank zero",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "conj:q-birch-swinnerton-dyer",
    "rem:q-bsd-rank-zero",
    "quantum-observable-universe:def:categorical-mordell-weil",
    "quantum-observable-universe:rem:aether-gm-torsion",
    "quantum-observable-universe:prop:ns-kummer-specialisation",
    "quantum-observable-universe:thm:qu-to-qou",
  ],
  cites: ["tate1974"],
  tags: ["birch-swinnerton-dyer", "gm-torsion", "kummer", "classical-limit"],
});
