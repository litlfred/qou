import { remark } from "../../schema/builders";

export default remark({
  label: "rem:julia-s1-photon-scatter",
  title: "Julia set on $S^1$ as photon scattering at the Big Bang",
  tags: ["julia-set", "photon", "big-bang", "reeb-flow"],
  uses: [
    "ex:q-reeb-flow",
    "def:fermion-boson-decomposition",
    "rem:reeb-exceptional-divisor",
  ],
});
