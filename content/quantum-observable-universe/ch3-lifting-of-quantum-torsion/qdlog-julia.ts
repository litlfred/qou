import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qdlog-julia",
  title: "Quantum dilogarithm integrand as $q$-deformed Böttcher potential density",
  tags: ["quantum-dilogarithm", "julia-set", "bottcher", "reeb-flow"],
  uses: [
    "def:substrate-parameter",
    "def:q-reeb-flow",
    "rem:reeb-exceptional-divisor",
  ],
});
