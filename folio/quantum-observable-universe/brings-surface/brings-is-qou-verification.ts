import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:brings-is-qou",
  label: "rem:brings-is-qou-verification",
  title: "Verification of the QOU data for Bring's surface",
  uses: [
    "prop:brings-is-qou",
    "def:brings-surface",
    "thm:qu-to-qou",
  ],
});
