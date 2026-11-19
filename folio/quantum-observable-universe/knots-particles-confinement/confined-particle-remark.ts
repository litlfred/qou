import { remark } from "../../schema/builders";

export default remark({
  label: "rem:confined-particle-remark",
  title: "Unstable species and particle identity",
  interprets: "def:confined-particle",
  tags: ["confinement"],
  uses: [
    "def:confined-particle",
  ],
});
