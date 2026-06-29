import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quantum-characteristic-classes",
  label: "rem:kummer-tower",
  title: "The Kummer tower and perpetual obstruction",
  tags: [
    "kummer",
    "filtration",
    "obstruction",
    "euler-characteristic",
    "complementary-subgroup",
  ],
  uses: [
    "thm:qu-to-qou",
  ],
});
