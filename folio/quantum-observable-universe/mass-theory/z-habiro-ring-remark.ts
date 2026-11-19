import { remark } from "../../schema/builders";

export default remark({
  label: "rem:z-habiro-ring-remark",
  title: "Elements and role of the z-Habiro ring",
  interprets: "def:z-habiro-ring",
  uses: [
    "def:z-habiro-ring",
    "cor:habiro-expansion-atomic",
  ],
});
