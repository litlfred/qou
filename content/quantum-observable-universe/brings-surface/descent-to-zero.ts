import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:descartes",
  label: "rem:descent-to-zero",
  title: "Descent to dimension zero",
  uses: ["thm:descartes", "def:substrate-parameter"],
});
