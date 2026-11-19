import { remark } from "../../schema/builders";

export default remark({
  label: "rem:information-theoretic-time-remark",
  title: "Information-theoretic time and the braiding-induced ordering",
  interprets: "def:information-theoretic-time",
  tags: ["definition-commentary"],
  uses: [
    "def:information-theoretic-time",
    "prop:ordering-jet-compatibility",
  ],
});
