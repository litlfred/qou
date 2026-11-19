import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-langlands-dual",
  label: "rem:q-langlands-dual-remark",
  title: "The hmBcLanglands dual of $\\mathrm{SU}_q(2)$ and the inversion  \\mapsto q^{-1}$",
  uses: ["def:q-langlands-dual", "def:quantum-su2"],
});
