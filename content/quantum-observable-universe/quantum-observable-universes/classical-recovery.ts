import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-q-ext-deriv",
  label: "rem:classical-recovery",
  title: "Classical recovery of q-deformed operators",
  tags: ["q-deformation", "classical-limit"],
  uses: [
    "def:categorical-q-ext-deriv",
    "def:categorical-q-connection",
    "ex:q-reeb-vector-field",
  ],
});
