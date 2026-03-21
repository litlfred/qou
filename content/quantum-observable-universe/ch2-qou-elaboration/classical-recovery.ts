import { remark } from "../../schema/builders";

export default remark({
  label: "rem:classical-recovery",
  title: "Classical recovery of q-deformed operators",
  tags: ["q-deformed", "classical-limit"],
  uses: [
    "def:q-ext-deriv",
    "def:q-lie-bracket",
    "def:q-connection",
    "def:q-reeb-vector-field",
  ],
});
