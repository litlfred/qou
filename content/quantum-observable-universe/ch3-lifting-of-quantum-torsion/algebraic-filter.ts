import { remark } from "../../schema/builders";

export default remark({
  label: "rem:algebraic-filter",
  title: "The algebraic filter",
  tags: ["fermion", "boson", "algebraic-filter", "curvature"],
  uses: [
    "rem:q-harmonic-basis-brane",
    "def:substrate-parameter",
    "rem:weight-space-decomposition",
  ],
});
