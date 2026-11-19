import { remark } from "../../schema/builders";

export default remark({
  label: "rem:planck-time-remark",
  title: "The Planck time as a rational function of q",
  interprets: "def:planck-time",
  tags: ["definition-commentary"],
  uses: [
    "def:planck-time",
  ],
});
