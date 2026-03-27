import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:hadron-operations-closure",
  label: "rem:hadron-operations",
  title: "Operations on hadrons",
  tags: ["hadron", "knot", "braiding", "hopf-link"],
  uses: ["def:hadron", "prop:hadron-operations-closure"],
});
