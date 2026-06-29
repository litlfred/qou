import { remark } from "../../schema/builders";

export default remark({
  label: "rem:information-theoretic-time-arrow",
  interprets: "def:information-theoretic-time",
  title: "The arrow of time inherited from the braiding order",
  tags: [
    "information-theory",
    "arrow-of-time",
    "braiding-order",
    "well-ordering",
    "reeb-flow",
  ],
  uses: [
    "def:information-theoretic-time",
    "rem:information-theoretic-time-properties",
    "prop:ordering-jet-compatibility",
  ],
});
