import { remark } from "../../schema/builders";

export default remark({
  label: "rem:b1-soft-sharpness-significance",
  title:
    "Soft vs strong sharpness: Goncharov is bigger than QOU needs",
  interprets: "prop:b1-soft-sharpness-theorem",
  uses: ["prop:depth-2-identification-bloch-suslin"],
  cites: ["bloch2000", "suslin1991"],
  tags: [
    "soft-sharpness",
    "strong-sharpness",
    "goncharov-conjecture",
    "beilinson-conjecture",
    "keystone-discharge",
    "borel-theorem",
  ],
});
