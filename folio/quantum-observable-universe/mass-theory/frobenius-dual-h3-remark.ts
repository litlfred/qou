import { remark } from "../../schema/builders";

export default remark({
  label: "rem:frobenius-dual-h3-remark",
  title: "Degeneracy on H_3 and existence of the Frobenius dual",
  interprets: "def:frobenius-dual-h3",
  uses: [
    "def:frobenius-dual-h3",
    "prop:frobenius-gram-matrix",
  ],
});
