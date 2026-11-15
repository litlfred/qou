import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-characteristic-classes",
  label: "rem:kummer-tower",
  title: "The Kummer tower and persistence of the obstruction",
  tags: [
    "kummer",
    "filtration",
    "obstruction",
    "euler-characteristic",
  ],
  uses: [
    "thm:qu-to-qou",
  ],
});
