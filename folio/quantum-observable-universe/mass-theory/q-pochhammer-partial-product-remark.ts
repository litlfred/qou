import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-pochhammer-partial-product-remark",
  title: "Poles, recurrence and truncation of the q-Pochhammer partial product",
  interprets: "def:q-pochhammer-partial-product",
  uses: [
    "def:q-pochhammer-partial-product",
    "conj:quantum-dilogarithm-stratified",
  ],
});
