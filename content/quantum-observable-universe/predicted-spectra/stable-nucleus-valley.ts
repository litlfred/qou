import { remark } from "../../schema/builders";

export default remark({
  label: "rem:stable-nucleus-valley",
  title: "The stability condition restricts the hadron to the valley of stability",
  interprets: "def:stable-nucleus",
  tags: ["nucleus", "stability", "hadron", "beta-stability", "valley"],
  uses: ["def:stable-nucleus", "def:hadron", "prop:beta-stability"],
});
