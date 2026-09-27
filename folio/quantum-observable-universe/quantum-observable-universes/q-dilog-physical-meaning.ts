import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-dilog-physical-meaning",
  interprets: "def:q-dilogarithm",
  title: "Physical meaning of $\\mathrm{Li}_2^q$: Bethe-ansatz generating function",
  tags: ["hopf-algebra", "dilogarithm", "bethe-ansatz", "entropy"],
  uses: [
    "def:q-dilogarithm",
  ],
});
