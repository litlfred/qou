import { remark } from "../../schema/builders";

export default remark({
  label: "rem:adelic-tate-bsd-reduction",
  title: "Speculative adelic prefactor analogy for the BSD leading coefficient",
  interprets: "conj:q-birch-swinnerton-dyer",
  uses: [
    "conj:q-birch-swinnerton-dyer",
    "rem:bsd-surreal-bound",
    "quantum-observable-universe:rem:adelic-tate-squeeze",
  ],
  cites: ["tate1967", "tate1974"],
  tags: ["birch-swinnerton-dyer", "adelic", "tate-thesis", "heuristic"],
});
