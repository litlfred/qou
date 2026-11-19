import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:hyperelliptic-quintic",
  label: "rem:hyperelliptic-quintic-remark",
  title: "Branch points, genus and the link to Bring's surface",
  uses: ["def:hyperelliptic-quintic", "prop:lagrange-resolvent-transform", "def:brings-surface"],
  cites: ["bolza1887"],
});
